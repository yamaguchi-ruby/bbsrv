#!/home/pi/.rbenv/shims/ruby
require "sqlite3"
require "cgi"
require "base64"

cgi = CGI.new
print cgi.header({
    "charset" => "utf8",
    "type" => "text/plain"
})

cgi.params["name"] = ["名無し"] if cgi.params["name"] == []
if cgi.params["text"] == []
    print("投稿がありません")
    exit(false)
end

text = Base64.encode64(cgi.params["text"][0])
name = Base64.encode64(cgi.params["name"][0])

DBFILE = "test.db"

db = SQLite3::Database.new(DBFILE)
db.execute("insert into poster
    values
        ('#{Time.new.strftime("%Y-%m-%d %H:%M:%S")}', '#{text}', '192.168.0.2', '#{name}', 'true');
    ")