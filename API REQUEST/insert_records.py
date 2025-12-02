from api_request import mock_get_api
import psycopg2

def connect_to_db():
    print("trying connect into PostgreSQL...")
    try:
        conn = psycopg2.connect(dbname="db_weather", 
                                    user='db_user',
                                    password='db_password',
                                    host="localhost", 
                                    port=3000)
        return conn
    except psycopg2.Error as e:
        print("Error while connecting to PostgreSQL", e)
        raise

def create_table(conn):
    print("Creating table if not exists...")
    try:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE SCHEMA IF NOT EXISTS dev;
            CREATE TABLE IF NOT EXISTS dev.raw_weather_data (
                id SERIAL PRIMARY KEY,
                city TEXT,
                temperature FLOAT,
                weather_desc TEXT,
                wind_speed FLOAT,
                time TIMESTAMP,
                inserted_at TIMESTAMP DEFAULT NOW()
            );
        ''')
        conn.commit()
        print("table is created")
    except psycopg2.Error as e:
        print(f"Table was failed to create: {e}")
        raise

def insert_data(conn,data):
    print("inserting weather data into the local database...")
    try:
        location = data['location']
        weather = data['current']
        cursor = conn.cursor()
        cursor.execute('''
        INSERT INTO dev.raw_weather_data (
            city,
            temperature,
            weather_desc,
            wind_speed,
            time,
            inserted_at,
            utc_offset
        ) VALUES (%s,%s,%s,%s,%s,NOW(),%s)
        ''',(
            location['name'],
            weather['temp_c'],
            weather['condition']['text'],
            weather['wind_kph'],
            location['localtime'],
            location['tz_id']

        ))
        conn.commit()
        print("data was succesfully inserted")
    except psycopg2.Error as e:
        print(f"Error inserting data into database {e}")
        raise

conn = connect_to_db()
data = mock_get_api()
create_table(conn)
insert_data(conn,data) 