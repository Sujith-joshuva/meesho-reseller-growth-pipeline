-- =====================================================
-- Query 1: Monthly category revenue
-- =====================================================

SELECT
    month,
    category,
    ROUND(SUM(quantity * unit_price), 2) AS revenue,
    COUNT(*) AS n_orders
FROM orders
GROUP BY
    month,
    category
ORDER BY
    CASE month
        WHEN 'April' THEN 1
        WHEN 'May' THEN 2
        WHEN 'June' THEN 3
    END,
    category;


-- =====================================================
-- Query 2: Region-wise revenue and order count
-- =====================================================

SELECT
    r.region,
    ROUND(SUM(o.quantity * o.unit_price), 2) AS revenue,
    COUNT(*) AS n_orders
FROM orders o
JOIN resellers r
    ON o.reseller_id = r.reseller_id
GROUP BY
    r.region
ORDER BY
    revenue DESC;


-- =====================================================
-- Query 3: Top resellers by total spending
-- =====================================================

SELECT
    r.reseller_id,
    r.reseller_name,
    ROUND(SUM(o.quantity * o.unit_price), 2) AS total_spend
FROM resellers AS r
INNER JOIN orders AS o
    ON r.reseller_id = o.reseller_id
GROUP BY
    r.reseller_id,
    r.reseller_name
HAVING
    SUM(o.quantity * o.unit_price) > 50000
ORDER BY
    total_spend DESC
LIMIT 5;


-- =====================================================
-- Query 4: Resellers with no orders
-- =====================================================

SELECT
    r.reseller_id,
    r.reseller_name,
    r.region
FROM resellers AS r
LEFT JOIN orders AS o
    ON r.reseller_id = o.reseller_id
WHERE
    o.order_id IS NULL;


-- =====================================================
-- Query 5: June Delivered Orders AOV
-- =====================================================

SELECT
    ROUND(
        SUM(unit_price * quantity) / COUNT(DISTINCT order_id),
        2
    ) AS average_order_value
FROM orders
WHERE
    month = 'June'
    AND status = 'Delivered';