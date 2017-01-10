# Created by: Quintin Gerbasi & David Currey
# Created on: Jan 2017
# Created for: ICS3U

from scene import *

class ControlButton(SpriteNode):
	# class represents user controls in game
	def __init__(self, direction, **kwargs):
		
		if direction == 'up':
			img = Texture('assets/sprites/buttons/arrowUp.png')
			pos = (100, 150)
		elif direction == 'down':
			img = Texture('assets/sprites/buttons/arrowDown.png')
			pos = (100, 50)
		elif direction == 'left':
			img = Texture('assets/sprites/buttons/arrowLeft.png')
			pos = (50, 100)
		elif direction == 'right':
			img = Texture('assets/sprites/buttons/arrowRight.png')
			pos = (150, 100)
		
		SpriteNode.__init__(self, img, pos, z_position = 1, alpha = 0.5, **kwargs)
		
		self.touched = False
