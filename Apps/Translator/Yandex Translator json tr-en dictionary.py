import requests

# time modulu ekle
# ingilizce kelimeler ekle -> https://dictionary.yandex.net/api/v1/dicservice.json/lookup?key=dict.1.1.20210105T190252Z.1bf16a1a72629b11.f723d8b4f7f900313a0bcb5af8faab64c3fb2e46&lang=en-tr&text=run
# baslangicta hangi ceviri yapmak istedigini sorsun sonra o sekilde devam etsin
# Aranan kelimeler ve cevaplar bir database e kaydedilsin
# Bu program icin bir arayuz tasarla
# Gecmis sorgular - kayitlar buraya gelsin
#ingilizce turkce veya turkce ingilizce (veya ingilizce ingilizce) arama yapilabilir
while True:
    print("-" * 50)
    aranan_kelime = input("\nAranan kelimeyi giriniz: ")
    url = ("https://dictionary.yandex.net/api/v1/dicservice.json/lookup?key=dict.1.1.20210105T190252Z.1bf16a1a72629b11.f723d8b4f7f900313a0bcb5af8faab64c3fb2e46&lang=tr-en&text=" + aranan_kelime)

    r = requests.get(url)

    data = r.json()

    tr_eng_ilk_anlam = data["def"][0]["tr"][0]["text"] 

    synonims = data["def"][0]["tr"][0]["syn"] 

    print("Kelimenin ilk ve en cok kullanilan karsiligi:\n")
    print(tr_eng_ilk_anlam)
    print("\nKelimenin diger esanlamlilari:\n")
    for i in synonims:
        print(i["text"])
