import requests
import random
from bs4 import BeautifulSoup
import os
url="https://www.imdb.com/chart/top"

def main():
    response=requests.get(url)
    html=response.text
    soup=BeautifulSoup(html,"html.parser")
    ineed=soup.select('td.titleColumn')
    def get_year(movieTag):
        stuff=movieTag.text.split()#it return array with year in the end of array
        year=stuff[-1]
        return year
    list_Years=[get_year(tag) for tag in ineed]
    innerIneed=soup.select('td.titleColumn a')
    list_Actors=[tag['title'] for tag in innerIneed]
    list_NameMovies=[tag.text for tag in innerIneed]
    
    allRating=soup.select('td.posterColumn span[name=ir]')
    list_Rating=[float(tag['data-value']) for tag in allRating]
    n_Movies=len(list_NameMovies)
    
    allLinks=soup.select('td.titleColumn a')
    list_Links=[tag['href'] for tag in allLinks]
    
    allImage=soup.select('td.posterColumn a img')
    list_Image=[tag['src'] for tag in allImage]
    
    SAVE_FOLDER="images"
    i=0
    #create random movie
    while True:
        index=random.randrange(0,n_Movies)
        print(f"{list_NameMovies[index]}, {list_Years[index]}, {list_Rating[index]}, {list_Actors[index]}, links: {list_Links[index]},link img: {list_Image[index]}")
        acctionLinkImg=requests.get(list_Image[index])
        imgname=SAVE_FOLDER+'/'+'data'+str(i+1)+'.jpg'
        i=i+1
        if not os.path.exists(SAVE_FOLDER):
            os.mkdir(SAVE_FOLDER)
        with open(imgname,"wb") as file:
            file.write(acctionLinkImg.content)
        user_choose=input("Do you want another movie (y/n)?")
        if user_choose!='y':
            break;
    

if __name__=="__main__":
    main()