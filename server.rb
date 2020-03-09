require "webrick"
require "json"

settings = JSON.parse(open("config.json").read)
srv = WEBrick::HTTPServer.new({
    :DocumentRoot => settings["root"],
    :Port => settings["port"]
})

Dir.glob("*.cgi").each do |cgi|
    srv.mount("/cgi-bin/#{cgi}", WEBrick::HTTPServlet::CGIHandler, cgi)
end

trap("INT") do
    srv.shutdown
end

srv.start