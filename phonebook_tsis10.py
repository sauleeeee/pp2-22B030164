import psycopg2
import re
import csv
params=psycopg2.connect(dbname='postgres', user='postgres', password='Ainurik501892', host='localhost')
current = params.cursor()

input_type = input('Terminal or from file?')
pattern_1 = r"\+{1}\d+$"
pattern_2 = r"\d+$"
if input_type == "Terminal":
    name = input("Add name\n")
    number = input("Add number\n")
    ok = True
    if re.match(pattern_1,number) or re.match(pattern_2,number):
        pass
    else:
        print("Impossible phone number")
        ok = False
    try:
        insert_into = '''
        INSERT INTO PhoneBook VALUES (%s,%s);
        '''
        if ok:
            current.execute(insert_into,(f'{name}',f'{number}'))
    except:
        print("phone number already written in the book")
elif input_type == "from file":
    with open("phones.csv","r") as file:
        data = csv.reader(file,delimiter =';')
        for line in data:
            ok = True
            if re.match(pattern_1,line[1]) or re.match(pattern_2,line[1]):
                pass
            else:
                print(f"Impossible phone number,with name {line[0]}")
                ok = False
            try:
                insert_into = '''
                    INSERT INTO PhoneBook VALUES (%s,%s);
                '''
                if ok:
                    current.execute(insert_into,(f'{line[0]}',f'{line[1]}'))
            except:
                print(f"phone number with name {line[0]} already written in the book")
current.close()
params.commit()
params.close()