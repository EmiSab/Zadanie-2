punkty = int(input())

if punkty >= 10:
    print("Zaliczone")
else:
    print("Niezaliczone")
    print(f"Brakujące punktów: {10 - punkty}")
    