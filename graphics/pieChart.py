import matplotlib.pyplot as plt

games = ['The last of us', 'The Witcher', 'Uncharted', 'FC24', 'Dota2']
hours = [20, 42, 18, 5, 6]

# autopct - numbers format in the chart
plt.pie(hours, labels=games, autopct='%1.f%%')
plt.title('Pie Chart')
plt.axis('equal')
plt.show()
