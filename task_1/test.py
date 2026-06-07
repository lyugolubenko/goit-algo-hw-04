import os
from task_1 import total_salary

def test_total_salary():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    salary_file = os.path.join(script_dir, "salary.txt")
    try:
        total, average = total_salary(salary_file)
        assert total == 6000, f"Очікувалось 6000, отримано {total}"
        assert average == 2000, f"Очікувалось 2000, отримано {average}"
        print("✓ Тест пройшов успішно!")
        print(f"  Загальна сума: {total}")
        print(f"  Середня зарплата: {average}")
    except Exception as e:
        print(f"Помилка: {e}")

if __name__ == "__main__":
    test_total_salary()
