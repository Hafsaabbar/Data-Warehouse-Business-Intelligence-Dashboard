# ============================================================
# 📊 ETL PIPELINE - PROJET TABLEAU DE BORD (VENTES)
# Version améliorée avec calcul intelligent et colonnes utiles
# ============================================================

import pandas as pd
from sqlalchemy import create_engine

# ============================================================
# 1. EXTRACT (Lecture des données)
# ============================================================

print("🔄 Chargement des données...")
df = pd.read_excel("Sales.xlsx", sheet_name="Orders")
print("✅ Données chargées avec succès")
print(df.head())

# ============================================================
# 2. CLEANING (Nettoyage des données)
# ============================================================

print("\n🧹 Nettoyage des données...")

df = df.drop_duplicates()
print("✔ Doublons supprimés")

print("\n🔍 Valeurs manquantes par colonne :")
print(df.isnull().sum())

df = df.dropna(subset=['Sales'])

if 'COGS' in df.columns:
    df['Profit'] = df['Profit'].fillna(df['Sales'] - df['COGS'])
else:
    df['Profit'] = df['Profit'].fillna(df['Sales']*0.2)

print("✔ Valeurs manquantes traitées")

df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Ship Date'] = pd.to_datetime(df['Ship Date'])
print("✔ Dates converties")

for col in df.select_dtypes(include='object').columns:
    df[col] = df[col].str.strip().str.lower()

df.to_excel("Sales_Cleaned.xlsx", index=False)
print("✔ Toutes les colonnes texte nettoyées et normalisées dans Sales_Cleaned.xlsx")

# ============================================================
# 3. TRANSFORM
# ============================================================
df = pd.read_excel("Sales_Cleaned.xlsx")

print("🔄 Rechargement des données nettoyées...")

df['Year'] = df['Order Date'].dt.year
df['Month'] = df['Order Date'].dt.month
df['Day'] = df['Order Date'].dt.day
df['Quarter'] = df['Order Date'].dt.quarter

df['Revenue'] = df['Sales']
df['Total_Cost'] = df['Sales'] - df['Profit']
df['Margin'] = df['Profit'] / df['Sales']

df['Sales_per_Product'] = df.groupby('Product Name')['Sales'].transform('sum')
df['Sales_per_Region'] = df.groupby('Region')['Sales'].transform('sum')
df['Sales_per_Category'] = df.groupby('Category')['Sales'].transform('sum')

df = df.sort_values('Order Date')
df['Previous_Sales'] = df['Sales'].shift(1)
df['Growth'] = (df['Sales'] - df['Previous_Sales']) / df['Previous_Sales']

df['Target'] = df['Sales'] * 1.1
df['Achievement'] = df['Sales'] / df['Target']

df['Month_Index'] = (df['Year'] - df['Year'].min())*12 + df['Month']

df['Region ID'] = df['Region'].astype('category').cat.codes + 1

print("✔ Colonnes calculées et enrichissement terminé")

# ============================================================
# 4. SCHÉMA ÉTOILE - FACT + DIMENSIONS
# ============================================================

# Renaming columns to match SQL table scripts
df.rename(columns={
    'Order ID'      : 'order_id',
    'Product ID'    : 'product_id',
    'Customer ID'   : 'customer_id',
    'Customer Name' : 'customer_name',
    'Segment'       : 'segment',
    'Order Date'    : 'order_date',
    'Region ID'     : 'region_id',
    'Region'        : 'region',
    'Country'       : 'country',
    'State'         : 'state',
    'City'          : 'city',
    'Product Name'  : 'product_name',
    'Category'      : 'category',
    'Sub-Category'  : 'sub_category',
    'Sales'         : 'sales',
    'Quantity'      : 'quantity',
    'Profit'        : 'profit',
    'Margin'        : 'margin',
    'Revenue'       : 'revenue',
    'Total_Cost'    : 'total_cost',
    'Growth'        : 'growth',
    'Target'        : 'target',
    'Achievement'   : 'achievement',
    'Month_Index'   : 'month_index',
    'Year'          : 'year',
    'Month'         : 'month',
    'Quarter'       : 'quarter',
}, inplace=True)

fact_sales = df[[
    'order_id', 'product_id', 'customer_id', 'order_date', 'region_id',
    'sales', 'quantity', 'profit', 'margin', 'revenue', 'total_cost',
    'growth', 'target', 'achievement', 'month_index'
]]

dim_customer = df[['customer_id', 'customer_name', 'segment']].drop_duplicates(subset=['customer_id'])
dim_product  = df[['product_id', 'product_name', 'category', 'sub_category']].drop_duplicates(subset=['product_id'])
dim_region   = df[['region_id', 'region', 'country', 'state', 'city']].drop_duplicates(subset=['region_id'])
dim_date     = df[['order_date', 'year', 'month', 'quarter']].drop_duplicates(subset=['order_date'])

print("✔ Tables FACT et DIMENSIONS prêtes")

# ============================================================
# 5. LOAD
# ============================================================

print("\n🛢️ Chargement dans la base de données SQL Server...")

engine = create_engine("mssql+pyodbc://YOUR_SERVER_NAME/SALESDW?driver=ODBC+Driver+17+for+SQL+Server&trusted_connection=yes")

dim_customer.to_sql("dim_customer", engine, if_exists="append", index=False)
dim_product.to_sql("dim_product",  engine, if_exists="append", index=False)
dim_region.to_sql("dim_region",    engine, if_exists="append", index=False)
dim_date.to_sql("dim_date",        engine, if_exists="append", index=False)
fact_sales.to_sql("fact_sales",    engine, if_exists="append", index=False)

print("✅ Toutes les tables chargées avec succès dans SALESDW")

# ============================================================
# 6. FIN DU PIPELINE
# ============================================================

print("\n🎉 ETL COMPLET TERMINÉ ! Prêt pour Power BI et analyses IA")