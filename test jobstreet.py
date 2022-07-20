# import requests
# from bs4 import BeautifulSoup
#
# url = 'https://www.jobstreet.co.id/id/job-search/python-jobs-in-jakarta-raya/'
# params = {
#     'q': 'Python',
#     'l': 'Depok'
# }
#
# headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 Edg/103.'}
#
# res = requests.get(url, params=params)
#
# def Get_Total_Pages():
#     url = 'https://www.jobstreet.co.id/id/job-search/python-jobs-in-jakarta-raya/'
#     params = {
#         'q': 'Python',
#         'l': 'Depok'
#     }
#
#     res = requests.get(url, params=params)
#     soup = BeautifulSoup(res.text, 'html.parser')
#     print(soup.prettify())
#
#
# if '__name__' == '__main__':
#     Get_Total_Pages()