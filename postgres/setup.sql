/* Create a test databse */
-- CREATE DATABASE test_db;

/* Create a test user */
DO
$body$
BEGIN
	IF NOT EXISTS ( SELECT * FROM pg_catalog.pg_user WHERE usename = 'test_user' ) THEN
		CREATE ROLE test_user WITH LOGIN CREATEDB PASSWORD 'password';
	END IF;
END
$body$;

/* Grant all priveleges to test_user */
-- GRANT ALL ON DATABASE test_db TO test_user;

