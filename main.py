import os

def calculate_calories():
    # Получаем данные из переменных окружения или используем значения по умолчанию
    weight = float(os.getenv("WEIGHT", "70"))    # вес в кг
    height = float(os.getenv("HEIGHT", "175"))   # рост в см
    age = int(os.getenv("AGE", "25"))            # возраст в годах
    activity = float(os.getenv("ACTIVITY", "1.55")) # коэффициент активности
    goal = os.getenv("GOAL", "maintain")         # цель (maintain, lose, gain)

    # Базовый метаболизм (BMR) по формуле Миффлина-Сан Жеора
    bmr = (10 * weight) + (6.25 * height) - (5 * age) + 5
    
    # Суточная норма с учетом активности
    tdee = bmr * activity

    # Корректировка в зависимости от цели
    if goal == "lose":
        target_calories = tdee - 400
        goal_text = "Схуднення (дефіцит калорій)"
    elif goal == "gain":
        target_calories = tdee + 400
        goal_text = "Набір маси (профіцит калорій)"
    else:
        target_calories = tdee
        goal_text = "Підтримання ваги"

    # Расчет БЖВ (Белки, Жиры, Углеводы)
    protein_grams = (target_calories * 0.30) / 4
    fat_grams = (target_calories * 0.25) / 9
    carb_grams = (target_calories * 0.45) / 4

    print("=" * 45)
    print("   КАЛЬКУЛЯТОР КАЛОРІЙ ТА БЖВ (DOCKER)   ")
    print("=" * 45)
    print(f"Вхідні дані: Вага={weight}кг, Зріст={height}см, Вік={age}р.")
    print(f"Рівень активності (коеф.): {activity}")
    print(f"Ціль: {goal_text}")
    print("-" * 45)
    print(f"Базовий обмін речовин (BMR): {round(bmr, 2)} ккал")
    print(f"Цільова добова калорійність: {round(target_calories, 2)} ккал")
    print("-" * 45)
    print("Розрахунок БЖВ:")
    print(f"  • Білки:  {round(protein_grams, 1)} г")
    print(f"  • Жири:   {round(fat_grams, 1)} г")
    print(f"  • Вуглеводи: {round(carb_grams, 1)} г")
    print("=" * 45)

if name == "main":
    calculate_calories()
