# # MATPLOTLIB

import matplotlib.pyplot as plt  
x = [1,2,3,4]
y = [2,4,6,8]
z = [10,20,30,40]
plt.plot(x,y)
plt.plot(y,z)
plt.title("graph")
plt.xlabel("x-values")
plt.ylabel("y-values")
# plt.plot(x,y, color = 'red',linestyle = '-',marker = 's')
plt.plot(x,y,'go-')
plt.plot(y,z,'bo-')
plt.show()

# # NUMPY
import numpy as np
x = [1,2,3,4]
y = [2,4,6,8]
plt.title("GRAPH-2")
plt.xlabel("x-values")
plt.ylabel("y-label")
plt.plot(x,np.sin(x),label = "Sine")
plt.plot(x, np.cos(x), label = "Cosine")
plt.legend(loc = "upper right")
plt.show()

# BAR GRAPH
x = [1,2,3,4]
y = [2,4,6,8]
plt.bar(x,y, color = 'green')
plt.title("GRAPH-3")
plt.xlabel("x-values")
plt.ylabel("y-values")
plt.show()

# # SCATTER PLOT
x = [1,2,3,4]
y = [2,4,6,8]
z = [1.5,2,4,5.5]
plt.scatter(x,y)
plt.scatter(y,z)
plt.title("GRAPH-4")
plt.xlabel("x-values")
plt.ylabel("y-label")
plt.show()

# PIE CHAT
plt.figure(figsize=(8, 5))
sizes = [25,30,20,25]
sectors = ['A','B','C','D']
plt.pie(x = sizes ,labels= sectors,startangle=90,autopct='%1.1f%%')
plt.title("PIE CHAT")
plt.savefig('my_plot.png')
plt.show()

# PIE CHAT TASK:Draw pie chart of population share of world's countries.
import matplotlib.pyplot as plt
sizes = [25,30,20,25]
countries = ['India','China','USA','Indonesia']

plt.pie(x = sizes,labels=countries, startangle= 90,autopct="%1.1f%%")
plt.title("Population Share of World's Countries")
plt.savefig('population_pie_chat.png')
plt.show()







# multiple graphs 

x = [1,2,3,4]
y = [2,4,6,8]
z = [1.5,2,4,5.5]
fig,axs = plt.subplots(1,2)
axs[0].plot(x,y)
axs[0].set_title('Linear')
axs[1].bar(y,z)
axs[1].set_title('Quadratic')
plt.show()







