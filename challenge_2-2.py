#create a class called Player
class Player:
#create a function called play
	def play(self):
		print("The player is playing cricket.")
#create a class called Batsman
class Batsman(Player):
#create a function called play
	def play(self):
		print("The batsman is batting.")
#create a class called Bowler
class Bowler(Player):
#create a function called play
	def play(self):
		print("The  bowler is bowling.")
#create two object called batsman and bowler
batsman = Batsman()
bowler = Bowler()
#call object and function or method
batsman.play()
bowler.play()
