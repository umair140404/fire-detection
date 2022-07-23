import imp
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
import io
from PIL import Image
import time


def download_image(download_path, url, file_name):
    try:
        image_content = requests.get(url).content
        image_file = io.BytesIO(image_content)
        image = Image.open(image_file)
        file_path = download_path + file_name

        with open(file_path, "wb") as f:
            image.save(f, "JPEG")

        print("Success")
    except Exception as e:
        print('FAILED -', e)


f = open('urls.txt', 'r')
urls = f.readlines()
f.close()

for i, url in enumerate(urls):
    download_image("sunset/", url, str(i) + ".jpg")

print('done')
