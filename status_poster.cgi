#!/home/pi/.rbenv/shims/ruby

require "cgi"

cgi = CGI.new
print "Access-Control-Allow-Origin: https://yamaguchi-ruby.github.io\n"
# print "Access-Control-Allow-Origin: *\n"
print cgi.header({
    "charset" => "utf8",
    "type" => "text/html"
})
print "OK"
