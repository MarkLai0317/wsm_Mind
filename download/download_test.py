# Download test.zip
import requests 
file_url = "https://mind201910small.blob.core.windows.net/release/MINDlarge_test.zip"
    
r = requests.get(file_url, stream = True) 
  
with open("./test.zip", "wb") as file: 
    for block in r.iter_content(chunk_size = 1024):
         if block: 
             file.write(block) 

#unzip -q test.zip -d test