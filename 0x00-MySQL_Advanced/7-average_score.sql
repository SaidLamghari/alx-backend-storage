-- Création de la procédure stockée
-- ComputeAverageScoreForUser
-- Cette procédure calcule et
-- met à jour le score moyen d'un étudiant.
-- Auteur SAID LAMGHARI

-- Supprime la procédure stockée ComputeAverageScoreForUser si elle existe déjà
DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser;
-- Change le délimiteur pour pouvoir utiliser '$$' comme délimiteur de fin pour la procédure
DELIMITER $$
-- Définit la procédure stockée ComputeAverageScoreForUser avec un paramètre en entrée
CREATE PROCEDURE ComputeAverageScoreForUser(
    IN user_id INT)  -- ID de l'utilisateur pour lequel calculer la moyenne
BEGIN
    -- Déclare une variable locale pour stocker la moyenne des scores
    DECLARE avg_score FLOAT;
    
    -- Calcule la moyenne des scores pour l'utilisateur donné
    SET avg_score = (SELECT AVG(score) FROM corrections AS C WHERE C.user_id = user_id);
    
    -- Met à jour la table 'users' avec la moyenne calculée
    UPDATE users SET average_score = avg_score WHERE id = user_id;
END$$
-- Restaure le délimiteur par défaut ';'
DELIMITER ;
