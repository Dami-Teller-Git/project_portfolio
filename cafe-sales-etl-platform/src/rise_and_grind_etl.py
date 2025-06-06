import csv
from datetime import datetime
import logging
from decimal import Decimal
import uuid

LOGGER = logging.getLogger()
LOGGER.setLevel(logging.INFO)

#Defining transaction columns 
DATAFIELDS = [
    'transaction_date',
    'location_name',
    'customer_name',
    'products',
    'total_cost',
    'payment_type',
    'card_number'
]

# Defining sensitive information fields to be removed in the transform step
SENSITIVEFIELDS = ['customer_name', 'card_number']

def extract(body_text):  
    LOGGER.info('extract: starting')
    reader = csv.DictReader(
        body_text,
        fieldnames=DATAFIELDS,
        delimiter=','
    )

    data = [row for row in reader]

    LOGGER.info(f'extract: done: rows={len(data)}')
    return data

#Removes sensitive data 
def remove_sensitive_information(data):
    LOGGER.info(f'remove_sensitive_information: processing rows={len(data)}')
    return [
        {k: v for k, v in item.items() if k not in SENSITIVEFIELDS} for item in data
    ]

#normalises datetime
def reformat_datetime(data):
    LOGGER.info('reformat_visit_date: starting')
    updated_data = []
    for item in data:
        updated_item = item.copy()
        try:
            input_format_string = '%d/%m/%Y %H:%M'
            dt = datetime.strptime(updated_item['transaction_date'], input_format_string)
            new_datetime = dt.strftime('%Y-%m-%d %H:%M')
            updated_item['transaction_date'] = new_datetime
            updated_data.append(updated_item)
        except ValueError:
            LOGGER.warning(f"reformat_datetime: Invalid date format in record {item} Skip")
            continue 
    LOGGER.info(f'reformat_visit_date: done: rows={len(updated_data)}')
    return updated_data
    
def split_order(products):
    items = [] 
    product_size = ['Small', 'Regular', 'Large']
    
    for product in products.split(','): #split with commas
        product = product.strip() #removes white space
        parts = product.split('-') #split each item
        if len(parts) < 2:
            LOGGER.warning(f"split_order: Invalid product format: '{products}' Skip")
            continue
        try: 
           product_name = parts[0].strip()
           product_flavour = parts[1].strip() if len(parts) == 3 else None #only if there are 3 parts 
           product_price = float(parts[-1].strip()) #-1 means last item in the list
        except (IndexError, ValueError) as e:
            LOGGER.error(f"split_order: Error parsing product '{products}': {e} Skip")
            continue
        item = { #create dictionary
        'product_name' : product_name,
        'product_flavour': product_flavour,
        'product_price': product_price
        }

        for size in product_size:
            if item['product_name'].startswith(size): #to check if the product name starts with size
                item['product_size'] = size #store the info
                item['product_name'] = item['product_name'][len(size):].strip() #remove size from the name and remove white space
                break
        items.append(item)
    return items
    
#numbers are interperted by python as text strings not actual numbers they need to be converted into
#numeric types for total_cost and product_price in redshift
def convert_decimal(cost_str):
    if cost_str is None or not cost_str.strip():
      return None
    try:
        return Decimal(cost_str) #takes the import decimal object and create the decimal number
        
    except Exception as e:
        LOGGER.error(f"Cant convert cost string '{cost_str}' to Decimal: {e}")
        return None #catches an error when the conversion happens 

# create a uuid
def create_guid():
    return str(uuid.uuid4())
    
# prepare data for loading into our sql tables
def normalise_data(rows, initial_locations, initial_products): #initial_locations):
    locations = []
    #location_lookup = location_lookup if location_lookup is not None else {}
    location_lookup = {}
    for entry in initial_locations:
        location_lookup[entry[1]] = entry[0]
    transactions = []
    products = []
    #product_lookup = product_lookup if product_lookup is not None else {}
    product_lookup = {}
    for entry in initial_products:
        product_lookup[(entry[0],entry[1],entry[2])] = entry[3]
    order_items = []
    for row in rows:
        #uses location lookup dictionary to check for location duplicates
        location_name = row["location_name"].strip().title()

        if location_name not in location_lookup:
            location_id = create_guid()
            location_lookup[location_name] = location_id
            locations.append({
                "location_id": location_id,
                "location_name": location_name
            })
        else: 
            location_id = location_lookup[location_name]

        # transactions - creates a list of dictionaries with key-value pairs corresponding to our database columns
        transaction_id = create_guid()
        try:
            formatted_date = datetime.strptime(row["transaction_date"], '%d/%m/%Y %H:%M').strftime('%Y-%m-%d %H:%M')
        except ValueError:
            LOGGER.warning(f"normalise_data: Invalid date format: {row['transaction_date']} Skip")
            continue
        new_transaction = {"transaction_id":transaction_id, 
                           "transaction_date": formatted_date,
                           "location_id":location_lookup[row["location_name"]],
                           "total_cost":row["total_cost"],
                           "payment_type":row["payment_type"]
                           }
        transactions.append(new_transaction)

        items = split_order(row["products"])
        for item in items:  # to avoid duplicates (if there are any)
            try:
                product_name = item['product_name'].strip().title()
                product_flavour = item.get('product_flavour')
                if product_flavour:
                    product_flavour = product_flavour.strip().title()
                product_size = item.get('product_size')
                if product_size:
                    product_size = product_size.strip().title()

                product_key = (product_name, product_flavour, product_size)
                if product_key not in product_lookup:
                   product_id = create_guid()            
                   product_lookup[product_key] = product_id

                   products.append({
                   "product_id": product_id,
                   "product_name": product_name,
                   "product_flavour": product_flavour,
                   "product_size": product_size,
                   "product_price": convert_decimal(str(item["product_price"])) if item.get("product_price") else None
                    })
                else:
                    product_id = product_lookup[product_key]

                    #order items is inside the loop
                new_order_items = {
                    "item_id": create_guid(),
                    "transaction_id": transaction_id,
                    "product_id": product_id
                }
                order_items.append(new_order_items)
            except Exception as e:
                LOGGER.error(f"normalise_data: Error processing product item: {item} Skip. Error: {e}")
                continue

    return locations, transactions, products, order_items

def transform(data, initial_locations, initial_products):
    LOGGER.info('transform: starting')
    data = remove_sensitive_information(data)

    #location_lookup = location_lookup if location_lookup is not None else {}
    LOGGER.info(f'location lookup intialised')
    LOGGER.info(f'Not Fetching')
    #product_lookup = product_lookup if product_lookup is not None else {}
    LOGGER.info(f'product lookup intialised')
    LOGGER.info(f'Not Fetching')
    LOGGER.info
    locations, transactions, products, order_items = normalise_data(data, initial_locations, initial_products)
    
    LOGGER.info(f'transform: done')
    return locations, transactions, products, order_items
