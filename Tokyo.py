import requests
import time
import math

from bs4 import BeautifulSoup


cookies = {
    'TADCID': 'A5IY8zPYUe3FC3lCABQCFdpBzzOuRA-9xvCxaMyI12fnA8PULjODmVx_wJj2B4HlL9WN9mPi-DtxwPJ-6T4DpIXArijFD1P0pPA',
    'TAUnique': '%1%enc%3ACMMOKLDtJ3uT9JiXQNFfymuqYyJlxtntn907NIsEsrgWyJIZOKp%2Fdg%3D%3D',
    'TASSK': 'enc%3AAFj%2BbV3V1JMCtGYkEPmiBSvy%2FLrTwSiSqz6Fo6DPHBlyZ60deAW6PQxQNCRLcpnOSP1Rr3KW%2BFtL1Bij8D893Me72ykUEsAnKXMEL1JZ3U2dwGJLliOMgbuy0k%2FlV60aRw%3D%3D',
    'PAC': 'ADlq7RVATVmz2EQFmHPhH55ZhlbGPKh7vHkYYXTAcF6vZywF29ef_T_6ZFcBrWa-VkD2KFyvx9IsxQfolcFztZ5cu7oZPTdb0ExmmCO1wQXm5MJvWPo58Hk2Ax6ZHo0AOIATitRzLJnrqU8Mb5IjIMPN8cttStDdoBMOzsXalHGzsLgPfjibYPAL3lzd8eibjw%3D%3D',
    'VRMCID': '%1%V1*id.14384*llp.%2F*e.1626554696390',
    'PMC': 'V2*MS.80*MD.20210710*LD.20210902',
    'TATrkConsent': 'eyJvdXQiOiIiLCJpbiI6IkFMTCJ9',
    '_ym_uid': '1625949904263931600',
    '_ym_d': '1625949904',
    '_lc2_fpi': 'f4e7d8ca3f73--01fa92n7jgpysxhszxk2qer9gn',
    '__gads': 'ID=a438d3211cd4bde1:T=1625949906:S=ALNI_MbXK6iV1WccIMQW1HH79nsN224JoA',
    'TART': '%1%enc%3Ak%2FSYl0DRX8qVg8koWKk8LOWwkFmdb8KlgixFkzQXENJla8j7iowSb9Jt%2BBQrhBMdOnZh7DXbNV0%3D',
    'TATravelInfo': 'V2*AY.2021*AM.9*AD.12*DY.2021*DM.9*DD.13*A.2*MG.-1*HP.2*FL.3*DSM.1630580452231*RS.1*RY.2021*RM.9*RD.2*RH.20*RG.2',
    'TAUD': 'LA-1630574761942-1*RDD-1-2021_09_02*ARDD-5691611-2021_09_12.2021_09_13*RD-16418523-2021_09_02.4316033*LD-21434737-2021.9.12.2021.9.13*LG-21434739-2.1.F.',
    'TAAUTHEAT': 'zyNUfP8a24Gdf5vRABQCab7fMZ8ORguCqJF_E5GxfSe-A5NA18aOOXGaYqcHfxcaw2gufNDmSu7uOKodwT3DzmJW1nSGRN5x_Fk5aB4pKDBWyZVMvD2hsszZP7FirlyRo2fSkrvCCR3Js2-2nrTdLJ0dUXmeqsePpZYkenaPLTf4ILa1piSVkmmDqzGHP0XvlgWrhhlL8_lbz0LlUXyE08g04dsSAE_NyW4',
    '_pbjs_userid_consent_data': '3524755945110770',
    'pbjs_pubcommonID': '7fc10c7a-0971-4abc-9ba2-029d03607a22',
    '_ym_isad': '2',
    'pbjs_li_nonid': '%7B%7D',
    'TASession': 'V2ID.7682DE49FA54483787C23F8149E415AB*SQ.15*LS.Restaurants*GR.20*TCPAR.34*TBR.38*EXEX.88*ABTR.5*PHTB.58*FS.84*CPU.13*HS.recommended*ES.popularity*DS.5*SAS.popularity*FPS.oldFirst*TS.BBD0F51D5A43BB44059EDFF76534C5FF*LF.ru*FA.1*DF.0*RT.0*TRA.true*LD.294229*EAU.8',
    'ServerPool': 'C',
    'TAReturnTo': '%1%%2FRestaurants-g294229-oa30-Jakarta_Java.html',
    '__vt': 'tFFJK-l-5pHRjecvABQCIf6-ytF7QiW7ovfhqc-AvRfGCETeVl-0Az8KhX7gtIxjurnQsJuR--lnTMU9mDTePB278K81GjqiU2Xad3sUOmTVrvtBXkmaj-pvz0Wf_sKeIv-9tQVc-ObZ6NbWl8DmR959LLXnJSbsQPiTd-DFSu1U8s79i1uWhJ4ybySP6GEel0D0jmNkcE_9kBSUfMXicDFkNp4DBq5xhfpguGyRVnbPx6W2ClD507sQDjE3rRQaRw',
    'ak_bmsc': 'ED951E21835C3034FEAF0155BC61D32C~000000000000000000000000000000~YAAQDotIF4biDKZ7AQAAqWfNpgy/xeWs9njvrDwH+C43vMaU2roPNgHKbxjhZ1bZkGACnDww3Ai4NQiIEMmX7uXah6Hty3kZLJKFM3M+bA29ZWYBVT4ggRbdjjfWdbNpaeLty9gTzgWWupUAGqHXOXyXBkA5Um/BHvwcb8vGTjM9boCYJ3mjpHqw7I8vu8iErvir9LTPqlezyZkK/7mtgKhAcJXET99Ea2iSwaVjZs/E4eN5cG82Ikc4zF6SZb+4at3dKmSLit2v4D5n2L+T3lkhY2nPKzWGhUnPUsTJSxdTxNdFVloG8V30vn2kbh7Ml0D/00mcsHDjhq0MrSMqCrvmmzq+S2Av7agOY0+7w8QjN44rZNkLUzG3JgJphFTlQ4OhKBDEmDcpqo1Q1KU=',
    'bm_sv': 'A289D76399CFBC12CA9B5400D0B793E6~/U7pDDjDRaPLJLuWjqlu26smI5OipBYTa2DrTnXq7nC0xsZPLA67ymOcLcEILZbX0mQaUtG92enBQYHpTR7WZBpY8eJUlM0W900mBXONKBsK/y8WyAZX+0m9HzDa4C+Q3YdaVKattP5Uc8tflBh+v6txDTg9qRMX+/L8/wnqGgg=',
    '_li_dcdm_c': '.tripadvisor.ru',
    'CM': '%1%PremiumMobSess%2C%2C-1%7Ct4b-pc%2C%2C-1%7CRestAds%2FRPers%2C%2C-1%7CRCPers%2C%2C-1%7CWShadeSeen%2C%2C-1%7CTheForkMCCPers%2C%2C-1%7CHomeASess%2C%2C-1%7CPremiumMCSess%2C%2C-1%7CSLMCSess%2C%2C-1%7CCrisisSess%2C%2C-1%7CUVOwnersSess%2C%2C-1%7CRestPremRSess%2C%2C-1%7CRepTarMCSess%2C%2C-1%7CCCSess%2C%2C-1%7CCYLSess%2C%2C-1%7CPremRetPers%2C%2C-1%7CViatorMCPers%2C%2C-1%7Csesssticker%2C%2C-1%7CPremiumORSess%2C%2C-1%7Ct4b-sc%2C%2C-1%7CRestAdsPers%2C%2C-1%7CMC_IB_UPSELL_IB_LOGOS2%2C%2C-1%7CTSMCPers%2C%2C-1%7Cb2bmcpers%2C%2C-1%7CPremMCBtmSess%2C%2C-1%7CMC_IB_UPSELL_IB_LOGOS%2C%2C-1%7CLaFourchette+Banners%2C%2C-1%7Csess_rev%2C%2C-1%7Csessamex%2C%2C-1%7CPremiumRRSess%2C%2C-1%7CTADORSess%2C%2C-1%7CAdsRetPers%2C%2C-1%7CCOVIDMCSess%2C%2C-1%7CListMCSess%2C%2C-1%7CTARSWBPers%2C%2C-1%7CSPMCSess%2C%2C-1%7CTheForkORSess%2C%2C-1%7CTheForkRRSess%2C%2C-1%7Cpers_rev%2C%2C-1%7CSPACMCSess%2C%2C-1%7CRBAPers%2C%2C-1%7CRestAds%2FRSess%2C%2C-1%7CHomeAPers%2C%2C-1%7CPremiumMobPers%2C%2C-1%7CRCSess%2C%2C-1%7CLaFourchette+MC+Banners%2C%2C-1%7CRestAdsCCSess%2C%2C-1%7CRestPremRPers%2C%2C-1%7CSLMCPers%2C%2C-1%7CRevHubRMPers%2C%2C-1%7CUVOwnersPers%2C%2C-1%7Csh%2C%2C-1%7Cpssamex%2C%2C-1%7CTheForkMCCSess%2C%2C-1%7CCrisisPers%2C%2C-1%7CCYLPers%2C%2C-1%7CCCPers%2C%2C-1%7CRepTarMCPers%2C%2C-1%7Cb2bmcsess%2C%2C-1%7CTSMCSess%2C%2C-1%7CSPMCPers%2C%2C-1%7CRevHubRMSess%2C%2C-1%7CPremRetSess%2C%2C-1%7CViatorMCSess%2C%2C-1%7CPremiumMCPers%2C%2C-1%7CAdsRetSess%2C%2C-1%7CPremiumRRPers%2C%2C-1%7CCOVIDMCPers%2C%2C-1%7CRestAdsCCPers%2C%2C-1%7CTADORPers%2C%2C-1%7CSPACMCPers%2C%2C-1%7CTheForkORPers%2C%2C-1%7CPremMCBtmPers%2C%2C-1%7CTheForkRRPers%2C%2C-1%7CTARSWBSess%2C%2C-1%7CPremiumORPers%2C%2C-1%7CRestAdsSess%2C%2C-1%7CRBASess%2C%2C-1%7CSPORPers%2C%2C-1%7Cperssticker%2C%2C-1%7CListMCPers%2C%2C-1%7C',
    'TASID': '7682DE49FA54483787C23F8149E415AB',
    'roybatty': 'TNI1625!AJ%2Bk8EpFNasZlVx%2BbDIxee4q%2FLHBH1Ym2XSJycam%2Bsgo%2FbO5UkEdmevivoHUz6dqRSMXz5YSL%2BR7P8RgFA0h1ISZBYWPELuSd9a0rxaN56WDaAbfditc2FKFmO3vpE%2FE3aQxKwhdZdLUApFIXrc73zypNfWwWEwOfW5IRGuO%2BbqD%2C1',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
    'Cache-Control': 'max-age=0',
    'TE': 'trailers',
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