
import time
import multiprocessing as mp

import tornado.httpserver
import tornado.websocket
import tornado.ioloop
import tornado.web

import pyrift

clients = []
 
class WSHandler(tornado.websocket.WebSocketHandler):
    def open(self):
        clients.append(self)
        self.t0 = time.time()
        print "Socket opened.", len(clients), "sockets open."
      
    def on_message(self, message):
        pass
 
    def on_close(self):
        clients.remove(self)
        print "Socket closed.", len(clients), "sockets open."

    def update(self):
        x, y, z, w = pyrift.get_orientation_quaternion()
        response = "%f,%f,%f,%f" % (w,x,y,z)
        self.write_message(response)
 

def update():
    for client in clients:
        client.update()
 
application = tornado.web.Application([
    (r'/', WSHandler),
])
 

def main():
    pyrift.initialize()
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(8808)
    callback = tornado.ioloop.PeriodicCallback(update, 1000/60.0)
    callback.start()
    tornado.ioloop.IOLoop.instance().start()

def start():
    proc = mp.Process(target = main)
    proc.daemon = True
    proc.start()

if __name__ == "__main__":
    start()
    while True:
        time.sleep(1)
