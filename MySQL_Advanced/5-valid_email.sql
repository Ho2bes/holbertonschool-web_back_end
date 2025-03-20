--  5. Create a trigger that sets the valid_email column to 0 if the email column is updated.
DELIMITER //

CREATE TRIGGER reset_valid_email_after_update
BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
    IF NEW.email <> OLD.email THEN
        SET NEW.valid_email = 0;
    END IF;
END //

DELIMITER ;
