# Created by: Quintin Gerbasi & David Currey
# Created on: Jan 2017
# Created for: ICS3U

from scene import *

class Door(SpriteNode):
	# class represents a door (exit) in game
	def __init__(self, **kwargs):
		SpriteNode.__init__(self, 'assets/sprites/environment/door.png', **kwargs)
