
var ParticleExplosion = function(N) {

	var self = this;

	self.N = N;

	self.initialize = function() {
		self.geometry = new THREE.BufferGeometry();
		self.geometry.addAttribute("position", Float32Array, N, 3);
		self.geometry.addAttribute("color", Float32Array, N, 3);
		self.positions = self.geometry.attributes.position.array;
		self.velocities = [];
		self.colors = self.geometry.attributes.color.array;
		var color = new THREE.Color();
		for (var i = 0; i < N; i++) {
			self.positions[i * 3 + 0] = (Math.random() - 0.5) * 0.01;
			self.positions[i * 3 + 1] = (Math.random() - 0.5) * 0.01;
			self.positions[i * 3 + 2] = (Math.random() - 0.5) * 0.01;
			self.velocities[i * 3 + 0] = (Math.random() - 0.5) * 0.01;
			self.velocities[i * 3 + 1] = (Math.random() - 0.5) * 0.01;
			self.velocities[i * 3 + 2] = (Math.random() - 0.5) * 0.01;
			color.setRGB(1,1,1);
			self.colors[i * 3 + 0] = color.r;
			self.colors[i * 3 + 1] = color.g;
			self.colors[i * 3 + 2] = color.b;
		}
		self.geometry.computeBoundingSphere();
		self.material = new THREE.ParticleSystemMaterial({size: 0.1, vertexColors: true});
		self.particleSystem = new THREE.ParticleSystem(self.geometry, self.material);
	}
}