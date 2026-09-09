import streamlit as st
import pandas as pd
from analytics import (
    get_total_sales,
    get_top_selling_products,
    get_sales_by_city,
    get_monthly_sales,
    get_top_customers,
    get_dashboard_summary

)

st.set_page_config(
    page_title="Retail Data Enginnering Dashbaord",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Retail Data Engineering Dashboard")
st.subheader("📅 Select Date Range")

start_date = st.date_input(
    "Start Date"
)

end_date = st.date_input(
    "End Date"
)
if start_date > end_date:
    st.error("Start date cannot be after end date.")
    st.stop()
st.write("Selected period:", start_date, "to", end_date)

st.write("Retail sales  analaytics powered by PostgreeSQL and Pyhton")

total_sales = get_total_sales(start_date, end_date)
top_products = get_top_selling_products(start_date, end_date)
sales_by_city = get_sales_by_city(start_date, end_date)
monthly_sales = get_monthly_sales(start_date, end_date)
if monthly_sales.empty:
    st.info("No sales data available for the selected date range.")
else:
    monthly_sales["month"] = pd.to_datetime(monthly_sales["month"])

    st.subheader("📈 Monthly Sales")

    st.line_chart(
        monthly_sales.set_index("month")["total_sales"]
    )
top_customers =  get_top_customers()
summary = get_dashboard_summary(start_date, end_date)

# Display total sales
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        label="💰 Total Sales",
        value=f"₹{summary['total_sales'].iloc[0]:,.2f}"
    )

with col2:
    st.metric(
        label="📦 Units Sold",
        value=f"{summary['total_units_sold'].iloc[0]:,.0f}"
    )

with col3:
    st.metric(
        label="👥 Customers",
        value=f"{summary['total_customers'].iloc[0]:,.0f}"
    )

with col4:
    st.metric(
        label="🛍️ Products Sold",
        value=f"{summary['products_sold'].iloc[0]:,.0f}"
    )

# Display top products
st.subheader("📦 Top Selling Products")
st.bar_chart(
    top_products.set_index("product_name")["total_quantity_sold"]
)

# Display sales by city
st.subheader("🏙️ Sales by City")
st.bar_chart(
    sales_by_city.set_index("city")["total_sales"]
)

# Display monthly sales
st.subheader("📅 Monthly Sales")
monthly_sales["month"] = pd.to_datetime(monthly_sales["month"])

st.line_chart(
    monthly_sales.set_index("month")["total_sales"]
)
# Display top customers
st.subheader("👥 Top Customers")

st.bar_chart(
    top_customers.set_index("customer_name")["total_spent"]
)