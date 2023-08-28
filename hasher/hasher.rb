require 'digest'
require 'sinatra'
require 'socket'
require 'logger'

set :bind, '0.0.0.0'
set :port, 80

logger = Logger.new(STDOUT)
logger.level = Logger::INFO
logger.datetime_format = "%Y-%m-%d %H:%M:%S"


logger.formatter = proc do |severity, datetime, progname, msg|
    "#{datetime} - #{severity} - #{msg}\n"
  end

post '/' do
    # Simulate a bit of delay
    sleep 0.1
    logger.info('hasher - POST - /')
    content_type 'text/plain'
    "#{Digest::SHA2.new().update(request.body.read)}"
end

get '/' do
    logger.info('hasher - GET - /')
    "HASHER running on #{Socket.gethostname}\n"
end