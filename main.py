import tornado.web
import tornado.httpserver
import tornado.ioloop
import tornado.options

import logging

logging.basicConfig(
level = logging.DEBUG,
format = "%(asctime)s | %(message)s")

from tornado.options import define
define("port", default=5000, help="open at given port", type=int)
define("cup", default="coffe")

class MainHandler(tornado.web.RequestHandler):
	def get(self):
		self.write("Hello world")

app = tornado.web.Application(
	# handlers
	[
		(r"/", MainHandler),
	],
	
	# settings
	{
	"debug": True,
	}
)

def start():
	tornado.options.parse_command_line()
	server = tornado.httpserver.HTTPServer(app)
	server.listen(tornado.options.options.port)
	
	print(tornado.options.options.items())
	print(tornado.options.options.cup)
	
	tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
	start()
	