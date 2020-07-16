# -*- coding: utf-8 -*-
import csv
import json

# # получаем данные пользователя из json файла и возвращаем словарь с данными пользователя
def get_user_data():
    with open('users.json', 'r') as f:
        users = json.loads(f.read()) #лист со словарями внутри
        user_data_list = []
        for user_data in users:
            user_name = user_data.get('name')
            user_gender = user_data.get('gender')
            user_address = user_data.get('address')
            user_dict = {'name': user_name,'gender': user_gender,'address': user_address}
            user_data_list.append(user_dict)
        return user_data_list
    
#получаем последовательно элементы списка с пользователями в виде dict
def user_generator():
    user_data_list = get_user_data()
    user_data_iter = iter(user_data_list)
    for user_generator in user_data_iter:
        yield user_generator

# получаем данные киниги из csv файла и возвращаем массив со словарями с данными книг
def get_book_data():
    with open('books_new.csv', 'r') as book_all:
        book_fields = ['Title', 'Author', 'Genre', 'Height', 'Publisher']
        book_csv_reader = csv.DictReader(book_all, book_fields, delimiter=',')
        next(book_csv_reader)
        books_data_list = []
        for book_row in book_csv_reader:
            title = book_row['Title']
            author = book_row['Author']
            height = book_row['Height']
            books = {'title': title, 'author': author, 'height': height}
            books_data_list.append(books)
        return books_data_list

#получаем последовательно элементы списка с книгами в виде dict
def book_generator():
    books_data_list = get_book_data()
    books_data_iter = iter(books_data_list)
    for book_generator in books_data_iter:
        yield book_generator

#собираем данные о пользователе и следующей книге в множество словарей и записываем в json
def create_data_for_json():
    data_example = []
    user_data = user_generator()
    book_data = book_generator()
    for user in user_data:
        user = dict(user)
        try:
            user['books'] = dict(next(book_data))
        except StopIteration:
            empty_list = list()
            user['books'] = empty_list
        data_example.append(user)
    with open('data.json', 'a') as finish_data:
        data_example = json.dumps(data_example, indent=4)
        finish_data.write(data_example)

if __name__ == '__main__':
    create_data_for_json()
