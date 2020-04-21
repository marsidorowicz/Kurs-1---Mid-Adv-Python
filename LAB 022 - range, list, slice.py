color = ["red", "orange", "green", "violet", "blue", "yellow"]
item = []
def Colors(n, list):
    for i in range(0, n):
        item.append(list[i])
    new_list = item
    return  new_list
n = 5
new_list = Colors(n, color)
print(new_list)

definition = 'Korporacja (z łac. corpo – ciało, ratus – szczur; pol. ciało szczura) – organizacja, która pod przykrywką prowadzenia biznesu włada dzisiejszym światem. Wydawać się może utopijnym miejscem realizacji pasji zawodowych. W rzeczywistości jednak nie jest wcale tak kolorowo. Korporacja służy do wyzyskiwania człowieka w imię postępu. Rządzi w niej prawo dżungli. '

print(definition[definition.index('(') + 1:definition.index(')')])


def get_list_of_colors(colors, n):
    return colors[:n]


colors = ["red", "orange", "green", "violet", "blue", "yellow"]

for i in range(1, len(colors) + 1):
    print(get_list_of_colors(colors, i))