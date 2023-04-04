import track
import util

croctool_path = "./croctool"

class Map:
	"""
	Represents a map and everything in it
	"""
	
	def __init__(self, path = None):
		"""
		Initialise the map object. It's the least effort to just not convert the map data
		to be a real object. And I don't really want to do setattr stuff today...
		"""
		
		self.data = self.load(path)
	
	def load(self, path):
		self.path = path
		
		if (path and (path.endswith(".map") or path.endswith(".MAP"))):
			if (util.run(f"{croctool_path} map decompile '{path}' '{path}.niced-json'")):
				print("Warning: map does not exist.")
			
			path = f"{path}.niced-json"
		
		data = util.load_json(path) if path else None
		
		if (not data):
			data = {
				"_meta":	{
					"version": 21,
					"format": "normal",
					"level": 0,
					"sublevel": 0,
					"checksum": 0
				},
				"path" : "default.map",
				"name" : "New Default Map",
				"width" : 16,
				"height" : 16,
				"depth" : 32,
				"style" : "wood",
				"flags" : 0,
				"cd_track" : 0,
				"background" : 0,
				"effect" : "none",
				"wait" : 0,
				"ambience" : "none",
				"start_rotation" : 0.0,
				"tracks" : [],
				"strats" : [],
				"doors" : [],
				"point_lights" : [],
				"direct_lights" : [],
				"ambient_colour" : [0, 0, 0],
			}
		
		self.data = data
	
	def save(self, path = None):
		if (not path):
			path = self.path
		
		self.data["path"] = path
		
		raw_map = path.endswith(".map") or path.endswith(".MAP")
		
		# If we should make a raw map, we need to rely on croctool to build it
		if (raw_map):
			util.save_json(f"{path}.niced-json", self.data)
			
			cmd = f"{croctool_path} map compile '{path}.niced-json' '{path}'"
			result = util.run(cmd)
			
			if (result):
				print(f"Error: could not convert map to raw map. (exit code {result})")
				print(f"Note: {cmd}")
		# Otherwise, we just save the json
		else:
			util.save_json(f"{path}", self.data)
	
	def show_track(self, i):
		tracks = self.data["tracks"]
		
		print(f"#{i} {self.get_track(i).show()}")
	
	def show_tracks(self):
		for i in range(len(self.data["tracks"])):
			self.show_track(i)
	
	def remove_track(self, i):
		"""
		Remove a track from the array
		"""
		
		tracks = self.data["tracks"]
		
		tracks.pop(i)
	
	def get_track(self, i):
		"""
		Get the specified trackpiece
		"""
		
		tracks = self.data["tracks"]
		
		if (i >= len(tracks)):
			return track.Track()
		
		return track.Track(tracks[i])
	
	def set_track(self, i, track):
		"""
		Set the track at the given index
		"""
		
		track = track.as_dict()
		tracks = self.data["tracks"]
		
		if (i >= len(tracks)):
			tracks.append(track)
		else:
			tracks[i] = track
