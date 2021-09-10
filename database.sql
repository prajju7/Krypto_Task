CREATE DATABASE krypto;
USE  krypto;
CREATE TABLE UserData (
    u_id VARCHAR(20) PRIMARY KEY,
    u_name VARCHAR(30),
    u_pass VARCHAR(30),
    alerts JSON
);
Alter table UserData add email varchar(30);
