import os

print("Wybierz lekcję do uruchomienia:")
print("1. Etapy rozwiązywania problemów")
print("2. Podstawy Pythona")
print("3. Instrukcje warunkowe")
print("4. Instrukcje iteracyjne")

wybor = input("Twój wybór (1-4): ")

if wybor == "1":
    os.system("python3 1_etapy_rozwiązywania_problemów_za_pomocą_komputera.py")
elif wybor == "2":
    os.system("python3 2_Podstawy_pythona.py")
elif wybor == "3":
    os.system("python3 3_Instrukcje_warunkowe_w_Pythonie.py")
elif wybor == "4":
    os.system("python3 4_Instrukcje_iteracyjne.py")
else:
    print("Nieprawidłowy wybór")