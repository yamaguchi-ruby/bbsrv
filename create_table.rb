require "sqlite3"

DBFILE = "test.db"

db = SQLite3::Database.new(DBFILE)

db.execute("drop table poster")
create_table = "
    create table poster(
        date datetime,
        poster varchar(1000),
        ip char(16),
        name varchar(50),
        removeflag integer
    );"

db.execute(create_table)