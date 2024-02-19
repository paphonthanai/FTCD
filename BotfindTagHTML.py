import bs4
from bs4 import BeautifulSoup
import requests
import os
import shutil

def getdata(url):
    r = requests.get(url)
    return r.text



Espisote = 1
while Espisote <= 202:
    data = getdata('https://www.oremanga.net/jujutsu-kaisen/jujutsu-kaisen-=' + str(Espisote))
    Soup = bs4.BeautifulSoup(data,'html.parser')
    ReadArea = Soup.find('div',{'class':'reader-area'})
    fileCartoon = ReadArea.findAll('img')
    souceFire = str(Soup.findAll('src'))
    Page = ""
    imageSrc = []
    imageLink = ""
    FolderPath = os.chdir(r"C:\Users\Name\Desktop\MyCartoonDownload\Jujutsu Kaisen")
    folderName = "Es" + str(Espisote)
    Espisote += 1

    # สร้างโฟล์เดอร์เก้็บไฟล?
    Createfolder = os.mkdir(folderName)
    # destination = r'C:\Users\Name\Desktop\MyCartoonDownload'
    # newfolder = r"C:\Users\Name\Desktop\MyCartoonDownload\Es0"
    CreatefolderSucess = True
    print("CreateFolder Success")
    
    if (CreatefolderSucess == True):
        NewFolderPath = os.chdir(os.getcwd() + "/" + str(folderName))
        folder_open = True
        print(os.getcwd())
        if (folder_open == True):
            NowFolder = r"C:\Users\Name\Desktop\MyCartoonDownload\Es0"
            count = 0
            for image in ReadArea.findAll('img'):
                print(image['src'])
                imageSrc.append(image['src'])
                respond = requests.get(str(image['src']))
                with open("fileImage" + str(count) + ".jpg","wb") as NewFolderPath:
                    NewFolderPath.write(respond.content)
                count += 1
            print("Download Success")    
        else:
            print("error")
