

def valid_pnr2(pnr):

    """Takes a "personnumber" and checks in it is a valid
    number or not. Then prints valid or prints not valid

    """
    # Saves and remove the last number in the number
    pnr = list(pnr)
    lastnr = int(pnr[-1])
    pnr.pop(-1)


    if "-" in pnr:
        pnr.pop(pnr.index("-"))

    if pnr[:2] == ["1","9"]:
        pnr = pnr[2:]


    faktor = 2
    product = 0

    #for every number in the personnumber (except if the first two numbers
    #is 1 and 9, and the last number) multiple them with 2
    for nr in pnr:
        nr = int(nr)
        if faktor == 2:
            temp = nr * faktor
            if temp >= 10:
                temp = (temp - 10) + 1
            product = product + temp
            faktor = 1
        else:
            temp = nr * faktor
            if temp >= 10:
                temp = (temp - 10) + 1
            product = product + temp
            faktor = 2

    product += lastnr
    if (product / 10) * 10 == product:
        print "valid"
    else:
        print "not valid"

valid_pnr2(pnr="19811218-9876")