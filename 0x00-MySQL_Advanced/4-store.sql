-- Création d'un déclencheur pour diminuer la quantité d'un article après l'ajout d'une nouvelle commande
-- Ce déclencheur mettra à jour automatiquement la quantité d'un article dans la table items
-- après l'insertion d'une nouvelle commande dans la table orders.

-- Changer le délimiteur pour gérer le corps du déclencheur
DELIMITER $$

-- Définition du déclencheur
CREATE TRIGGER decrease_quantity_trigger AFTER INSERT ON orders
FOR EACH ROW
BEGIN
    -- Mettre à jour la table items pour diminuer la quantité de l'article commandé
    -- Le mot-clé NEW fait référence à la nouvelle ligne insérée dans la table orders
    UPDATE items
    SET quantity = quantity - NEW.number
    WHERE name = NEW.item_name;
END$$

-- Réinitialiser le délimiteur par défaut
DELIMITER ;
