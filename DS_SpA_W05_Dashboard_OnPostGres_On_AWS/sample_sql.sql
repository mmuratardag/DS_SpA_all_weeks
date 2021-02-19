
-- Percentage of Orders from Countries grouped by Employees
SELECT "public"."orders"."shipcountry" AS "shipcountry", "Employees"."lastname" AS "lastname", count(distinct "public"."orders"."shipcountry") AS "count"
FROM "public"."orders"
LEFT JOIN "public"."customers" "Customers" ON "public"."orders"."customerid" = "Customers"."customerid" LEFT JOIN "public"."employees" "Employees" ON "public"."orders"."employeeid" = "Employees"."employeeid"
GROUP BY "public"."orders"."shipcountry", "Employees"."lastname"
ORDER BY "public"."orders"."shipcountry" ASC, "Employees"."lastname" ASC

-- Percentage of Orders from Customers grouped by Employees
SELECT "public"."orders"."customerid" AS "customerid", "Employees"."lastname" AS "lastname", count(distinct "public"."orders"."orderid") AS "count"
FROM "public"."orders"
LEFT JOIN "public"."customers" "Customers" ON "public"."orders"."customerid" = "Customers"."customerid" LEFT JOIN "public"."employees" "Employees" ON "public"."orders"."employeeid" = "Employees"."employeeid"
GROUP BY "public"."orders"."customerid", "Employees"."lastname"
ORDER BY "public"."orders"."customerid" ASC, "Employees"."lastname" ASC

-- Employees with Country counts
SELECT "Employees"."lastname" AS "lastname", count(distinct "public"."orders"."shipcountry") AS "count"
FROM "public"."orders"
LEFT JOIN "public"."customers" "Customers" ON "public"."orders"."customerid" = "Customers"."customerid" LEFT JOIN "public"."employees" "Employees" ON "public"."orders"."employeeid" = "Employees"."employeeid"
GROUP BY "Employees"."lastname"
ORDER BY "Employees"."lastname" ASC

-- Employees with Customer counts
SELECT "Employees"."lastname" AS "lastname", count(distinct "public"."orders"."customerid") AS "count"
FROM "public"."orders"
LEFT JOIN "public"."customers" "Customers" ON "public"."orders"."customerid" = "Customers"."customerid" LEFT JOIN "public"."employees" "Employees" ON "public"."orders"."employeeid" = "Employees"."employeeid"
GROUP BY "Employees"."lastname"
ORDER BY "Employees"."lastname" ASC
