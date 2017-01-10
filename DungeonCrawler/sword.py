# Created by: Quintin Gerbasi & David Currey
# Created on: Jan 2017
# Created for: ICS3U

from scene import *

class Sword(SpriteNode):
	# class represents a sword for the player in game
	def __init__(self, **kwargs):
		SpriteNode.__init__(self, 'assets/sprites/environment/sword.png', **kwargs)
