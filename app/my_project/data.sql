-- Створення схеми, якщо вона не існує
DROP SCHEMA IF EXISTS `company_inventory`;
CREATE SCHEMA `company_inventory`;
USE `company_inventory`;

-- -----------------------------------------------------
-- Таблиця `access_points`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `access_points`;
CREATE TABLE IF NOT EXISTS `access_points` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `serial_number` VARCHAR(100) NULL DEFAULT NULL,
  `model` VARCHAR(100) NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `idx_serial_number` (`serial_number`)
);

-- Заповнення таблиці access_points
INSERT INTO `access_points` (`serial_number`, `model`)
VALUES
('AP-1001', 'Cisco Aironet 1850'),
('AP-1002', 'Ubiquiti UniFi AC Lite'),
('AP-1003', 'TP-Link EAP245'),
('AP-1004', 'Cisco Meraki MR33'),
('AP-1005', 'Aruba Instant On AP22');

-- -----------------------------------------------------
-- Таблиця `configurations`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `configurations`;
CREATE TABLE IF NOT EXISTS `configurations` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `processor` VARCHAR(100) NULL DEFAULT NULL,
  `memory` INT NULL DEFAULT NULL,
  `disk` INT NULL DEFAULT NULL,
  `graphics_card` VARCHAR(100) NULL DEFAULT NULL,
  PRIMARY KEY (`id`)
);

-- Заповнення таблиці configurations
INSERT INTO `configurations` (`processor`, `memory`, `disk`, `graphics_card`)
VALUES
('Intel i5', 8, 256, 'Intel UHD Graphics'),
('Intel i7', 16, 512, 'NVIDIA GeForce GTX 1050'),
('AMD Ryzen 5', 16, 1024, 'AMD Radeon Vega 8'),
('Intel i3', 4, 128, 'Intel HD Graphics'),
('Intel i9', 32, 2048, 'NVIDIA GeForce RTX 2080');

-- -----------------------------------------------------
-- Таблиця `computers`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `computers`;
CREATE TABLE IF NOT EXISTS `computers` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `serial_number` VARCHAR(100) NULL DEFAULT NULL,
  `type` VARCHAR(50) NULL DEFAULT NULL,
  `model` VARCHAR(100) NULL DEFAULT NULL,
  `configuration_id` INT NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  INDEX `idx_configuration_id` (`configuration_id`),
  UNIQUE KEY `idx_serial_number` (`serial_number`),
  CONSTRAINT `computers_ibfk_1`
    FOREIGN KEY (`configuration_id`)
    REFERENCES `configurations` (`id`)
    ON DELETE CASCADE
);

-- Заповнення таблиці computers
INSERT INTO `computers` (`serial_number`, `type`, `model`, `configuration_id`)
VALUES
('PC-1001', 'Desktop', 'Dell OptiPlex 7070', 1),
('PC-1002', 'Laptop', 'HP EliteBook 840', 2),
('PC-1003', 'Desktop', 'Lenovo ThinkCentre M720', 3),
('PC-1004', 'Laptop', 'MacBook Pro 13"', 4),
('PC-1005', 'Laptop', 'Acer Aspire 7', 5);

-- -----------------------------------------------------
-- Таблиця `employees`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `employees`;
CREATE TABLE IF NOT EXISTS `employees` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(100) NULL DEFAULT NULL,
  `last_name` VARCHAR(100) NULL DEFAULT NULL,
  `email` VARCHAR(100) NULL DEFAULT NULL,
  `phone` VARCHAR(15) NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `idx_email` (`email`)
);

-- Заповнення таблиці employees
INSERT INTO `employees` (`first_name`, `last_name`, `email`, `phone`)
VALUES
('John', 'Doe', 'john.doe@example.com', '123-456-7890'),
('Jane', 'Smith', 'jane.smith@example.com', '098-765-4321'),
('Jim', 'Beam', 'jim.beam@example.com', '555-123-4567'),
('Alice', 'Brown', 'alice.brown@example.com', '555-987-6543'),
('Bob', 'White', 'bob.white@example.com', '555-000-1111');

-- -----------------------------------------------------
-- Таблиця `offices`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `offices`;
CREATE TABLE IF NOT EXISTS `offices` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(100) NULL DEFAULT NULL,
  `address` VARCHAR(255) NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `idx_name` (`name`)
);

