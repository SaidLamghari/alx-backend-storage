-- Liste des groupes avec le style
-- principal Glam rock, classés par
-- leur longévité en années jusqu'à 2022
-- Auteur SAID LAMGHARI

SELECT band_name,
	IFNULL (split, 2022) - formed As lifespan
FROM metal_bands
WHERE style LIKE '%Glam rock%'
ORDER BY lifespan DESC, band_name;
