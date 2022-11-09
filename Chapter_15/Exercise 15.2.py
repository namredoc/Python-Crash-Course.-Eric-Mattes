import matplotlib.pyplot as plt

# Define data.
x_values = list(range(1, 5001)) 
cubes = [x**3 for x in x_values]


#Make plot
plt.style.use('seaborn')
fig, ax = plt.subplots() 
ax.scatter(x_values, cubes, s=10)


# Цветовые карты
ax.scatter(x_values, cubes, c=cubes, cmap=plt.cm.Purples, s=10)

# Set chart title and label axes.
ax.set_title("Cubes", fontsize=14)
ax.set_xlabel('Value', fontsize=14)
ax.set_ylabel('Cube of Value', fontsize=14)


# Set size of tick labels.
ax.tick_params(axis='both', labelsize=14)

# Назначение диапазона для каждой оси.
ax.axis([0, 5000, 0, 5000**3])

# Show plot.
plt.show()