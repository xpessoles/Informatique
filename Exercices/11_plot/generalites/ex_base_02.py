import matplotlib.pyplot as plt

x = [1, 3, 4, 2]
y = [2, 1, 4, 2]

plt.clf()
plt.plot(x,y,'or--')
plt.savefig("ex_base_02.png")

plt.clf()
plt.plot(x,y,marker='o',color='r',linestyle='--')
plt.savefig("ex_base_02_bis.png")
