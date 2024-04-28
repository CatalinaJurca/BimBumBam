import random
def joc_bim_bum_bam():
    optiuni = ["piatra", "foarfeca", "hartie"]
    while True:
        alegere_jucator = input("Alege piatra, foarfeca sau hartie").lower()
        if alegere_jucator not in optiuni:
            print("Te rog sa alegi una din optiunile valide:piatra, foarfeca, hartie")
            continue
        alegere_computer = random.choice(optiuni)
        print(f"Calculatorul a ales:{alegere_computer}")

        if alegere_jucator == alegere_computer:
            print("Egalitate! Incercati din nou")
        elif (alegere_jucator == "piatra" and alegere_computer == "foarfeca") or \
             (alegere_jucator == "foarfeca"and alegere_computer == "hartie") or \
             (alegere_jucator == "hartie"and alegere_computer == "piatra"):
            print("Felicitari! Ai castigat!")
        else:
            print("Ai pierdut!")

print(joc_bim_bum_bam())
