# Mixed Practice - Python + Sales CSV
# Uses the same sales_data.csv as the Power BI project.

import csv

total_sales = 0
total_quantity = 0
highest_sale = 0

with open("sales_data.csv", "r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        sale = float(row["Sales"])
        quantity = int(row["Quantity"])

        total_sales += sale
        total_quantity += quantity

        if sale > highest_sale:
            highest_sale = sale

print("--- Sales Summary ---")
print(f"Total Sales: ₹{total_sales:.2f}")
print(f"Total Quantity: {total_quantity}")
print(f"Highest Sale: ₹{highest_sale:.2f}")
