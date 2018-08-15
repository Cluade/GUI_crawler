import selenium
import re
from selenium import webdriver

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pyquery import PyQuery as pq
import time
import pandas as pd

chromedriver = "/Users/duanyiqun/anaconda3/envs/crawler/chromedriver"
browser = webdriver.Chrome(chromedriver)
frame = {
            'image': 0,
            'price': 0,
            'deal': 0,
            'title': 0,
            'shop': 0,
            'location': 0
        }
frame = pd.DataFrame(frame, index = [0])

def search():
    try:
        browser.get('https://www.taobao.com')
        wait = WebDriverWait(browser, 10)
        location = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="J_SiteNavBdL"]/li[1]')))
        location.click()
        select_mad = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="J_SiteNavRegionList"]/li[2]')))
        select_mad.click()
        input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#q')))
        input.send_keys('美食')
        submit = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#J_TSearchForm > div.search-button > button')))
        submit.click()
        total_p = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="mainsrp-pager"]/div/div/div/div[1]')))
        return total_p.text

    except TimeoutException:
        return search()

def next_page(page_number):
    try:
        wait = WebDriverWait(browser, 10)
        input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#mainsrp-pager > div > div > div > div.form > input')))
        input.clear()
        input.send_keys(page_number)
        submit = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#mainsrp-pager > div > div > div > div.form > span.btn.J_Submit')))
        submit.click()
        wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,'#mainsrp-pager > div > div > div > ul > li.item.active > span'),str(page_number)))
        get_product()
    except TimeoutException:
        next_page(page_number)

#pro_ls=['image','price','deal-cnt','title','shop','location']
#df_prod=pd.DataFrame([0,0,0,0,0,0], columns= ['image','price','deal-cnt','title','shop','location'])

def get_product():
    global frame
    wait = WebDriverWait(browser, 10)
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#mainsrp-itemlist .items .item')))
    html = browser.page_source
    doc = pq(html)
    items = doc('#mainsrp-itemlist .items .item').items()
    for item in items:
        
        product={
            'image': item.find('.pic .img').attr('src'),
            'price': item.find('.price').text()[2:],
            'deal': item.find('.deal-cnt').text()[:-3],
            'title': item.find('.title').text(),
            'shop': item.find('.shop').text(),
            'location': item.find('.location').text()
        }
        #product= [item.find('.pic .img').attr('src'),item.find('.price').text(),item.find('.deal-cnt').text()[:-3],item.find('.title').text(),item.find('.shop').text(),item.find('.location').text()]
        frame=pd.concat([frame,pd.DataFrame(product,index = [0])])
        #df_prod = pd.concat(df_prod,df)

        print(product)
    frame.to_csv('taobao_meishi.csv', encoding="utf_8_sig")

def main():
    total = search()
    total = int(re.compile('(\d+)').search(total).group(1))
    print(total)
    for i in range(2, total+1):
        next_page(i)

if __name__ == '__main__':
    main()
    
