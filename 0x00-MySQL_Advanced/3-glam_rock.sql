-- Liste des groupes avec le style
-- principal Glam rock, classés par
-- leur longévité en années jusqu'à 2022
-- Auteur SAID LAMGHARI

SELECT band_name,
       IF(split != 0 AND formed != 0, (2022 - formed) - split, 0) as lifespan
FROM metal_bands
WHERE style LIKE '%Glam rock%'
ORDER BY lifespan DESC, band_name;
