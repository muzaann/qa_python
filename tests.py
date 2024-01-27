from main import BooksCollector
import pytest


# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()


    def test_set_book_genre_by_real_book_name_true(self):
        collector = BooksCollector()
        collector.add_new_book('Десять негритят')
        collector.set_book_genre('Десять негритят', 'Детектив')
        assert ('Десять негритят': 'Детектив') in collector.books_genre

    def test_set_book_genre_if_genre_not_in_genre_list_false(self):
        collector = BooksCollector()
        collector.add_new_book('Укрытие')
        collector.set_book_genre('Укрытие', 'Постапокалипсис')
        assert ('Укрытие': 'Постапокалипсис') not in collector.books_genre

    def test_get_book_genre_by_real_book_name_true(self):
        collector = BooksCollector()
        collector.add_new_book('Десять негритят')
        collector.set_book_genre('Десять негритят', 'Детектив')
        assert collector.get_book_genre('Десят негритят') == 'Детектив'

    def test_get_book_with_specific_genre_exicting_genre_added_book_true(self):
        collector = BooksCollector()
        collector.add_new_book('Десять негритят')
        collector.set_book_genre('Десять негритят', 'Детектив')
        assert collector.get_books_with_specific_genre('Детектив') == books_with_specific_genre

    def test_get_book_with_specific_genre_non_existent_genre_added_book_false(self):
        collector = BooksCollector()
        collector.add_new_book('Десять негритят')
        collector.set_book_genre('Десять негритят', 'Детектив')
        assert collector.get_books_with_specific_genre('Фэнтези') == []

    def test_get_books_genre_existing_book_and_genre_true(self):
        collector = BooksCollector()
        collector.add_new_book('Десять негритят')
        collector.set_book_genre('Десять негритят', 'Детектив')
        assert ('Десять негритят':'Детектив') in collector.books_genre

    def test_get_books_for_children_added_valid_book_true(self):
        collector = BooksCollector()
        collector.add_new_book('Гарри Поттер и философский камень')
        collector.set_book_genre('Гарри Поттер и философский камень','Фантастика')
        assert collector.get_books_for_children() == ['Гарри Поттер и философский камень']

    def test_get_books_for_children_added_invalid_book_false(self):
        collector = BooksCollector()
        collector.add_new_book('Десять негритят')
        collector.set_book_genre('Десять негритят', 'Детектив')
        assert collector.get_books_for_children() != ['Десять негритят']

    def test_add_book_in_favorites_existing_book_true(self):
        collector = BooksCollector()
        collector.add_new_book('Десять негритят')
        collector.add_book_in_favorites('Десять негритят')
        assert 'Десять негритят' in collector.favorites


    def test_add_book_in_favorites_non_existed_book_false(self):
        collector = BooksCollector()
        collector.add_book_in_favorites('Десять негритят')
        assert 'Десять негритят' not in collector.favorites


    def test_add_book_in_favorites_already_existing_book_false(self):
        collector = BooksCollector()
        collector.add_new_book('Десять негритят')
        collector.add_book_in_favorites('Десять негритят')
        collector.add_book_in_favorites('Десять негритят')
        assert len(collector.favorites) == 1

    def test_delete_book_from_favorites_existing_book_true(self):
        collector = BooksCollector()
        collector.add_new_book('Десять негритят')
        collector.add_book_in_favorites('Десять негритят')
        collector.delete_book_from_favorites('Десять негритят')
        assert 'Десять негритят' not in collector.favorites


    def test_get_list_of_favotites_books_when_books_in_list(self):
        collector = BooksCollector()
        collector.add_new_book('Десять негритят')
        collector.add_book_in_favorites('Десять негритят')
        assert collector.favorites == ['Десять негритят']