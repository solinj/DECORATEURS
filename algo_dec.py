def controle_nbe_params(nombre_max_params):
    print("début contrôle")
    def mon_decorateur(fonction_decoree):
        print("dans fonction mon_decorateur qui à appel de la fonction {}".format(fonction_decoree))
        def mon_substitut(*pnn, **pn):
            print("contrôle des params de la fonction {}".format(fonction_decoree))
            nbre_pnn = len(pnn)
            nbre_pn = len(pn)
            nbre_params = nbre_pnn + nbre_pn
            if nbre_params <= nombre_max_params:
                return fonction_decoree(*pnn, **pn)
            else:
                print("nombre de paramètres dépasse limite autorisée")
        return mon_substitut
    return mon_decorateur

@controle_nbe_params(2)
def fonction1(a, b, c):
    print("ici fonction1 avec 3 paramètres")
@controle_nbe_params(2)
def fonction2(a):
    print("ici fonction 2 avec 1 paramètre")

# fonction1("oui", "non", "peut-être")
# print("la fonction1 est de type {}".format(fonction1))

fonction2("yes")
print("la fonction2 est de type {}".format(fonction2))
print("fin")