# from django.test import TestCase
# import requests
# # Create your tests here.
# response = requests.get(
#     f"https://www.googleapis.com/books/v1/volumes?q=intitle:clean code")
# book = response.json()

# # for ids in book['items'][0]['id']:
# #     title = book['items'][0]['volumeInfo']['subtitle']

# #     # for reaction in data:
# #     #     title = reaction.get('title')
# #     #     # else:
# #     #     #     title = data['items']['volumeInfo'].get('title')

# #     context = {
# #         # 'title': book['items'][0]['volumeInfo']['title'],
# #         # 'publishedDate': book['items'][0]['volumeInfo']['publishedDate'],
# #         # 'image': book['items'][0]['volumeInfo']['imageLinks']['thumbnail']

# #     }

# # for element in book['title']:
# #         print(element['title']['subtitle'])
# # print(range(len(book['items'][0]['volumeInfo']['subtitle'])))
# subtitlesl = []
# titlesl = []
# linksl = []
# # frontimagel = []
# for i in range(len(book['items'][0]['volumeInfo']['subtitle'])):
#     subtitles = book['items'][i]['volumeInfo'].get('subtitle')
#     if subtitles == None:
#         subtitlesl.append('Aucun')
#     else:
#         subtitlesl.append(subtitles)

#     titles = book['items'][0]['volumeInfo'].get('title')
#     titlesl.append(titles)

#     links = book['items'][0]['volumeInfo']['previewLink']
#     linksl.append(links)

#     # frontimage = book['items'][i]['volumeInfo']['imageLinks'].get(
#     #     'smallThumbnail')
#     # frontimagel.append(frontimage)

#     # if subtitles == None:
#     #     print(titles+'  '+'Aucun')
#     # else:
#     #     print(titles+'  '+subtitles)

# # print(subtitlesl)
# # print(titlesl)
#     dictionary = dict(zip(titlesl, subtitlesl))
#     titless = dictionary.keys()
#     subtitless = dictionary.values()
#     mylist = zip(titless, subtitless, linksl)

# for k, v, i in mylist:
#     print(k, v, i)
import time
import requests
from bs4 import BeautifulSoup

# URL = "https://www.pdfdrive.com/"
URL = "https://www.pdfdrive.com/search?q=The+Clean+Coder&pagecount=&pubyear=&searchin=&em="
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
els = soup.find("h2")
hrf = soup.find("a", {"class": "ai-search"}, href=True)

print(els.text)
# for ahr in hrf:
print(hrf['href'])


response = requests.get(f"https://www.pdfdrive.com{hrf['href']}")
pagezz = BeautifulSoup(response.content, "html.parser")
redirectToDownloadPage = pagezz.find(
    "a", {"class": "btn"}, href=True)

print(redirectToDownloadPage['href'])

response2 = requests.get(
    f"https://www.pdfdrive.com{redirectToDownloadPage['href']}")
soupz = BeautifulSoup(response2.content, "html.parser")
print(soupz)
# time.sleep(20)
# pagezzDown = BeautifulSoup(response2.content, "html.parser")
# redirectTofilePDF = pagezzDown.find(
#     "a", {"class": "btn"}, href=True)

# print(redirectTofilePDF['href'])
