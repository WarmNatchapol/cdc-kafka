CREATE TABLE source.fares (
    passenger_id INT,
    card_type VARCHAR(7),
    origin_id INT,
    origin_name VARCHAR(50),
    destination_id INT,
    destination_name VARCHAR(50),
    PRIMARY KEY (passenger_id)
);


INSERT INTO source.fares (
    passenger_id,
    card_type,
    origin_id,
    origin_name,
    destination_id,
    destination_name
) VALUES 
(1,"adult",1,"Khu Khot",5,"Saphan Mai"),
(2,"student",24,"Siam",17,"Mo Chit");