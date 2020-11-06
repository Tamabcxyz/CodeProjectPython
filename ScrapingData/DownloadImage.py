import os
import json
import requests
from bs4 import BeautifulSoup

'''this is google search image url'''
GOOGLE_IMAGE='https://www.google.com/search?site=&tbm=isch&source=hp&biw=1873&bih=990'

'''this is request header'''
usr_agent={
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) coc_coc_browser/89.0.124 Chrome/83.0.4103.124 Safari/537.36',
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Charset':'utf-8, iso-8859-1;q=0.5',
    'Accept-Encoding':'none',
    'Accept-Language':'en-US, en;q=0.8,',
    'Connection':'keep-alive',
}
SAVE_FOLDER="images"
i=0
def DownloadImages():
    your_find=input("What are you looking for??")
    n_image=int(input("How many images do you want?"))
    print("Start searching...")
    searchurl=GOOGLE_IMAGE+'&q='+your_find
    print(searchurl)
    response=requests.get(searchurl, headers=usr_agent)
    print(response)
    html=response.text
    soup=BeautifulSoup(html, 'html.parser')
    results=soup.findAll('img',{'class':'rg_i Q4LuWd'} ,limit=n_image)
    print(results)
    link=[]
    rr=requests.get(https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcQyrPs6Db_CVvymqFTt2bbTNburC7e-kL1_Gg&amp;usqp=CAU)
    imgname=SAVE_FOLDER+'/'+'data'+str(i+1)+'.jpg'
    i=i+1
    with open(imgname,'wb') as file:
        file.write(response.content)
    print("done")
    
    
    
def main():
    if not os.path.exists(SAVE_FOLDER):
        os.mkdir(SAVE_FOLDER)
    DownloadImages()
    
if __name__ == '__main__':
    main()