import matplotlib.pyplot as plt

yp = ['Apples', 'Bananas', 'Cherries', 'Dates', 'Elderberries']
xp = [25, 30, 15, 10, 20]

font1 = {'family':'serif','size':20}

color = ['#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0']

plt.pie(xp, labels = yp, colors = color, startangle = 135, autopct='%1.1f%%')
plt.title("Fruit Distribution",fontdict = font1)
plt.show()
