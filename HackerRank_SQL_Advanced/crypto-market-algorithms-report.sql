WITH quarterly_volume AS(
    SELECT
        c.algorithm,
        SUM(volume) AS volume,
        YEAR(dt) AS year,
        QUARTER(dt) AS quarter
    FROM coins c
    JOIN transactions t ON t.coin_code = c.code
    WHERE YEAR(dt) = 2020
    GROUP BY c.algorithm, YEAR(dt), QUARTER(dt)
)
SELECT
    c.algorithm,
    qv1.volume AS transactions_Q1,
    qv2.volume AS trasnactions_Q2,
    qv3.volume AS transactions_Q3,
    qv4.volume AS transactions_Q4
FROM coins c
LEFT JOIN quarterly_volume qv1
    ON c.algorithm = qv1.algorithm AND qv1.year = 2020 AND qv1.quarter = 1
LEFT JOIN quarterly_volume qv2
    ON c.algorithm = qv2.algorithm AND qv2.year = 2020 AND qv2.quarter = 2
LEFT JOIN quarterly_volume qv3
    ON c.algorithm = qv3.algorithm AND qv3.year = 2020 AND qv3.quarter = 3
LEFT JOIN quarterly_volume qv4
    ON c.algorithm = qv4.algorithm AND qv4.year = 2020 AND qv4.quarter = 4
WHERE c.code <> "DOGE" -- NOT LIKE == <>
ORDER BY c.algorithm



