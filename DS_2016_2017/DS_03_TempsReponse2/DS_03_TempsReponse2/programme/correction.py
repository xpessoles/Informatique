### question 4

les_y1=[0] #initialisation avec conditions initiales
les_y2=[0]
n=int(T/h)
for i in range(1,n):
    les_y1.append(les_y1[-1]+h*phi_1(i*h,les_y1[-1],les_y2[-1])
    les_y2.append(les_y2[-1]+h*phi_2(i*h,les_y1[-1],les_y2[-1])
    
### question 5
les_t=[i*h for i in range(n)]
plt.plot(les_t,les_y1)
plt.show()

### question 11

    