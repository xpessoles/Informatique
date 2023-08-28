                                ###################################################################
                                ######################CORRIGE DU TP 4 2017-18######################
                                ###################################################################

####################
##### cesar.py #####
####################

#liste des fréquences en % d'apparitions des lettres dans la langue française

#fr =[9.42,1.02,2.64,3.39,15.87,0.95,1.04,0.77,8.41,0.89,0.00,5.34,3.24,7.15,5.14,2.86,1.06,6.46,7.90,7.26,6.24,2.15,0.00,0.30,0.24,0.32] #ancienne liste

fr = [8.4,1.06,3.03,4.18,17.26,1.12,1.27,0.92,7.34,0.31,0.05,6.01,2.96,7.13,5.26,3.01,0.99,6.55,8.08,7.07,5.74,1.32,0.04,0.45,0.30,0.12] #nouvelle liste: plus proche de la réalité?

#les 3 messages suivants sont codés. Ils pourront être décodés à la fin du paragraphe 4

message1 = """xmvlivb ti amkwvlm ocmzzm uwvlqitm tma iumzqkiqva muxtwgmzmvb lma qvlqmva
vidirwa xwcz kzgxbmz lma umaaioma. k'mab t'cv lma zizma kwlma lm t'pqabwqzm i v'idwqz riuiqa mbm
jzqam. t'quxmvmbzijqtqbm lc kwlm vidirw dqmvb mv xizbqkctqmz lc niqb ycm kmbbm tivocm
v'i ickcv tqmv idmk cvm ycmtkwvycm tivocm mczwxmmvvm wc iaqibqycm.""".replace('\n',' ')


message2 = 'slz lslclz kl jlaal jshzzl zhclua wyvnyhttly lu wfaovu'

message3 = """bpiwxast ti bpiwxph dci xcktcit jc bdntc st rdbbjcxrpixdc htrgti. a'tmetsxitjg trgxi
at itmit axvct epg axvct spch jc gtripcvat st 6 axvcth ti 3 rdadccth. tchjxit xa at gtrdext rdadcct
epg rdadcct. bpiwxast, etcspci at rdcigdat st bpiwtbpixfjth, p djqaxt hp rparjatiit. taat tckdxt at
bthhpvt hjxkpci: STIUOEEFSAR?POQTZ. fjtaat sdxi tigt ap gtedcht st bpiwxph?""".replace('\n',' ')

#le message suivant concerne le paragraphe amélioration

message4 = """Acquérir ces compétences n'est pas important seulement pour votre avenir ; c'est important pour l'avenir de notre pays. Si nous voulons que
l'Amérique reste à la pointe, nous avons besoin que de jeunes américains comme vous maîtrisent les outils et les technologies qui vont changer nos façons
de faire dans tous les domaines. C'est pourquoi je vous demande de vous impliquer personnellement.
Ne vous contentez pas d'acheter un nouveau jeu vidéo, faites-en un.
Ne vous contentez pas de télécharger la dernière application à la mode, participez à sa conception.
Ne vous contentez pas de jouer sur votre smartphone, programmez-le
Personne ne naît informaticien, mais avec un peu de travail, des maths et des sciences,
à peu près tout le monde peut le devenir. Ne laisser personne vous dire que vous ne pouvez pas réussir.
Que vous soyez un jeune homme ou une jeune femme, que vous viviez à la ville ou à la campagne, l'informatique va occuper une place importante dans votre avenir.
Et si vous êtes prêt à travailler dur et à étudier, cet avenir, vous pourrez le façonner vous-même.""".replace('\n',' ')

####################
##### partie 1 #####
####################

#q1
for i in range (97,123):
    print(chr(i))

#q2

def ordre(c):
    """donne code simplifie du caractere c """
    return(ord(c) - ord('a'))

#q3

def lettre(nb):
    """donne la lettre correspondant à un ordre simplifie"""
    return(chr(ord('a') + nb))

