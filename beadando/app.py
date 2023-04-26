import customtkinter

from home_frame import *
from previous_generations_frame import *
from key_frame import *
from navigation_frame import *

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("StoryGen")
        self.geometry("1280x720")
        
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # create home/story gen frame
        self.home_frame = HomeFrame(master=self, fg_color="transparent", corner_radius=0)
        
        # create previous generations frame
        self.previous_generations_frame = PreviousGenerationsFrame(master=self, fg_color="transparent", corner_radius=0)

        # create api key frame
        self.key_frame = KeyFrame(master=self, fg_color="transparent", corner_radius=0)
        
        # create navigation frame
        self.navigation_frame = NavigationFrame(master=self, home_frame=self.home_frame, previous_generations_frame=self.previous_generations_frame, key_frame=self.key_frame, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(4, weight=1)
        

if __name__ == "__main__":
    app = App()
    app.mainloop()

