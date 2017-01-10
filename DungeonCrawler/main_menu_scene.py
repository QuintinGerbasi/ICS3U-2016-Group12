# Created by: Quintin Gerbasi & David Currey
# Created on: Jan 2017
# Created for: ICS3U
# This scene shows the main menu.

from scene import *
from help_scene import *
from dungeon_scene import *
import ui

class MainMenuScene(Scene):
    def setup(self):
        # this method is called, when user moves to this scene
        
        # add background color
        self.background = SpriteNode('assets/sprites/background/main_menu_background.jpg',
                                     position = (self.size.x/2, self.size.y/2), 
                                     parent = self, 
                                     size = self.size)
        
                                     
        self.start_button = SpriteNode('assets/sprites/buttons/start button.png',
                                       parent = self,
                                       position = self.size/2)
                                       
        self.help_button = SpriteNode('assets/sprites/buttons/help_button.png',
                                       parent = self,
                                       position = (self.size.x/2, self.size.y/2 - 200))
                                       
        self.music = sound.Player('assets/sounds/main_menu_music.mp3')
        self.music.number_of_loops = -1
        self.music.play()
        
        self.previous_scene = None
        self.name = 'main_menu_scene'
        
    def update(self):
        # this method is called, hopefully, 60 times a second
        
        # play correct music based on scene being displayed
        if self.presented_scene != self.previous_scene:
            if self.presented_scene != None:
                if self.presented_scene.name == 'dungeon_scene':
                    self.music = sound.Player('assets/sounds/dungeon_music.mp3')
                    self.music.play()
                elif self.previous_scene != None:
                    self.music = sound.Player('assets/sounds/main_menu_music.mp3')
                    self.music.play()
            else:
                if self.previous_scene.name != 'help_scene':
                    self.music = sound.Player('assets/sounds/main_menu_music.mp3')
                    self.music.play()
            
            self.previous_scene = self.presented_scene
            
    def touch_began(self, touch):
        # this method is called, when user touches the screen
        pass
    
    def touch_moved(self, touch):
        # this method is called, when user moves a finger around on the screen
        pass
    
    def touch_ended(self, touch):
        # this method is called, when user releases a finger from the screen
        
        # if start button is pressed, goto game scene
        if self.start_button.frame.contains_point(touch.location):
            sound.play_effect('assets/sounds/interface.wav')
            self.present_modal_scene(DungeonScene())
            
        # if help button is pressed, goto help scene
        if self.help_button.frame.contains_point(touch.location):
            sound.play_effect('assets/sounds/interface.wav')
            self.present_modal_scene(HelpScene())
    
    def did_change_size(self):
        # this method is called, when user changes the orientation of the screen
        # thus changing the size of each dimension
        pass
    
    def pause(self):
        # this method is called, when user touches the home button
        # save anything before app is put to background
        pass
    
    def resume(self):
        # this method is called, when user place app from background 
        # back into use. Reload anything you might need.
        pass
