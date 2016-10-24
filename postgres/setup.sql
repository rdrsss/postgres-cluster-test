DO
$body$
BEGIN
	IF NOT EXISTS ( SELECT * FROM pg_catalog.pg_user WHERE usename = 'puser' ) THEN
		CREATE ROLE puser LOGIN PASSWORD 'password';
	END IF;
END
$body$;

