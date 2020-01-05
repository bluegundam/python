import requests
from bs4 import BeautifulSoup

from common_mail import send_mail as sm



#URL = "https://whatismyipaddress.com/"
URL = "https://www.whatismyip.com/"
agent = {"User-Agent":"Mozilla/5.0"}

result = requests.get(URL, headers=agent)
soup = BeautifulSoup(result.text, 'html.parser')

print(soup)

# result_file = open('ipcheck/aa1.html', mode='rt', encoding='utf-8')
# soup = BeautifulSoup(result_file, 'html.parser')
# result_file.close()

card_body = soup.find("div", {"class" : "card-body"}).find_all("li", {"class" : "list-group-item"})

public_ip = ""

print("-----------------------")
# print(card_body)
for item in card_body:
    print(item.string)

    search = "My Public IPv4 is: "
    if item.string is not None :
        if search in item.string :
            print("Hear !!!")
            public_ip = item.string[len(search):]
        else : 
            print("None")
    else :
        print("String is null")

    print("")
print("-----------------------")

print(f"Public IP : {public_ip}")



# 확인된 public ip 메일 발송

addr = 'backfire000@naver.com'
subj_layout = 'Public IP share 2'
cont_layout = f"Public IP : {public_ip}"

# try:
#     sm(addr, subj_layout, cont_layout)
# except Exception as ex:
#     print('에러발생', ex)

