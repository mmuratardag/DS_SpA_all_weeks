
SELECT c."customerID", c."companyName", sum(od."unitPrice"*od.quantity) as totalrevenue
FROM customers AS c
JOIN orders AS o ON o."customerID" = c."customerID"
JOIN order_details AS od ON od."orderID" = o."orderID"
GROUP BY c."customerID", c."companyName"
ORDER BY totalrevenue DESC
LIMIT 3;
