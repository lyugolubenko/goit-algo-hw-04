import pathlib

def get_cats_info(path):
    cats_list = []
    
    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                clean_line = line.strip()
                if not clean_line:
                    continue
                
                try:
                    cat_id, name, age = clean_line.split(",")
                    cat_dict = {
                        "id": cat_id,
                        "name": name,
                        "age": age
                    }
                    cats_list.append(cat_dict)
                    
                except ValueError:
                    print(f"Попередження: Некоректні дані у рядку: '{clean_line}'")
                    continue
                    
        return cats_list

    except FileNotFoundError:
        print(f"Помилка: Файл за шляхом '{path}' не знайдено.")
        return []
    except Exception as e:
        print(f"Виникла непередбачувана помилка: {e}")
        return []

# Перевірка роботи скрипту (Приклад використання)
if __name__ == "__main__":
    # 1. Знаходимо абсолютний шлях до папки, де лежить цей скрипт (task_2.py)
    current_dir = pathlib.Path(__file__).parent
    
    # 2. Об'єднуємо шлях до папки з назвою файлу cats_info.txt
    file_path = current_dir / "cats_info.txt"
    
    # 3. Передаємо цей динамічний шлях у функцію
    cats_info = get_cats_info(file_path)
    print(cats_info)