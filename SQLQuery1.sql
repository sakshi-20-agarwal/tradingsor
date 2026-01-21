USE TradingSandbox;
GO

CREATE VIEW TopSellingProducts AS
SELECT 
    p.ProductID,
    p.ProductName,
    SUM(o.Quantity) AS TotalUnitsSold,
    SUM(o.Quantity * p.UnitPrice) AS TotalSales
FROM Orders o
INNER JOIN Products p ON o.ProductID = p.ProductID
GROUP BY p.ProductID, p.ProductName;

