# Created by: Quintin Gerbasi & David Currey
# Created on: Jan 2017
# Created for: ICS3U
# This scene shows the main game.

from scene import *
from player import *
from monster import *
from wall import *
from door import *
from sword import *
from coin import *
from control_button import *
import sound
import ui
import dialogs
import random
import time

# Constants
font = ('Futura', 20)
max_player_speed = 5

class DungeonScene(Scene):
	def setup(self):
		# this method is called, when user moves to this scene
 
 		self.name = 'dungeon_scene'
		self.monster_timeout = 0
		self.items = []
		
		# build dungeon layout and place items in game
		self.build_dungeon()
		
		# health label tracking the player's health status
		health_label = LabelNode('Health:', font, parent=self)
		health_label.position = (165, self.size.h - 13)
		health_label.z_position = 1
		health_label.color = 'white'
		
		posx = 220
		self.health_count = Node(parent=self)
		for x in xrange(self.player.health):
			health = SpriteNode('assets/sprites/environment/heart.png', (posx, self.size.h - 14), 0, 0.5, 0.5)
			health.scale = 1.3
			self.health_count.add_child(health)
			posx += 28
			
		# gold label tracking the number of coins the player collected
		gold_label = LabelNode('Gold:', font, parent=self)
		gold_label.position = (self.size.w - 200, self.size.h - 13)
		gold_label.z_position = 1
		gold_label.color = 'white'
		
		self.gold_count = LabelNode('0', font, parent=self)
		self.gold_count.position = (self.size.w - 155, self.size.h - 13)
		self.gold_count.z_position = 1
		self.gold_count.color = 'gold'
		
		# control buttons in game
		self.up_button = ControlButton(parent=self, direction='up')
		self.down_button = ControlButton(parent=self, direction='down')
		self.left_button = ControlButton(parent=self, direction='left')
		self.right_button = ControlButton(parent=self, direction='right')
		
	
	def build_dungeon(self):
		# method to build the dungeon
		# used concept from http://pygame.org/project-Rect+Collision+Response-1061-.html
		
		self.background = SpriteNode(position = self.size / 2, 
																	color = '#252525', 
																	parent = self, 
																	size = self.size)
		level = [
				"WWWWWWWWWWWWWWWWW",
				"W W CW          W",
				"W W    WWWWWW   W",
				"W   WWWW   SW   W",
				"W   W    WWWW   W",
				"WMWWW  WWW      W",
				"W   WM   W   W CW",
				"W      W   WWW WW",
				"W WWW WWW  W W  W",
				"W      WC  W W  W",
				"W      WWWWW W  W",
				"W    PWWE   M   W",
				"WWWWWWWWWWWWWWWWW"
			]

		# Parse the level string above. 
		# W = wall, E = exit, P = Player, S = Sword, C = Coin
		x = 0
		y = self.size.h
		monster_action = 0
		monster_action_direction = ['up/down', 'left/right', 'up/down']
		
		for row in level:
			for col in row:
				
				if col == "W":
					wall = Wall(parent=self)
					wall.position = (x, y)
					self.items.append(wall)
				
				elif col == "M":
					monster = Monster(parent=self)
					monster.position = (x, y)
					if monster_action_direction[monster_action] == 'left/right':
						monster.walk_direction = monster_action_direction[monster_action]
						monster.action = Action.repeat(Action.sequence(Action.move_to(x + 190, y, 3.0), Action.move_to(x, y, 1.5)), 0)
					elif monster_action_direction[monster_action] == 'up/down':
						monster.walk_direction = monster_action_direction[monster_action]
						monster.action = Action.repeat(Action.sequence(Action.move_to(x, y + 150, 2.0), Action.move_to(x, y, 1.5)), 0)
					monster.run_action(monster.action)
					monster_action += 1
					self.items.append(monster)
		
				elif col == "E":
					exit = Door(parent=self)
					exit.position = (x, y)
					self.items.append(exit)
					
				elif col == "S":
					sword = Sword(parent=self)
					sword.position = (x, y)
					self.items.append(sword)
					
				elif col == "C":
					coin = Coin(parent=self)
					coin.position = (x, y)
					self.items.append(coin)
					
				elif col == "P":
					self.player = Player(parent=self)
					self.player.position = (x, y)
					
				x += 64
			y -= 64
			x = 0

			
	def update(self):
		# this method is called, hopefully, 60 times a second

		# check if user moved player
		player_moved = True
		if not self.left_button.touched and not self.right_button.touched and not self.up_button.touched and not self.down_button.touched:
			self.player.texture = player_standing_texture
			self.player.walk_step = -1
			player_moved = False
		
		# current player position
		x = self.player.position.x
		y = self.player.position.y
		
		# determine new player position
		if self.left_button.touched:
			x = max(0, min(self.size.w, x - 1 * max_player_speed))
			self.player.x_scale = -1
		elif self.right_button.touched:
			x = max(0, min(self.size.w, x + 1 * max_player_speed))
			self.player.x_scale = 1
		elif self.up_button.touched:
			y = max(0, min(self.size.h, y + 1 * max_player_speed))
		if self.down_button.touched:
			y = max(0, min(self.size.h, y - 1 * max_player_speed))
				
		# check if user interacted with any items in the dungeon
		hit_item = False
		for item in list(self.items):
			
			# reset monster movement after initial attack
			if isinstance(item, Monster):
				if item.attacked:
					if time.time() - self.monster_timeout > 3:
						item.attacked = False
						item.run_action(item.action)
						
				# monster move animation
				else:
					step = int(item.position.x / 20) % 2
					if item.walk_direction == 'up/down':
						step = int(item.position.y / 20) % 2
					
					if step != item.walk_step:
						item.texture = monster_walk_textures[step]
						item.walk_step = step
			
			# check in player interacts with items in game		
			if item.frame.intersects(self.player.hitbox(x, y, False)):
				
				# monster attack
				if isinstance(item, Monster):
					
					# monster dies if player has a sword
					if self.player.has_sword:
						item.texture = monster_dead_texture
						item.remove_all_actions()
						self.items.remove(item)
						sound.play_effect('assets/sounds/sword_swing.wav')
						
					# player loses one health. player dies if all health is lost.
					elif not item.attacked:
						item.attacked = True
						item.texture = monster_standing_texture
						self.monster_timeout = time.time()
						self.player.health -= 1
						item.remove_all_actions()
						sound.play_effect('assets/sounds/monster_attack.wav')
						hit_item = True
						self.disableControls()
							
						if (self.player.health >= 0):
							self.health_count.children[self.player.health].texture = Texture('assets/sprites/environment/empty_heart.png')
							
						if (self.player.health == 0):
							dialogs.alert('You\'re Dead', button1 = 'OK', hide_cancel_button = True)
							self.dismiss_modal_scene()
							
					else:
							if item.frame.intersects(self.player.hitbox(x, y, True)):
								hit_item = True
							
				elif isinstance(item, Sword):
					item.remove_from_parent()
					self.items.remove(item)
					sound.play_effect('assets/sounds/sword_pickup.wav')
					self.player.has_sword = True
						
				elif isinstance(item, Coin):
					item.remove_from_parent()
					self.items.remove(item)
					sound.play_effect('assets/sounds/pickup_coin.mp3')
					self.player.gold += item.get_coin_value()
					self.gold_count.text = str(self.player.gold)
						
				elif isinstance(item, Door):
					self.disableControls()
					dialogs.alert('You Win!!!', button1 = 'OK', hide_cancel_button = True)
					self.dismiss_modal_scene()
						
				elif isinstance(item, Wall):
					hit_item = True
			
		# move player if they didn't run into an item
		if not hit_item and player_moved:
			self.player.position = x, y
				
			# animate player moving and play sound
			step = int(self.player.position.x / 40) % 2
			if self.up_button.touched or self.down_button.touched:
				step = int(self.player.position.y / 40) % 2
					
			if step != self.player.walk_step:
				self.player.texture = player_walk_textures[step]
				sound.play_effect('assets/sounds/footstep.mp3', 0.5, 1.0 + 0.5 * step)
				self.player.walk_step = step
	
			
	def disableControls(self):
		# this method resets the user controls
		
		self.left_button.touched = False
		self.right_button.touched = False
		self.up_button.touched = False
		self.down_button.touched = False
		
		
	def touchControls(self, touch):
		# this method determines which user control was used
		
		if self.left_button.frame.contains_point(touch.location):
			self.left_button.touched = True

		elif self.right_button.frame.contains_point(touch.location):
			self.right_button.touched = True

		elif self.up_button.frame.contains_point(touch.location):
			self.up_button.touched = True
			
		elif self.down_button.frame.contains_point(touch.location):
			self.down_button.touched = True
		
		
	def touch_began(self, touch):
		# this method is called, when user touches a finger on the screen
		
		self.touchControls(touch)
			
			
	def touch_moved(self, touch):
		# this method is called, when user moves a finger around on the screen
		
		self.disableControls()
		self.touchControls(touch)
		
		
	def touch_ended(self, touch):
		# this method is called, when user releases a finger from the screen
		
		self.disableControls()
		
#if __name__ == '__main__':
#	run(DungeonScene(), LANDSCAPE, show_fps=True)
