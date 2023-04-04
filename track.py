class Track:
	def __init__(self, data = None):
		if (not data):
			self.pos = [0, 0, 0]
			self.rot = 0.0
			self.tile = 0
		else:
			self.pos = data["position"]
			self.rot = data["yr"]
			self.tile = data["index"]
	
	def as_dict(self):
		return {
			"position": self.pos,
			"yr": self.rot,
			"index": self.tile,
		}
	
	def set_pos(self, pos):
		self.pos = pos
	
	def set_rot(self, rot):
		self.rot = rot
	
	def set_tile(self, tile):
		self.tile = tile
	
	def move(self, amount):
		self.pos[0] += amount[0]
		self.pos[1] += amount[1]
		self.pos[2] += amount[2]
	
	def show(self):
		return f"pos = {self.pos}   rot = {self.rot}   tile = {self.tile}"
