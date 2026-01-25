import os

print("Wybierz lekcję do uruchomienia:")
print("1. Etapy rozwiązywania problemów")
print("2. Podstawy Pythona")
print("3. Funkcja matematyczna i złożone operatory przypisania")
print("4. Instrukcje warunkowe")
print("5. Instrukcje iteracyjne")
print("6. Funkcje w Pythonie")
print("7. Algorytm Euklidesa")
print("8. Zadanie (NWW i NWD)")

wybor = input("Twój wybór (1-8): ")

if wybor == "1":
    os.system("python3 1_etapy_rozwiązywania_problemów_za_pomocą_komputera.py")
elif wybor == "2":
    os.system("python3 2_Podstawy_pythona.py")
elif wybor == "3":
    os.system("python3 3_Instrukcje_warunkowe_w_Pythonie.py")
elif wybor == "4":
    os.system("python3 4_Instrukcje_iteracyjne.py")
elif wybor == "5":
    os.system("python3 5_Instrukcje_warunkowe_w_Pythonie.py")
elif wybor == "6":
    os.system("python3 6_Funkcje_w_pythone.py")
elif wybor == "7":
    os.system("python3 7_Algorytm_Eukildesa.py")
elif wybor == "8":
    os.system("python3 zadanie.py")
else:
    print("Nieprawidłowy wybór")