-- Заповнення таблиці offices
INSERT INTO `offices` (`name`, `address`)
VALUES
('Headquarters', '123 Main St, City A'),
('Branch Office', '456 Elm St, City B'),
('Remote Office', '789 Oak St, City C'),
('Satellite Office', '101 Maple St, City D'),
('Warehouse', '202 Pine St, City E');

-- -----------------------------------------------------
-- Таблиця `monitors`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `monitors`;
CREATE TABLE IF NOT EXISTS `monitors` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `serial_number` VARCHAR(100) NULL DEFAULT NULL,
  `model` VARCHAR(100) NULL DEFAULT NULL,
  `screen_size` DECIMAL(5,2) NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `idx_serial_number` (`serial_number`)
);

-- Заповнення таблиці monitors
INSERT INTO `monitors` (`serial_number`, `model`, `screen_size`)
VALUES
('MON-1001', 'Dell U2718Q', 27.00),
('MON-1002', 'HP Z24n', 24.00),
('MON-1003', 'Samsung S32D850T', 32.00),
('MON-1004', 'LG 29WK600', 29.00),
('MON-1005', 'Acer Predator X34', 34.00);

-- -----------------------------------------------------
-- Таблиця `printers`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `printers`;
CREATE TABLE IF NOT EXISTS `printers` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `serial_number` VARCHAR(100) NULL DEFAULT NULL,
  `model` VARCHAR(100) NULL DEFAULT NULL,
  `type` VARCHAR(50) NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `idx_serial_number` (`serial_number`)
);

-- Заповнення таблиці printers
INSERT INTO `printers` (`serial_number`, `model`, `type`)
VALUES
('PR-1001', 'HP LaserJet Pro', 'Laser'),
('PR-1002', 'Canon PIXMA TS9120', 'Inkjet'),
('PR-1003', 'Epson EcoTank ET-4760', 'Inkjet'),
('PR-1004', 'Brother HL-L2350DW', 'Laser'),
('PR-1005', 'Xerox VersaLink B400', 'Laser');

-- -----------------------------------------------------
-- Таблиця `routers`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `routers`;
CREATE TABLE IF NOT EXISTS `routers` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `serial_number` VARCHAR(100) NULL DEFAULT NULL,
  `model` VARCHAR(100) NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `idx_serial_number` (`serial_number`)
);

-- Заповнення таблиці routers
INSERT INTO `routers` (`serial_number`, `model`)
VALUES
('R-1001', 'Cisco RV340'),
('R-1002', 'Netgear Nighthawk AX8'),
('R-1003', 'TP-Link Archer C7'),
('R-1004', 'Linksys EA7500'),
('R-1005', 'ASUS RT-AC68U');

-- -----------------------------------------------------
-- Таблиця `ip_phones`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `ip_phones`;
CREATE TABLE IF NOT EXISTS `ip_phones` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `serial_number` VARCHAR(100) NULL DEFAULT NULL,
  `model` VARCHAR(100) NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `idx_serial_number` (`serial_number`)
);

-- Заповнення таблиці ip_phones
INSERT INTO `ip_phones` (`serial_number`, `model`)
VALUES
('IP-1001', 'Cisco IP Phone 7841'),
('IP-1002', 'Polycom VVX 250'),
('IP-1003', 'Yealink SIP-T46S'),
('IP-1004', 'Avaya J139'),
('IP-1005', 'Grandstream GXP2170');

-- -----------------------------------------------------
-- Таблиця `employee_equipment`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `employee_equipment`;
CREATE TABLE IF NOT EXISTS `employee_equipment` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `employee_id` INT NULL DEFAULT NULL,
  `computer_id` INT NULL DEFAULT NULL,
  `monitor_id` INT NULL DEFAULT NULL,
  `printer_id` INT NULL DEFAULT NULL,
  `router_id` INT NULL DEFAULT NULL,
  `access_point_id` INT NULL DEFAULT NULL,
  `ip_phone_id` INT NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  INDEX `idx_employee_id` (`employee_id`),
  INDEX `idx_computer_id` (`computer_id`),
  INDEX `idx_monitor_id` (`monitor_id`),
  INDEX `idx_printer_id` (`printer_id`),
  INDEX `idx_router_id` (`router_id`),
  INDEX `idx_access_point_id` (`access_point_id`),
  INDEX `idx_ip_phone_id` (`ip_phone_id`),
  CONSTRAINT `employee_equipment_ibfk_1`
    FOREIGN KEY (`employee_id`)
    REFERENCES `employees` (`id`)
    ON DELETE CASCADE,
  CONSTRAINT `employee_equipment_ibfk_2`
    FOREIGN KEY (`computer_id`)
    REFERENCES `computers` (`id`)
    ON DELETE CASCADE,
  CONSTRAINT `employee_equipment_ibfk_3`
    FOREIGN KEY (`monitor_id`)
    REFERENCES `monitors` (`id`)
    ON DELETE CASCADE,
  CONSTRAINT `employee_equipment_ibfk_4`
    FOREIGN KEY (`printer_id`)
    REFERENCES `printers` (`id`)
    ON DELETE CASCADE,
  CONSTRAINT `employee_equipment_ibfk_5`
    FOREIGN KEY (`router_id`)
    REFERENCES `routers` (`id`)
    ON DELETE CASCADE,
  CONSTRAINT `employee_equipment_ibfk_6`
    FOREIGN KEY (`access_point_id`)
    REFERENCES `access_points` (`id`)
    ON DELETE CASCADE,
  CONSTRAINT `employee_equipment_ibfk_7`
    FOREIGN KEY (`ip_phone_id`)
    REFERENCES `ip_phones` (`id`)
    ON DELETE CASCADE
);

