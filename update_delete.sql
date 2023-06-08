DELETE FROM source.fares WHERE passenger_id = 1;

UPDATE source.fares 
SET card_type = 'adult'
WHERE passenger_id = 2;