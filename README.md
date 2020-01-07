# SQLAlchemyExp

# SQL COMMAND TO CREATE PROCEDURE
DELIMITER //
 
CREATE PROCEDURE GetUsersByAge(
	IN age INT
)
BEGIN
    SELECT * FROM users WHERE age = age;
END //
 
DELIMITER ;