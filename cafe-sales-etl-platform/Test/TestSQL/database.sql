CREATE TABLE transactions(
    transaction_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    transaction_date DATETIME,
    location_id UUID REFERENCES location(location_id),
    total_cost DECIMAL(8,2),
    payment_type VARCHAR(30)
);

CREATE TABLE location(
    location_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    location_name VARCHAR(30)
);

CREATE TABLE order_items(
    item_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    transaction_id UUID REFERENCES transactions(transaction_id),
    product_id UUID REFERENCES products(product_id)
);

CREATE TABLE products(
    product_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    product_name VARCHAR(30),
    product_price DECIMAL(8,2)
);
