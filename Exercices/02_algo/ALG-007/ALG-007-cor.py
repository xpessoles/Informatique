n = 0
fact = 1 
# Inv. : fact = n !
while fact <= 123456789 :
    # Invariant : fact = n !
    # Variant : 123456789-fact
    n = n + 1 # fact = (n-1)!
    fact = fact * n
    # Invariant : fact = n!
# Invariant : fact = n!
# Sortie de boucle while : fact > 123456789
# Au tour précédent, fact <= 123456789

