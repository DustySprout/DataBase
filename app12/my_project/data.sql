CREATE SCHEMA IF NOT EXISTS `company_inventory` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci ;
USE `company_inventory` ;

-- -----------------------------------------------------
-- Table `company_inventory`.`access_points`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `company_inventory`.`access_points` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `serial_number` VARCHAR(100) NULL DEFAULT NULL,
  `model` VARCHAR(100) NULL DEFAULT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 6
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `company_inventory`.`configurations`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `company_inventory`.`configurations` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `processor` VARCHAR(100) NULL DEFAULT NULL,
  `memory` INT NULL DEFAULT NULL,
  `disk` INT NULL DEFAULT NULL,
  `graphics_card` VARCHAR(100) NULL DEFAULT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 6
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `company_inventory`.`computers`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `company_inventory`.`computers` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `serial_number` VARCHAR(100) NULL DEFAULT NULL,
  `type` VARCHAR(50) NULL DEFAULT NULL,
  `model` VARCHAR(100) NULL DEFAULT NULL,
  `configuration_id` INT NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  INDEX `configuration_id` (`configuration_id` ASC) VISIBLE,
  INDEX `idx_serial_number` (`serial_number` ASC) VISIBLE,
  CONSTRAINT `computers_ibfk_1`
    FOREIGN KEY (`configuration_id`)
    REFERENCES `company_inventory`.`configurations` (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 6
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `company_inventory`.`employees`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `company_inventory`.`employees` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(100) NULL DEFAULT NULL,
  `last_name` VARCHAR(100) NULL DEFAULT NULL,
  `email` VARCHAR(100) NULL DEFAULT NULL,
  `phone` VARCHAR(15) NULL DEFAULT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 6
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `company_inventory`.`offices`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `company_inventory`.`offices` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(100) NULL DEFAULT NULL,
  `address` VARCHAR(255) NULL DEFAULT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 6
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `company_inventory`.`monitors`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `company_inventory`.`monitors` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `serial_number` VARCHAR(100) NULL DEFAULT NULL,
  `model` VARCHAR(100) NULL DEFAULT NULL,
  `screen_size` DECIMAL(5,2) NULL DEFAULT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 6
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `company_inventory`.`printers`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `company_inventory`.`printers` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `serial_number` VARCHAR(100) NULL DEFAULT NULL,
  `model` VARCHAR(100) NULL DEFAULT NULL,
  `type` VARCHAR(50) NULL DEFAULT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 6
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `company_inventory`.`routers`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `company_inventory`.`routers` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `serial_number` VARCHAR(100) NULL DEFAULT NULL,
  `model` VARCHAR(100) NULL DEFAULT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 6
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `company_inventory`.`ip_phones`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `company_inventory`.`ip_phones` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `serial_number` VARCHAR(100) NULL DEFAULT NULL,
  `model` VARCHAR(100) NULL DEFAULT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 6
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `company_inventory`.`employee_equipment`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `company_inventory`.`employee_equipment` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `employee_id` INT NULL DEFAULT NULL,
  `equipment_id` INT NULL DEFAULT NULL,
  `equipment_type` VARCHAR(50) NULL DEFAULT NULL,
  `office_id` INT NULL DEFAULT NULL,
  `issue_date` DATE NULL DEFAULT NULL,
  `return_date` DATE NULL DEFAULT NULL,
  `monitors_id` INT NOT NULL,
  `printers_id` INT NOT NULL,
  `routers_id` INT NOT NULL,
  `ip_phones_id` INT NOT NULL,
  `access_points_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `office_id` (`office_id` ASC) VISIBLE,
  INDEX `idx_employee` (`employee_id` ASC) VISIBLE,
  INDEX `idx_equipment` (`equipment_id` ASC) VISIBLE,
  INDEX `fk_employee_equipment_monitors1_idx` (`monitors_id` ASC) VISIBLE,
  INDEX `fk_employee_equipment_printers1_idx` (`printers_id` ASC) VISIBLE,
  INDEX `fk_employee_equipment_routers1_idx` (`routers_id` ASC) VISIBLE,
  INDEX `fk_employee_equipment_ip_phones1_idx` (`ip_phones_id` ASC) VISIBLE,
  INDEX `fk_employee_equipment_access_points1_idx` (`access_points_id` ASC) VISIBLE,
  CONSTRAINT `employee_equipment_ibfk_1`
    FOREIGN KEY (`employee_id`)
    REFERENCES `company_inventory`.`employees` (`id`),
  CONSTRAINT `employee_equipment_ibfk_2`
    FOREIGN KEY (`office_id`)
    REFERENCES `company_inventory`.`offices` (`id`),
  CONSTRAINT `fk_employee_equipment_monitors1`
    FOREIGN KEY (`monitors_id`)
    REFERENCES `company_inventory`.`monitors` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_employee_equipment_printers1`
    FOREIGN KEY (`printers_id`)
    REFERENCES `company_inventory`.`printers` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_employee_equipment_routers1`
    FOREIGN KEY (`routers_id`)
    REFERENCES `company_inventory`.`routers` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_employee_equipment_ip_phones1`
    FOREIGN KEY (`ip_phones_id`)
    REFERENCES `company_inventory`.`ip_phones` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_employee_equipment_access_points1`
    FOREIGN KEY (`access_points_id`)
    REFERENCES `company_inventory`.`access_points` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
AUTO_INCREMENT = 8
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;

-- Insert data into access_points
INSERT INTO `company_inventory`.`access_points` (`id`, `serial_number`, `model`)
VALUES 
(1, 'AP1001', 'Model A'),
(2, 'AP1002', 'Model B'),
(3, 'AP1003', 'Model C'),
(4, 'AP1004', 'Model D'),
(5, 'AP1005', 'Model E');

-- Insert data into configurations
INSERT INTO `company_inventory`.`configurations` (`id`, `processor`, `memory`, `disk`, `graphics_card`)
VALUES 
(1, 'Intel i5', 8, 256, 'NVIDIA GTX 1050'),
(2, 'Intel i7', 16, 512, 'NVIDIA GTX 1660'),
(3, 'AMD Ryzen 5', 16, 512, 'AMD RX 580'),
(4, 'AMD Ryzen 7', 32, 1024, 'NVIDIA RTX 3060'),
(5, 'Intel i3', 4, 128, 'None');

-- Insert data into computers
INSERT INTO `company_inventory`.`computers` (`id`, `serial_number`, `type`, `model`, `configuration_id`)
VALUES 
(1, 'C1001', 'Laptop', 'Dell XPS', 1),
(2, 'C1002', 'Desktop', 'HP Envy', 2),
(3, 'C1003', 'Desktop', 'Custom Build', 3),
(4, 'C1004', 'Laptop', 'MacBook Pro', 4),
(5, 'C1005', 'Laptop', 'Lenovo ThinkPad', 5);

-- Insert data into employees
INSERT INTO `company_inventory`.`employees` (`id`, `first_name`, `last_name`, `email`, `phone`)
VALUES 
(1, 'John', 'Doe', 'john@example.com', '1234567890'),
(2, 'Jane', 'Smith', 'jane@example.com', '2345678901'),
(3, 'Alice', 'Johnson', 'alice@example.com', '3456789012'),
(4, 'Bob', 'Brown', 'bob@example.com', '4567890123'),
(5, 'Charlie', 'Davis', 'charlie@example.com', '5678901234');

-- Insert data into offices
INSERT INTO `company_inventory`.`offices` (`id`, `name`, `address`)
VALUES 
(1, 'HQ', '123 Main St'),
(2, 'Branch A', '456 Elm St'),
(3, 'Branch B', '789 Oak St'),
(4, 'Branch C', '101 Pine St'),
(5, 'Branch D', '202 Maple St');

-- Insert data into monitors
INSERT INTO `company_inventory`.`monitors` (`id`, `serial_number`, `model`, `screen_size`)
VALUES 
(1, 'M1001', 'Dell 24', 24.0),
(2, 'M1002', 'HP 27', 27.0),
(3, 'M1003', 'Samsung 32', 32.0),
(4, 'M1004', 'LG UltraFine', 24.5),
(5, 'M1005', 'BenQ 28', 28.0);

-- Insert data into printers
INSERT INTO `company_inventory`.`printers` (`id`, `serial_number`, `model`, `type`)
VALUES 
(1, 'P1001', 'HP LaserJet', 'Laser'),
(2, 'P1002', 'Canon Pixma', 'Inkjet'),
(3, 'P1003', 'Epson EcoTank', 'Tank'),
(4, 'P1004', 'Brother HL', 'Laser'),
(5, 'P1005', 'Samsung Xpress', 'Laser');

-- Insert data into routers
INSERT INTO `company_inventory`.`routers` (`id`, `serial_number`, `model`)
VALUES 
(1, 'R1001', 'Cisco 2900'),
(2, 'R1002', 'Netgear Nighthawk'),
(3, 'R1003', 'TP-Link Archer'),
(4, 'R1004', 'Ubiquiti Edge'),
(5, 'R1005', 'Asus RT-AX');

-- Insert data into ip_phones
INSERT INTO `company_inventory`.`ip_phones` (`id`, `serial_number`, `model`)
VALUES 
(1, 'IP1001', 'Polycom VVX'),
(2, 'IP1002', 'Cisco CP-8800'),
(3, 'IP1003', 'Yealink SIP'),
(4, 'IP1004', 'Avaya 9600'),
(5, 'IP1005', 'Grandstream GXP');

-- Insert data into employee_equipment
INSERT INTO `company_inventory`.`employee_equipment` 
(`id`, `employee_id`, `equipment_id`, `equipment_type`, `office_id`, `issue_date`, `return_date`, `monitors_id`, `printers_id`, `routers_id`, `ip_phones_id`, `access_points_id`)
VALUES 
(1, 1, 1, 'Monitor', 1, '2024-01-01', NULL, 1, 1, 1, 1, 1),
(2, 2, 2, 'Printer', 2, '2024-02-01', NULL, 2, 2, 2, 2, 2),
(3, 3, 3, 'Router', 3, '2024-03-01', NULL, 3, 3, 3, 3, 3),
(4, 4, 4, 'IP Phone', 4, '2024-04-01', NULL, 4, 4, 4, 4, 4),
(5, 5, 5, 'Access Point', 5, '2024-05-01', NULL, 5, 5, 5, 5, 5);

SELECT 
    o.name AS office_name,
    e.first_name,
    e.last_name
FROM 
    company_inventory.offices o
LEFT JOIN 
    company_inventory.employee_equipment ee ON o.id = ee.office_id
LEFT JOIN 
    company_inventory.employees e ON ee.employee_id = e.id
ORDER BY 
    o.name, e.last_name;


SELECT 
    e.first_name,
    e.last_name,
    ee.equipment_type,
    CASE ee.equipment_type
        WHEN 'Monitor' THEN m.model
        WHEN 'Printer' THEN p.model
        WHEN 'Router' THEN r.model
        WHEN 'IP Phone' THEN ip.model
        WHEN 'Access Point' THEN ap.model
        ELSE 'Unknown'
    END AS equipment_model
FROM 
    company_inventory.employee_equipment ee
JOIN 
    company_inventory.employees e ON ee.employee_id = e.id
LEFT JOIN 
    company_inventory.monitors m ON ee.monitors_id = m.id
LEFT JOIN 
    company_inventory.printers p ON ee.printers_id = p.id
LEFT JOIN 
    company_inventory.routers r ON ee.routers_id = r.id
LEFT JOIN 
    company_inventory.ip_phones ip ON ee.ip_phones_id = ip.id
LEFT JOIN 
    company_inventory.access_points ap ON ee.access_points_id = ap.id
ORDER BY 
    e.last_name, ee.equipment_type;
    
DELIMITER //

CREATE PROCEDURE get_all_access_points()
BEGIN
    SELECT * FROM `company_inventory`.`access_points`;
END //

SELECT * FROM `company_inventory`.`access_points_log`;

DELIMITER ;

CALL get_all_access_points();

CREATE TABLE `company_inventory`.`access_points_log` (
    id INT AUTO_INCREMENT PRIMARY KEY,
    action VARCHAR(50),
    action_time DATETIME,
    details TEXT
);

DELIMITER //

CREATE TRIGGER access_points_insert_log
AFTER INSERT ON `company_inventory`.`access_points`
FOR EACH ROW
BEGIN
    INSERT INTO access_points_log (action, action_time, details)
    VALUES ('INSERT', NOW(), CONCAT('Added ID: ', NEW.id, ', Serial: ', NEW.serial_number));
END //

DELIMITER ;

DELIMITER //

CREATE TRIGGER access_points_update_log
AFTER UPDATE ON `company_inventory`.`access_points`
FOR EACH ROW
BEGIN
    INSERT INTO access_points_log (action, action_time, details)
    VALUES ('UPDATE', NOW(), CONCAT('Updated ID: ', OLD.id, ', New Serial: ', NEW.serial_number));
END //

DELIMITER ;


DELIMITER //

CREATE PROCEDURE insert_access_point(
    IN p_serial_number VARCHAR(100),
    IN p_model VARCHAR(100)
)
BEGIN
    INSERT INTO `company_inventory`.`access_points` (serial_number, model)
    VALUES (p_serial_number, p_model);
END //

DELIMITER ;

CALL insert_access_point('serial_number_value', 'model_value');
