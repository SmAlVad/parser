import requests, bs4

s = requests.get('http://svobzan.amur.ru/Vak.htm');
b = bs4.BeautifulSoup(s.text, 'html.parser')

td = b.find('table').find('td', class_='tbl_brd_cnt')
print(td.text)
