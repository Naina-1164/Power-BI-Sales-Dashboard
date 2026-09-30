# Power BI Sales Dashboard

A beginner-friendly sales project improved step by step using the same small CSV dataset.

## Learning Progress

**Version 1:** Basic Power BI visuals and Category slicer  
**Version 2:** Quantity card, Product slicer, and cleaner presentation  
**Version 3:** First basic DAX measures  
**Mixed Practice:** Read the same Power BI CSV with beginner Python  
**Version 4:** Sales percentage measure and first filter-context practice

## Version 4 - Sales % of Total

Version 4 introduces one small DAX step beyond basic `SUM()`: calculating the selected sales value as a percentage of overall sales.

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

### Practice in Power BI Desktop

- Format `Sales % of Total` as Percentage
- Add it to a Card visual
- Test the existing Category and Product slicers
- Use the report title **Sales Dashboard - Version 4**

### Concepts Practiced

- Reusing an existing measure
- `DIVIDE()`
- First use of `CALCULATE()`
- `ALL()`
- Beginner introduction to filter context

## Mixed Practice - Python + Sales CSV

The same `sales_data.csv` is also used by `sales_summary.py` to calculate Total Sales, Total Quantity, and Highest Sale with Python's built-in `csv` module.

Advanced DAX, relationships, time intelligence, and complex dashboard design are intentionally left for later versions.
