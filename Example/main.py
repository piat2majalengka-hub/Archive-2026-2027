import random

choices = ["Gunting", "Batu", "Kertas"]
name = input("masukan nama kamu : ")   

while True:
    print(f'hai {name}, selamat datang di permainan gunting-batu-kertas')
    print("Silahkan pilih :")
    print("1 - Gunting")
    print("2 - Batu")
    print("3 - Kertas")
  
    try:
        choice = int(input("Masukan pilihanmu : "))
    except ValueError:
        print("Masukan nomor yang valid!.\n")
        continue

    while choice < 1 or choice > 3:
        choice = int(input("Tolong masukan pilihan yang benar (1-3): "))

    # User choice
    user_choice = choices[choice - 1]

    print(f"\nPilihan {name} adalah:", user_choice)
    print("Sekarang, giliran komputer...")

    # Computer choice
    comp_choice = random.randint(1, 3)
    computer_choice = choices[comp_choice - 1]

    print("Komputer memilih :", computer_choice)
    print(user_choice, "vs", computer_choice)

    # Determine winner
    if choice == comp_choice:
        print("<== Seri ==>")

    elif (
        (choice == 1 and comp_choice == 3) or
        (choice == 2 and comp_choice == 1) or
        (choice == 3 and comp_choice == 2)
    ):
        print(f"<== {name} menang! ==>")

    else:
        print("<== Komputer menang! ==>")

    # Play again
    while True:
        ans = input("\nMau main lagi? (Y/N): ").lower()

        if ans in ['y', 'n']:
            break

        print("Tolong cuman pilih Y atau N")

    if ans == 'n':
        break

    print()

print("\nThanks for playing!")
