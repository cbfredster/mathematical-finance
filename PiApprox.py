import random
import numpy as np
import matplotlib.pyplot as plt

number = 10000

def pointGeneration(n):
 RandomList = []
 for i in range(0,n):
  tempList = []
  xnumber = random.uniform(-1,1)
  ynumber = random.uniform(-1,1)
  tempList.append(xnumber)
  tempList.append(ynumber)
  RandomList.append(tempList)
  tempList.clear
 return(np.array(RandomList))
 

plt.xlim(-1,1)
plt.ylim(-1,1)
plt.axis("equal")

theta = np.linspace(0,2*np.pi, 150)
radius = 1
a = radius * np.cos(theta)
b = radius * np.sin(theta)


figure, axes = plt.subplots(1)
axes.plot(a,b)
axes.set_aspect(1)

x, y = pointGeneration(number)[:,0], pointGeneration(number)[:,1]

inside = x**2 + y**2 <= 1

plt.scatter(x, y, c=np.where(inside, "red", "blue"))
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)
plt.show()

def piAprrox(number):
 circleTotal = 0
 throughNumber = 0
 for i in range(len(pointGeneration(number))):
  if ((pointGeneration(number)[i][0])**2)+((pointGeneration(number)[i][1])**2) <= 1:
   circleTotal = circleTotal + 1
  throughNumber = throughNumber + 1
  print(throughNumber, 4*circleTotal/throughNumber)
 approximation = 4*circleTotal/number
 return(approximation)
 
print(piAprrox(number))
 





