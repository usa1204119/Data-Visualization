import matplotlib.pyplot as plt

flowers = ['Mogara','Jai','Hibiscus','Chrysanthemum']
no_of_flowers = [70,50,45,80]

plt.pie(flowers,no_of_flowers,linewidth=14)
plt.title('No of flowers per 5 tree',fontsize=15)
plt.xlabel('flowers',fontsize=15)
plt.ylabel('no_of_flowers',fontsize=15)

plt.axis([-1,5,0,90])
plt.tick_params(axis='both',labelsize=25)
plt.show()