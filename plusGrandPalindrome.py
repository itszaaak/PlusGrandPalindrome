def estPalindrome(nombre):
    nombre_str = str(nombre)  #converqion en str pour comparision
    return nombre_str == nombre_str[::-1] #comparision avec version inversee de la str


def plusGrandPalindrome(n):
    if n <= 0:
        return None, []        #on renvoye la liste vide

    limiteSup = 10 ** n - 1     #plus grand palindrome possible avec n chifres
    limiteInf = 10 ** (n - 1)   # plus petit palindrome possible avec n chifres

    palindromes = []    #liste palindormes
    plusGrand = 0       #Plus grand palindrome

    for i in range(limiteSup, limiteInf - 1, -1):   #le -1 nous garantis l'exlusivité n
        for j in range(i, limiteInf - 1, -1):       #calculs des valeurs possibles avec 
            produit = i * j                         #nos deux bornes sup et inf
            if estPalindrome(produit):
                palindromes.append(produit)         #on l'ajoute a la liste
                if produit > plusGrand:             #verification pour le palindrome
                    plusGrand = produit

    return plusGrand, palindromes                   #retour liste et plus grand

print(plusGrandPalindrome(2))