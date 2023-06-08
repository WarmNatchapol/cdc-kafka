CREATE STREAM ksqlstream WITH (KAFKA_TOPIC='mysql-source.source.fares', VALUE_FORMAT='AVRO');

CREATE OR REPLACE STREAM ksqlstream_processed AS
SELECT
after->passenger_id AS passenger_id,
after->card_type AS card_type,
after->origin_id AS origin_id,
after->origin_name AS origin_name,
after->destination_id AS destination_id,
after->destination_name AS destination_name,
ABS(after->origin_id - after->destination_id) AS total_stations,
10 + ABS(after->origin_id - after->destination_id) AS fares
FROM ksqlstream
WHERE op in ('c','u','r');