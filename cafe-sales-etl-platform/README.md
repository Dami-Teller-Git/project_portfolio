# Café Sales Insights Platform (Team Project)

The Rise and Grind ETL Pipeline for SuperCafe
A scalable ETL pipeline and data analytics platform designed to centralize sales data across a nationwide chain of cafés — enabling real-time business insights, smarter decision-making, and company-wide trend analysis.

---

## 🌟 Project Overview

Following the success of a command-line order tracking system built for a local café, the business scaled rapidly to hundreds of outlets across the country. With this growth came new challenges: siloed data, inefficient reporting, and no centralized system to identify key customer or product trends.

This project addresses those challenges by building a cloud-based data platform that consolidates daily CSV sales reports from each branch into a centralized data warehouse. The goal: unlock actionable insights through automated analytics and dashboards.

---

##  Objectives

- Develop a fully scalable ETL (**Extract, Transform, Load**) pipeline.
- Process and consolidate large volumes of branch-level CSV sales data.
- Store transformed data in a centralized data warehouse.
- Enable business intelligence reporting across all locations.
- Implement application monitoring for operational health and uptime visibility.

---

##  System Architecture


Architecture Diagram of ETL Process:

![image](https://github.com/user-attachments/assets/67eed100-ba05-46bf-9ac5-51271c2e0e1f)


## 🛠️ Technologies Used
Category **|** Tools/Technologies

Programming Language **|**	Python

Source Control **|**	GitHub

Cloud Platform **|**	AWS (S3, Lambda, Redshift,CloudWatch)

Monitoring **|**	Grafana

## Team & Agile Workflow
This project was completed over 5 weekly sprints in a team-based, Agile environment:

Sprint Planning every Monday with backlog reviews

Task assignment via GitHub Projects

Pair programming and independent work sessions

Weekly retrospectives to reflect and improve

## Outcomes
Enabled the client to:

Consolidate national sales data in near real-time

Gain insight into high-performing products and peak hours

Monitor system health and performance across the data pipeline

Make data-driven decisions to support future expansion

## What I would do differently
Spend more time planning the data schema and transformations upfront
→ This would have avoided rework caused by early assumptions about data formats across cafés.

Establish clearer task ownership from the beginning
→ Early on, roles weren’t clearly defined, which led to duplicated efforts and slowed progress.

Set up monitoring and logging (CloudWatch & Grafana) earlier in the process
→ We waited until mid-project, which delayed issue detection and troubleshooting.

Automate the deployment pipeline from the start
→ Manual deployments introduced inconsistencies; automation would have improved reliability and speed.

Incorporate unit tests
→ Catches bugs early & enables safe refactoring to confirm the existing code has not broken 

[Team Presentation to client](https://www.figma.com/slides/A5VHXpZtS65ZoILGD3T06s/Agency-Pitch-S5?node-id=1-255&t=iCp8DEr0m82lt9uO-0)




