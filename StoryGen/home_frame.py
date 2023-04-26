import customtkinter
from openai_api import *
from PIL import Image

import os
import json
import datetime
import re


class HomeFrame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.no_api_key_count = 0
        self.image_path = ""
        self.switch_var = customtkinter.StringVar(value="on")

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.new_idea_button = customtkinter.CTkButton(
            self,
            text="Create a new story!",
            command=self.new_idea,
            width=150,
            height=50,
            font=customtkinter.CTkFont(size=16),
        )
        self.new_idea_button.place(relx=0.5, rely=0.3, anchor="center")

    def new_idea(self):
        # Check if the user has inputted the API key
        if get_api_key() is None:
            self.no_api_key_found = customtkinter.CTkLabel(
                master=self,
                text="No API key found!\n\nPlease enter API key on the 'API key' tab!",
                width=300,
                height=100,
                fg_color="#b211b8",
                corner_radius=15,
            )
            if self.no_api_key_count == 0:
                self.no_api_key_found.grid(row=0, column=0, padx=20, pady=20)
            self.no_api_key_count += 1
            return

        # Grid and pack are mortal enemies
        if self.no_api_key_count > 0:
            self.no_api_key_found.destroy()
            self.no_api_key_count = 0

        # Hide new idea button
        self.new_idea_button.forget()

        self.new_idea_frame = customtkinter.CTkFrame(self)
        self.new_idea_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
        self.new_idea_frame.grid_columnconfigure(0, weight=1)

        self.new_idea_label = customtkinter.CTkLabel(
            master=self.new_idea_frame,
            text="Please enter your idea here!",
            font=customtkinter.CTkFont(size=20, weight="bold"),
        )
        self.new_idea_label.grid(row=1, column=0, padx=20, pady=10)

        # Idea entry box
        self.new_idea_entry_box = customtkinter.CTkTextbox(
            master=self.new_idea_frame,
            width=900,
            height=150,
            font=customtkinter.CTkFont(size=15),
        )
        self.new_idea_entry_box.grid(row=2, column=0, padx=20, pady=10)

        # Generate idea button
        self.generate_button = customtkinter.CTkButton(
            master=self.new_idea_frame, text="Generate", command=self.generate
        )
        self.generate_button.grid(row=3, column=0, padx=20, pady=10)

        self.new_idea_entry_box.focus()

    def generate(self):
        # Get the prompt from the entry box
        prompt = self.new_idea_entry_box.get("0.0", "end")

        # Get the response from the ChatGPT API
        response = get_response(prompt)
        print(response)

        # Hide the new idea frame
        self.new_idea_frame.grid_forget()

        # Show prompt
        self.generated_idea_frame = customtkinter.CTkScrollableFrame(self)
        self.generated_idea_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
        self.generated_idea_frame.grid_columnconfigure((0, 1), weight=1)

        # Your prompt was...
        self.your_prompt = customtkinter.CTkLabel(
            master=self.generated_idea_frame,
            text="Your prompt was:",
            font=customtkinter.CTkFont(size=20, weight="bold"),
        )
        self.your_prompt.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

        self.prompt = customtkinter.CTkTextbox(
            master=self.generated_idea_frame,
            width=800,
            height=80,
            wrap="word",
            font=customtkinter.CTkFont(size=18),
        )
        self.prompt.grid(row=1, column=1, padx=10, pady=10, sticky="ew")
        self.prompt.insert("0.0", prompt)
        self.prompt.configure(state="disabled")

        # Handle response
        self.handle_response(response)

    def handle_response(self, response):
        if response == "invalid_prompt":
            self.error_in_response("Please enter a valid prompt!")
            return

        title = self.create_clean_title(response)

        self.response_label = customtkinter.CTkLabel(
            master=self.generated_idea_frame,
            text=f"{title}",
            font=customtkinter.CTkFont(size=20, weight="bold"),
        )
        self.response_label.grid(row=2, column=0, padx=10, pady=10, columnspan=2)

        self.response_text = customtkinter.CTkTextbox(
            master=self.generated_idea_frame,
            width=800,
            height=400,
            wrap="word",
            font=customtkinter.CTkFont(size=18),
        )
        self.response_text.grid(row=3, column=0, padx=10, pady=10, columnspan=2)
        self.response_text.insert("0.0", response.lstrip(" \n"))
        self.response_text.configure(state="disabled")

        # Option to generate an image for the story
        self.generate_image_switch = customtkinter.CTkSwitch(
            master=self.generated_idea_frame,
            text="Generate image for the story",
            command=self.switch_event,
            variable=self.switch_var,
            onvalue="on",
            offvalue="off",
        )

        self.generate_image_switch.grid(row=4, column=0, padx=10, pady=10, columnspan=2)

        self.generate_image_switch.deselect()

        # Generate image fields
        self.generate_image_label = customtkinter.CTkLabel(
            master=self.generated_idea_frame,
            text="Enter the prompt for the image generation\n(feel free to change the title if you want to): ",
            font=customtkinter.CTkFont(size=14),
        )

        self.generate_image_entry = customtkinter.CTkEntry(
            master=self.generated_idea_frame,
            width=200,
            font=customtkinter.CTkFont(size=16),
        )
        self.generate_image_entry.insert(0, title)
        image_entry = self.generate_image_entry.get().strip()

        self.generate_image_entry_specify_further = customtkinter.CTkEntry(
            master=self.generated_idea_frame,
            placeholder_text="Specify the image parameters further (optional).",
            width=400,
            font=customtkinter.CTkFont(size=16),
        )
        specification = self.generate_image_entry_specify_further.get().strip()

        # Show image in frame
        self.generate_image_button = customtkinter.CTkButton(
            self.generated_idea_frame,
            text="Generate image",
            command=lambda: self.show_image(image_entry, specification),
        )

        self.save_response_button = customtkinter.CTkButton(
            self.generated_idea_frame,
            text="Save this Story",
            command=lambda: self.save_response(title, response, self.image_path),
        )
        self.save_response_button.grid(row=9, column=0, padx=10, pady=10, sticky="")

        self.new_idea_button_on_error = customtkinter.CTkButton(
            self.generated_idea_frame,
            text="Try something else...",
            command=self.new_idea,
        )
        self.new_idea_button_on_error.grid(
            row=9, column=1, padx=10, pady=10, sticky="w"
        )

        # Center the buttons in the frame
        self.generated_idea_frame.grid_columnconfigure(0, weight=1)
        self.generated_idea_frame.grid_columnconfigure(1, weight=1)

    # Show error on the generated idea frame
    def error_in_response(self, error_message):
        self.error_in_response_label = customtkinter.CTkLabel(
            master=self.generated_idea_frame,
            text=f"{error_message}",
            font=customtkinter.CTkFont(size=14),
            width=200,
            fg_color="#f51616",
            corner_radius=20,
        )
        self.error_in_response_label.grid(row=2, columnspan=2)

        self.new_idea_button_on_error = customtkinter.CTkButton(
            self.generated_idea_frame, text="Try again", command=self.new_idea
        )
        self.new_idea_button_on_error.grid(row=3, columnspan=2)

        # Create folder "Stories" if it doesn't exist else create a new directory with the title given by ChatGPT

    # Create "stories.json" if it doesn't exist else put in new story data
    # stories.json stores:
    #   title:   <title of the story>
    #   content: <the content of the story>
    #   date created: <datetime now only date>
    #   image_path: <the path of generated image (if there is none it's an empty string)>
    def save_response(self, title, response, image_path):
        # get absolute path of current script file
        current_dir = os.path.dirname(os.path.relpath(__file__))
        # create "Stories" folder if it doesn't exist
        stories_dir = os.path.join(current_dir, "Stories")
        if not os.path.exists(stories_dir):
            os.mkdir(stories_dir)
        # get current date and time
        date_created = datetime.datetime.now().strftime("%Y-%m-%d")
        # create dictionary with story data
        story_data = {
            "title": title,
            "content": response,
            "date created": date_created,
            "image_path": image_path,
        }
        # open stories.json file
        file_path = os.path.join(stories_dir, "stories.json")
        if os.path.exists(file_path):
            # read existing data from stories.json
            with open(file_path, "r") as file:
                stories = json.load(file)
            # add new story data to existing data if it isn't already saved
            already_exists = False
            for story in stories:
                if (
                    story_data.get("title") == story.get("title")
                    and story_data.get("content")[0:10] == story.get("content")[0:10]
                ):
                    already_exists = True

            if not already_exists:
                stories.append(story_data)
                # write updated data back to stories.json
                with open(file_path, "w") as file:
                    json.dump(stories, file)
                self.story_save_success = customtkinter.CTkLabel(
                    master=self.generated_idea_frame,
                    text="Your story has been saved!",
                    width=120,
                    height=30,
                    fg_color="#2c7d0a",
                    corner_radius=15,
                    font=customtkinter.CTkFont(size=16),
                )
                self.story_save_success.grid(
                    row=10, column=0, padx=10, pady=10, columnspan=2
                )
            else:
                self.story_save_error = customtkinter.CTkLabel(
                    master=self.generated_idea_frame,
                    text="This story has already been saved!",
                    width=120,
                    height=30,
                    fg_color="#b8b2b2",
                    corner_radius=15,
                    font=customtkinter.CTkFont(size=16),
                )
                self.story_save_error.grid(
                    row=10, column=0, padx=10, pady=10, columnspan=2
                )
        else:
            # create new stories.json file with story data
            with open(file_path, "w") as file:
                json.dump([story_data], file)

    def create_clean_title(self, response):
        title = response.split("\n")[0]

        if "title:" in title.lower():
            title = title[5:]

        # characters to remove
        pattern = r'[<>:"/\\|?*\x00-\x1F]'

        clean_title = re.sub(pattern, "", title)

        return clean_title

    def switch_event(self):
        # If user wants to generate image
        print(self.switch_var.get())

        if self.switch_var.get() == "on":
            self.generate_image_label.grid(
                row=5, column=0, padx=10, pady=10, columnspan=2
            )
            self.generate_image_entry.grid(
                row=6, column=0, padx=10, pady=10, columnspan=2
            )
            self.generate_image_entry_specify_further.grid(
                row=7, column=0, columnspan=2, padx=10, pady=10
            )
            self.generate_image_button.grid(
                row=8, column=0, columnspan=2, padx=10, pady=10
            )

        else:
            self.generate_image_label.grid_forget()
            self.generate_image_entry.grid_forget()
            self.generate_image_entry_specify_further.grid_forget()
            self.generate_image_button.grid_forget()

    def show_image(self, image_entry, specification):
        image_path = generate_image(image_entry, specification)

        image = Image.open(image_path)
        image.show()
        self.image_path = image_path
