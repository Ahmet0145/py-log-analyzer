from colorama import Fore, Style, init
init(autoreset=True)
# Wrong Attemptleri saymak için boş bir sözlük oluşturuyoruz
wrong_ips = {}
threshold_value = 3  # Kaç Wrong Attemptden sonra alarm verilsin?

# 1. 'server.log' dosyasını okuma ("r") modunda açıyoruz
with open(r"C:\Users\Ahmet\New folder\server.log", "r", encoding="utf-8") as dosya:

    # 2. Dosyadaki her bir satırı sırayla geziyoruz

    for line in dosya:
        # Satır sonundaki gizli alt satıra geçme karakterini (.strip) siliyoruz
        clean_line = line.strip()

        # satırlar arası boşlukları silmek için strip metodu

        if "FAIL" in clean_line:
            # Eğer satırın içinde "FAIL" kelimesi geçiyorsa...
           
            # Satırı boşluklardan bölüp ilk elemanı (yani IP adresini) alıyoruz
            separating = clean_line.split()
            ip = separating[0]

            if ip in wrong_ips:
                # Eğer bu IP daha önce sözlükte varsa sayısını 1 artır, yoksa 1 olarak ekle
                wrong_ips[ip] = wrong_ips[ip] + 1
            else:
                wrong_ips[ip] = 1


# 2. Eşik değerini aşan IP'leri tespit et
print("--- Analysis results ---")

with open("rapor.txt", "w", encoding="utf-8") as rapor_dosyasi:
    rapor_dosyasi.write("=== Analysis results ===\n\n")

    for ip, number in wrong_ips.items():
        if number >= threshold_value:
            print(f"{Fore.RED}[ALERT] Brute-Force Detected! IP: {ip} - Number Of Wrong Attempt: {number}{Style.RESET_ALL}")
            rapor_dosyasi.write(f"[THREAT] IP: {ip} | Wrong Attempt: {number}\n")
        else:
            print(f"{Fore.GREEN}[INFO] Normal Aktivite. IP: {ip} - Number Of Wrong Attempt: {number}{Style.RESET_ALL}")
            rapor_dosyasi.write(f"[SAFE] IP: {ip} | Wrong Attempt: {number}\n")