####################
##### partie 2 #####
####################

#q4

#P = (N + K) % 26
#N = (P - K) % 26


#q5

def crypte(cle, c):
    """donne le cryptage deu caractere car selon cle"""
    P = (ordre(c) + ordre(cle)) % 26
    return(lettre(P))

#q6

def clair(cle, c):
    """donne le decodage du caractere car selon cle"""
    N = (ordre(c) - ordre(cle)) % 26
    return(lettre(N))

####################
##### partie 3 #####
####################

#q7

def codage(cle, texte):
    """code texte selon cle"""
    s = ''
    for c in texte:
        if ordre(c) in range(26):
            s = s + crypte(cle, c)
        else:
            s = s + c
    return(s)

#q9

def decodage(cle, texte):
    """decode texte selon cle"""
    s = ''
    for c in texte:
        if ordre(c) in range(26):
            s = s + clair(cle, c)
        else:
            s = s + c
    return(s)
    
####################
##### partie 5 #####
####################

for i in range(26):
    cle=lettre(i)
    print("cle utilisée : " + cle)
    print(decodage(cle,message3))
    print("\n")

#Message 1 : clé I
#Message 2 : clé H
#Message 3 : clé P


####################
##### partie 4 #####
####################

#q1

def frequence(texte):
    """calcule la frequence d'apparition en pourcent de chacune des lettres de texte"""
    liste = [0 for i in range(26)]
    for x in texte:
        if ordre(x) in range(26):
            liste[ordre(x)] = liste[ordre(x)] + 1
    nb_lettres = sum(liste)
    for i in range(26):
        liste[i] = liste[i] / nb_lettres * 100
    return(liste)
    #return([u/sum(l)*100 for u in l]), methode prematuree pour les eleves

#q2

def distance(texte):
    """calcule la liste distance"""
    fc = frequence(texte)
    d = []
    for i in range(26):
        s = 0
        for j in range(26):
            s = s + abs(fr[j] - fc[(j+i) % 26])
        #s = sum(abs(fr[j] - fc[(j+i) % 26]) for j in range(26))
        d.append(s)
    return(d)

#q3

def minimum_distance(texte):
    """calcule l'indice minimum du tableau distance(texte)"""
    d = distance(texte)
    index_min = 0
    for j in range(1,26):
        if d[j] < d[index_min]:
            index_min = j            
    return(index_min)

#q4

def decodage_auto(texte):
    """decode un texte de maniere automatique"""
    cle = lettre(minimum_distance(texte))
    return(decodage(cle,texte))

print(decodage_auto(codage('r','vous suivez le cours le python')))

#q5

#print("\n                 ############## tests sur message1, message2, message3 ##############" + "\n")
    
# i = 1
# for message in [message1, message2, message3]:
#     print('message' + str(i) +  ' : ' + decodage_auto(message) + "\n")
#     i = i + 1

#donne:
    
##message1 : pendant la seconde guerre mondiale les americains employerent des indiens navajos pour crypter des messages.
##c'est l'un des rares codes de l'histoire a n'avoir jamais ete brise.
##l'impenetrabilite du code navajo vient en particulier du fait que cette langue n'a aucun lien avec une quelconque langue europeenne ou asiatique.
    
##message2 : les eleves de cette classe savent programmer en python
    
##message3 : mathilde et mathias ont invente un moyen de communication secret.
##l'expediteur ecrit le texte ligne par ligne dans un rectangle de 6 lignes et 3 colonnes.
##ensuite il le recopie colonne par colonne. mathilde, pendant le controle de mathematiques, a oublie sa calculette.
##elle envoie le message suivant: STIUOEEFSAR?POQTZ. quelle doit etre la reponse de mathias?

#correction exo de message3 : sept fois quatorze

####################
##### partie 5 #####
####################

#q1
    
