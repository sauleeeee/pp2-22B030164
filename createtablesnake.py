import psycopg2

config = psycopg2.connect(dbname='postgres', user='postgres', password='Ainurik501892', host='localhost')
current = config.cursor()

create_table = '''
    CREATE TABLE records(
        name VARCHAR(255) NOT NULL,
        record INT NOT NULL
    );
'''

current.execute(create_table)

current.close()
config.commit()
config.close()