import customtkinter
import os
from openai_api import check_api_key, set_api_key


class KeyFrame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.grid_columnconfigure(0, weight=1)

        self.key_frame_label = customtkinter.CTkLabel(
            master=self,
            text="API key",
            compound="left",
            font=customtkinter.CTkFont(size=20),
        )
        self.key_frame_label.grid(row=0, column=0, padx=20, pady=(200, 10))

        # Enter API key
        self.key_frame_entry = customtkinter.CTkEntry(
            master=self,
            placeholder_text="Your API key goes here",
            width=600,
            font=customtkinter.CTkFont(size=16),
        )
        self.key_frame_entry.grid(row=1, column=0, padx=10, pady=0)

        # Save API key button
        self.save_api_key_button = customtkinter.CTkButton(
            master=self,
            text="Save API key",
            width=150,
            height=40,
            command=self.save_api_key_event,
            corner_radius=20,
            font=customtkinter.CTkFont(size=16),
        )
        self.save_api_key_button.grid(row=2, column=0, padx=20, pady=30)

    def save_api_key(self, key_input):
        key_input = key_input.strip(" \n")
        if check_api_key(key_input):
            print("API key is valid")
            self.key_frame_entry_success = customtkinter.CTkLabel(
                master=self,
                text="API key successfully set!",
                width=150,
                height=40,
                fg_color="#2c7d0a",
                corner_radius=20,
                font=customtkinter.CTkFont(size=16),
            )
            self.key_frame_entry_success.grid(row=3, column=0, padx=10, pady=30)

            os.environ["API_KEY"] = key_input
            set_api_key()

            # Replace the whole key for some security and disable the field
            self.key_frame_entry.delete(0, last_index=len(key_input) - 1)
            key_input = key_input[:5] + " ... " + key_input[-5:]
            self.key_frame_entry.insert(0, key_input)
            self.key_frame_entry.configure(
                state="disabled", fg_color="#2c7d0a", text_color="#b8b2b2"
            )
        else:
            self.key_frame_entry_fail = customtkinter.CTkLabel(
                master=self,
                text="Invalid API key!",
                width=150,
                fg_color="#f51616",
                height=40,
                corner_radius=20,
                font=customtkinter.CTkFont(size=16),
            )
            self.key_frame_entry_fail.grid(row=3, column=0, padx=10, pady=30)
            print("Invalid API key")

    def save_api_key_event(self):
        self.save_api_key(self.key_frame_entry.get())
