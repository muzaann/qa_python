test_add_new_book_different_len_of_name - параметиризированный тест, проверяющий позитивные тест-данные с учетом граничных значений
test_set_book_genre_by_real_book_name_true - тест, проверяющий добавление жанра из списка жанров, добавленной книге
test_set_book_genre_if_genre_not_in_genre_list_fals - тест, проверяющий что не доавляется жанр, если его нет в списке жанров
test_get_book_with_specific_genre_exicting_genre_added_book_true - тест, проверяющий вывод названий книг определенного жанра
test_get_book_with_specific_genre_non_existent_genre_added_book_false - тест, проверющий что не выводятся названия книг если указать несуществующий жанр
test_get_books_genre_existing_book_and_genre_true - тест, проверяющий вывод словаря при существующих названии и жанре
test_get_books_for_children_added_valid_book_true - тест, проверяющий что в список детских книмг выводятся книга допустимого жанра
test_get_books_for_children_added_invalid_book_false - тест, проверяющий что в список детских книг не попадет книга недопустимого жанра
test_add_book_in_favorites_existing_book_true - тест, проверяющий добавление книги из словаря books_genre в избранное
test_add_book_in_favorites_non_existed_book_false - тест, проверяющий что невозможно добавление в избранное книги, которой нет в словаре books_genre
test_add_book_in_favorites_already_existing_book_false - тест, проверяяющий что книга не добавляется в избранное повторно
test_delete_book_from_favorites_existing_book_true - тест, проверяющий удаление книги из избранного
test_get_list_of_favotites_books_when_books_in_list - тест, проверяющий вывод книг в избранном
