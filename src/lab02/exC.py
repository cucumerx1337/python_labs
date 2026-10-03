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