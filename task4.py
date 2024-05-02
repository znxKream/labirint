#задача 1
empty_tuple = ()
tuple_with_one_item = (1,)
tuple_ = (1, 2, "str")
print("Содержимое переменной empty_tuple:", empty_tuple,
type(empty_tuple))
print("Содержимое переменной tuple_with_one_item:",
tuple_with_one_item, type(tuple_with_one_item))
print("Содержимое переменной tuple_:", tuple_, type(tuple_))
list_ = [] # Пустой список
chars_list = ["a", "b", "c"]
print("Содержимое переменной list_:", list_, type(list_))
print("Содержимое переменной chars_list:", chars_list,
type(chars_list))
empty_string = ""
str_ = "test"
print("Содержимое переменной empty_string:", empty_string,
type(empty_string))
print("Содержимое переменной str_:", str_, type(str_))
empty_set = set()
set_ = {3, 2, 1, 1}

print("Содержимое переменной empty_set:", empty_set,
type(empty_set))
print("Содержимое переменной set_:", set_, type(set_))
empty_dict = {} # Пустой словарь
dict_ = { "Имя": "Ваше имя","Фамилия": "Ваша фамилия","Возраст": 18,"Возраст": 20,}
print("Содержимое переменной empty_dict:", empty_dict,
type(empty_dict))
print("Содержимое переменной dict_:", dict_, type(dict_))

#задача 2
list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл"]
last_player = list_players[-1]
reestr = {"Первый участник": list_players[0]}
print("Последний участник:", last_player)
print("Первый участник:", reestr["Первый участник"])