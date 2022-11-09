import matplotlib.pyplot as plt

# from matplotlib import pyplot as plt

# ========Hанесение и оформление отдельных точек функцией scatter()

# plt.style.use('seaborn') 
# fig, ax = plt.subplots() 
# ax.scatter(2, 4)

# plt.show()

# =======================

# plt.style.use('seaborn') 
# fig, ax = plt.subplots() 
# ax.scatter(2, 4)

# # Назначение заголовка диаграммы и меток осей. 
# ax.set_title("Square Numbers", fontsize=24) 
# ax.set_xlabel("Value", fontsize=14) 
# ax.set_ylabel("Square of Value", fontsize=14)

# # Назначение размера шрифта делений на осях.
# ax.tick_params(axis='both', which='major', labelsize=14)

# plt.show()

# =========Вывод серии точек функцией scatter()

# x_values = [1, 2, 3, 4, 5] 
# y_values = [1, 4, 9, 16, 25]

# plt.style.use('seaborn') 
# fig, ax = plt.subplots() 
# ax.scatter(x_values, y_values, s=100)

# # Назначение заголовка диаграммы и меток осей. 
# ax.set_title("Square Numbers", fontsize=24) 
# ax.set_xlabel("Value", fontsize=14) 
# ax.set_ylabel("Square of Value", fontsize=14)

# # Назначение размера шрифта делений на осях.
# ax.tick_params(axis='both', which='major', labelsize=14)

# plt.show()

# ============Автоматическое вычисление данных

x_values = list(range(1, 1001)) 
y_values = [x**2 for x in x_values]

plt.style.use('seaborn') 
fig, ax = plt.subplots()
# ax.scatter(x_values, y_values, s=10)

# Added color
# ax.scatter(x_values, y_values, c='red', s=10)

# ax.scatter(x_values, y_values, c=(0, 0.8, 0), s=10)


# Цветовые карты
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)

# Назначение заголовка диаграммы и меток осей. 
ax.set_title("Square Numbers", fontsize=24) 
ax.set_xlabel("Value", fontsize=14) 
ax.set_ylabel("Square of Value", fontsize=14)

# Назначение диапазона для каждой оси.
ax.axis([0, 1100, 0, 1100000])

# Автоматическое сохранение диаграмм
# plt.savefig('squares_plot.png', bbox_inches='tight')

plt.show()


