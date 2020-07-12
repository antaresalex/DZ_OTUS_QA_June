# -*- coding: utf-8 -*-
import csv
import json
import random

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

# собираем данные о пользователе и книгах в множество словарей и записываем в json
def create_data_for_json():
    user_data = get_user_data()
    book_data = get_book_data()
    data_example = []
    for user in user_data:
        user = dict(user)
        user['books'] = random.choices(book_data, k=3)
        data_example.append(user)
    with open('data.json', 'a') as finish_data:
        data_example = json.dumps(data_example, indent=4)
        finish_data.write(data_example)

if __name__ == '__main__':
    create_data_for_json()
