import numpy
from numpy import random
import csv
import matplotlib.pyplot as plt
import h5py
import pickle

Ttrie = []
tab = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
       0, 0, 0, 0, 0, 0, 0, 0]
tab2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29,
        30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45]
nbr = 0
i = 0
j = 0
mylist = 0

tire = 0
myint = []


def tirage():
    global mylist, tire, myint

    seed = int(input("entrer la valeur de la seed: "))
    tire = int(input("entrer le nombre de tirage voulue: "))

    random.seed(seed)
    tab = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
           0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    tab2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28,
            29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45]

    for i in range(tire):
        loto = numpy.random.choice(range(1, 45), 5, replace=False)
        mylist = list(loto)

        for j in range(45):
            nbr = mylist.count(j)
            tab[j] = (tab[j] + nbr)
            nbr = 0

        fichiercsv(mylist)
        fichierhdf5(mylist)
        fichierbinaire(mylist)

    plt.hist(tab2, bins=45, weights=tab, edgecolor="darkblue")
    plt.show()

    return mylist


##############################################################

def fichiercsv(x):
    with open('monFichier.csv', 'a', newline='') as fichier:
        writer = csv.writer(fichier, delimiter=' ')
        writer.writerow(x)


def fichierhdf5(x):
    with h5py.File('tirage.hdf5', 'w') as f:
        dset = f.create_dataset("tirage", data=mylist)


def fichierbinaire(x):
    with open("fichierbinaire.bin", "ab") as fb:
        pickle.dump(x, fb)


#######################################################

def tri_cocktail(tab):
    change = True
    while change:
        change = False
        for i in range(0, len(tab) - 1):
            if tab[i] > tab[i + 1]:
                tab[i], tab[i + 1] = tab[i + 1], tab[i]
                change = True
        for i in range(len(tab) - 2, -1, -1):
            if tab[i] > tab[i + 1]:
                tab[i], tab[i + 1] = tab[i + 1], tab[i]
                change = True
    print(tab)


def tri_insertion(tab):
    for i in range(1, len(tab)):
        k = tab[i]
        j = i - 1
        while j >= 0 and k < tab[j]:
            tab[j + 1] = tab[j]
            j -= 1
        tab[j + 1] = k
    print(tab)
    return tab


def fusionner(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result


def tri_fusion(tableau):
    if len(tableau) <= 1:
        return tableau

    middle = len(tableau) // 2
    left = tri_fusion(tableau[:middle])
    right = tri_fusion(tableau[middle:])
    fu = fusionner(left, right)
    return fu
    print(fu)


#############################################"


def choixtri():
    num = int(input("entrer le tirage voulue: "))
    monfichier = open("monFichier.csv", "r")

    for i in range(num):
        ligne = monfichier.readline()

    print(f"voici le tirage numéro {num}\n{ligne}")

    choix = int(input("choisisser un type de trie \n 1:tri coktail \n 2:tri insertion \n 3:tri fusion \n >"))

    res = ligne.split(" ")

    for i in range(5):
        Ttrie.append(int(res[i]))

    if choix == 1:
        tri_cocktail(Ttrie)

    if choix == 2:
        tri_insertion(Ttrie)

    if choix == 3:
        print(tri_fusion(Ttrie))

    return Ttrie


######################################"

def dicotom(trie):
    global tire
    num = int(input("entrer le tirage voulue: "))
    monfichier = open("monFichier.csv", "r")
    if num > tire and num < 0:
        print("le nombre est trop grand\n")
    else:
        for i in range(num):
            ligne = monfichier.readline()

        res = ligne.split(" ")

        for i in range(5):
            Ttrie.append(int(res[i]))
    ##############################################################
    dicotoms = int(input("quel nombre voulez vous rechercher: "))
    left = 0
    right = len(Ttrie) - 1
    while left <= right:
        mid = (left + right) // 2

        if Ttrie[mid] == dicotoms:
            return mid

        elif Ttrie[mid] < dicotoms:
            left = mid + 1
        else:
            right = mid - 1
    return -1


#################

def tiragedictomrec():
    Ttrie = []
    num = int(input("entrer le tirage voulue: "))
    monfichier = open("monFichier.csv", "r")

    for i in range(num):
        ligne = monfichier.readline()

    res = ligne.split(" ")

    for i in range(5):
        Ttrie.append(int(res[i]))

    dicotoms = int(input("quel nombre voulez vous rechercher: "))
    tri_insertion(Ttrie)
    print(dichotomrec(Ttrie, dicotoms, 0, len(Ttrie) - 1))

def dichotomrec(arr, x, left, right):
    if left > right:
        return False

    mid = (left + right) // 2
    if arr[mid] == x:
        return True

    elif x < arr[mid]:
        return dichotomrec(arr, x, left, mid - 1)
    else:
        return dichotomrec(arr, x, mid + 1, right)

#################################

def lectureHDF5():
    with h5py.File('tirage.hdf5', 'r') as f:
        data = f['tirage']
        print(data[:15])


def lecturebinaire():
    with open('fichierbinaire.bin', 'rb') as fichier:
        données = pickle.load(fichier)
        print(données)

def lecturecsv():
    with open('monfichier.csv', newline='') as f:
        reader = csv.reader(f, delimiter=':', quoting=csv.QUOTE_NONE)
        for row in reader:
            print(row)


def menu():
    L = 0
    exi = 0
    dic = 0

    while exi != 1:
        dic = 0
        fich = 0
        print("\n____________________________________________")
        print("\n1: Tirage\n2: tri\n3: dichotomie\n4: lecture de fichier\n5: EXIT")
        choix = int(input("Que voulez vous faire? \n>"))

        if choix > 0 and choix < 6:
            if choix == 1:
                tirage()
                L = 1
            elif choix == 2 and L == 1:
                choixtri()

            elif choix == 3 and L == 1:
                while dic != 1:
                    print("\n____________________________________________")
                    print("\n1: dichotomie itérative\n2: dichotomie récursive ")
                    choixdic = int(input("Que voulez vous faire? \n>"))
                    if choixdic == 1:
                        resu = dicotom(Ttrie)

                        if resu != -1:
                            print(f"Le nombre que vous rechercher est présent ")
                        else:
                            print(f"Le nombre que vous rechercher n'est pas présent dans le tableau")

                        dic = 1
                    elif choixdic == 2:
                        tiragedictomrec()
                        dic = 1
                    else:
                        print("l'opération est impossible\n")

            elif choix == 4  and L == 1:
                while fich !=1:
                    print("\n____________________________________________")
                    print("\n1: lecture csv\n2: lecture HDF5\n3: lecture binaire")
                    choixfich = int(input("Que voulez vous faire? \n>"))
                    if choixfich == 1:
                        lecturecsv()

                        fich = 1
                    elif choixfich == 2:

                        lectureHDF5()

                        fich = 1

                    elif choixfich == 3:

                        lecturebinaire()

                        fich = 1
                    else:
                        print("l'opération est impossible\n")

            elif choix == 5:
                break

            else:
                print("Il faut d'abord faire un tirage avant de pouvoir faire autre choses\n")

        else:
            print("l'opération est impossible\n")

menu()