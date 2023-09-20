-- increases the max length for group concat
SET SESSION group_concat_max_len = 1000000;
WITH
ranked_scores AS(
    SELECT
        event_id,
        participant_name,
        score,
        DENSE_RANK() OVER(
            PARTITION BY event_id
            ORDER BY score DESC
        ) AS ranking
    FROM (
        SELECT event_id, participant_name, MAX(score) AS score
        FROM scoretable
        GROUP BY event_id, participant_name
    ) t
)
SELECT 
    event_id,
    GROUP_CONCAT(CASE WHEN ranking = 1 THEN participant_name END ORDER BY participant_name) AS first,
    GROUP_CONCAT(CASE WHEN ranking = 2 THEN participant_name END ORDER BY participant_name) AS second,
    GROUP_CONCAT(CASE WHEN ranking = 3 THEN participant_name END ORDER BY participant_name) AS third
FROM ranked_scores
GROUP BY event_id
ORDER BY event_id;