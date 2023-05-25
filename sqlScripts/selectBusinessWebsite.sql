#Selects all business name and website with valid address

SELECT n.business_name,c.website
FROM business_name_category AS n 
LEFT JOIN business_contact AS c 
ON n.business_id=c.business_id
WHERE REGEXP_LIKE(c.website,'[a-zA-Z0-9./-_:]*[.]com$');