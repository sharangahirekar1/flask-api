from urllib.request import urlopen
from bs4 import BeautifulSoup
import cv2
from PIL import Image
import numpy as np
import io
from datetime import date

def scrape_news():
    news_data = []

    def scrape(url="https://timesofindia.indiatimes.com/",keyword="tech",img=False,branch_scrape=True):
        
        page = urlopen(url)

        html = page.read().decode("utf-8")
        soup = BeautifulSoup(html,'html.parser')
    #     print(soup.get_text())
        divs_for_text = soup.find_all("figure")
        for i in range(0, len(divs_for_text)):
            try:
                element = divs_for_text[i]
                link = element.find_all("a")[0]["href"]
                text = element.get_text()
    #             print(link.find(keyword), "---- link find keyword", link)
                if link.find(keyword) != -1:
                    print(element.get_text(), link, "\n\n")
                    data = f"{element.get_text()}  {link} \n\n"
                    news_data.append(data)
            except Exception as exp:
                print(exp,"eexpcetion")
                continue
        if branch_scrape:
            all_hyperlinks = soup.find_all("a")
    #         print(len(all_hyperlinks), 'length of hyperlinks')
            for i in range(0,len(all_hyperlinks)):
                try:
                    sub_url = all_hyperlinks[i]["href"]
                    print(sub_url, "sub url :")
                    if "unknown url" not in sub_url:
                        scrape(sub_url,keyword,img=False,branch_scrape=False)
                except Exception as exp:
                    print(exp)
                    continue
        if img:
            all_img = soup.find_all("img")
    #         print(len(all_img))
    #         print(all_img[0])
            for i in range(0,len(all_img)): 
                try:
                    imgUrl = all_img[i]["src"]
    #                 print(imgUrl, 'before image url')
                    if imgUrl[0] == "/":
                        imgUrl = url + imgUrl
    #                 print(imgUrl,' image url <-')
                    img = urlopen(imgUrl).read()
                    img
                    image = Image.open(io.BytesIO(img))

                    if image.mode != "RGB":
                        image = image.convert("RGB")

                    img_rgb = np.array(image)
                    r = img_rgb[:,:,0]
                    img_rgb[:,:,0] =img_rgb[:,:,2]
                    img_rgb[:,:,2] = r
                except Exception as excp:
                    continue
                # img_rgb.shape
                # soup.get_text()
                cv2.imshow("window",img_rgb)
                k = cv2.waitKey(1000) & 0xFF
                if k == 27 or k == ord("q"):
                    cv2.destroyAllWindows()
                    break
    
    scrape()
    return news_data
                
                
