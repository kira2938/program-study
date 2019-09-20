import os, csv, time, datetime
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import CreateForm
from .models import AreaData
from django.utils import timezone
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np


def index(request):
    station = AreaData.objects.all()
    run = {
            'title': 'エリアを選択してください',
            'data': station,
        }    
    return render(request, 'tblog/index.html', run)

#create
def create(request):
    run = {
        'title': 'エリア追加',
        'form': CreateForm(),        
    }
    if (request.method == 'POST'):
        obj = AreaData()
        area = CreateForm(request.POST, instance = obj)
        area.save()
        return redirect(to = '/tblog')
    return render(request, 'tblog/create.html', run)


#search
def search(request):
    run = {
        'title': '検索中',
        'message': 'しばらくお待ちください。'
    }
    return render(request, 'tblog/search.html', run)

#edit
def edit(request, num):
    obj = AreaData.objects.get(id=num)
    if request.method == 'POST':
        area = CreateForm(request.POST, instance = obj)
        area.save()
        return redirect(to = '/tblog')
    run = {
            'title': 'エリア編集',
            'id': num,
            'form': CreateForm(instance = obj),
    }
    return render(request, 'tblog/edit.html', run)

#delete
def delete(request, num):
    del_area = AreaData.objects.get(id=num)
    if request.method =='POST':
        del_area.delete()
        return redirect(to='/tblog')
    run = {
            'title': 'エリア削除',
            'id': num,
            'obj': del_area,
    }
    return render(request, 'tblog/delete.html', run)

