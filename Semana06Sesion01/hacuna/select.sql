select o.idenvio, e.detalle, count(o.idenvio) from Ordenes O
inner join envios e on o.idenvio = e.idenvio
group by o.idenvio,e.detalle

select * from ordenes

select c.nombrecliente,
e.detalle,
pr.nombreproducto,
s.detalle,
cd.detalle,
* from ordenes o
inner join clientes c on o.idcliente = c.idcliente
inner join envios e on o.idenvio = e.idenvio
inner join productos pr on o.idproduto = pr.idproduto
inner join segmentos s on c.idsegmento = s.idsegmento
inner join ciudades cd on c.idciudad = cd.idciudad
