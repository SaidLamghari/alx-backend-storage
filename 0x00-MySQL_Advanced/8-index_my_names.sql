-- Importer le dump de la table names si ce n'est pas déjà fait
-- Exécutez la commande suivante pour importer :
-- cat names.sql | mysql -uroot -p holberton
-- Auteur SAID LAMGHARI

-- Création de l'index idx_name_first sur la première lettre du champ name
CREATE INDEX idx_name_first ON names (name(1));
