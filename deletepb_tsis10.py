import psycopg2
params=psycopg2.connect(dbname='postgres', user='postgres', password='Ainurik501892', host='localhost')
current = params.cursor()
name = input("name:")
delete_raw = '''
    DELETE FROM PhoneBook WHERE name = %s;
'''
current.execute(delete_raw,(name,))
current.close()
params.commit()
params.close()