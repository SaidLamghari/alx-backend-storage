-- Script pour créer la procédure stockée ComputeAverageWeightedScoreForUsers
-- Cette procédure calcule et enregistre
-- le score moyen pondéré pour tous les étudiants
-- Auteur SAID LAMGHARI

-- Délimiteur pour gérer les blocs de code
DELIMITER //

-- Définition de la procédure stockée sans paramètres d'entrée
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers ()
BEGIN
    DECLARE done INT DEFAULT FALSE;  -- Variable pour contrôler la fin de la boucle
    DECLARE user_id INT;             -- Variable pour stocker user_id
    DECLARE cur CURSOR FOR           -- Curseur pour itérer sur les user_id distincts
        SELECT DISTINCT user_id FROM corrections;
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE; -- Gestionnaire pour la fin du curseur
    
    -- Ouvrir le curseur et commencer à récupérer les user_id
    OPEN cur;
    read_loop: LOOP
        FETCH cur INTO user_id;
        IF done THEN
            LEAVE read_loop;
        END IF;
        
        -- Variables pour calculer le score moyen pondéré
        DECLARE total_wghtd_score FLOAT;
        DECLARE total_wghtd FLOAT;
        DECLARE average_score FLOAT;

        -- Calculer le score pondéré total pour l'utilisateur
        SELECT SUM(c.score * p.weight) INTO total_wghtd_score
        FROM corrections c
        JOIN projects p ON c.project_id = p.id
        WHERE c.user_id = user_id;

        -- Calculer le poids total pour l'utilisateur
        SELECT SUM(p.weight) INTO total_wghtd
        FROM corrections c
        JOIN projects p ON c.project_id = p.id
        WHERE c.user_id = user_id;

        -- Calculer le score moyen si total_wghtd
        -- est différent de zéro pour éviter la division par zéro
        IF total_wghtd > 0 THEN
            SET average_score = total_wghtd_score / total_wghtd;
        ELSE
            SET average_score = 0;
        END IF;

        -- Mettre à jour le champ average_score dans la table users pour le user_id actuel
        UPDATE users
        SET average_score = average_score
        WHERE id = user_id;
        
    END LOOP;
    
    -- Fermer le curseur
    CLOSE cur;

END //

-- Restaurer le délimiteur par défaut
DELIMITER ;
