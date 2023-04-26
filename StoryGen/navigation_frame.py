import customtkinter
import os
from PIL import Image


class NavigationFrame(customtkinter.CTkFrame):
    # create navigation frame
    def __init__(
        self, master, home_frame, previous_generations_frame, key_frame, **kwargs
    ):
        super().__init__(master, **kwargs)

        self.home_frame = home_frame
        self.previous_generations_frame = previous_generations_frame
        self.key_frame = key_frame

        # load images with light and dark mode image
        image_path = os.path.join(
            os.path.dirname(os.path.realpath(__file__)), "app_images"
        )

        self.logo_image = customtkinter.CTkImage(
            Image.open(os.path.join(image_path, "logo.png")), size=(35, 35)
        )

        self.home_image = customtkinter.CTkImage(
            light_image=Image.open(os.path.join(image_path, "home_light.png")),
            dark_image=Image.open(os.path.join(image_path, "home_dark.png")),
            size=(22, 22),
        )
        self.chat_image = customtkinter.CTkImage(
            light_image=Image.open(os.path.join(image_path, "paint_brush_light.png")),
            dark_image=Image.open(os.path.join(image_path, "paint_brush_dark.png")),
            size=(22, 22),
        )
        self.add_user_image = customtkinter.CTkImage(
            light_image=Image.open(os.path.join(image_path, "key_light.png")),
            dark_image=Image.open(os.path.join(image_path, "key_dark.png")),
            size=(22, 22),
        )

        self.navigation_frame_label = customtkinter.CTkLabel(
            self,
            text="  StoryGen",
            image=self.logo_image,
            compound="left",
            font=customtkinter.CTkFont(size=18, weight="bold"),
        )
        self.navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)

        self.home_button = customtkinter.CTkButton(
            self,
            corner_radius=0,
            height=40,
            border_spacing=10,
            text="Home",
            fg_color="transparent",
            text_color=("gray10", "gray90"),
            hover_color=("gray70", "gray30"),
            image=self.home_image,
            anchor="w",
            command=self.home_button_event,
        )
        self.home_button.grid(row=1, column=0, sticky="ew")

        self.previous_generations_button = customtkinter.CTkButton(
            self,
            corner_radius=0,
            height=40,
            border_spacing=10,
            text="Previous generations",
            fg_color="transparent",
            text_color=("gray10", "gray90"),
            hover_color=("gray70", "gray30"),
            image=self.chat_image,
            anchor="w",
            command=self.previous_generations_button_event,
        )
        self.previous_generations_button.grid(row=2, column=0, sticky="ew")

        self.key_button = customtkinter.CTkButton(
            self,
            corner_radius=0,
            height=40,
            border_spacing=10,
            text="API key",
            fg_color="transparent",
            text_color=("gray10", "gray90"),
            hover_color=("gray70", "gray30"),
            image=self.add_user_image,
            anchor="w",
            command=self.key_button_event,
        )
        self.key_button.grid(row=3, column=0, sticky="ew")

        self.appearance_mode_optionmenu = customtkinter.CTkOptionMenu(
            self,
            values=["Light", "Dark", "System"],
            command=self.change_appearance_mode_event,
        )
        self.appearance_mode_optionmenu.grid(row=6, column=0, padx=20, pady=(10, 10))

        # select default frame
        self.select_frame_by_name("home")

        # set default appearance
        self.appearance_mode_optionmenu.set("System")

    def add_frame(self, frame):
        self.frames.update(frame)
        print(self.frames)

    def home_button_event(self):
        self.select_frame_by_name("home")

    def previous_generations_button_event(self):
        self.select_frame_by_name("previous_generations")

    def key_button_event(self):
        self.select_frame_by_name("key")

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def select_frame_by_name(self, name):
        # set button color for selected button
        self.home_button.configure(
            fg_color=("gray75", "gray25") if name == "home" else "transparent"
        )
        self.previous_generations_button.configure(
            fg_color=("gray75", "gray25")
            if name == "previous_generations"
            else "transparent"
        )
        self.key_button.configure(
            fg_color=("gray75", "gray25") if name == "key" else "transparent"
        )

        # show selected frame
        if name == "home":
            self.home_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.home_frame.grid_forget()
        if name == "previous_generations":
            self.previous_generations_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.previous_generations_frame.grid_forget()
        if name == "key":
            self.key_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.key_frame.grid_forget()
