import matplotlib.pyplot as plt

x = [1.5, 3, 3.5, 2]
y = [3, 2, 4, 2]

plt.clf()
plt.plot(x,y,'or')
plt.plot([1,4],[1,4])
plt.savefig("ex_base_03.png")
