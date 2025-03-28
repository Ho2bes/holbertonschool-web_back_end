-- Use the metal_bands table to find the lifespan of glam rock bands.
SELECT
    band_name,
    (IFNULL(split, 2024) - formed) AS LIFESPAN
FROM
    metal_bands
WHERE
    style LIKE '%Glam rock%'
ORDER BY
    LIFESPAN DESC;
