import sys
import requests
import os
import urllib.parse as urlparse

def is_downloadable(url):
    h= requests.head(url,allow_redirects=True)
    header= h.headers
    contentType=header.get('content-type')
    
    if 'text' in contentType.lower():
        return False
    
    if 'html' in contentType.lower():
        return False
    
    return True
    
def get_filename_from_cd(url):
    urlparser = urlparse(url)
    return os.path.basename(urlparser.path)
    
def imageDownloader(url):
    allow = is_downloadable(url)
    
    if allow:
        try:
            response = request.get(url,allow_redirects=True)
            fname=get_filename_from_cd(url)
            dir = open(fname,"wb")
        
            for buffer in response.iter_content(1024):
                dir.write(buffer)
            dir.close()
            return True
        except Exception as error:
            return False

def main():
    
    url = 'https://www.google.com/favicon.ico'
    result = imageDownloader(url)
    
    if result:
        print("Images downloaded successfully")
    else:
        print("Failed to download")

if __name__ == "__main__":
    main()