-- Change le délimiteur temporairement
-- pour pouvoir inclure des blocs de code
-- Auteur SAID LAMGHARI

DELIMITER $$

-- Définit la fonction SafeDiv
CREATE FUNCTION SafeDiv(a INT, b INT)
RETURNS FLOAT
BEGIN
    -- Déclare une variable locale pour stocker le résultat de la division
    DECLARE result FLOAT;

    -- Vérifie si le dénominateur (b) est égal à 0
    IF b = 0 THEN
        -- Si b est 0, retourne 0
        SET result = 0;
    ELSE
        -- Sinon, effectue la division a / b
        SET result = a / b;
    END IF;

    -- Retourne le résultat de la division
    RETURN result;
END$$

-- Restaure le délimiteur par défaut ;
DELIMITER ;
