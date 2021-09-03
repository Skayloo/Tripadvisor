import requests
import time
import math

from bs4 import BeautifulSoup


cookies = {
}

headers = {
}


def find_hrefs(page):
    try:
        Name_hrefs = BeautifulSoup(page.text, 'html.parser')
        Name = Name_hrefs.find_all(class_="_15_ydu6b", href = True)
        for call in Name:
            if call.get_text().__contains__("."):
                find_pages(call)
                
    except:
        a = 1
        while a == 1:
            find_pages(call)

def find_pages(call):
    page_to_find_info = requests.get("https://www.tripadvisor.ru" + call['href'], headers=headers, cookies=cookies)
    find_name(page_to_find_info)
    find_adress(page_to_find_info)
    find_tel(page_to_find_info)
    find_bill_cuisine(page_to_find_info)
    find_rating(page_to_find_info)



def find_bill_cuisine(page):
    # Bill = BeautifulSoup(page.text, 'html.parser')
    # if Bill.find(class_="_14zKtJkz Wf b C0 S2 H2").get_text() == "ДИАПАЗОН ЦЕН":
    #     Bill_rest = Bill.find(class_="_1XLfiSsv Pd PN Pt PA S4 H3").get_text()
    #     if Bill.find(class_="_14zKtJkz Wf b C0 S2 H2").next.get_text() == "ТИП КУХНИ":
    #         Cuisine_rest = Bill.find(class_="_1XLfiSsv Pd PN Pt PA S4 H3").next.get_text()
    #     else:
    #         print("Cuisine is null")
    #     print(Bill_rest, "\n", Cuisine_rest)
    # else:
    #     print("Bill is null")
    #     if Bill.find(class_="_14zKtJkz Wf b C0 S2 H2").get_text() == "ТИП КУХНИ":
    #         Cuisine_rest = Bill.find(class_="_1XLfiSsv Pd PN Pt PA S4 H3").get_text()
    #         print(Cuisine_rest)
    #     else:
    #         print("Cuisine is null")
    try:
        pathfinder = BeautifulSoup(page.text, 'html.parser')
        All_info_from_block = BeautifulSoup(page.text, 'html.parser')
        All_info = pathfinder.find_all(class_="_14zKtJkz")
        if All_info[0].get_text() == "ДИАПАЗОН ЦЕН":
            info = All_info_from_block.find_all(class_="_1XLfiSsv")
            with open ('Tokyo.txt', '+a', encoding='cp1251') as f:
                f.write(info[0].get_text() + ";" + info[1].get_text() + ";")
        else:
            info = All_info_from_block.find_all(class_="_1XLfiSsv")
            with open ('Tokyo.txt', '+a', encoding='cp1251') as f:
                f.write("Bill is null" + ";" + info[0].get_text() + ";")
    except:
        with open ('Tokyo.txt', '+a', encoding='cp1251') as f:
                f.write("Bill is null" + ";" + "Cuisine is null" + ";")
    # for l in All_info:
    #     print(l.get_text())

def find_name(page):
    try:
        Name_restaurant = BeautifulSoup(page.text, 'html.parser')
        name = Name_restaurant.find(class_ = "_3a1XQ88S")
        with open ('Tokyo.txt', '+a', encoding='cp1251') as f:
                f.write(name.get_text() + ";")
    except:
        with open ('Tokyo.txt', '+a', encoding='cp1251') as f:
                f.write("Name is null" + ";")

def find_adress(page):
    try:
        Adress = BeautifulSoup(page.text, 'html.parser')
        Adress_rest = Adress.find(class_="_2wKz--mA _27M8V6YV").get_text()
        with open ('Tokyo.txt', '+a', encoding='cp1251') as f:
                f.write(Adress_rest + ";")
    except:
        with open ('Tokyo.txt', '+a', encoding='cp1251') as f:
                f.write("Adress is null" + ";")

def find_tel(page):
    try:
        Tel = BeautifulSoup(page.text, 'html.parser')
        Tel_rest = Tel.find_all(class_="_105c0u5l")
        with open ('Tokyo.txt', '+a', encoding='cp1251') as f:
                f.write(Tel_rest[1].get_text() + ";")
    except:
        with open ('Tokyo.txt', '+a', encoding='cp1251') as f:
                f.write("Telephone is null" + ";")

def find_rating(page):
    try:
        rate = BeautifulSoup(page.text, 'html.parser')
        rate_rest = rate.find(class_="r2Cf69qf").get_text()
        with open ('Tokyo.txt', '+a', encoding='cp1251') as f:
                f.write(rate_rest + '\n')
    except:
        with open ('Tokyo.txt', '+a', encoding='cp1251') as f:
                f.write("Rating is null" + '\n')

# def find_bill(page):
#     try:
#         Bill = BeautifulSoup(page.text, 'html.parser')
#         if Bill.find(class_="_14zKtJkz Wf b C0 S2 H2").get_text() == "ДИАПАЗОН ЦЕН":
#             Bill_rest = Bill.find(class_="_1XLfiSsv Pd PN Pt PA S4 H3").get_text()
#             print(Bill_rest)
#         else:
#             print("Bill is null")
#     except:
#         print("Bill is null")

def main():
    try:
        # start_page = requests.get('https://www.tripadvisor.ru/Restaurants-g294229-Jakarta_Java.html', headers=headers, cookies=cookies)
        # max = BeautifulSoup(start_page.text, 'html.parser')
        # max_count = max.find(class_="_1D_QUaKi b")
        max_count = 101578
        max_count = float(max_count) // 30
        max_count = round(max_count) + 1
        count = 0
        for i in range(0,max_count):
            if i == 1:
                page = requests.get('https://www.tripadvisor.ru/Restaurants-g298184-Tokyo_Tokyo_Prefecture_Kanto.html', headers=headers, cookies=cookies)
                count = count + 30
                find_hrefs(page)
                print(count)
            else:
                page = requests.get("https://www.tripadvisor.ru/Restaurants-g298184-oa"+ str(count) +"-Tokyo_Tokyo_Prefecture_Kanto.html", headers=headers, cookies=cookies)
                page.encoding = 'utf-8'
                #if page.status_code == "200":
                find_hrefs(page)
                count = count + 30
    except:
        print("Cannot access change cookies")

if __name__ == "__main__":
    main()
