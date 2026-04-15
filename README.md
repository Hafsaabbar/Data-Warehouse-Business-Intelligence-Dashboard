# Data Warehouse & Business Intelligence Dashboard

## Overview
This project focuses on the design and implementation of a complete decision-support system based on a Data Warehouse architecture.

The system integrates data from multiple sources, processes it through an ETL pipeline, stores it in an optimized analytical database, and presents insights through interactive dashboards.

The objective is to help decision-makers monitor business performance, analyze trends, and support strategic decisions using data.

---

## Objectives
- Design and implement a Data Warehouse using a star schema  
- Develop an ETL pipeline for data extraction, transformation, and loading  
- Build interactive dashboards for different user profiles  
- Integrate machine learning models for advanced analytics  
- Provide meaningful insights for business decision-making  

---

## System Architecture
The system follows a multi-layer architecture:

1. Data Sources (Excel dataset – Superstore)
2. ETL Pipeline (data cleaning and transformation)
3. Data Warehouse (SQL Server, star schema)
4. Visualization Layer (Power BI dashboards)

---

## Data Warehouse Design

### Star Schema
The Data Warehouse is structured using a star schema:

- Fact table: `fact_sales`
- Dimension tables:
  - `dim_date`
  - `dim_product`
  - `dim_customer`
  - `dim_region`

This design ensures efficient analytical queries and fast dashboard performance.

---

## ETL Pipeline
The ETL process is implemented in Python and includes:

- Data extraction from Excel files  
- Data cleaning (missing values, duplicates, normalization)  
- Data transformation and enrichment  
- Loading into SQL Server  

Main libraries used:
- pandas  
- SQLAlchemy  

---

## Dashboards

### Available Dashboards
- Executive Dashboard (Direction)  
  - Global KPIs (sales, profit, growth)  
  - Trends and performance overview  

- Manager Dashboard  
  - Product and regional performance  
  - Profitability analysis  

- Sales Dashboard (Commercial)  
  - Customer segmentation  
  - Top clients and sales evolution  

### Features
- Dynamic filters (year, region, category, segment)  
- Drill-down (time, geography, product)  
- Cross-filtering between visualizations  

---

## Machine Learning Integration

### Sales Forecasting
- Algorithm: Linear Regression  
- Predicts future sales trends  

### Customer Segmentation
- Algorithm: K-Means  
- Groups customers into clusters  

### Anomaly Detection
- Method: Z-score  
- Identifies unusual patterns in revenue  

---

## Technologies Used

- Python  
- SQL Server  
- Microsoft Power BI  
- Visual Studio Code  
- SQL Server Management Studio  
- Git & GitHub  

---

## Project Structure
