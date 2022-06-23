from pyuseragents import random as random_useragent
from requests import Session

print("Софт от лучшего канала - https://t.me/cryptoblinchik")
print("Почты должны быть в виде: email или email:password")
file = input("Введите названия файла с почтами (файл должен находиться в папке с файлом скрипта): ")
with open(file) as f:
    for i in f.readlines():
        email = i.split(":")[0]
        session = Session()
        session.headers.update({'user-agent': random_useragent(),
                                'accept': '*/*',
                                'accept-language': 'ru,en;q=0.9',
                                'content-type': 'application/json',
                                'origin': 'https://nft.bentleymotors.com',
                                'referer': 'https://nft.bentleymotors.com/?utm_source=BMwebsite'
                                })
        r = session.post("https://nft.bentleymotors.com/api/signup",
                         json={"email": email})
        if r.ok:
            print(email, "on the waitlist")