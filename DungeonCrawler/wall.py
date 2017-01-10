# Created by: Quintin Gerbasi & David Currey
# Created on: Jan 2017
# Created for: ICS3U

from scene import *

class Wall(SpriteNode):
	# class represents a wall in game
	def __init__(self, **kwargs):
		SpriteNode.__init__(self, 'assets/sprites/environment/wall.png', **kwargs)
