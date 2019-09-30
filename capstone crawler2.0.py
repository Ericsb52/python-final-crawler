import requests
from bs4 import BeautifulSoup as bs
from collections import Counter
import statistics
above = []
below = []

def get_data(file):
    clean_urls =[]
    text_file = open(file, "r")
    urls = text_file.readlines()
    text_file.close()
    for url in urls:
        clean_urls.append(url.split("\n")[0])
    return clean_urls

def scraper(url, tag):
    print("collecting Data")
    r = requests.get(url)
    soup = bs(r.text,"html.parser")
    links = soup.find_all("a")
    titles = titles_gen(links)
    return titles
    

def titles_gen(links):
    titles = []   

    def data_formater(url):
        if "https://" in url:
            url = url.split("https://")[-1]
            url = url.split("www.")[-1]
            url = url.split(".")[0]
            titles.append(url)


        
    for link in links:
        data_formater(link["href"])



    return titles


def stats(links,above,below):
    alllinks = set()
    for link in links:
        alllinks.add(link)
    counts = Counter(links)
    counts_sorted = sorted(counts.items(), key=lambda x: x[1])
    
    def find_median(data):
        if len(data)%2 == 0:
           median = len(data)/2
        else:
            median = len(data)//2+1
        return median
    links = []
    for x in counts_sorted:
        links.append(x)

    median = find_median(alllinks)
    for item in range(len(alllinks)):
        if item < median:
            below.append(links[item])
        else:
            above.append(links[item])
        
            
    
            
        

    

def main(above, below):
    file = "test_url_list.txt"
    data = get_data(file)
    #data = ["http://www.youtube.com","http://www.microsoft.com","http://www.facebook.com"]
    for item in data:
        links = scraper(item,"a")
        stats(links,above,below)
    print ("Above the Median")
    print(above)
    print()
    print("Below the Median")
    print(below)

    
   








main(above, below)
input("press enter to exit")
