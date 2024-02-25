import matplotlib.pyplot as plt

games = ['The last of us', 'The Witcher', 'Uncharted', 'FC24', 'Dota2']
hours = [20, 42, 18, 5, 6]

# Added some extra logic for diagram. The most and the least turned on games are filled red color
colors = ['#000000' if i != max(hours) and i != min(hours) else '#05210c' for i in hours]
print(colors)

plt.bar(games, hours, color=colors, edgecolor='green')
plt.title('Game addiction')
plt.xlabel('Game')
plt.ylabel('Hours')

plt.show()
