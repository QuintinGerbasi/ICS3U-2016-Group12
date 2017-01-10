# Created by: Quintin Gerbasi & David Currey
# Created on: Jan 2017
# Created for: ICS3U

from scene import *

# Monster Textures
monster_dead_texture = Texture('assets/sprites/monster/monster_dead.png')
monster_standing_texture = Texture('assets/sprites/monster/monster_standing.png')
monster_walk_textures = [Texture('assets/sprites/monster/monster_shuffle1.png'), Texture('assets/sprites/monster/monster_shuffle2.png')]

class Monster(SpriteNode):
	# class represents a monster in game
	def __init__(self, **kwargs):
		SpriteNode.__init__(self, monster_standing_texture, **kwargs)
		
		self.action = None
		self.attacked = False;
		self.walk_step = -1
		self.walk_direction = None
