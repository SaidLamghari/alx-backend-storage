-- Crée la vue need_meeting
-- Auteur SAID LAMGHARI

CREATE VIEW need_meeting AS
-- Sélectionne le nom des étudiants
-- qui ont un score strictement inférieur à 80
-- et qui n'ont pas eu de dernière réunion ou dont
-- la dernière réunion remonte à plus d'un mois
SELECT name
FROM students
WHERE score < 80
  AND (last_meeting IS NULL OR last_meeting < DATE_SUB(CURDATE(), INTERVAL 1 MONTH));
