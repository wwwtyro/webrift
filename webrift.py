import pygtk
pygtk.require('2.0')
import gtk

import server


class WebRiftApp:

    def delete_event(self, widget, event, data=None):
        return False

    def destroy(self, widget, data=None):
        gtk.main_quit()

    def __init__(self):
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.window.set_title(title="WebRift Server")
        self.window.connect("delete_event", self.delete_event)
        self.window.connect("destroy", self.destroy)
        self.window.set_border_width(10)
        self.window.show()
        label = gtk.Label("WebRift server running at http://localhost:8808\nClose this window to exit the server.")
        label.show()
        self.window.add(label)

    def main(self):
        gtk.main()


if __name__ == "__main__":
    app = WebRiftApp()
    server.start()
    app.main()