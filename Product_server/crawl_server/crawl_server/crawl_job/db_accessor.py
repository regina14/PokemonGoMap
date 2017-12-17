import psycopg2
import os

# INSERT INTO pokemon_map (encounter_id , expire , pokemon_id , latitude , longitude ) VALUES (1,1,1,1,1) ON CONFLICT (encounter_id) DO NOTHING;
def add_pokemon_to_db(encounter_id , expire , pokemon_id , latitude , longitude):
    conn = psycopg2.connect(host = os.environ["DB_HOST"],
                            port = 5432,
                            user = os.environ["DB_USER"],
                            password = os.environ["DB_PASSWORD"],
                            database = os.environ["DB_NAME"])
    with conn.cursor() as cur:
        cur.execute("INSERT INTO pokemon_map (encounter_id , expire , pokemon_id , latitude , longitude )" + 
                    " VALUES (%s, %s, %s, %s, %s)" + 
                    " ON CONFLICT (encounter_id) DO NOTHING", (encounter_id , expire , pokemon_id , latitude , longitude))

    # 3. connection commit 
    conn.commit()
    conn.close()
    return

if __name__ == "__main__":
    add_pokemon_to_db(1, 1, 1, 1,1)