def enleve_majuscules(texte):
    """transforme les majuscules en minuscules dans texte"""
    majuscule = 'AZERTYUIOPQSDFGHJKLMWXCVBN'
    minuscule = 'azertyuiopqsdfghjklmwxcvbn'
    texte_sans_maj = ''
    n = len(texte)
    for i in range(n):
        j = 0
        while j < len(majuscule) and texte[i] != majuscule[j]:
            j = j + 1
        if j < len(majuscule):
            texte_sans_maj = texte_sans_maj + minuscule[j]
        else:
            texte_sans_maj = texte_sans_maj + texte[i]
    return(texte_sans_maj)

#q2

def enleve_accents(texte):
    """enlève les accents dans texte"""
    accent = 'àâéèêôûîîç'
    sans_accent= 'aaeeeouiic'
    texte_sans_accent = ''
    n = len(texte)
    for i in range(n):
        j = 0
        while j < len(accent) and texte[i] != accent[j]:
            j = j + 1
        if j < len(accent):
            texte_sans_accent = texte_sans_accent + sans_accent[j]
        else:
            texte_sans_accent = texte_sans_accent + texte[i]
    return(texte_sans_accent)

#print("\n                 ############## test amélioration sur message4 ##############" + "\n")

cle = 'x'
message = enleve_accents(enleve_majuscules(message4))
#print("message4 sans accents : " +  message + "\n")

message_code = codage(cle, message)
#print("message4 sans accents codé : " + message_code + "\n")

message_decode = decodage_auto(message_code)
#print("message4 décodé automatiquement : " + message_decode + "\n")

#donne acquerir ces competences n'est pas important seulement pour votre avenir ;
#c'est important pour l'avenir de notre pays. si nous voulons que l'amerique reste a la pointe,
#nous avons besoin que de jeunes americains comme vous maitrisent les outils et les technologies
#qui vont changer nos facons de faire dans tous les domaines. c'est pourquoi je vous demande de vous impliquer personnellement.
#ne vous contentez pas d'acheter un nouveau jeu video, faites-en un. ne vous contentez pas de telecharger la derniere application a la mode,
#participez a sa conception. ne vous contentez pas de jouer sur votre smartphone, programmez-le personne ne nait informaticien,
#mais avec un peu de travail, des maths et des sciences, a peu pres tout le monde peut le devenir.
#ne laisser personne vous dire que vous ne pouvez pas reussir. que vous soyez un jeune homme ou une jeune femme,
#que vous viviez a la ville ou a la campagne, l'informatique va occuper une place importante dans votre avenir.
#et si vous etes pret a travailler dur et a etudier, cet avenir, vous pourrez le faconner vous-meme.


#############################
##### Approfonidssement #####
#############################

#contenu de vigenere.py

