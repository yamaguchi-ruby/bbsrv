#!/home/pi/.rbenv/shims/ruby
require "sqlite3"
require "cgi"
require "base64"

cgi = CGI.new
print "Access-Control-Allow-Origin: https://yamaguchi-ruby.github.io\n"
# print "Access-Control-Allow-Origin: *\n"
print cgi.header({
    "charset" => "utf8",
    "type" => "text/plain"
})

DBFILE = "test.db"
db = SQLite3::Database.new(DBFILE)

str = ""
db.execute("select * from poster") do |row|
    text = Base64.decode64(row[1])
    name = Base64.decode64(row[3])
    str += "#{row[0]}, #{text}, #{row[2]}, #{name}, #{row[4]}\n"
end

print str
