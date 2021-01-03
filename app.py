from flask import Flask
from flask import request

app = Flask(__name__)

# Libary data structure
file_handle = None
books_list = []


@app.route('/books')
def books():
    response = {
        "message": "There are no books in libarary. Please add books",
        "books": []
    }
    # import pdb; pdb.set_trace()
    # print(request.environ['REQUEST_METHOD'])
    return response

@app.route('/')
def hello():
    global file_handle
    file_handle = open("libraryDatabase", 'a');
    return "Welcome to our library! How can we help you today"

if __name__ == '__main__':
    app.run()