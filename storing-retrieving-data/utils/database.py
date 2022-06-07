books_file = 'books.txt'

def create_book_file():
    """Makes sure file exists"""
    with open(books_file,'w'):
        pass

def add_book(name, author):
    with open('books.txt','a') as file:
        file.write(f'{name},{author},No\n')



def get_all_books():
    with open(books_file, 'r') as file:
        lines = [line.strip().split(',') for line in file.readlines()]      #lines = [[name,author,read],[name,author,read]] without \n

    books = [                                                                  #books = [[name,author,read],[name,author,read]]
        {'name': line[0], 'author': line[1], 'read': line[2]}
        for line in lines
    ]

    return books


def mark_book_as_read(name):
    books = get_all_books()
    for book in books:
        if book['name'] == name:
            book['read'] = 'Yes'

    _save_all_books(books)



def _save_all_books(books):
    with open('books.txt','w') as file:
        for book in books:
            file.write(f"{book['name']},{book['author']},{book['read']}\n")


def delete_book(name):  # Using list comprehension to add each book to new list if book['name'] != name
    books = get_all_books()
    books = [book for book in books if book['name'] != name]

    _save_all_books(books)
