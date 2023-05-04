import psycopg2
import re
import csv
params=psycopg2.connect(dbname='postgres', user='postgres', password='Ainurik501892', host='localhost')
current = params.cursor()


update_type = input("what you want to update?(name or number):")
if update_type == "name":
    name = input("name in phonebook:")
    new_name = input("new name:")
    try:
        upd = '''
        UPDATE phonebook SET name = %s WHERE name = %s;
        '''
        current.execute(upd,(new_name,name))
    except:
        print("contact with this number does not exist")
elif update_type == "number":
    name = input("name in phonebook:")
    new_number = input("new number")
    pattern_1 = r"\+{1}\d+$"
    pattern_2 = r"\d+$"
    ok = True
    if re.match(pattern_1,new_number) or re.match(pattern_2,new_number):
        pass
    else:
        print("Impossible phone number")
        ok = False
    try:
        if ok:
            upd='''
            UPDATE phonebook SET number = %s WHERE name = %s
            '''
            current.execute(upd,(new_number,name))
    except:
        print("contact with this number does not exist")
current.close()
params.commit()
params.close()