import random

def play_game():
    secret_number = random.randint(1, 100)
    attempts = 0
    
    print("=== GAME LAKKOOFSA TILMAAMUU ===")
    print("1 hanga 100 keessaa lakkoofsa tokko tilmaami!")
    
    while True:
        try:
            guess = int(input("Lakkoofsa kee galchi: "))
            attempts += 1
            
            if guess < secret_number:
                print("Gadiidha! Oliif siiquun tilmaami.\n")
            elif guess > secret_number:
                print("Oliidha! Gadiif siiquun tilmaami.\n")
            else:
                print(f"BAAYYEE GAARII! Baay'ina yaalii {attempts} keessatti deebii sirrii argatte!")
                break
        except ValueError:
            print("Moo! Maaloo lakkoofsa sirrii galchi.\n")

if __name__ == "__main__":
    play_game()
