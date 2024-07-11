-- Script pour créer la procédure stockée ComputeAverageWeightedScoreForUsers
-- Cette procédure calcule et enregistre
-- le score moyen pondéré pour tous les étudiants
-- Auteur SAID LAMGHARI

-- Supprime la procédure stockée ComputeAverageWeightedScoreForUsers si elle existe déjà
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUsers;

-- Change le délimiteur pour pouvoir utiliser $$ à la place de ;
DELIMITER $$

-- Crée une nouvelle procédure stockée ComputeAverageWeightedScoreForUsers
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
    -- Étape 1: Crée une table temporaire pour stocker les scores moyens pondérés calculés
    CREATE TEMPORARY TABLE IF NOT EXISTS temp_avg_weighted_scores (
        user_id INT PRIMARY KEY,
        avg_weighted_score FLOAT
    );

    -- Étape 2: Calcul des scores moyens pondérés pour chaque utilisateur et insertion dans la table temporaire
    INSERT INTO temp_avg_weighted_scores (user_id, avg_weighted_score)
    SELECT C.user_id, SUM(C.score * P.weight) / SUM(P.weight) AS avg_weighted_score
    FROM corrections AS C
    JOIN projects AS P ON C.project_id = P.id
    GROUP BY C.user_id;

    -- Étape 3: Mise à jour des scores moyens pondérés dans la table users à partir de la table temporaire
    UPDATE users AS U
    JOIN temp_avg_weighted_scores AS T ON U.id = T.user_id
    SET U.average_score = T.avg_weighted_score;

    -- Étape 4: Supprime la table temporaire une fois la mise à jour terminée pour libérer l'espace mémoire
    DROP TEMPORARY TABLE IF EXISTS temp_avg_weighted_scores;
END
$$

-- Rétablit le délimiteur par défaut
DELIMITER ;
