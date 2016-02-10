#!/usr/bin/python3
import sys

sys.path.append("/itemhut/pydb")
import dbconn


def create_build_schema():
    dbconn.cur.execute(
        """
        create schema if not exists build;
        """)

def create_schema_helper():
    dbconn.cur.execute(
        """
        create or replace function build.create_schemas
                  (schema_list varchar[])
        returns void
        as
        $$
        declare
        s varchar;

        begin

        foreach s in array schema_list
        loop
	execute format('CREATE SCHEMA IF NOT EXISTS %I', s);
        end loop;

        end;
        $$ language plpgsql;
        """)

def create_template_tables_helper():
    dbconn.cur.execute(
        """
        create or replace function build.create_template_tables
                  (schema_list varchar[])
        returns void
        as
        $$
        declare
        s varchar;

        begin

        foreach s in array schema_list
        loop
	     execute format('
             CREATE TABLE IF NOT EXISTS %I.template ();
             ', s);
        end loop;

        end;
        $$ language plpgsql;
        """)


def create_valid_tables_helper():
    dbconn.cur.execute(
        """
        create or replace function build.create_valid_tables
	      (schema_name varchar, tbls varchar[])
        returns void
        as
        $$
        declare
        t varchar;

        begin
        foreach t in array tbls
        loop
	    execute format('
            CREATE TABLE IF NOT EXISTS %1$I.valid_%2$I (
			%2$I VARCHAR PRIMARY KEY
            );', schema_name, t);
        end loop;

        end;
        $$ language plpgsql;
        """)

def create_add_varchar_helper():
    dbconn.cur.execute(
        """
        create or replace function build.add_varchar_column
	(schema_name varchar, cname varchar, data_type varchar, optional varchar)
        returns void
        as
        $$
        declare
        t_varchar_n int := substring(data_type, '\d+');

        begin

        if (t_varchar_n is not null
        and cname = 'item_sku')
        then

        execute format('
	alter table %1$I.template
	add column item_sku varchar(' || t_varchar_n ||') primary key;',
	schema_name);
        
        elsif (t_varchar_n is null
        and cname = 'item_sku')
        then
        
        execute format('
	alter table %1$I.template
	add column item_sku varchar primary key;',
	schema_name);
        
        elsif (t_varchar_n is not null
        and optional = 'Required')
        then

        execute format('
	alter table %1$I.template
	add column %2$I varchar(' || t_varchar_n || ') not null;',
	schema_name, cname);

        elsif (t_varchar_n is null
        and optional = 'Required')
        then
        
        execute format('
	alter table %1$I.template
	add column %2$I varchar not null;',
	schema_name, cname);
        
        elsif (t_varchar_n is not null
        and optional <> 'Required')
        then
        
        execute format('
	alter table %1$I.template
	add column %2$I varchar(' || t_varchar_n || ');',
	schema_name, cname);
        
        elsif (t_varchar_n is null
        and optional <> 'Required')
        then
        
        execute format('
	alter table %1$I.template
	add column %2$I varchar;',
	schema_name, cname);
        
        end if;
        
        end;
        $$ language plpgsql;
        """)

def create_add_int_helper():
    dbconn.cur.execute(
        """
        create or replace function build.add_int_column
        (schema_name varchar, cname varchar, optional varchar)
        returns void
        as
        $$
        begin
        if optional = 'required'
        then
        
        execute format('
	alter table %1$I.template
	add column %2$I integer not null;',
	schema_name, cname);
        
        else

        execute format('
	alter table %1$I.template
	add column %2$I integer;',
	schema_name, cname);

        end if;
        end;
        $$ language plpgsql;
        """)

def create_add_date_helper():
    dbconn.cur.execute(
        """
        create or replace function build.add_date_column
        (schema_name varchar, cname varchar, optional varchar)
        returns void
        as
        $$
        begin
        
        if optional = 'required'
        then

        execute format('
	alter table %1$I.template
	add column %2$I date not null;',
	schema_name, cname);

        else

        execute format('
	alter table %1$I.template
	add column %2$I date;',
	schema_name, cname);

        end if;

        end;
        $$ language plpgsql;
        """)
    
def create_add_numeric_helper():
    dbconn.cur.execute(
        """
        create or replace function build.add_numeric_column
        (schema_name varchar, cname varchar, data_type varchar, optional varchar)
        returns void
        as
        $$
        declare
        t_numeric_first int := substring(data_type, '\d+')::int;
        t_numeric_stage varchar := substring(data_type, '\d+\)');
        t_numeric_second int := substring(t_numeric_stage, '\d+')::int;

        begin

        if (optional = 'Required'
        and t_numeric_first is not null)
        then

        execute format('
	alter table %1$I.template
	add column %2$I numeric(%3$I, %4$I) not null;',
	schema_name, cname, t_numeric_first, t_numeric_second);

        elsif (optional = 'Required'
        and t_numeric_first is not null)
        then 

        execute format('
	alter table %1$I.template
	add column %2$I numeric(%3$I, %4$I);',
	schema_name, cname, t_numeric_first, t_numeric_second);

        elsif (optional <> 'Required'
        and t_numeric_first is null)
        then

        execute format('
	alter table %1$I.template
	add column %2$I numeric not null;',
	schema_name, cname);
        
        elsif (optional <> 'Required'
        and t_numeric_first is null)
        then 
        execute format('
	alter table %1$I.template
	add column %2$I numeric;',
	schema_name, cname);

        end if;
        
        end;
        $$ language plpgsql;
        """)

def add_column_to_template_helper():
    dbconn.cur.execute(
        """
        create or replace function build.add_columns_to_tamplate_tables
	(schema_name varchar, column_array varchar[], data_type varchar, optional varchar)
        returns void
        as
        $$
        declare
        cname varchar;
        t_data_type varchar := substring(data_type, '\w+');

        begin

        foreach cname in array column_array
        loop
	if not exists
		(select *
		 from information_schema.columns
		 where (table_schema, table_name, column_name)
		      = (schema_name, 'template', cname))

	then
		if t_data_type = 'varchar'
		then
		execute build.add_varchar_column
		 (schema_name, cname, data_type, optional);

	elsif t_data_type = 'int'
	then
		execute build.add_int_column
			(schema_name, cname, optional);

	elsif t_data_type = 'numeric'
	then
	execute build.add_numeric_column
	(schema_name, cname, data_type, optional);
        
	elsif t_data_type = 'date'
	then
	execute build.add_date_column
	(schema_name, cname, optional);

	end if;
        end if;

        end loop;
        end;
        $$ language plpgsql;
        """)

def drop_build_schema():
    dbconn.cur.execute(
        """
        drop schema if exists build cascade;
        """)
    
def create_helper_functions():
    create_build_schema()
    create_schema_helper()
    create_template_tables_helper()
    create_valid_tables_helper()
    create_add_varchar_helper()
    create_add_int_helper()
    create_add_date_helper()
    create_add_numeric_helper()
    add_column_to_template_helper()

if __name__=='__main__':
    create_helper_functions()
