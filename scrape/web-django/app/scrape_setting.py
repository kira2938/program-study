class UserSide():
    def __init__(self, search_url, select_area, csv_name):
        self.url = search_url
        self.area = select_area
        self.csv = csv_name
    
    def base_url(self): # 検索url
        return self.url
    
    def search_area(self): # 検索地域
        return self.area
    
    def search_keyword(self): # 検索キーワード
        return self.key
    
    def output_csv(self): # 選択する地域のhtmlからidを選択
        return self.csv
    
class BrowserSide():
    def __init__(self, area_input, area_class, search_btn_id, nextpage_btn_id):
        self.area_input = area_input
        self.area_class = area_class
        self.search_btn_id = search_btn_id
        self.nextpage_btn_id = nextpage_btn_id
    
    def area_input_select(self): # htmlから選択した地域のidを選択
        return self.area_input
    
    def key_input_select(self): # htmlから選択した地域のidを選択
        return self.key_input
    
    def area_class_select(self): # htmlから選択した地域のidを選択
        return self.area_class
    
    def key_id_select(self): # htmlから選択したキーワードのidを選択
        return self.keyword_id
    
    def search_id_select(self): # htmlから検索ボタンのidを選択
        return self.search_btn_id
    
    def nextpage_id_select(self): # htmlから次のページボタンのidを選択
        return self.nextpage_btn_id
