import requests
import zipfile

url = "https//:somewebsite.com/file.zip"

r = requests.get(url)

# save the zip file in current directory with the name "myzip.zip"
with open("myzip.zip", "wb") as zip
  zip.write(r.content)
  
# extract zip file and put all files in a folder named "myzipfolder"
with zipfile.ZipFile("myzip.zip", "r") as zf:
  zf.extractall("myzipfolder/")
