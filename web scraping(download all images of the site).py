import os

from sphinx.util import requests

main_url='https://www.ducatindia.com'
all_apps=[]
resp=requests.get(main_url)
soap=bs4.BeautifulSoup(resp.text,'html.parser')
anchor_data=soap.find_all('a')
count=0
for i in anchor_data:
    url=i.get('href')
    if (url.startswith('https') or url.startswith('http')) and 'www.ducatindia.com' in url:
        all_apps.append(url)

for i in all_apps:
    res=requests.get(main_url)
    soup=bs4.BeautifulSoup(resp.text,'html.parser')
    anchor=soap.find_all('img')
    for j in anchor:
        imgs_url=j.get('src')
        if not imgs_url.startswith('https://'):
            imgs_url=main_url+imgs_url
        if main_url in imgs_url:
            img_name=imgs_url[imgs_url.rindex('/')+1:]
            req=requests.get(imgs_url)
            img_bytes=req.content
            if not os.path.isdir('images2'):
                os.mkdir('images2')
            try:    
                file=open(f'images2/{img_name}','wb')
                file.write(img_bytes)
                print(img_name)
                file.close()
            except Exception as e:
                print(e)
    if(count==5):
        break
    count+=1
    print(count)
print('work is Done......')
     