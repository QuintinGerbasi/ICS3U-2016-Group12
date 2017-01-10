# Created by: Quintin Gerbasi & David Currey
# Created on: Jan 2017
# Created for: ICS3U

from scene import *

# Player Textures
player_standing_texture = Texture('assets/sprites/hero/player_standing_front.png')
player_walk_textures = [Texture('assets/sprites/hero/player_walking_right2.png'), Texture('assets/sprites/hero/player_walking_right1.png')]

class Player(SpriteNode):
	# class represents the player in game.
	def __init__(self, **kwargs):
		SpriteNode.__init__(self, player_standing_texture, **kwargs)
		
		self.has_sword = False
		self.health = 3
		self.gold = 0
		self.walk_step = -1
	
	def hitbox(self, x, y, attacked):
		# method returns area of player that interacts with items in game
		if attacked:
			return Rect(x-13, y-24, 26, 42)
		else:
			return Rect(x-13, y-24, 30, 46)
