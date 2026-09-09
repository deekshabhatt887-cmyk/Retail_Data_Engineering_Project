from analytics import (
        get_total_sales, 
        get_top_selling_products,
        get_sales_by_city,
        get_monthly_sales,
        get_top_customers
        )

print("\nSALES BY CITY")
print("-----------------")
result = get_sales_by_city()
print(result)

print("\nTOTAL SALES")
print("-----------------")



result = get_total_sales()

print(result)

print("\nTOP SELLING PRODUCTS")
print("---------------------")

result = get_top_selling_products()
print(result)

print("\nMonthly Sales")
print("------------")
result = get_monthly_sales()
print(result)

print("\nTOP CUSTOMERS")
print("-----------")
result = get_top_customers()
print(result)

