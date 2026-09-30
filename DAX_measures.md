# Power BI DAX Measures

## Version 3 - Basic Measures

```DAX
Total Sales = SUM(sales_data[Sales])
Total Quantity = SUM(sales_data[Quantity])
```

## Version 4 - Sales Percentage

```DAX
Sales % of Total =
DIVIDE(
    [Total Sales],
    CALCULATE(
        [Total Sales],
        ALL(sales_data)
    )
)
```

Format `Sales % of Total` as Percentage and use it in a Card visual. Test the Category and Product slicers to observe how the selected sales value compares with overall sales.

This is the first small introduction to `CALCULATE()`, `ALL()`, and filter context. More complex DAX is intentionally left for later.
