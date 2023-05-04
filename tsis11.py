import psycopg2 as pgsql

connection=pgsql.connect(dbname='postgres', user='postgres', password='Ainurik501892', host='localhost')
cur=connection.cursor()

#PROCEDURES & functions
#1 searching by name
cur.execute("""CREATE OR REPLACE FUNCTION search_from_pb_byname(a character varying)
  RETURNS SETOF phonebook
AS
$$
SELECT * 
FROM phonebook 
WHERE name=a;
$$
language sql;
""")
#2 updating if exist inserting if not
cur.execute("""CREATE OR REPLACE PROCEDURE insert_to_pb(a character varying, b character varying)
LANGUAGE plpgsql
AS $$
DECLARE v_exists INTEGER;
BEGIN
    SELECT into v_exists (SELECT count(*) FROM public.phonebook WHERE name = a);
    IF v_exists=0 THEN
        INSERT INTO public.PhoneBook (name, number) values(a, b);
    END IF;
	IF v_exists IS NOT NULL THEN
        UPDATE public.PhoneBook
		SET number = b
		WHERE name=a;
    END IF;
END;
$$;
""")
#3 inserting in loop

cur.execute("""CREATE OR REPLACE PROCEDURE insert_loop()
LANGUAGE plpgsql
AS $$
DECLARE
   m   text[];
   num integer;
   arr text[] := '{{qasym,12345},{nursultan, 46465},{asdasd, 46451}}'; 
BEGIN
   FOREACH m SLICE 1 IN ARRAY arr
   LOOP
      SELECT INTO num CAST(m[2] AS TEXT);
      INSERT INTO phonebook ( name, number) values(m[1],num);
   END LOOP;
END
$$;""")

#4pagination
cur.execute("""CREATE OR REPLACE FUNCTION paginating(a integer, b integer)
RETURNS SETOF phonebook
AS $$
    SELECT * FROM phonebook 
	ORDER BY name
	LIMIT a OFFSET b;
$$
language sql;""")

#5deleting
cur.execute("""CREATE OR REPLACE PROCEDURE delete_from_pb(a character varying)
LANGUAGE plpgsql
AS $$
DECLARE v_exists INTEGER;
BEGIN
    SELECT into v_exists (SELECT count(*) FROM public.phonebook WHERE name = a);
	IF v_exists IS NOT NULL THEN
        DELETE FROM phonebook
		WHERE name=a;
    END IF;
END;
$$;""")

#executing
cur.execute("""CALL insert_to_pb('tosql','465465654');
""")
cur.execute("""SELECT *
FROM search_from_pb_byname('saule');""")
print(cur.fetchall())
cur.execute("""CALL insert_to_pb('pip','66');""")
cur.execute("""SELECT *
FROM paginating(5, 2);""")
print(cur.fetchall())
cur.execute("""CALL delete_from_pb( 'tosql');""")
cur.execute("""CALL insert_loop();""")


connection.commit()
cur.close()
connection.close()