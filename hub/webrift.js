"use strict";

var Webrift = function(url) {

	var self = this;

	self.initialize = function() {
		self.url = url;
		self.ws = new WebSocket(url);
		self.ws.onmessage = self.onMessage;
		self.ws.onopen = self.onOpen;
		self.ws.onclose = self.onClose;
		self.x = 0.0;
		self.y = 0.0;
		self.z = 0.0;
		self.w = 1.0;
	}

	self.onMessage = function(e) {
		var msg = JSON.parse('[' + e.data + ']');
		self.x = msg[1];
		self.y = msg[2];
		self.z = msg[3];
		self.w = msg[0];
	}

	self.onOpen = function() {
		console.log("Webrift socket connected.");
	}

	self.onClose = function() {
		console.log("Webrift socket disconnected.");
	}

	self.initialize();

}