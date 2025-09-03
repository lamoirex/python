# Ввод значений

print("Для добавления данных в словарь напишите строку в формате 'ключ=значение', при необходимости остановить ввод введите слово 'стоп'")
data_dict = {}
def process_raw_data():
    s = ""
    while s.lower() != "стоп" and s.lower() != "stop":
        s = input()
        if "=" in s:
            a, b = s.split("=")
            data_dict[a] = b
        elif s.lower() != "стоп" and s.lower() != "stop":
            print("Неправильный формат ввода")

# Функция продам гараж

def apply_businness_rules(data_dict: dict) -> dict:
    if isinstance(data_dict, dict):
        if 'age' in data_dict:
            try:
                data_dict['age'] = int(data_dict['age'])
            except (ValueError, SyntaxError):
                print('Значение ключа "age" нельзя преобразовать')

        if 'city' in data_dict:
            data_dict.pop('city', None)

        data_dict['processed'] = 'True'

        return data_dict

    return "Входные данные не являются словарем"

# Приведение к верхнему регистру

def transform_data(data_dict):
    if isinstance(data_dict, dict):
        return {
            transform_data(key).upper() if isinstance(key, str) else key:
            transform_data(value) for key, value in data_dict.items()
        }
    elif isinstance(data_dict, str):
        return data_dict.upper()
    else:
        return data_dict
        
# Функция вывода

def format_output(data_dict):
    if not isinstance(data_dict, dict):
        raise TypeError('На вход ожидался словарь: dict')
    if not data_dict:
        return 'Словарь пуст'
    sorted_keys = sorted(data_dict.keys(),  key = lambda x: str(x))
    l = [f'{i}: {data_dict[i]}' for i in sorted_keys]
    return '\n'.join(l)

process_raw_data()
new_dict = data_dict
new_dict = apply_businness_rules(new_dict)
new_dict = transform_data(new_dict)
print(format_output(new_dict))