-- Заповнення таблиці employee_equipment
INSERT INTO `employee_equipment` (`employee_id`, `computer_id`, `monitor_id`, `printer_id`, `router_id`, `access_point_id`, `ip_phone_id`)
VALUES
(1, 1, 1, 1, 1, 1, 1),
(2, 2, 2, 2, 2, 2, 2),
(3, 3, 3, 3, 3, 3, 3),
(4, 4, 4, 4, 4, 4, 4),
(5, 5, 5, 5, 5, 5, 5);

-- -----------------------------------------------------
-- Таблиця `office_equipment`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `office_equipment`;
CREATE TABLE IF NOT EXISTS `office_equipment` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `office_id` INT NULL DEFAULT NULL,
  `printer_id` INT NULL DEFAULT NULL,
  `router_id` INT NULL DEFAULT NULL,
  `access_point_id` INT NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  INDEX `idx_office_id` (`office_id`),
  INDEX `idx_printer_id` (`printer_id`),
  INDEX `idx_router_id` (`router_id`),
  INDEX `idx_access_point_id` (`access_point_id`),
  CONSTRAINT `office_equipment_ibfk_1`
    FOREIGN KEY (`office_id`)
    REFERENCES `offices` (`id`)
    ON DELETE CASCADE,
  CONSTRAINT `office_equipment_ibfk_2`
    FOREIGN KEY (`printer_id`)
    REFERENCES `printers` (`id`)
    ON DELETE CASCADE,
  CONSTRAINT `office_equipment_ibfk_3`
    FOREIGN KEY (`router_id`)
    REFERENCES `routers` (`id`)
    ON DELETE CASCADE,
  CONSTRAINT `office_equipment_ibfk_4`
    FOREIGN KEY (`access_point_id`)
    REFERENCES `access_points` (`id`)
    ON DELETE CASCADE
);

-- Заповнення таблиці office_equipment
INSERT INTO `office_equipment` (`office_id`, `printer_id`, `router_id`, `access_point_id`)
VALUES
(1, 1, 1, 1),
(2, 2, 2, 2),
(3, 3, 3, 3),
(4, 4, 4, 4),
(5, 5, 5, 5);

SELECT 
    e.first_name, 
    e.last_name,
    c.model AS computer_model,
    m.model AS monitor_model,
    p.model AS printer_model,
    r.model AS router_model,
    ap.model AS access_point_model,
    ip.model AS ip_phone_model
FROM 
    employee_equipment ee
JOIN 
    employees e ON ee.employee_id = e.id
JOIN 
    computers c ON ee.computer_id = c.id
JOIN 
    monitors m ON ee.monitor_id = m.id
JOIN 
    printers p ON ee.printer_id = p.id
JOIN 
    routers r ON ee.router_id = r.id
JOIN 
    access_points ap ON ee.access_point_id = ap.id
JOIN 
    ip_phones ip ON ee.ip_phone_id = ip.id
ORDER BY 
    e.last_name;


   
SELECT 
    o.name AS office_name,
    p.model AS printer_model,
    r.model AS router_model,
    ap.model AS access_point_model
FROM 
    office_equipment oe
JOIN 
    offices o ON oe.office_id = o.id
JOIN 
    printers p ON oe.printer_id = p.id
JOIN 
    routers r ON oe.router_id = r.id
JOIN 
    access_points ap ON oe.access_point_id = ap.id
ORDER BY 
    o.name;
	



