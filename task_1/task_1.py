from pathlib import Path

def total_salary(path):
    # Використовуємо Path замість os.path за рекомендацією ментора
    path_obj = Path(path)
    
    total = 0.0  # Використовуємо float для підтримки копійок
    count = 0
    
    try:
        with open(path_obj, "r", encoding="utf-8") as file:
            for line in file:
                clean_line = line.strip()
                if not clean_line:
                    continue
                
                try:
                    name, salary_str = clean_line.split(",")
                    # Перетворюємо на float, щоб уникнути потенційних помилок
                    total += float(salary_str)
                    count += 1
                except ValueError:
                    print(f"Попередження: Некоректний формат у рядку: '{clean_line}'")
                    continue
                    
        if count == 0:
            return 0.0, 0.0
            
        average = total / count
        return total, average

    except FileNotFoundError:
        print(f"Помилка: Файл за шляхом '{path_obj}' не знайдено.")
        return 0.0, 0.0
    except Exception as e:
        print(f"Виникла непередбачувана помилка: {e}")
        return 0.0, 0.0

# Перевірка роботи скрипту
if __name__ == "__main__":
    # Визначаємо шлях до файлу за допомогою pathlib
    script_dir = Path(__file__).parent
    salary_file = script_dir / "salary.txt"
    
    total, average = total_salary(salary_file)
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")