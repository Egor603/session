from abc import ABC, abstractmethod


class AbstractProduct(ABC):
    @abstractmethod
    def get_description(self):
        pass


class Product(AbstractProduct):
    def __init__(self, name: str, quantity: int, price: float):
        self.name = name
        self.quantity = quantity
        self._price = price  # Приватное свойство
        self._validate_price()

    def _validate_price(self):
        """Проверка, что цена не отрицательная"""
        if self._price < 0:
            raise ValueError("Цена не может быть отрицательной")

    def get_price(self):
        return self._price

    def set_price(self, new_price: float):
        if new_price < 0:
            raise ValueError("Цена не может быть отрицательной")
        self._price = new_price

    def __add__(self, other):
        if isinstance(other, Product):
            new_quantity = self.quantity + other.quantity
            total_value = ((self._price * self.quantity) +
                           (other.get_price() * other.quantity))
            new_price = total_value / new_quantity if new_quantity > 0 else 0

            return Product(f"{self.name} + {other.name}",
                          new_quantity, new_price)
        else:
            raise TypeError("Можно складывать только объекты Product")

    def __lt__(self, other):
        if isinstance(other, Product):
            return self._price < other.get_price()
        else:
            raise TypeError("Можно сравнивать только объекты Product")

    def __gt__(self, other):
        if isinstance(other, Product):
            return self._price > other.get_price()
        else:
            raise TypeError("Можно сравнивать только объекты Product")

    def __str__(self):
        return (f"{self.name} (Количество: {self.quantity}, "
                f"Цена: {self._price})")

    def get_description(self):
        return (f"Товар: {self.name}, Количество: {self.quantity}, "
                f"Цена: {self._price}")


class Book(Product):
    def __init__(self, name: str, quantity: int, price: float, author: str):
        super().__init__(name, quantity, price)
        self.author = author

    def __str__(self):
        return (f"Книга: {self.name}, Автор: {self.author} "
                f"(Количество: {self.quantity}, Цена: {self.get_price()})")

    def get_description(self):
        return (f"Книга: {self.name}, Автор: {self.author}, "
                f"Количество: {self.quantity}, Цена: {self.get_price()}")


class Laptop(Product):
    def __init__(self, name: str, quantity: int, price: float, brand: str):
        super().__init__(name, quantity, price)
        self.brand = brand

    def __str__(self):
        return (f"Ноутбук: {self.name}, Бренд: {self.brand} "
                f"(Количество: {self.quantity}, Цена: {self.get_price()})")

    def get_description(self):
        return (f"Ноутбук: {self.name}, Бренд: {self.brand}, "
                f"Количество: {self.quantity}, Цена: {self.get_price()}")


try:
    try:
        invalid_book = Book("Ошибка наследования", 1, -100, "Автор")
        print(invalid_book)
    except ValueError as e:
        print("Ошибка значения:", e)

    book1 = Book("Война и мир", 10, 500, "Лев Толстой")
    book2 = Book("Преступление и наказание", 5, 450, "Федор Достоевский")
    laptop = Laptop("MacBook Pro", 3, 150000, "Apple")

    print("\nИнформация о товарах:")
    print(book1)
    print(book2)
    print(laptop)

    print("\nОписания товаров:")
    print(book1.get_description())
    print(book2.get_description())
    print(laptop.get_description())

    print("\nСложение товаров:")
    combined_product = book1 + book2
    print(f"Результат сложения: {combined_product}")

    print("\nСравнение цен:")
    print(f"book1 < book2: {book1 < book2}")
    print(f"book1 > book2: {book1 > book2}")
    print(f"book1 < laptop: {book1 < laptop}")

    print(f"\nТекущая цена книги: {book1.get_price()}")
    book1.set_price(550)
    print(f"Новая цена книги: {book1.get_price()}")

    try:
        book1.set_price(-100)
    except ValueError as e:
        print(f"Ошибка при установке цены: {e}")

except Exception as e:
    print(f"Произошла ошибка: {e}")
