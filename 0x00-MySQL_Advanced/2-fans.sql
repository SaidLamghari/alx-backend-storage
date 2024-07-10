-- Calcul du nombre total de fans
-- par origine des groupes de métal,
-- classé par ordre décroissant

SELECT origin, SUM(nb_fans) AS nb_fans
FROM `metal_bands`
GROUP BY origin
ORDER BY nb_fans DESC;
