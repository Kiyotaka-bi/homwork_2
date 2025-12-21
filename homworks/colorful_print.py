from blessed import Terminal
from homworks.homwork1 import Person

term = Terminal()

person1 = Person("Аскат", "12.08.2005", "программист", True)
person2 = Person("Данияр", "23.04.2004", "дизайнер", False)

print(term.bold + "=== Люди ===" + term.normal)
person1.introduce()
person2.introduce()
print()

fruits = [
    "🍎 apple",
    "🍌 banana",
    "🍒 cherry",
    "🍇 grape",
    "🥭 mango",
    "🍊 orange",
    "🍑 peach"
]

colors = [
    term.red,
    term.yellow,
    term.magenta,
    term.darkgreen,
    term.darkorange,
    term.orange,
    term.pink
]

for fruit, color in zip(fruits, colors):
    print(color + fruit + term.normal)
