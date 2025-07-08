

CREATE TEMPORARY TABLE transmitidas (
    cod_empresa INT,
    numero_os INT
);

INSERT INTO transmitidas (cod_empresa, numero_os)
SELECT DISTINCT cod_empresa, numero_os  
FROM transferred_os;


SELECT cod_empresa, numero_os FROM transmitidas;


SELECT oc.cod_empresa
	,oc.numero_os
	FROM os_capa oc 
	INNER JOIN os_cliente c ON(oc.cod_empresa = c.cod_empresa and oc.numero_os = c.numero_os)
	WHERE NOT EXISTS (SELECT 1 
						FROM transmitidas t
						WHERE t.cod_empresa = oc.cod_empresa
						AND t.numero_os = oc.numero_os
						);
						