import requests
from bs4 import BeautifulSoup
import re
import time
import random
import csv





def wait_xs():
  sec = random.uniform(0.1, 0.5)
  time.sleep(sec)

def mirror_search(gutugutu):
  # トップページからリンクをクロールして、そこのHTMLをパースしたやつを返してくれるぺこ
  res_mirror = requests.get('http://www.xssed.com' + gutugutu)
  soup_mirror = BeautifulSoup(res_mirror.text, 'html.parser')
  no_tag_soup_mirror = soup_mirror.text
  # print(type(no_tag_soup_mirror))
  # gutugutu_soup_mirror = no_tag_soup_mirror
  # gutugutu_soup_mirror = soup_mirror.select('tr > .row3')
  gutugutu_soup_mirror = soup_mirror.find_all('th', {'colspan': '4'})
  return gutugutu_soup_mirror[1]#ここをずらすとその頁の別の要素が取得できるぺこ
  # print(type(gutugutu_soup_mirror))
  #for gutugutu_ingredient in gutugutu_soup_mirror:
  #  print(gutugutu_ingredient)

def extract_url(before_cutting):
  s = before_cutting
  p = r'URL: (.*)'  # 「URL: 」の後ろにある時間だけを抽出するぺこ
  m = re.search(p, s)
  return m.group(1)

def input_csv(ans):
  with open('/content/drive/MyDrive/Colab Notebooks/pekopeko_datasets/新抗/XSSed.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerows(ans)
    


def main():
  ans_list = []
  ans_list_box = []
  k=int(input("(ここに入力した数-1)×30のデータが手に入るよ！"))
  
  for i in range(636,k):#ここを調整すると、何ページマックスか選べるぺこ！30個データセットもらえるぺこ！
  # 601-635(テストデータ)
  # 709でおわりかな
    load_url = "http://www.xssed.com/archive/page={0}/".format(i)
    html = requests.get(load_url)
    soup = BeautifulSoup(html.content, "html.parser")

    elems = soup.select('a')
    for elem in elems:
      elem_href = elem.get('href')
      if 'mirror' in elem_href:
        mirror_href = elem_href
        tagged_ans = str(mirror_search(mirror_href))
        ans = ''.join(list(extract_url(tagged_ans)))
        ans_list_box.append(ans)
        ans_list.append(ans_list_box)
        ans_list_box = []
                        
      wait_xs()
    print("------------------------------------------------------------")
    print(ans_list[-1])
    input_csv(ans_list)




main()





