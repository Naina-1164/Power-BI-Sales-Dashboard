# Power BI Sales Dashboard

A beginner-friendly sales project improved step by step using the same small CSV dataset.

## Learning Progress

**Version 1:** Basic Power BI visuals and Category slicer  
**Version 2:** Quantity card, Product slicer, and cleaner presentation  
**Version 3:** First basic DAX measures  
**Mixed Practice:** Read the same Power BI CSV with beginner Python

## Version 3 - First DAX Measures

```DAX
Total Sales = SUM(sales_data[Sales])
Total Quantity = SUM(sales_data[Quantity])
```

These measures can be used in Card visuals and tested with the existing slicers.

## Mixed Practice - Python + Sales CSV

The same `sales_data.csv` is now also used by `sales_summary.py`. The Python script uses the built-in `csv` module to calculate:

- Total Sales
- Total Quantity
- Highest Sale

### Python Concepts Practiced

- `csv.DictReader()`
- Reading CSV rows
- `int()` and `float()` conversion
- Loops and running totals
- A simple `if` condition

This is intentionally a small cross-tool exercise. Pandas, advanced DAX, relationships, and complex analysis are left for later.
