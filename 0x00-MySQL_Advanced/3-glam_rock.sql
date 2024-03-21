-- filter by glam rock
SELECT band_name,
    CASE
        WHEN split = NULL THEN 2022 - formed
        ELSE split - formed
    END AS lifespan
FROM metal_bands
WHERE style = 'Glam rock'
ORDER BY lifespan DESC;