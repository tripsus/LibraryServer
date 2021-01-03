from flask import Flask
from flask import request

app = Flask(__name__)

# Libary data structure
file_handle = None
books_list = []

def add_book(title, author, genre):
    global books_list
    book = {
        'title': None,
        'author': None,
        'genre': None
    }
    book['title'] = title
    book['author'] = author
    book['genre'] = genre
    books_list.append(book)

@app.route('/books', methods=['POST','GET'])
def books():
    global books_list
    response = {
        "message": "There are no books in libarary. Please add books",
        "books": []
    }
    # import pdb; pdb.set_trace()
    print(request.form)
    if (request.environ['REQUEST_METHOD'] == 'POST'):
        add_book(request.form['title'],request.form['author'],request.form['genre'])
        response['books'] = books_list
        response['message'] = 'We have found some books in your library'

    else:
        if (len(books_list) > 0):
            response['books'] = books_list
            response['message'] = 'We have found some books in your library'

    return response

@app.route('/')
def hello():
    global file_handle
    file_handle = open("libraryDatabase", 'a');
    return "Welcome to our library! How can we help you today"

if __name__ == '__main__':
    app.run(debug=1)