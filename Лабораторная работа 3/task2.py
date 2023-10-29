# TODO Напишите функцию find_common_participants
def find_common_participants(string1, string2, delimiter=","):
    first_group = set(string1.split(delimiter))
    second_group = set(string2.split(delimiter))
    return sorted(first_group.intersection(second_group))

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
print(find_common_participants(participants_first_group, participants_second_group))