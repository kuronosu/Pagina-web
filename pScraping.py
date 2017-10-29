from bs4 import BeautifulSoup
import requests

class Curso(object):
    def __init__(self, src, alt):
        self.src = src
        self.alt = alt

def scraping():
    url = 'www.platzi.com/@KR0N0S31'
    rensponse = requests.get("https://" + url)
    soup = BeautifulSoup(rensponse.content, 'html.parser')
    images_container = soup.find_all('figure', {'class':'Course-badge'})
    cursos = []
    for i in images_container:
        image_src = i.find('img')['src']
        image_alt = i.find('img')['alt']
        cursos.append(Curso(image_src, image_alt))
    return cursos

# if __name__ == '__main__':
#     cursos = scraping()
#     for i in cursos:
#         print(i)
