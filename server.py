
import time
import json
import multiprocessing as mp

import tornado.httpserver
import tornado.websocket
import tornado.ioloop
import tornado.web

import pyrift

clients = []
 
class RiftHandler(tornado.websocket.WebSocketHandler):
    def open(self):
        clients.append(self)
    def on_message(self, message):
        pass
    def on_close(self):
        clients.remove(self)
    def update(self):
        pass

class QuaternionHandlerCSV(RiftHandler):
    def update(self):
        x, y, z, w = pyrift.get_orientation_quaternion()
        data = "%f,%f,%f,%f" % (w,x,y,z)
        self.write_message(data)

class QuaternionHandlerJSON(RiftHandler):
    def update(self):
        x, y, z, w = pyrift.get_orientation_quaternion()
        data = json.dumps(dict(w=w, x=x, y=y, z=z))
        self.write_message(data)

class EulerHandlerJSON(RiftHandler):
    def update(self):
        yaw, pitch, roll = pyrift.get_orientation()
        data = json.dumps(dict(yaw = yaw, pitch = pitch, roll=roll))
        self.write_message(data)

def update():
    for client in clients:
        client.update()
 
application = tornado.web.Application([
    (r'/', QuaternionHandlerCSV),
    (r'/csv/quat', QuaternionHandlerCSV),
    (r'/json/quat', QuaternionHandlerJSON),
    (r'/json/euler', EulerHandlerJSON),
])

def main():
    pyrift.initialize()
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(1981)
    callback = tornado.ioloop.PeriodicCallback(update, 1000/120.0)
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
