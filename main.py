from map import Map
import track
Track = track.Track
import util

class Context:
	def __init__(self):
		self.map = Map()
		self.track = Track()
	
	def get_name(self):
		return "NICed"
	
	def run(self, cmd):
		parts = cmd.split(" ")
		
		op = parts[0]
		
		try:
			match (op):
				case "load":
					path = " ".join(parts[1:])
					print(f"Loading map at: '{path}'")
					self.map.load(path)
				
				case "save":
					path = " ".join(parts[1:])
					print(f"Saving map to: '{path}'")
					self.map.save(path)
				
				case "track.list":
					print(" " * 35 + "TRACK LIST")
					print("=" * 80)
					self.map.show_tracks()
				
				case "track.remove":
					self.map.remove_track(int(parts[1]))
				
				case "track.use":
					self.track = self.map.get_track(int(parts[1]))
				
				case "track.set":
					self.map.set_track(int(parts[1]), self.track)
					self.track = Track()
				
				case "track.pos":
					self.track.set_pos([float(parts[1]), float(parts[2]), float(parts[3])])
				
				case "track.rot":
					self.track.set_rot(float(parts[1]))
				
				case "track.tile":
					self.track.set_tile(int(parts[1]))
				
				case "track.show":
					print(self.track.show())
				
				case "help":
					print_help()
				
				case "shell":
					cmd = " ".join(parts[1:])
					print(f"Running system command: {cmd}")
					print(f"Exit code: {util.run(cmd)}")
				
				case _:
					print(f"The command '{op}' wasn't recognised. Use 'help' to get help.")
		except IndexError as e:
			print("Error: Not enough arguments to this command.")

def print_help():
	print(util.load_text("help.txt"))

def run_repl(ctx, path = None):
	if (path):
		ctx.run(f"load {path}")
	
	while (True):
		cmd = input(f"{ctx.get_name()}> ")
		
		if (cmd == "exit"):
			break
		
		ctx.run(cmd)

def main():
	import sys
	
	ctx = Context()
	run_repl(ctx, sys.argv[1] if len(sys.argv) > 1 else None)

if (__name__ == "__main__"):
	main()
