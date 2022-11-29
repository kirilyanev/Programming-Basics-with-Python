searched_book = input()
checked_book = input()
book_cnt = 0

while checked_book != "No More Books":
    book_cnt += 1
    if checked_book == searched_book:
        break
    checked_book = input()

if checked_book == searched_book:
    print(f"You checked {book_cnt - 1} books and found it.")
else:
    print(f"The book you search is not here!")
    print(f"You checked {book_cnt} books.")
