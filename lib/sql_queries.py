select_all_female_bears_return_name_and_age = """
    SELECT name, age
    FROM bears
    WHERE sex='F';
"""

select_alive_bears_return_name_and_age = """
    SELECT name, age
    FROM bears
    WHERE alive=1;
"""

select_brown_bears_return_name_and_age = """
    SELECT name, age
    FROM bears
    WHERE color='Brown';
"""

select_old_bears_return_name_and_age = """
    SELECT name, age
    FROM bears
    WHERE age > 10;
"""

select_young_dead_bears_return_name_and_age = """
    SELECT name, age
    FROM bears
    WHERE alive=0 AND age < 10;
"""
