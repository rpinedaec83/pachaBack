--SELECT

SELECT * FROM ordenes;

--filter
SELECT * FROM Ordenes
WHERE idcliente  = 234
order by venta desc

SELECT * FROM Ordenes order by venta asc

--count
SELECT idenvio, count (idenvio) from Ordenes
group by idenvio

