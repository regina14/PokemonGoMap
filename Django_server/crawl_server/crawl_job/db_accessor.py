import psycopg2

# INSERT INTO pokemon_map (encounter_id , expire , pokemon_id , latitude , longitude ) VALUES (1,1,1,1,1) ON CONFLICT (encounter_id) DO NOTHING;
def add_pokemon_to_db(encounter_id , expire , pokemon_id , latitude , longitude):
    # 1. Open connection
    conn = psycopg2.connect(host = "pokemondb.c2dcrfootdyi.us-west-2.rds.amazonaws.com",
                            port = 5432,
                            user = "regina",
                            password = "12345678",
                            database = "pokemonDB")

    # 2. Execute SQL
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