#detail
def detail(request, num):
    select_area = AreaData.objects.get(id=num)
    if request.method == 'POST':
        # ブラウザを立ち上がらないように設定
        browser_path = r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
        chromedriver_path = r'C:\Users\study\Desktop\chromedriver_win32\chromedriver.exe' 
        options = Options()
        options.binary_location = browser_path # chromeのパスを指定
        options.add_argument('--headless') # ヘッドレスモードを有効にする（コメントアウトするとブラウザ表示）
        driver = webdriver.Chrome(chrome_options = options, executable_path=chromedriver_path) # webdriverのパス指定
            
        # サーバーに負担をかけないように待機 implicitly_wait(秒)
        driver.implicitly_wait(5)
        
        # UserSide("食べログURL", "検索するエリア", "検索するキーワード", "csvのファイル名(エリアを英語で)") 
        # 編集するところはエリアとキーワード、csvファイル名
        
        
        url = "https://tabelog.com/"
        area1 = select_area.area_list
        area2 = '//*[@id="rstsearch_form"]/div/div[5]/div/ul/li[' + str(select_area.list_id) + ']'
        search = "js-global-search-btn"
        #next_page = "c-pagination__arrow--next"
        
        #tabe_input = UserSide("https://tabelog.com/", area1, area2)
        
        # 編集するところは "ui-id-6", "ui-id-14"
        # エリア、キーワードを入力するとリストが表示され、そのリストから検索したいエリア（キーワード）を選択する
        # エリアのリストは"ui-id-3"が一番上にくる
        # キーワードのリストは"ui-id-13"が一番上にくる
        
        
        # ブラウザでページを開く
        driver.get(url)
        
        
        #############################地域#############################
        # 検索地域入力欄に指定したキーワード入力
        elem = driver.find_element_by_id('sa')
        elem.clear()
        elem.send_keys(area1)
        
        # ドロップダウンリストから選んで選択
        elem = driver.find_element_by_xpath(area2)
        elem.click()
        ##############################################################
        
        ########################キーワード#############################
        # 検索地域入力欄に指定したキーワード入力
        #elem = driver.find_element_by_id(tabe_html.key_input_select())
        #elem.clear()
        #elem.send_keys(tabe_input.search_keyword())
        
        # ドロップダウンリストから選んで選択
        #elem = driver.find_element_by_id(tabe_html.key_id_select())
        #elem.click()
        ##############################################################
        
        # 検索ボタンをクリック
        elem = driver.find_element_by_id(search)
        elem.click()
        
        page = 1
        now = datetime.datetime.now()
        #ファイルの存在をチェック
        #ファイルがない場合(False)スクレイピングしてファイル作成&保存
        if(os.path.isfile(os.path.expanduser('~') + r'\desktop\tabelog_' + select_area.list_jpen + '_{0:%Y%m%d}.csv'.format(now)) == False):
        
            with open(os.path.expanduser('~') + r'\desktop\tabelog_' + select_area.list_jpen + '_{0:%Y%m%d}.csv'.format(now), 'w', encoding='utf_8_sig') as f:
                header =['id', '店舗名', 'エリア/ジャンル', '店舗URL', '評価点', '口コミ数']
                writer = csv.writer(f, lineterminator='\n')
                writer.writerow(header)
                
                while True:
                    if len(driver.find_elements_by_class_name('c-pagination__arrow--next')) > 0:
                        print("##############################page: {} ##############################".format(page))
                        driver.implicitly_wait(10)
                        page_source = driver.page_source
                        bs = BeautifulSoup(page_source, 'html.parser')
            
                        shop_id = []
                        shop_name = []
                        area_genre = []
                        shop_url = [] 
                        shop_rate = [] 
                        shop_review_cnt = []
                        data_list = [
                            shop_id , shop_name, area_genre, shop_url, shop_rate, shop_review_cnt
                        ]
                        osaki_shop_list = bs.find_all('li', class_='js-rst-cassette-wrap')
                        for lists in osaki_shop_list:
                            data_id = lists.get('data-rst-id')
                            shop_id.append(data_id)
            
                            shop_names = lists.find('a', class_='cpy-rst-name')
                            shop_name.append(shop_names.text)
            
                            area_genres = lists.find('span', class_='list-rst__area-genre')
                            area_genre.append(area_genres.text)
            
                            shop_urls = lists.find('a', class_='list-rst__rst-name-target')
                            href = shop_urls.get('href')
                            shop_url.append(href)
            
                            shop_rates = lists.find('span', class_='list-rst__rating-val')
                            if shop_rates is None:
                                shop_rate.append('-')
                            else:
                                shop_rate.append(shop_rates.text)
            
                            review_count = lists.find('a', class_='list-rst__rvw-count-target')
                            if review_count is None:
                                shop_review_cnt.append('-')
                            else:
                                shop_review_cnt.append(review_count.text)            
            
                        tabelog_done = pd.DataFrame(data_list)
                        #df = df.append(tabelog_done, ignore_index=True)
            
                        print(tabelog_done)
            
                        nextpage = driver.find_element_by_class_name('c-pagination__arrow--next').get_attribute("href")
                        driver.get(nextpage)
                        page += 1
                        driver.implicitly_wait(10)
                        time.sleep(5)
                    else:
                        print('##################################################Last page##################################################')
                        page_source = driver.page_source
                        bs = BeautifulSoup(page_source, 'html.parser')
            
                        shop_id = []
                        shop_name = []
                        area_genre = [] 
                        shop_url = [] 
                        shop_rate = [] 
                        shop_review_cnt = []
                        data_list = [
                            shop_id , shop_name, area_genre, shop_url, shop_rate, shop_review_cnt
                        ]
                        osaki_shop_list = bs.find_all('li', class_='js-rst-cassette-wrap')
                        for lists in osaki_shop_list:
                            data_id = lists.get('data-rst-id')
                            shop_id.append(data_id)
            
                            shop_names = lists.find('a', class_='cpy-rst-name')
                            shop_name.append(shop_names.text)
            
                            area_genres = lists.find('span', class_='list-rst__area-genre')
                            area_genre.append(area_genres.text)
            
                            shop_urls = lists.find('a', class_='list-rst__rst-name-target')
                            href = shop_urls.get('href')
                            shop_url.append(href)
            
                            shop_rates = lists.find('span', class_='list-rst__rating-val')
                            if shop_rates is None:
                                shop_rate.append('-')
                            else:
                                shop_rate.append(shop_rates.text)
            
                            review_count = lists.find('a', class_='list-rst__rvw-count-target')
                            if review_count is None:
                                shop_review_cnt.append('-')
                            else:
                                shop_review_cnt.append(review_count.text)
            
                        tabelog_done = pd.DataFrame(data_list)
                        #df = df.append(tabelog_done, ignore_index=True)
            
                        print(tabelog_done)
                        break
                        
                    data_list_n = np.array(tabelog_done)        
                    writer.writerows(data_list_n.T)
                        
                data_list_n = np.array(tabelog_done)        
                writer.writerows(data_list_n.T)
            
        else:
            print('ファイルが存在します')
            pass
        
        print("DONE")
    
    if __name__ == '__main__':
        select_area.detail()
        
        
    
    #ファイルがある場合(True)、プリントする
    
    time.sleep(5)
    run = {
            'id': num,
            'form': select_area,
            }
    return render(request, 'tblog/detail.html', run)
 
    
