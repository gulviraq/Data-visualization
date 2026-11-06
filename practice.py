
import matplotlib.pyplot as plt


days = [1, 2, 3, 4, 5, 6, 7]
temperature = [12, 15, 14, 17, 19, 18, 21]

plt.figure(figsize=(8, 5))
plt.plot(days, temperature, color='blue', marker='o')

plt.title('Температура воздуха за неделю')
plt.xlabel('День')
plt.ylabel('Температура, °C')
plt.grid(True)

plt.show()


subjects = ['Математика', 'Физика', 'Информатика', 'Английский язык']
grades = [4.1, 3.8, 4.7, 4.3]

colors = ['red', 'blue', 'green', 'orange']

plt.figure(figsize=(9, 5))
plt.bar(subjects, grades, color=colors)

plt.title('Средняя успеваемость студентов')
plt.xlabel('Предметы')
plt.ylabel('Средняя оценка')
plt.xticks(rotation=15)

plt.show()

print("Задание 2:")
print("Самая высокая оценка по информатике: 4.7")


categories = ['Продукты', 'Транспорт', 'Коммунальные услуги', 'Связь', 'Прочее']
expenses = [120000, 30000, 45000, 15000, 40000]

plt.figure(figsize=(8, 6))
plt.pie(
    expenses,
    labels=categories,
    autopct='%1.1f%%'
)

plt.title('Структура ежемесячных расходов семьи')

plt.show()

print("Задание 3:")
print("Наибольшие расходы — продукты: 120000 (48%)")


results = [
    45, 52, 55, 58, 60, 62, 65, 67, 70, 70,
    72, 74, 75, 78, 80, 82, 85, 88, 90, 95
]

plt.figure(figsize=(8, 5))
plt.hist(
    results,
    bins=5,
    color='orange',
    edgecolor='black'
)

plt.title('Распределение результатов тестирования')
plt.xlabel('Количество баллов')
plt.ylabel('Количество студентов')

plt.show()

print("Задание 4:")
print("Больше всего результатов находится в диапазоне 65–75 баллов")


hours = [1, 2, 2, 3, 4, 5, 5, 6, 7, 8]
scores = [48, 52, 55, 60, 65, 70, 73, 78, 84, 90]

plt.figure(figsize=(8, 5))
plt.scatter(hours, scores, color='blue', marker='o')

plt.title('Зависимость результата экзамена от времени подготовки')
plt.xlabel('Количество часов подготовки')
plt.ylabel('Результат экзамена')
plt.grid(True)

plt.show()

print("Задание 5:")
print("1. Наблюдается положительная связь.")
print("2. Да, при увеличении времени подготовки результат повышается.")
print("3. Нет, подготовка не является единственной причиной высокого результата.")

print("\nВсе 5 заданий выполнены!")
