def main():

    nombre_a_gauche = input("Entrez un nombre positif : ")
    nombre_a_droite = input("Entrez un nombre positif : ")

    symbole = input("Entrez l'opération souhaitée ['+', '-', '*' ou '/']: ")
    result = 0


    if not nombre_a_gauche.isnumeric() and not nombre_a_droite.isnumeric() :
        print("Erreur : Les deux nombres doivent être des nombres entiers")
    else:
        nombre_a_gauche = int(nombre_a_gauche)
        nombre_a_droite = int(nombre_a_droite)
        
        match symbole:
            case "+":
                result = nombre_a_gauche + nombre_a_droite
            case "-":
                result = nombre_a_gauche - nombre_a_droite
            case "*":
                result = nombre_a_gauche * nombre_a_droite
            case "/":
                if nombre_a_droite != 0:
                    print("Impossible de diviser par zero")
                else:
                    result = nombre_a_gauche / nombre_a_droite
            case _:
                print("l'operation est invalide !")
        
        print(f"le resultat de l'operation est : {result}")

if __name__ == "__main__":
    main()
                
            


    
    