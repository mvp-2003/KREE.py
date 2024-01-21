import requests
import os
import shutil

a = input("Enter complete URL: ")

r = requests.get(a)

with open("websiteHTML.txt","w") as f:
    f.write(r.text)

shutil.move("websiteHTML.txt", "store")