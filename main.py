import tornado.web
import tornado.httpserver
import tornado.ioloop

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
	server = tornado.httpserver.HTTPServer(app)
	server.listen(5000)
	
	tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
	start()
	