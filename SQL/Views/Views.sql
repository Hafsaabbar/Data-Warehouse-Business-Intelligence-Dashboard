-- CA total par mois
CREATE VIEW vue_ca_par_mois AS
SELECT d.year, d.month, SUM(f.sales) AS chiffre_affaires
FROM fact_sales f JOIN dim_date d ON f.order_date = d.order_date
GROUP BY d.year, d.month;
GO

-- Performance par produit
CREATE VIEW vue_ventes_par_produit AS
SELECT p.product_name, p.category, SUM(f.sales) AS ca, SUM(f.profit) AS profit
FROM fact_sales f JOIN dim_product p ON f.product_id = p.product_id
GROUP BY p.product_name, p.category;
GO

-- Performance par région
CREATE VIEW vue_ventes_par_region AS
SELECT r.region, r.country, SUM(f.sales) AS ca, AVG(f.margin) AS marge_moyenne
FROM fact_sales f JOIN dim_region r ON f.region_id = r.region_id
GROUP BY r.region, r.country;
GO

-- Suivi des objectifs
CREATE VIEW vue_objectifs AS
SELECT d.year, d.month, 
       SUM(f.sales) AS ca_realise,
       SUM(f.target) AS ca_objectif,
       AVG(f.achievement) AS taux_realisation
FROM fact_sales f JOIN dim_date d ON f.order_date = d.order_date
GROUP BY d.year, d.month;
GO

-- Indicateurs financiers globaux
CREATE VIEW vue_indicateurs_financiers AS
SELECT d.year, d.quarter,
       SUM(f.sales) AS chiffre_affaires,
       SUM(f.profit) AS benefice,
       SUM(f.total_cost) AS couts_operationnels,
       AVG(f.margin) AS marge_brute_moyenne
FROM fact_sales f JOIN dim_date d ON f.order_date = d.order_date
GROUP BY d.year, d.quarter;
GO