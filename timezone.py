import warnings
from datetime import datetime
from textwrap import dedent
import re
import requests
from bs4 import BeautifulSoup

# Suppress DeprecationWarning
warnings.filterwarnings("ignore", category=DeprecationWarning)


def CurrentDateTime(current_timestamp=False,Current_Date=False,encode=False,Country='India')->str|datetime:
    
    
    headers= {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-language": "en-US,en;q=0.9",
    "content-type": "application/json",
    "cache-control": "max-age=0",
    "priority": "u=0, i",
    "sec-ch-ua": "\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Google Chrome\";v=\"126\"",
    "sec-ch-ua-arch": "\"x86\"",
    "sec-ch-ua-bitness": "\"64\"",
    "sec-ch-ua-full-version": "\"126.0.6478.127\"",
    "sec-ch-ua-full-version-list": "\"Not/A)Brand\";v=\"8.0.0.0\", \"Chromium\";v=\"126.0.6478.127\", \"Google Chrome\";v=\"126.0.6478.127\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-model": "\"\"",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-ch-ua-platform-version": "\"19.0.0\"",
    "sec-ch-ua-wow64": "?0",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "same-origin",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
    ""
  }
    html = requests.get(f"https://www.google.com/search?q=current+time+in+{Country}", headers=headers)
    if html.status_code!=200:raise Exception("Invalid Country name or error while fetching time date")
    elif html.status_code == 200:
        soup = BeautifulSoup(html.content, 'html.parser')
        with open("a.html","w",encoding="utf-8") as f:
            f.write(html.text)

        if current_timestamp and Current_Date:
            try:
                time_element = soup.select_one('.Ww4FFb.vt6azd .gsrt.vk_bk.FzvWSb.YwPhnf')
                time_obj = time_element.get_text() if time_element else None
                if encode and time_obj:
                    time_obj = time_obj.replace('\u202f', '')  # Remove Unicode character
                    try:
                        time_obj = datetime.strptime(time_obj, "%I:%M%p").time()
                    except:
                        time_obj = datetime.strptime(time_obj, "%I:%M %p").time()

                date_element = soup.select_one('.Ww4FFb.vt6azd .vk_gy.vk_sh .KfQeJ')
                date_text = date_element.get_text() if date_element else None
                if date_text:
                    current_date_obj = date_text.strip() + ' 2024'
                    if encode:
                        try:
                            current_date_obj = datetime.strptime(current_date_obj, '%d %B %Y').date()
                        except:
                            current_date_obj = None

                    return time_obj, current_date_obj
                return None, None
            except:
                return None, None
        elif current_timestamp:
            try:
                time_element = soup.select_one('.Ww4FFb.vt6azd .gsrt.vk_bk.FzvWSb.YwPhnf')
                time_obj = time_element.get_text() if time_element else None
                if encode and time_obj:
                    time_obj = time_obj.replace('\u202f', '')  # Remove Unicode character
                    try:
                        time_obj = datetime.strptime(time_obj, "%I:%M%p").time()
                    except:
                        time_obj = datetime.strptime(time_obj, "%I:%M %p").time()

                return time_obj
            except:
                return None
        elif Current_Date:
            try:
                date_element = soup.select_one('.Ww4FFb.vt6azd .vk_gy.vk_sh .KfQeJ')
                date_text = date_element.get_text() if date_element else None
                if date_text:
                    current_date_obj = date_text.strip() + ' 2024'
                    if encode:
                        try:
                            current_date_obj = datetime.strptime(current_date_obj, '%d %B %Y').date()
                        except:
                            current_date_obj = None

                    return current_date_obj
                return None
            except:
                return None

            
        
        
        
print(CurrentDateTime(current_timestamp=True,Current_Date=True,Country="India"))