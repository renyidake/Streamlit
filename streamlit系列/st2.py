import matplotlib.pyplot as plt

data = [1, 2, 3, 4, 5]
x_labels = ['Category A', 'Category B', 'Category C', 'Category D', 'Category E']
plt.bar(x_labels, data)
plt.title('Bar Chart')
plt.xlabel('Categories')
plt.ylabel('Values')
plt.show()