-- Rank country origins of bands by the number of non-unique fans
SELECT origin, SUM(nb_fans) AS nb_fans
FROM metal_bands
GROUP BY origin
ORDER BY SUM(nb_fans) DESC;
