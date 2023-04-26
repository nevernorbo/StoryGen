import customtkinter
import os
import json
from PIL import Image


class PreviousGenerationsFrame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.no_stories_yet = customtkinter.CTkLabel(self, text="You don't have any saved stories yet!\n", width=150,
                                                     height=50, font=customtkinter.CTkFont(size=16))
        if not self.stories_exist():
            self.no_stories_yet.place(relx=0.5, rely=0.3, anchor='center')
            return
        else:
            self.no_stories_yet.destroy()

        self.stories_frame = customtkinter.CTkScrollableFrame(self)
        self.stories_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
        self.stories_frame.columnconfigure(0, weight=1)

        self.refresh_button = customtkinter.CTkButton(master=self, text="Refresh stories!", command=self.get_stories,
                                                      width=150, height=50, corner_radius=20,
                                                      font=customtkinter.CTkFont(size=16))
        self.refresh_button.grid(row=1, column=0, pady=(0, 10), sticky="s")

    def stories_exist(self):
        current_dir = os.path.dirname(os.path.relpath(__file__))
        stories_dir = os.path.join(current_dir, "Stories")
        file_path = os.path.join(stories_dir, "stories.json")

        if os.path.exists(file_path):
            return True
        else:
            return False

    def get_stories(self):
        current_dir = os.path.dirname(os.path.relpath(__file__))
        stories_dir = os.path.join(current_dir, "Stories")
        file_path = os.path.join(stories_dir, "stories.json")

        # read data from stories.json
        with open(file_path, 'r') as f:
            data = json.load(f)

        # for each story create labels and textboxes
        frame_count = 0
        for i, story in enumerate(data):
            frame = customtkinter.CTkFrame(self.stories_frame, border_width=3)
            frame.grid(row=i * 3, column=0, sticky='nsew', padx=10, pady=20)
            frame.columnconfigure(0, weight=1)

            # title and date
            title_label = customtkinter.CTkLabel(master=frame, text=f"Title: {story['title']}")
            date_label = customtkinter.CTkLabel(master=frame, text=f"Date created: {story['date created']}")

            # textbox for story content
            story_textbox = customtkinter.CTkTextbox(master=frame, wrap="word", height=300)
            story_textbox.insert('1.0', story['content'])

            # A button for viewing the image if there is one
            if (story['image_path'] != ""):
                view_image_button = customtkinter.CTkButton(master=frame, text="View image", command=lambda
                    image_path=story['image_path']: self.open_image(image_path))
                view_image_button.grid(row=i * 3 + 3, column=0, sticky='w', padx=10, pady=10)

            title_label.grid(row=i * 3 + 1, column=0, sticky="w", padx=10, pady=10)
            date_label.grid(row=i * 3 + 2, column=0, sticky="w", padx=10, pady=10)
            story_textbox.grid(row=i * 3 + 4, column=0, sticky="nsew", padx=10, pady=(10, 20))

            if (frame_count % 2 == 0):
                frame.configure(border_color='#663781')
            else:
                frame.configure(border_color='#687eea')

            frame_count += 1

    def open_image(self, image_path):
        image = Image.open(image_path)
        image.show()
