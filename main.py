
import requests
import json
import os
from PIL import Image


def download_image(folder_name):
    url = "https://disk.yandex.ru/d/V47MEP5hZ3U1kg"
    params = {"path": f"/{folder_name}"}
    response = requests.get(url, params=params)
    try:
        download_url = response.json()
        print(download_url)
        response = requests.get(download_url)
        with open(f"{folder_name}.png", "wb") as file:
            file.write(response.content)
    except json.decoder.JSONDecodeError:
        print("Error from server: " + str(response.content))

def tiff_file(folder_names):
    images = []
    for folder_name in folder_names:
        download_image(folder_name)
        img_path = f"{folder_name}.png"
        if os.path.exists(img_path):
            img = Image.open(img_path)
            images.append(img)
        else:
            print(f"File not found: {img_path}")

    if images:
        images[0].save("Result.tif", save_all=True, append_images=images[1:])

folder_names = ['1369_12_Наклейки 3-D_3']
tiff_file(folder_names)





