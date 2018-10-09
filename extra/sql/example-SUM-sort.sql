--create temp table

CREATE TABLE #tmpOrders (
	merchantID int
	,name VARCHAR(30)
	,spending decimal
	,spendDate DATETIME
)

--insert values into temp table
INSERT INTO #tmpOrders (
	merchantID, name, spending, spendDate
)
SELECT * FROM (VALUES 
	(311,'Mary', 45.35, '2018-05-11')
	,(432,'Jane', 789.56, '2018-04-28') 
	,(23,'Bob', 24.50, '2018-02-01')
	,(432,'Jane', 224.50, '2018-12-31') 
	,(54,'Jack', 67.67, '2019-10-22') 
	,(432,'Jane', 884.56, '2018-07-08') 
	,(23,'Bob', 743.50, '2018-03-01')
	) 
AS sampleTable(orderID, name, spending, spendDate)


--attempt SUM  as a filter condition; the WRONG way
SELECT name, SUM(spending)
FROM #tmpOrders
WHERE SUM(spending) > 100
--throws this error: An aggregate may not appear in the WHERE clause unless it is in a subquery contained in a HAVING clause or a select list, and the column being aggregated is an outer reference.


--using SUM with GROUP BY and HAVING; the proper way
SELECT name, SUM(spending)
FROM #tmpOrders
Group By spending, name HAVING  SUM(spending) > 100

/*
name	(No column name)
Bob	    1488
Jack	136
Jane	450
Jane	1580
Jane	1770
*/