import psycopg2
import time
import os

# INSERT INTO pokemon_map (encounter_id , expire , pokemon_id , latitude , longitude ) VALUES (1,1,1,1,1) O\N CONFLICT (encounter_id) DO NOTHING;
def query_pokemons_from_db(north, south, west, east):
    # 1. Open connection
    conn = psycopg2.connect(host = "beta-pokemon.c2dcrfootdyi.us-west-2.rds.amazonaws.com",
                            port = 5432,
                            user = "regina",
                            password = "12345678",
                            database = "pokemonDB")
 # 2. Execute SQL
    with conn.cursor() as cur:
        cur.execute("SELECT expire,pokemon_id, latitude, longitude" +
                    " FROM pokemon_map " +
                    " WHERE longitude > %s" +
                    " AND longitude < %s" +
                    " AND latitude > %s" +
                    " AND latitude < %s" +
#                    " AND expire > %s" +
                    " LIMIT 100",
#                    (west, east, south, north, time.time() * 1000))
                    (west, east, south, north))
        items = cur.fetchall()
        pokemons = []
        for item in items:
            # 1476566289000.0, 231, 41.4195807480884, -73.9995309631575)
            pokemon = {
                            "expire" : item[0] / 1000,
                            "pokemon_id" : item[1],
                            "latitude" : item[2],
                            "longitude" : item[3]
                          }
#            print pokemon
            pokemons.append(pokemon)

    conn.close()
    return pokemons

if __name__ == "__main__":
    print query_pokemons_from_db(41, 40,-73, -74)
