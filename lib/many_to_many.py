class Author:
    def __init__(self, name):
        self.name = name
    
    def contracts(self):
        contracts = [contract for contract in Contract.all if contract.author == self]
        return contracts

    def books(self):
        books = [contract.book for contract in Contract.all if contract.author == self]
        return books
    
    def sign_contract(self, book, date, royalties):
        return Contract(self, book, date, royalties)
    
    def total_royalties(self):
        total_royalties = [contract.royalties for contract in Contract.all if contract.author == self]
        return sum(total_royalties)


class Book:
    def __init__(self, title):
        self.title = title

    def contracts(self):
        contracts = [contract for contract in Contract.all if contract.book == self]
        return contracts

    def authors(self):
        authors = [contract.author for contract in Contract.all if contract.book == self]
        return authors


class Contract:
    all = []

    def __init__(self, author, book, date, royalties):
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all.append(self)
    
    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, author):
        if not isinstance(author, Author):
            raise TypeError("Author must be Author object")
        self._author = author
    
    @property
    def book(self):
        return self._book
    
    @book.setter
    def book(self, book):
        if not isinstance(book, Book):
            raise TypeError("Book must be Book object")
        self._book = book
    
    @property
    def date(self):
        return self._date
    
    @date.setter
    def date(self, date):
        if not isinstance(date, str):
            raise TypeError("Date must be String")
        self._date = date
    
    @property
    def royalties(self):
        return self._royalties
    
    @royalties.setter
    def royalties(self, royalties):
        if not isinstance(royalties, int):
            raise TypeError("royalties must be Integer")
        self._royalties = royalties

    def contracts_by_date(date):
        sorted_contracts_by_date = [contract for contract in Contract.all if contract.date == date]
        return sorted_contracts_by_date