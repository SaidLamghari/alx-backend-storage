-- Création de la table users
-- si elle n'existe pas déjà
-- Assure que l'email est unique
-- et définit la liste des pays autorisés

CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255),
    country ENUM('US', 'CO', 'TN') NOT NULL DEFAULT 'US'
);
