-- Création de la procédure stockée
-- ComputeAverageScoreForUser
-- Cette procédure calcule et
-- met à jour le score moyen d'un étudiant.
-- Auteur SAID LAMGHARI

DELIMITER $$

CREATE PROCEDURE ComputeAverageScoreForUser(
    IN user_id INT
)
BEGIN
    DECLARE avg_score DECIMAL(10, 2);

    -- Calculer la moyenne des scores pour l'utilisateur donné
    SELECT AVG(score) INTO avg_score
    FROM corrections
    WHERE user_id = user_id;

    -- Mettre à jour la colonne average_score dans la table users
    UPDATE users
    SET average_score = avg_score
    WHERE id = user_id;

END$$

DELIMITER ;
