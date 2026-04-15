CREATE TABLE fact_sales (
    order_id VARCHAR(20),
    product_id VARCHAR(20) REFERENCES dim_product(product_id),
    customer_id VARCHAR(20) REFERENCES dim_customer(customer_id),
    order_date DATE REFERENCES dim_date(order_date),
    region_id INT REFERENCES dim_region(region_id),
    sales DECIMAL(12,2),
    quantity INT,
    profit DECIMAL(12,2),
    margin DECIMAL(8,4),
    revenue DECIMAL(12,2),
    total_cost DECIMAL(12,2),
    growth DECIMAL(8,4),
    target DECIMAL(12,2),
    achievement DECIMAL(8,4),
    month_index INT
);