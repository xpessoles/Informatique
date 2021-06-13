f=open("bode.txt","w")
f.write("pulsation"+";"+"gain"+";"+"phase"+"\n")
for i in range(len(w)):
    f.write(str(w[i])+";"+str(gain[i])+";"+str(phase[i])+"\n")
f.close()
