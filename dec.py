def un_deco(fonction):
    print("D1")
    def a_deco():
        print("D4")
    return a_deco


def un_autre_deco(fonction):
    print("D2")
    def another_deco():
        print("D3")

    return another_deco


@un_deco
@un_autre_deco
def une_fonction():
    print("la fonction en question")

une_fonction()