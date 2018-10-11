def controle_type_params(*types_params_attendus, **types_params_attendus_dict):
    li = []
    lu = []
    la = []
    le = []
    la = list(types_params_attendus_dict.values())
    for i in types_params_attendus:
        li.append(i)
    print("début contrôle")
    def mon_decorateur(fonction_decoree):
        print("dans fonction mon_decorateur qui à appel de la fonction {}".format(fonction_decoree))
        def mon_substitut(*param_env, **param_env_dict): #, **parametres_envoyes
            k = 0
            le = list(param_env_dict.values())
            if len(lu) == len(li):
                for i in param_env:
                    lu.append(type(i))
                for l in li:
                    # print(i)
                    for j in lu:
                        # print(j)
                        if l == j:
                            # print("i == j")
                            k += 1
            if len(la) == len(le):
                for m in la:
                    for n in le:
                        if n == m:
                            k += 1
            if k == (len(lu) + len(le)):
                print("TYPES COMPATIBLES")
                return fonction_decoree(*param_env, **param_env_dict)
            else:
                    print("TYPES INCOMPATIBLES")
        return mon_substitut
    return mon_decorateur

# @controle_type_params(int)
# def fonction1(a):
#     print("ici fonction1 avec 1 paramètres")
@controle_type_params(int, str)
def fonction2(a = 0, b = " "):
    print("ici fonction 2 avec 2 paramètre")

# fonction1("oui")
# print("la fonction1 est de type {}".format(fonction1))
fonction2(1, "yes")
print("la fonction2 est de type {}".format(fonction2))
print("fin")