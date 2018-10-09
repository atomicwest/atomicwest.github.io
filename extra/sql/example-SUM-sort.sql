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


--attempt SUM  as a filter condition
SELECT name, SUM(spending)
FROM #tmpOrders
WHERE SUM(spending) > 100

