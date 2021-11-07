# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays"
user_table_drop = "DROP TABLE IF EXISTS users"
song_table_drop = "DROP TABLE IF EXISTS songs"
artist_table_drop = "DROP TABLE IF EXISTS artists"
time_table_drop = "DROP TABLE IF EXISTS time"

# CREATE TABLES

songplay_table_create = ("""
    CREATE TABLE IF NOT EXISTS songplays(
        songplay_id SERIAL PRIMARY KEY,
        start_time VARCHAR(20) NOT NULL,
        user_id INT DEFAULT NULL, 
        level VARCHAR(4),
        song_id VARCHAR(50) NOT NULL,
        artist_id VARCHAR(50) NOT NULL, 
        session_id NUMERIC NOT NULL, 
        location VARCHAR(50) NOT NULL,
        user_agent TEXT NOT NULL
    );
""")

user_table_create = ("""
    CREATE TABLE IF NOT EXISTS users(
        user_id INT DEFAULT NULL,
        first_name VARCHAR(50) NOT NULL,
        last_name VARCHAR(50) NOT NULL,
        gender CHAR DEFAULT NULL, 
        level VARCHAR(4)
    );
""")

song_table_create = ("""
    CREATE TABLE IF NOT EXISTS songs(
        song_id VARCHAR(50) NOT NULL PRIMARY KEY,
        title VARCHAR(50) NOT NULL,
        artist_id VARCHAR(50) NOT NULL UNIQUE,  
        year NUMERIC NOT NULL DEFAULT 0, 
        duration NUMERIC NOT NULL  
    );
""")

artist_table_create = ("""
    CREATE TABLE IF NOT EXISTS artists (
        artist_id VARCHAR(50) PRIMARY KEY,
        artist_name VARCHAR(50) NOT NULL, 
        artist_latitude NUMERIC,
        artist_longitude NUMERIC, 
        artist_location VARCHAR(50)
    );
""")

time_table_create = ("""
    CREATE TABLE IF NOT EXISTS time(
        start_time VARCHAR(50) NOT NULL,
        hour NUMERIC NOT NULL,
        day VARCHAR(20) NOT NULL,
        week NUMERIC NOT NULL,
        month VARCHAR(20) NOT NULL,
        year NUMERIC NOT NULL,
        weekday VARCHAR(20) NOT NULL
    );
""")

# INSERT RECORDS

songplay_table_insert = ("""
    INSERT INTO songplays(songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent)
    VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)
    ON CONFLICT (songplay_id)
    DO UPDATE 
    SET start_time = EXCLUDED.start_time,
        user_id = EXCLUDED.user_id,
        level = EXCLUDED.level,
        song_id = EXCLUDED.song_id,
        artist_id = EXCLUDED.artist_id,
        session_id = EXCLUDED.session_id,
        location = EXCLUDED.location,
        user_agent = EXCLUDED.user_agent;
""")

user_table_insert = ("""
    INSERT INTO users(user_id, first_name, last_name, gender, level)
    VALUES(%s, %s, %s, %s, %s)
    ON CONFLICT (user_id)
    DO UPDATE
    SET first_name = EXCLUDED.first_name,
        last_name = EXCLUDED.last_name,
        gender = EXCLUDED.gender,
        level = EXCLUDED.level; 
""")

song_table_insert = ("""
    INSERT INTO songs(song_id, title, artist_id, year, duration)
    VALUES(%s, %s, %s, %s, %s)
    ON CONFLICT (song_id)
    DO UPDATE
    SET title = EXCLUDED.title,
        artist_id = EXCLUDED.artist_id,
        year = EXCLUDED.year,
        duration = EXCLUDED.duration;
""")

artist_table_insert = ("""
    INSERT INTO artists(artist_id, artist_name, artist_latitude, artist_longitude, artist_location)
    VALUES(%s, %s, %s, %s, %s)
    ON CONFLICT (artist_id)
    DO UPDATE
    SET artist_name = EXCLUDED.artist_name,
        artist_latitude = EXCLUDED.artist_latitude,
        artist_longitude = EXCLUDED.artist_longitude,
        artist_location = EXCLUDED.artist_location;
""")

time_table_insert = ("""
    INSERT INTO time(start_time, hour, day, week, month, weekday)
    VALUES(%s, %s, %s, %s, %s);
""")

# FIND SONGS

song_select = ("""
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create,
                        song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop,
                      song_table_drop, artist_table_drop, time_table_drop]
