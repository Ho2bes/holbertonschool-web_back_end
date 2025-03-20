-- Content: Create a view named need_meeting that contains the names of students who have a score less than 80 and have not had a meeting in the last month.
CREATE VIEW need_meeting AS
SELECT name
FROM students
WHERE score < 80 AND
	(last_meeting IS NULL OR last_meeting < DATE_SUB(CURDATE(), INTERVAL 1 MONTH));
