/* Create a test user */
DO
$body$
BEGIN
	IF NOT EXISTS ( SELECT * FROM pg_catalog.pg_user WHERE usename = 'test_user' ) THEN
		CREATE ROLE test_user WITH LOGIN CREATEDB PASSWORD 'password';
	END IF;
END
$body$;

/*Create databases, and add extensions */
-- test db
-- create
CREATE DATABASE test_db WITH OWNER test_user;
-- connect to db
\c test_db
-- create schema
CREATE SCHEMA extensions AUTHORIZATION test_user;
GRANT ALL ON SCHEMA extensions TO postgres;
GRANT ALL ON SCHEMA extensions TO public;
CREATE EXTENSION "uuid-ossp" SCHEMA extensions;
-- dev db
-- create
CREATE DATABASE dev_db WITH OWNER test_user;
-- connect to db
\c dev_db
-- create schema
CREATE SCHEMA extensions AUTHORIZATION test_user;
GRANT ALL ON SCHEMA extensions TO postgres;
GRANT ALL ON SCHEMA extensions TO public;
CREATE EXTENSION "uuid-ossp" SCHEMA extensions;

