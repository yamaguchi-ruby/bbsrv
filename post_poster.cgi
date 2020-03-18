#!/home/pi/.rbenv/shims/ruby
require "sqlite3"
require "cgi"
require "base64"

cgi = CGI.new
print "Access-Control-Allow-Origin: https://yamaguchi-ruby.github.io\n"
# print "Access-Control-Allow-Origin: *\n"
print cgi.header({
    "charset" => "utf8",
    "type" => "text/html"
})

cgi.params["name"] = ["名無し"] if cgi.params["name"] == [""]
if cgi.params["text"] == [""]
    print("投稿がありません 3秒後に移動します")
    print "<meta http-equiv=\"refresh\" content=\"3;#{ENV["HTTP_REFERER"]}\">"
    exit(false)
end

cgi.params["text"][0].gsub!(/\r\n/, "<br>")
cgi.params["name"][0].gsub!(/\r\n/, "")
cgi.params["text"][0].gsub!(/\,/, "&#44;")
cgi.params["name"][0].gsub!(/\,/, "&#44;")

text = Base64.encode64(cgi.params["text"][0])
name = Base64.encode64(cgi.params["name"][0])

DBFILE = "test.db"

db = SQLite3::Database.new(DBFILE)
db.execute("insert into poster
    values
        ('#{Time.new.strftime("%Y-%m-%d %H:%M:%S")}', '#{text}', '192.168.0.2', '#{name}', 'true');
    ")
print "<meta http-equiv=\"refresh\" content=\"0;#{ENV["HTTP_REFERER"]}\">"