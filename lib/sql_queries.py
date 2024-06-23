# 1. Select all female bears and return their names and ages
select_all_female_bears_return_name_and_age = """
    SELECT
        name,
        age
    FROM bears
    WHERE sex = 'F';
"""

# 2. Select all bears that are alive and return their names and temperaments
select_alive_bears_return_name_and_temperament = """
    SELECT
        name,
        temperament
    FROM bears
    WHERE alive = 1;
"""

# 3. Select all bears and return their names and colors, ordered by name alphabetically
select_all_bears_ordered_by_name = """
    SELECT
        name,
        color
    FROM bears
    ORDER BY name ASC;
"""

# 4. Select the oldest bear that is alive and return its name and age
select_oldest_alive_bear_return_name_and_age = """
    SELECT
        name,
        age
    FROM bears
    WHERE alive = 1
    ORDER BY age DESC
    LIMIT 1;
"""