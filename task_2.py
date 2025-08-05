class Dog:
    """
    Represents a dog and allows conversion of its age to human years.
    """
    age_factor = 7  # Conversion factor: dog years → human years

    def __init__(self, dog_age: int):
        """
        Initialize the dog's age.

        :param dog_age: Age of the dog in dog years (must be a positive integer).
        """
        if not isinstance(dog_age, int) or dog_age < 0:
            raise ValueError("Dog's age must be a non-negative integer.")
        self.dog_age = dog_age

    def human_age(self) -> int:
        """
        Converts dog's age to human equivalent.

        :return: Age in human years.
        """
        return self.dog_age * self.age_factor

# --- Приклад використання ---
print("--- Створення об'єктів Dog та обчислення людського віку ---")

# Створюємо першого собаку віком 3 роки
dog1 = Dog(3)
print(f"Собаці {dog1.dog_age} роки. Її вік у людських роках: {dog1.human_age()} років.")

# Створюємо другого собаку віком 7 років
dog2 = Dog(7)
print(f"Собаці {dog2.dog_age} років. Її вік у людських роках: {dog2.human_age()} років.")

# Створюємо другого собаку віком 7 років
dog3 = Dog(0)
print(f"Собаці {dog3.dog_age} років. Її вік у людських роках: {dog3.human_age()} років.")

# --- Тест на помилку --- #
try:
    bad_dog = Dog(-5)
except ValueError as e:
    print(f"❌ Помилка: {e}")

# Демонстрація зміни age_factor (впливає на всі майбутні об'єкти або на перерахунок)
print("\n--- Зміна age_factor класу ---")
Dog.age_factor = 6 # Змінюємо коефіцієнт віку для всіх собак

# Тепер перерахуємо вік першого собаки з новим коефіцієнтом
print(f"Після зміни age_factor на 6:")
print(f"Собаці {dog1.dog_age} роки. Її вік у людських роках: {dog1.human_age()} років.")
print(f"Собаці {dog2.dog_age} років. Її вік у людських роках: {dog2.human_age()} років.")
print(f"Собаці {dog3.dog_age} років. Її вік у людських роках: {dog3.human_age()} років.")