message_vigenere = """lpekwcsjwdplylzwudvgldziqzkwrcsrlksjkgomvbnltxwawpnlmpcoinmkveizllyinqwpfrwcpfrawmfellqztwatdgamoteuipmdgspsfidyntwnimfpbfihqkcikgldz
iqzecijefzttwavkmrupdaeolwfirzzrfiotsdeczplgejkwreeglteehqugqliywtznmkcnjwxlrioaspstofdpvemkglcsdpeeebeksvocpqpakzkrkoyemmaviwedownlvhiujacsfcoyfwmtlvbozc
qwqlgtcocpyhwqlnolfopdizmecnuoyedmhmhnazgtcoibiatelbpnzynwfpeusxlckqmjktvgglweebtkeezlapmjmvgsvzpgpvabvgclstwwmntwufcsfcduqifftfielnsqxmplrdtympwvucuompfivk
awuprgdlavaavglcstwycwdsktiwpywezmtkeesezyrwvlgtrztnprabjqumoxpxilikvrvgpievwwjfieotcphavlgnufpalvhmjnecoatyuqqkgdzglteedrstrzjpclmpzgrtrfopycowfierbelavaaa
nllwdpxfhitkeeefpwpaimtazhofdijmlqnescxlmoamtlvazxprpkwnacitlgeebhcrlhzferwbmtecqpaprzifvqloyowihihknmwyelxezwtuesxzyxnmvgsfbrzfwomlnaisrlchwxmksjsactxwkgwr
zfopapqatglcslwtgaaswtrgfcdioxagdjtclatamvgcvhepthamiweaoxltwatdgnrjltezqlwnagwylgiycfiolgdpeipcfgmfbecpijbjciespalvhiuwrzcdteiatdgsvzlyneocjuejhclnioiltamsc
dwiypsopvhlccmrilqukxfdeiwbwopjdzfcpadgkruwdalvwqlteuoydfrhijiekfzflylqwfdlbpslmacfknjhlyeelzwuacwnppxwqlclrdzfcwqqlgdlzlatrzifulvhpccmazkcnjgzyrinkgomvbepwp
amfuoihtclmpxwpdrbefyfkclfetvpxtrhmltolowwlmpbgwtufztegkueguehfyyihxmkskcfelgkchklgzzyriwqlreidpyomycdciisxpyxzcfgfrqzydmxzmuqlsbflpekwuejsyetxpwedeiqzxxizif
uuedftewzcfggioyoptnwxqnusfclzwvloedsolgsezhgnjsldpvabwpiiwwyjeriavrzsywlhajagnvhzyyejbwvacwnpyipzgwvrapxptwaltejsiecekzvknrwcpoijbwpdisalcpazdglrdtybyeawfij
otellfijtimscltxnwhvairpyjwkvygaehlacioqdnuzgpxmpwjagnhipwwiwcjcikrfdprabgpnvfxltwocjnedcxpyxymdcllwlglmpxstukcfeyepcjgltsapyhwvlsurbowppwxapvzbelemnmjwnvazy
evalwuoeuzfdwabdcrvulcoelcausvdcteeywmtiirpawyojwnlvowtnioimvajicdpwlqwfswflaaialweekhptoiaymgjraltdihtwpamotegyzmdcpzblgpgqvyqujgpepxqvwooehcpprpzsknvsalcp
wkmtifgtepihtwuecoynlwqzkgskflnpwwbjcvvfdwpgdierekocctzwbgwtaidepepmersgcfcwirwatdzgalceebjgdrbdfypwzygticflftemvfuessltiqvapskoyeltnmkclzqppeeebsnagcfcdyebw
fucoatyhwvknekscctinaspsjcyrpvyweoeehpwwiavkqrkwcltx""".replace('\n','')

def enleve_ponctuation(texte):
    sans_ponctuation = ''
    for x in texte:
        if ordre(x) in range(26):
            sans_ponctuation = sans_ponctuation + x
    return(sans_ponctuation)

#q1

def codage_vigenere(cle, texte):
    n = len(cle)
    texte_code = ''
    j = 0
    for x in texte:
        cle_cesar = cle[j % n]
        texte_code = texte_code + crypte(cle_cesar, x)
        j = j + 1        
    return(texte_code)

#q2

def decodage_vigenere(cle, texte):
    n = len(cle)
    texte_clair = ''
    j = 0
    for x in texte:
        cle_cesar = cle[j % n]
        texte_clair = texte_clair + clair(cle_cesar, x)
        j = j + 1       
    return(texte_clair)

#q3

def decodage_vigenere_ameliore(longueur, texte):
    cle = ''
    for i in range(longueur):
        morceau = ''
        for j in range(i, len(texte), longueur):
            morceau = morceau + texte[j]
        cle = cle + lettre(minimum_distance(morceau))
    return(cle, decodage_vigenere(cle, texte))

#print("\n                 ############## Approfondissement avec Vigenère: décryptage de message_vigenere ##############" + "\n")
        
#print(decodage_vigenere_ameliore(11, message_vigenere))

#la cle est 'lewiscaroll' et message_code est un passage d'Alice au pays des merveilles
        

        
            
            


    
    
        


