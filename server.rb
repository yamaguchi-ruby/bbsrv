require "webrick"
require 'webrick/https'
require "json"

settings = JSON.parse(open("config.json").read)
srv = WEBrick::HTTPServer.new({
    :DocumentRoot => settings["root"],
    :Port => settings["port"],
    :SSLEnable => (settings["ssl"] == "true"),
    :SSLCertificate => OpenSSL::X509::Certificate.new(open(settings["crt_file_name"]).read),
    :SSLPrivateKey => OpenSSL::PKey::RSA.new(open(settings["rsa_file_name"]).read),
    :RequestCallback => Proc.new{ |req,res| res['Access-Control-Allow-Origin'] = settings["main_site"] }
})

Dir.glob("*.cgi").each do |cgi|
    srv.mount("/cgi-bin/#{cgi}", WEBrick::HTTPServlet::CGIHandler, cgi)
end

trap("INT") do
    srv.shutdown
end

srv.start