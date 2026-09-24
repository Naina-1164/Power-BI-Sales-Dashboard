# Power BI Sales Dashboard

A beginner-friendly Power BI project improved step by step using the same small sales dataset.

## Version 3 - First DAX Measures

Version 3 introduces basic DAX measures without adding complex relationships or advanced calculations.

### Measures

```DAX
Total Sales = SUM(sales_data[Sales])
Total Quantity = SUM(sales_data[Quantity])
```

### Suggested Report Update

- Use `Total Sales` in the Total Sales card
- Use `Total Quantity` in the Quantity card
- Keep Category and Product slicers
- Check that the cards respond to slicer selections
- Report title: **Sales Dashboard - Version 3**

## Concepts Practiced

- Creating a Power BI measure
- Basic DAX `SUM()`
- Using measures in Card visuals
- Understanding filter interaction with slicers

## Learning Progress

**Version 1:** Basic visuals and Category slicer  
**Version 2:** Total Quantity card, Product slicer, and cleaner presentation  
**Version 3:** First basic DAX measures

Complex DAX, relationships, time intelligence, and advanced Power Query work are intentionally left for later versions.
