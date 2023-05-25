#return business name, phone number and contact 
#from businesses with valid phone and contact
/*
WITH CTE AS(
    SELECT l.business_id AS id,
    l.phone AS phone,
    c.contact AS contact 
    FROM business_contact AS c, business_location AS l 
    WHERE l.business_id=c.business_id
)



SELECT id, phone, contact 
FROM CTE;
*/

SELECT l.business_id AS id,
    l.phone AS phone,
    c.contact AS contact 
    FROM business_contact AS c, business_location AS l 
    WHERE c.business_id=l.business_id;