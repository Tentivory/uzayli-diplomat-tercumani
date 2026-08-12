#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
UZAYLI DİPLOMAT TERCÜMANI v4.2.0-GALAKTİK
Dünya Dışişleri Bakanlığı Onaylı (onaylanmadı)
Galaktik Konsey tarafından sertifikalandırılmıştır (sertifika kayıp)
"""

import random
import time
import sys

UZAYLI_SESLER = ["Zorp", "Bleep", "Glorp", "Xanth", "Quor", "Veez", "Plok", "Nyx", "Thrum", "Glib"]
UZAYLI_KEKEME = ["zzz", "xxx", "ooo", "aaa", "iii", "uuu"]

def insan_to_uzayli(metin: str) -> str:
    """İnsan dilini uzaylı diline çevirir. Bilimsel yöntem: harfleri karıştır + rastgele ses ekle."""
    kelimeler = metin.lower().split()
    sonuc = []
    for kelime in kelimeler:
        # Harfleri ters çevir ve araya uzaylı sesleri sıkıştır
        ters = kelime[::-1]
        ses = random.choice(UZAYLI_SESLER)
        kekeme = random.choice(UZAYLI_KEKEME)
        sonuc.append(f"{ses}-{ters}-{kekeme}")
    return " ".join(sonuc).upper()

def uzayli_cevabi_uret(orijinal: str) -> str:
    """Uzaylıdan gelen 'gerçek' cevabı simüle eder."""
    cevaplar = [
        "ZORP-PLÖK: Anlaşıldı kardeş, galaktik barış anlaşması imzalandı. Ama önce çay ikram edin.",
        "GLEEB-XOR: Mesajınız kuantum dalgalarında yankılandı. Cevabımız: 'Hayır, senin pizza siparişin değil.'",
        "NYX-THRAX: Biz de sizi seviyoruz ama lütfen o kadar yüksek sesle konuşmayın, antenlerimiz hassas.",
        "QUOR-VIB: Talebiniz değerlendirildi. Sonuç: Evrenin merkezi siz değilsiniz. Özür dileriz.",
        "BLOP-ZEE: Mesaj alındı. Karşılık olarak size bir kara delik koordinatı gönderiyoruz. Bol şans.",
        "XANTH-GLOP: Anladık. Ama önce o 'meme' dediğiniz şeyin ne olduğunu açıklayın. Ciddiyiz.",
        "THRUM-PLOK: Diplomatik misyon başarılı. Şimdi lütfen o garip mavi gezegeninizi temizleyin.",
        "VEEZ-GLIB: Cevabımız 42. Başka soru?",
    ]
    return random.choice(cevaplar)

def dramatize_bekle():
    """Ciddi bir diplomatik süreç hissi vermek için bekleme animasyonu."""
    print("\n📡 Galaktik frekans taranıyor...")
    for i in range(3):
        print("   " + "." * (i+1) + " sinyal aranıyor")
        time.sleep(0.6)
    print("✅ Bağlantı kuruldu! Uzaylı elçi yanıt veriyor...\n")
    time.sleep(0.8)

def main():
    print("=" * 60)
    print("   🛸 UZAYLI DİPLOMAT TERCÜMANI 🛸")
    print("   Versiyon: 4.2.0-GALAKTİK (Kararlı olmayan sürüm)")
    print("   Lisans: Galaktik Kamu Malı (kimse umursamıyor)")
    print("=" * 60)
    print("\nMerhaba Dünya vatandaşı.")
    print("Bu program ile uzaylılara resmi mesaj gönderebilirsiniz.")
    print("Dikkat: Mesajlarınız gerçekten uzaya gönderilmez. (muhtemelen)")
    print("-" * 60)

    while True:
        try:
            mesaj = input("\n🌍 İnsan mesajınızı yazın (çıkmak için 'exit'): ").strip()
            if not mesaj:
                continue
            if mesaj.lower() in ["exit", "çık", "quit", "q"]:
                print("\n🛸 Bağlantı kesiliyor... Galaktik barış korunsun. Hoşça kalın.")
                break

            print("\n🔄 Çeviri işlemi başlıyor...")
            time.sleep(0.5)
            uzayli_metin = insan_to_uzayli(mesaj)
            print(f"📤 Uzaylı diline çevrildi:\n   {uzayli_metin}")

            dramatize_bekle()

            cevap = uzayli_cevabi_uret(mesaj)
            print(f"📥 Uzaylı Elçi'den gelen yanıt:\n   {cevap}")
            print("-" * 60)

        except KeyboardInterrupt:
            print("\n\n⚠️ Acil bağlantı kesme protokolü aktif. Güvenli çıkış yapıldı.")
            break
        except Exception as e:
            print(f"\n💥 Galaktik hata oluştu: {e}")
            print("Muhtemelen bir kara delik araya girdi. Tekrar deneyin.")

if __name__ == "__main__":
    main()
