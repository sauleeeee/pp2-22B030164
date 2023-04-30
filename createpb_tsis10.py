import psycopg2
params=psycopg2.connect(dbname='postgres', user='postgres', password='Ainurik501892', host='localhost')
current = params.cursor()

create_table = '''
    CREATE TABLE PhoneBook(
        name VARCHAR(255) ,
        number VARCHAR(255) UNIQUE
    );
'''

current.execute(create_table)
delete_raw = '''
    DELETE FROM PhoneBook WHERE name = %s;
'''
current.execute(delete_raw,('Eer',))
current.close()
params.commit()
params.close()