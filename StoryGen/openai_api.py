import requests
import os
import openai
from base64 import b64decode


# Most of the code used in this file can be viewed on:
# https://platform.openai.com/docs/guides/chat


def get_api_key():
    return os.environ.get("API_KEY")


def set_api_key():
    openai.api_key = get_api_key()


def check_api_key(api_key):
    url = "https://api.openai.com/v1/engines/davinci/codex/generate"

    # Set headers with API key
    headers = {"Content-Type": "application/json", "Authorization": f"Bearer {api_key}"}

    # Send a test request
    response = requests.post(url, headers=headers)

    # Check response code
    if response.status_code == 401:
        return False
    else:
        return True


def get_response(prompt):
    prompt = prompt.strip(" \n")

    # Handle potential errors with the prompt
    if prompt == "":
        return "invalid_prompt"

    set_api_key()
    # Query ChatGPT
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            # TODO more juice? system commands
            {
                "role": "system",
                "content": "You are a creative assistant, you create colorful stories.",
            },
            {"role": "user", "content": f"{prompt}"},
            {"role": "user", "content": "Give the story a title on the first line"},
        ],
    )

    # TODO Handle errors from chatGPT

    response = completion["choices"][0]["message"]["content"]
    return response


# https://platform.openai.com/docs/guides/images/usage
def generate_image(image_entry, specification):
    set_api_key()

    response = openai.Image.create(
        prompt=f"{image_entry}. {specification}",
        n=1,
        size="512x512",
        response_format="b64_json",
    )
    image = response["data"][0].b64_json

    current_dir = os.path.dirname(os.path.relpath(__file__))
    images_dir = os.path.join(current_dir, "created_images")
    # Save image to created_images folder if it doesn't exist create it
    if not os.path.exists(images_dir):
        os.makedirs(images_dir)

    image_entry = image_entry.lower().replace(" ", "_")
    image_path = os.path.join(images_dir, f"{image_entry}.jpg")
    with open(image_path, "wb") as f:
        f.write(b64decode(image))

    return image_path
