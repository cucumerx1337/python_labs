# Лаба 2

## Задание А - массивы и матрицы

Набор функций для работы со списками и матрицами. Все функции чистые: ничего не читают с клавиатуры, возвращают результат через `return`, а на некорректные данные отвечают исключениями.

### find_min_max()

Проходит по списку один раз и запоминает наименьший и наибольший элементы. Возвращает кортеж `(min, max)`. Для пустого списка выбрасывает `ValueError`.

```python
def find_min_max(values):
    if not values:
        raise ValueError("empty list")

    low = values[0]
    high = values[0]
    for num in values:
        if num < low:
            low = num
        if num > high:
            high = num
    return (low, high)


print(find_min_max([3, -1, 5, 5, 0]))  # (-1, 5)
print(find_min_max([42]))  # (42, 42)
```

### get_unique_sorted()

Сначала собирает в новый список только уникальные элементы (вложенным циклом проверяется, был ли такой элемент), затем сортирует результат пузырьком по возрастанию. Встроенные `set` и `sorted` не используются.

```python
def get_unique_sorted(items):
    unique = []
    for item in items:
        found = False
        for u in unique:
            if u == item:
                found = True
        if not found:
            unique.append(item)

    n = len(unique)
    for i in range(n):
        for j in range(n - 1):
            if unique[j] > unique[j + 1]:
                temp = unique[j]
                unique[j] = unique[j + 1]
                unique[j + 1] = temp
    return unique


print(get_unique_sorted([3, 1, 2, 1, 3]))  # [1, 2, 3]
print(get_unique_sorted([]))  # []
```

### merge_elements()

Склеивает список строк (списков или кортежей) в один плоский список. Если среди строк попался элемент другого типа, выбрасывает `TypeError`.

```python
def merge_elements(matrix):
    result = []
    for row in matrix:
        if not isinstance(row, (list, tuple)):
            raise TypeError("not a list or tuple")
        for element in row:
            result.append(element)
    return result


print(merge_elements([[1, 2], (3, 4, 5)]))  # [1, 2, 3, 4, 5]
```

![Вывод exA](images/lab02/exA.png)

### transpose()

Транспонирует матрицу: строки становятся столбцами. Пустая матрица даёт `[]`. Если длины строк различаются («рваная» матрица), выбрасывает `ValueError`.

```python
def transpose(mat):
    if len(mat) > 0:
        first_len = len(mat[0])
        for row in mat:
            if len(row) != first_len:
                raise ValueError("рваная матрица")
    if len(mat) == 0:
        return []
    rows = len(mat)
    cols = len(mat[0])
    result = []
    for j in range(cols):
        new_row = []
        for i in range(rows):
            new_row.append(mat[i][j])
        result.append(new_row)
    return result


print(transpose([[1, 2, 3]]))  # [[1], [2], [3]]
print(transpose([[1], [2], [3]]))  # [[1, 2, 3]]
print(transpose([[1, 2], [3, 4]]))  # [[1, 3], [2, 4]]
print(transpose([]))  # []
```

### row_sums()

Считает сумму элементов в каждой строке матрицы. Для «рваной» матрицы выбрасывает `ValueError`.

```python
def row_sums(mat):
    if len(mat) > 0:
        first_len = len(mat[0])
        for row in mat:
            if len(row) != first_len:
                raise ValueError("рваная матрица")
    result = []
    for row in mat:
        s = 0
        for x in row:
            s = s + x
        result.append(s)
    return result


print(row_sums([[1, 2, 3], [4, 5, 6]]))  # [6, 15]
print(row_sums([[-1, 1], [10, -10]]))  # [0, 0]
print(row_sums([[0, 0], [0, 0]]))  # [0, 0]
```

### col_sums()

Считает сумму элементов в каждом столбце матрицы. Пустая матрица даёт `[]`, для «рваной» матрицы выбрасывается `ValueError`.

```python
def col_sums(mat):
    if len(mat) > 0:
        first_len = len(mat[0])
        for row in mat:
            if len(row) != first_len:
                raise ValueError("рваная матрица")
    if len(mat) == 0:
        return []
    rows = len(mat)
    cols = len(mat[0])
    result = []
    for j in range(cols):
        s = 0
        for i in range(rows):
            s = s + mat[i][j]
        result.append(s)
    return result


print(col_sums([[1, 2, 3], [4, 5, 6]]))  # [5, 7, 9]
print(col_sums([[-1, 1], [10, -10]]))  # [9, -9]
print(col_sums([[0, 0], [0, 0]]))  # [0, 0]
```

![Вывод exG](images/lab02/exG.png)

## Задание B - кортежи

### format_record()

Принимает запись студента в виде кортежа `(ФИО, группа, GPA)` и возвращает аккуратно оформленную строку: фамилия с заглавной буквы, инициалы, группа и GPA с двумя знаками после запятой.

Проверки входных данных:

- запись должна быть кортежем из трёх элементов (`TypeError` / `ValueError`);
- ФИО и группа должны быть строками, GPA - числом (`int` или `float`);
- GPA должен быть в диапазоне от 0.0 до 5.0;
- в ФИО должно быть 2 или 3 слова, группа не может быть пустой.

Лишние пробелы в ФИО и регистр букв исправляются автоматически.

```python
def format_record(rec):
    if type(rec) is not tuple:
        raise TypeError("Запись должна быть кортежем")
    if len(rec) != 3:
        raise ValueError("В кортеже должно быть 3 элемента")

    fio = rec[0]
    group = rec[1]
    gpa = rec[2]

    if type(fio) is not str:
        raise TypeError("Имя должно быть строкой")
    if type(group) is not str:
        raise TypeError("Группа должна быть строкой")
    if type(gpa) is not float and type(gpa) is not int:
        raise TypeError("Оценка должна быть вещественным числом")
    if gpa < 0.0 or gpa > 5.0:
        raise ValueError("GPA должен быть от 0.0 до 5.0")

    words = fio.strip().split()
    if len(words) != 2 and len(words) != 3:
        raise ValueError("Введено не полное ФИО")
    if len(group.strip()) == 0:
        raise ValueError("Группа не может быть пустой")

    fam = words[0].capitalize()
    name_letter = words[1][0].upper()

    if len(words) == 3:
        otch_letter = words[2][0].upper()
        head = fam + " " + name_letter + "." + otch_letter + "."
    else:
        head = fam + " " + name_letter + "."

    return head + ", гр. " + group + ", GPA " + "{:.2f}".format(gpa)


print(format_record(("Иванов Иван Иванович", "BIVT-25", 4.6)))
# Иванов И.И., гр. BIVT-25, GPA 4.60

print(format_record(("Петров Пётр", "IKBO-12", 5.0)))
# Петров П., гр. IKBO-12, GPA 5.00

print(format_record(("Петров Пётр Петрович", "IKBO-12", 5.0)))
# Петров П.П., гр. IKBO-12, GPA 5.00

print(format_record(("  сидорова  анна   сергеевна ", "ABB-01", 3.999)))
# Сидорова А.С., гр. ABB-01, GPA 4.00
```

![Вывод exR](images/lab02/exR.png)
