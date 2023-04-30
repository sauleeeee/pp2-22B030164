import psycopg2
params=psycopg2.connect(dbname='postgres', user='postgres', password='Ainurik501892', host='localhost')
current = params.cursor()

get_type = input("type of query:")
if get_type == "number":
    name = input("name:")
    get = '''
        SELECT number FROM phonebook WHERE name = %s;
    '''
    current.execute(get,(name,))
    output = current.fetchone()
    print(output[0])
elif get_type == "name":
    number = input("Number:")
    get = '''
        SELECT name FROM phonebook WHERE number = %s;
    '''
    current.execute(get,(number,))
    output = current.fetchone()
    print(output[0])