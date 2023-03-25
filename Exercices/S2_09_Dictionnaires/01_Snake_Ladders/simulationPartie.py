import random as r

dSeE = {  1: 38,  4: 14,  9: 31, 17:  7, 21: 42, 28: 84, 51: 67, 54: 34,
         62: 19, 64: 60, 71: 91, 80: 99, 87: 24, 93: 73, 95: 75, 98: 79}

LSeE = [[ 1,  4,  9, 17, 21, 28, 51, 54, 62, 64, 71, 80, 87, 93, 95, 98],
        [38, 14, 31,  7, 42, 84, 67, 34, 19, 60, 91, 99, 24, 73, 75, 79]]


def lancerDe():
    return r.randint(1, 6)

def caseFuture(case):
    if case in LSeE[0]:
        for i in range(len(LSeE[0])):
            caseD = LSeE[0][i]
            if caseD == case:
                return LSeE[1][i]
    else:
        return case

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

def partie(choix):
    case = 0
    L = [case]
    while case != 100:
        de = lancerDe()
        case = avanceCase(case, de, choix)
        L.append(case)
    return L

r.seed(2)
print(partie('r'))
print(partie('i'))
print(partie('q'))

r.seed(0)
longR, longI, longQ = [], [], []
for i in range(100000):
    longR.append(len(partie('r'))-1)
    longI.append(len(partie('i'))-1)
    longQ.append(len(partie('q'))-1)

plt.hist(longR)
plt.hist(longR)




