
def init_T(Tmax,dt):
    if Tmax % dt == 0:
       N = Tmax//dt
    else :
       N = Tmax//dt
    print(N)
    T=[i*dt for i in range(int(N)+1)]
  
    return T

#print(init_T(10,1))
print(init_T(10,1.5))
