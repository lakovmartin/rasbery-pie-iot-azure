SELECT
    System.Timestamp AS timestamp,
    AVG(CAST(JSON_VALUE(messageBody, '$.temperature') AS float)) AS avg_temperature,
    AVG(CAST(JSON_VALUE(messageBody, '$.humidity') AS float)) AS avg_humidity
INTO
    output
FROM
    input
TIMESTAMP BY
    timestamp
GROUP BY
    TumblingWindow(second, 10)
