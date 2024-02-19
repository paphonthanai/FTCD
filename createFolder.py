import os
import requests

folder_name  = "Folder"
respond = requests.get('https://img.oremanga.net/47/6c/65/27BTE3S6AC-1627926360.jpg')
os.chdir(r"C:\Users\Name\Desktop\MyCartoonDownload")
os.mkdir(folder_name)
out_file = open(r"C:\Users\Name\Desktop\MyCartoonDownload"+ str(folder_name) ,"w")
out_file.write('https://img.oremanga.net/47/6c/65/27BTE3S6AC-1627926360.jpg')