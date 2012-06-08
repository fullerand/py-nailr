import tornado.httpserver
import tornado.ioloop
import tornado.web
import urllib2
 
class Handler(tornado.web.RequestHandler):
    def get(self):
	imgUrl = self.get_argument("img")
	outputRes = self.get_argument("outputRes", "60x60")
        # self.write(imgUrl + "   " + outputRes)
	try:
		response = urllib2.urlopen(imgUrl)
		imgBytes = response.read()
	except URLError, e:
		print 'We failed to reach a server.'
		print 'Reason: ', e.reason
		sys.exit()
	else:	
		imgBytes = response.read()
		responseinfo = response.info()
		contentType = responseinfo['Content-Type']
		self.set_header('Content-Type', contentType)
		self.write(imgBytes)
	
 
application = tornado.web.Application([(r"/nailr", Handler),])
 
if __name__ == "__main__":
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
