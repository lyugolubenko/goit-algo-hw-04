import os

def total_salary(path):
    total = 0
    count = 0
    
    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                clean_line = line.strip()
                if not clean_line:
                    continue
                
                try:
                    name, salary_str = clean_line.split(",")
                    total += int(salary_str)
                    count += 1
                except ValueError:
                    print(f"Попередження: Некоректний формат у рядку: '{clean_line}'")
                    continue
                    
        if count == 0:
            return 0, 0
            
        average = total / count
        return total, average

    except FileNotFoundError:
        print(f"Помилка: Файл за шляхом '{path}' не знайдено.")
        return 0, 0
    except Exception as e:
        print(f"Виникла непередбачувана помилка: {e}")
        return 0, 0

# Перевірка роботи скрипту
if __name__ == "__main__":
    # Абсолютний шлях до файлу відносно розташування скрипту
    script_dir = os.path.dirname(os.path.abspath(__file__))
    salary_file = os.path.join(script_dir, "salary.txt")
    total, average = total_salary(salary_file)
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {int(average)}")