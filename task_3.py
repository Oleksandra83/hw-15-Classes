from typing import Union

class TVController:
    """
    Простий контролер телевізора. Дозволяє перемикати канали, перевіряти їх існування та отримувати поточний канал.
    """

    def __init__(self, channels: list):
        self.channels = channels
        self.current_channel_index = 0  # стартовий канал — перший (індекс 0)

    def first_channel(self) -> str:
        self.current_channel_index = 0
        return self.channels[0]

    def last_channel(self) -> str:
        self.current_channel_index = len(self.channels) - 1
        return self.channels[-1]

    def turn_channel(self, n: int) -> str:
        if 1 <= n <= len(self.channels):
            self.current_channel_index = n - 1
            return self.channels[self.current_channel_index]
        raise IndexError(f"Канал №{n} не існує.")

    def next_channel(self) -> str:
        self.current_channel_index = (self.current_channel_index + 1) % len(self.channels)
        return self.channels[self.current_channel_index]

    def previous_channel(self) -> str:
        self.current_channel_index = (self.current_channel_index - 1) % len(self.channels)
        return self.channels[self.current_channel_index]

    def current_channel(self) -> str:
        return self.channels[self.current_channel_index]

    def exists(self, query: Union[int, str]) -> str:
        if isinstance(query, int):
            return "Yes" if 1 <= query <= len(self.channels) else "No"
        if isinstance(query, str):
            return "Yes" if query in self.channels else "No"
        return "No"

CHANNELS = ["1+1", "СТБ", "Новий Канал", "ICTV", "Україна"]
controller = TVController(CHANNELS)

print("--- Тестування TVController ---")

# Тест: first_channel()
print(f"Перший канал: {controller.first_channel()} (Очікується: 1+1) -> {controller.current_channel()}")
assert controller.first_channel() == "1+1"
assert controller.current_channel() == "1+1"

# Тест: last_channel()
print(f"Останній канал: {controller.last_channel()} (Очікується: Україна) -> {controller.current_channel()}")
assert controller.last_channel() == "Україна"
assert controller.current_channel() == "Україна"

# Тест: turn_channel(N)
print(f"Увімкнути канал 1: {controller.turn_channel(1)} (Очікується: 1+1) -> {controller.current_channel()}")
assert controller.turn_channel(1) == "1+1"
assert controller.current_channel() == "1+1"

# Тест: next_channel()
print(f"Наступний канал: {controller.next_channel()} (Очікується: СТБ) -> {controller.current_channel()}")
assert controller.next_channel() == "СТБ"
assert controller.current_channel() == "СТБ"

# Тест: previous_channel()
print(f"Попередній канал: {controller.previous_channel()} (Очікується: 1+1) -> {controller.current_channel()}")
assert controller.previous_channel() == "1+1"
assert controller.current_channel() == "1+1"

# Тест: current_channel()
print(f"Поточний канал: {controller.current_channel()} (Очікується: 1+1)")
assert controller.current_channel() == "1+1"

# Тест: exists(N) - спробуємо канал, якого немає (наприклад, 6, якщо каналів 5)
print(f"Канал 6 існує? {controller.exists(6)} (Очікується: No)")
assert controller.exists(6) == "No"

# Тест: exists('name')
print(f"Канал 'СТБ' існує? {controller.exists('СТБ')} (Очікується: Yes)")
assert controller.exists("СТБ") == "Yes"

# Додатковий тест: існування каналу, якого немає за назвою
print(f"Канал 'Футбол' існує? {controller.exists('Футбол')} (Очікується: No)")
assert controller.exists("Футбол") == "No"

print("\nВсі тести пройшли успішно!")

