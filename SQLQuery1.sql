--1. Average price for each rating

select rating, AVG(price) AS avg_price  from test.dbo.books group by rating;

--2. The 5 most expensive books rated 4 or 5

select top 5 title , price ,rating from test.dbo.books where rating in (4,5) ORDER BY price DESC; 

--3. How many books are out of stock, per rating

select rating,count(*)AS out_of_stock_count from test.dbo.books where in_stock = 'False' group by rating;