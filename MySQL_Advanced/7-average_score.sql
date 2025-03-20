-- This script creates a stored procedure that computes the average score for a given user and updates the average_score column in the users table.
DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser;
DELIMITER //
CREATE PROCEDURE ComputeAverageScoreForUser(
    IN p_user_id INT
    )
BEGIN
	DECLARE avg_score DECIMAL(10, 2);

    SELECT AVG(score) INTO avg_score
 	FROM corrections
 	WHERE user_id = p_user_id;

	UPDATE users
    SET average_score = avg_score
    WHERE id = p_user_id;
END //
DELIMITER ;
