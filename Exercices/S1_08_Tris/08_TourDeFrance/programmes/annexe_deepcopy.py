from copy import copy, deepcopy

L = [['JULIAN ALAPHILIPPE ', '21', 250756], ['GERAINT THOMAS ', '1', 250851],['STEVEN KRUIJSWIJK ', '81', 250863]]

L_copy = copy(L)   # copie superficielle
L_deepcopy = deepcopy(L)  # copie profonde

L[1][0] = 5

copy:  [['JULIAN ALAPHILIPPE ', '21', 250756], [5, '1', 250851],
['STEVEN KRUIJSWIJK ', '81', 250863]]
deepcopy:  [['JULIAN ALAPHILIPPE ', '21', 250756], ['GERAINT THOMAS ', '1', 250851],
['STEVEN KRUIJSWIJK ', '81', 250863]]