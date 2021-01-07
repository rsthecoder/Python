import requests

# time modulu ekle
# ingilizce kelimeler ekle -> https://dictionary.yandex.net/api/v1/dicservice.json/lookup?key=dict.1.1.20210105T190252Z.1bf16a1a72629b11.f723d8b4f7f900313a0bcb5af8faab64c3fb2e46&lang=en-tr&text=run
# baslangicta hangi ceviri yapmak istedigini sorsun sonra o sekilde devam etsin
# Aranan kelimeler ve cevaplar bir database e kaydedilsin
# Bu program icin bir arayuz tasarla
# Gecmis sorgular - kayitlar buraya gelsin
#ingilizce turkce veya turkce ingilizce (veya ingilizce ingilizce) arama yapilabilir


while True:
    try:
        print("-" * 50)
        ceviri_num = int(input("""
        Turkce-Ingilizce ceviri icin 1'e basip Enter a basiniz.
        Ingilizce-Turkce ceviri icin 2'ye basip Enter a basiniz.
        """))

        if ceviri_num == 1:
            aranan_kelime = input("\nTurkce-Ingilizce ceviri icin Aranan kelimeyi giriniz: ")
            url = ("https://dictionary.yandex.net/api/v1/dicservice.json/lookup?key=dict.1.1.20210105T190252Z.1bf16a1a72629b11.f723d8b4f7f900313a0bcb5af8faab64c3fb2e46&lang=tr-en&text=" + aranan_kelime)
            r = requests.get(url)
            data = r.json()
            tr_eng_ilk_anlam = data["def"][0]["tr"][0]["text"]
            synonims = data["def"][0]["tr"][0]["syn"]
            print("Kelimenin ilk ve en cok kullanilan karsiligi:\n")
            print(tr_eng_ilk_anlam)
            print("\nKelimenin esanlamlilari ve kullanilislari:\n")
            for i in synonims:
                print(i["text"])
        else:
            aranan_kelime = input("\nIngilizce-Turkce ceviri icin Aranan kelimeyi giriniz: ")
            url = ("https://dictionary.yandex.net/api/v1/dicservice.json/lookup?key=dict.1.1.20210105T190252Z.1bf16a1a72629b11.f723d8b4f7f900313a0bcb5af8faab64c3fb2e46&lang=en-tr&text=" + aranan_kelime)
            r = requests.get(url)
            data = r.json()
            eng_tr_ilk_anlam = data["def"][0]["tr"][0]["text"]
            eng_tr_synonims = data["def"][0]["tr"][0]["syn"]
            print("Kelimenin ilk ve en cok kullanilan karsiligi:\n")
            print(eng_tr_ilk_anlam)
            print("\nKelimenin esanlamlilari ve kullanilislari:\n")
            for i in eng_tr_synonims:
                print(i["text"])

    except:
        print("\nAranan kelime bulunamadi lutfen baska bir kelime giriniz!")
