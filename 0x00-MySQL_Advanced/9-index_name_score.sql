-- Crée l'index idx_name_first_score
-- sur le premier caractère du nom
-- et le premier chiffre du score
-- Auteur SAID LAMGHARI

CREATE INDEX idx_name_first_score ON names ((name(1)), (score));

