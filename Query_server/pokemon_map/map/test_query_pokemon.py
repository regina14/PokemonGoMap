from db_accessor import query_pokemons_from_db

for i in range(100):
    query_pokemons_from_db(east=-73.99837592515519, south=40.74279758800707,north=40.74847928621097,west=-74.00130489739945)
