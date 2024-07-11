-- Script pour créer la procédure stockée ComputeAverageWeightedScoreForUser
-- Cette procédure calcule et met à jour le score moyen pondéré pour un utilisateur
-- Auteur SAID LAMGHARI

-- Délimiteur personnalisé pour gérer les blocs de code
DELIMITER //

-- Définition de la procédure stockée avec un paramètre en entrée : user_id
CREATE PROCEDURE ComputeAverageWeightedScoreForUser (IN user_id INT)
BEGIN
    -- Déclaration des variables locales pour le calcul
    DECLARE total_weighted_score FLOAT;
    DECLARE total_weight FLOAT;
    DECLARE average_score FLOAT;

    -- Calcul du score pondéré total pour l'utilisateur
    SELECT SUM(c.score * p.weight) INTO total_weighted_score
    FROM corrections c
    JOIN projects p ON c.project_id = p.id
    WHERE c.user_id = user_id;

    -- Calcul du poids total pour l'utilisateur
    SELECT SUM(p.weight) INTO total_weight
    FROM corrections c
    JOIN projects p ON c.project_id = p.id
    WHERE c.user_id = user_id;

    -- Calcul du score moyen si total_weight est
    -- différent de zéro pour éviter une division par zéro
    IF total_weight > 0 THEN
        SET average_score = total_weighted_score / total_weight;
    ELSE
        SET average_score = 0;
    END IF;

    -- Mise à jour du champ average_score dans la table users pour l'user_id spécifié
    UPDATE users
    SET average_score = average_score
    WHERE id = user_id;

END //

-- Restauration du délimiteur par défaut
DELIMITER ;
