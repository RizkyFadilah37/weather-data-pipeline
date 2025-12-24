{{config(
    materialized='table',
    unique_key='id'
)}}

with source as (SELECT * 
FROM {{ source('dev', 'raw_weather_data') }}),

deduped as (
    SELECT 
        *,
        ROW_NUMBER() OVER (PARTITION BY id ORDER BY inserted_at DESC) as row_num
    FROM source
)

SELECT 
    id,
    city,
    temperature,
    weather_desc as weather_description,
    wind_speed,
    time as weather_time_local,
    inserted_at AT TIME ZONE 'UTC' AT TIME ZONE utc_offset as inserted_at_local,
    inserted_at as inserted_at_utc
FROM deduped
WHERE row_num = 1