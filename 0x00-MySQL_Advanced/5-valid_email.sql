-- Création d'un déclencheur pour réinitialiser valid_email lors de la modification de l'email
-- Ce déclencheur assure que valid_email est remis à 0 lorsque l'email est changé.

-- Changer le délimiteur pour gérer le corps du déclencheur
DELIMITER $$

-- Définition du déclencheur
CREATE TRIGGER reset_valid_email_trigger BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
    -- Vérifier si l'email a été modifié en comparant OLD et NEW values
    IF OLD.email != NEW.email THEN
        SET NEW.valid_email = 0; -- Réinitialiser valid_email à 0
    END IF;
END$$

-- Réinitialiser le délimiteur par défaut
DELIMITER ;
