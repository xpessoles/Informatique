dSeE = {  1: 38,  4: 14,  9: 31, 17:  7, 21: 42, 28: 84, 51: 67, 54: 34,
         62: 19, 64: 60, 71: 91, 80: 99, 87: 24, 93: 73, 95: 75, 98: 79}

def caseFuture(case):
    if case in dSeE.keys():
        return dSeE[case]
    else:
        return case

def avanceCase(case, de, choix):
    if case + de <= 100:
        return caseFuture(case + de)
    else:
        if choix == 'r':
            case_ = 100 - (case+de)%100
            return caseFuture(case_)
        elif choix == 'i':
            return case
        elif choix == 'q':
            return 100

def casesAccessibles(case):
    cases = []
    for de in range(1, 7):
        cases.append(avanceCase(case, de, 'q'))
    return cases

def meilleurChoix(case):
    cases = casesAccessibles(case)
    caseMax = cases[0]
    for case in cases:
        if case > caseMax:
            caseMax = case
    return caseMax

def partieGloutonne():
    case = 0
    L = [case]
    while case != 100:
        case = meilleurChoix(case)
        L.append(case)
    return L

print(partieGloutonne())