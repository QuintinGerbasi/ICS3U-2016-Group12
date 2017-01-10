# Created by: Quintin Gerbasi & David Currey
# Created on: Jan 2017
# Created for: ICS3U

from scene import *

# Constant
coin_value = 10

class Coin(SpriteNode):
	# class represents a coin the player can collect in game
	def __init__(self, **kwargs):
		SpriteNode.__init__(self, 'assets/sprites/environment/gold.png', **kwargs)
		
	def get_coin_value(self):
	# value of coin
		return coin_value
	
