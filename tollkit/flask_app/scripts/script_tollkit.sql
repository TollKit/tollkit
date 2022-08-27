-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema esquema_tollkit_intercon
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema esquema_tollkit_intercon
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `esquema_tollkit_intercon` DEFAULT CHARACTER SET utf8 COLLATE utf8_bin ;
-- -----------------------------------------------------
-- Schema new_schema2
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema new_schema3
-- -----------------------------------------------------
USE `esquema_tollkit_intercon` ;

-- -----------------------------------------------------
-- Table `esquema_tollkit_intercon`.`universities`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `esquema_tollkit_intercon`.`universities` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(255) NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `esquema_tollkit_intercon`.`admins`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `esquema_tollkit_intercon`.`admins` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` TEXT NULL,
  `lastname` TEXT NULL,
  `email` TEXT NULL,
  `password` TEXT NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `universities_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_admins_universities_idx` (`universities_id` ASC) VISIBLE,
  CONSTRAINT `fk_admins_universities`
    FOREIGN KEY (`universities_id`)
    REFERENCES `esquema_tollkit_intercon`.`universities` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `esquema_tollkit_intercon`.`students`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `esquema_tollkit_intercon`.`students` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(255) NULL,
  `lastname` VARCHAR(255) NULL,
  `temp` TEXT NULL,
  `has_mask` TEXT NULL,
  `has_studentCard` TEXT NULL,
  `has_covidCard` TEXT NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  `universities_id` INT NOT NULL,
  PRIMARY KEY (`id`, `universities_id`),
  INDEX `fk_students_universities1_idx` (`universities_id` ASC) VISIBLE,
  CONSTRAINT `fk_students_universities1`
    FOREIGN KEY (`universities_id`)
    REFERENCES `esquema_tollkit_intercon`.`universities` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `esquema_tollkit_intercon`.`tollkits`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `esquema_tollkit_intercon`.`tollkits` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `number_door` VARCHAR(255) NULL,
  `has_alcohol` VARCHAR(255) NULL,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `admins_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_tollkits_admins1_idx` (`admins_id` ASC) VISIBLE,
  CONSTRAINT `fk_tollkits_admins1`
    FOREIGN KEY (`admins_id`)
    REFERENCES `esquema_tollkit_intercon`.`admins` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `esquema_tollkit_intercon`.`tollkits_has_students`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `esquema_tollkit_intercon`.`tollkits_has_students` (
  `tollkits_id` INT NOT NULL,
  `students_id` INT NOT NULL,
  `students_universities_id` INT NOT NULL,
  PRIMARY KEY (`tollkits_id`, `students_id`, `students_universities_id`),
  INDEX `fk_tollkits_has_students_students1_idx` (`students_id` ASC, `students_universities_id` ASC) VISIBLE,
  INDEX `fk_tollkits_has_students_tollkits1_idx` (`tollkits_id` ASC) VISIBLE,
  CONSTRAINT `fk_tollkits_has_students_tollkits1`
    FOREIGN KEY (`tollkits_id`)
    REFERENCES `esquema_tollkit_intercon`.`tollkits` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_tollkits_has_students_students1`
    FOREIGN KEY (`students_id` , `students_universities_id`)
    REFERENCES `esquema_tollkit_intercon`.`students` (`id` , `universities_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
