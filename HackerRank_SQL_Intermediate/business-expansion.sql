-- Business Expansion
SELECT ua.id, ua.first_name, ua.last_name, cu.id, cu.customer_name, COUNT(cu.id)
FROM customer cu, user_account ua, contact c
WHERE cu.id = ua.customer_id AND ua.id = c.user_account_id
GROUP BY ua.id, ua.first_name, ua.last_name, cu.id, cu, customer_name
HAVING COUNT(cu.id) > 1;