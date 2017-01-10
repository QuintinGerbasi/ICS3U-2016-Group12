# Created by: Quintin Gerbasi & David Currey
# Created on: Jan 2017
# Created for: ICS3U
# This scene shows the help scene.

from scene import *
import ui
import sound

from main_menu_scene import *

class HelpScene(Scene):
    def setup(self):
        # this method is called, when user moves to this scene
        
        center_of_screen = self.size/2
        self.name = 'help_scene'
        
        # add background color
        self.background = SpriteNode('assets/sprites/background/main_menu_background.jpg',
                                     position = (self.size.x/2, self.size.y/2), 
                                     parent = self, 
                                     size = self.size)
                                     
        self.help_text = LabelNode(text = 'Design by: Quintin Gerbasi & David Currey',
                                      font=('Helvetica', 20),
                                      parent = self,
                                      position = (self.size.x/2 + 100, self.size.y/2),
                                      scale = 1)
                                      
        back_button_position = self.size
        back_button_position.x = 30
        back_button_position.y = 50
        self.back_button = SpriteNode('assets/sprites/buttons/backward.png',
                                       parent = self,
                                       position = back_button_position,
                                       scale = 2)
        
    def update(self):
        # this method is called, hopefully, 60 times a second
        pass
    
    def touch_began(self, touch):
        # this method is called, when user touches the screen
        pass
    
    def touch_moved(self, touch):
        # this method is called, when user moves a finger around on the screen
        pass
    
    def touch_ended(self, touch):
        # this method is called, when user releases a finger from the screen
        
        # if start button is pressed, goto game scene
        if self.back_button.frame.contains_point(touch.location):
            sound.play_effect('assets/sounds/interface.wav')
            self.dismiss_modal_scene()
    
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
    
