class Book:
    book_count = 0

    def __init__(self,title,author,genre,publication_year,price,availability=True):
        self.title = title
        self.author = author
        self.genre = genre
        self.publication_year = publication_year
        self.__price = price
        self.__availability = availability

        Book.book_count += 1
    def get_price(self):
        return f"{self.__price}$"
    def set_price(self,new_price):
        if new_price < 0:
            raise ValueError("Bunday qilishni iloji yoq")
        self.__price = new_price
    def is_available(self):
        return self.__availability
    def set_available(self,new):
        self.__availability = new
    def desplay_details(self):
        return (
            f"Kitob nomi: {self.title}, "
            f"Muallif: {self.author}, "
            f"Janr: {self.genre}, "
            f"Nashr yili: {self.publication_year}, "
            f"Narxi: {self.__price}$, "
            f"Mavjudligi: {'Ha' if self.__availability else "Yo\'q"}"
        )
    
    def discount_percentage(self,percent):
        if self.__availability :
            self.__price -= self.__price * (percent / 100 )
        else :
            return f"bu kitobimiz hozircha yoq"
    def mark_univailable(self):
        self.__availability = False
        return self.__availability
    
    def get_book_count (self):
        return Book.book_count
    
kitob = Book('qoch','Men','drama',2024,12.99)
kitob2 = Book('qoch','Men','drama',2024,12.99)
print(kitob.desplay_details())
print(kitob.get_book_count())