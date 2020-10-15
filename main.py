import requests
import json
import urllib.request
import re
import os.path

js_url = "https://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&mkt=en-US"

try:
    js_data = json.loads(requests.get(js_url).text)
    image_url_1 = 'http://www.bing.com' + js_data['images'][0]['url']
    image_url_2 = 'http://www.bing.com/hpwp/' + js_data['images'][0]['hsh']

    image_name = js_data['images'][0]['enddate']

    if os.path.exists("./image_1/" + image_name+".jpg") == False:
        urllib.request.urlretrieve(
            image_url_1, filename="./image_1/" + image_name+".jpg")
    else:
        print("./image_1/" + image_name+".jpg"+" Already exist.")

    if os.path.exists("./image_2/" + image_name+".jpg") == False:
        urllib.request.urlretrieve(
            image_url_2, filename="./image_2/" + image_name+".jpg")
    else:
        print("./image_2/" + image_name+".jpg"+" Already exist.")
except:
    print("error!")
