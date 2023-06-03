import requests
from bs4 import BeautifulSoup


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/58.0.3029.110 Safari/537.3'
}

tested_page = (
    "https://www.fotocasa.es/es/alquiler/viviendas/barcelona-capital/"
    "todas-las-zonas/l?conservationStatusIds=0&constructionTypeIds=1%"
    "2C2&maxPrice=1300&minRooms=3&minSurface=60&sortType=publication"
    "Date"
)

if __name__ == "__main__":

    # Retrieves the tested page
    response_page = requests.get(tested_page, headers=headers)

    # Parsing time with beautiful soup
    soup = BeautifulSoup(response_page.content, "html.parser")

    print("test in debugging time!")
