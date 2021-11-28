The Small Libre

This project is Library web application. You are able to post books by their title and author and give them a rating, 
update the rating, search for a book. You are also able to delete a book. This was one of the exercises from the 
Udacity FullStack Nano Degree course. This exercise was used in strengthing my skill in structuring and implementing well 
formatted API endpoints. I will continue working on this API and will be hoping I can collaborate with
other developers and build something out of this

Getting Started
Developers using this project should have python3, pip and node already installed.


Backend
From the backend folder run pip install requirements.txt. All packages are included in the requirements file.
To run the application run the following commands:

export FLASK_APP=flaskr
export FLASK_ENV=development
flask run


Frontend
From the frontend folder, run the following commands to start the client:

npm install // only once to install dependencies
npm start 
By default, the frontend will run on localhost:3000.


Tests
In order to run tests navigate to the backend folder and run the following commands:

dropdb bookshelf_test
createdb bookshelf_test
psql bookshelf_test < books.psql
python test_flaskr.py


API REFERENCE

Just Getting Started? 
The Library API is organized around REST. The API has predictable resource-oriented URLs,
accepts form-encoded request bodies, returns JSON-encoded responses, and uses standard
HTTP response codes, authentication, and verbs.

### BASE URL
http://127.0.0.1:5000/. At present this app is only run locallly and not hosted as a base
URL from the backend and runs a proxy on the frontend.

### AUTHENTICATION
This version does not require authentification or API keys.

### ERRORS
Library uses conventional HTTP response codes to indicate the success or failure of
an API request. In general: Codes in the 2xx range indicate success. Codes in the 
4xx range indicate an error that failed given the information provided (e.g., a 
required parameter was omitted, a charge failed, etc.). 

### Error Handling
Erros are returned in JSON objects in the following format:

{
    "success: "false",
    "error": "404",
    "mesage": "BAd Request"
}


The Library API will return this four errors when request fails
HTTP STATUS CODE SUMMARY
400 - Bad                   The request was unacceptable, often due to missing a required parameter.
404 - Not Found	            The requested resource doesn't exist.
422 - Uproccessable         The request could not be processed.
405 - Method not allowed    The request is not allowed for the particular URL. 

### RESOURCES
Books

Endpoint: 
GET /books

This represents a list of books books and total number of books. 
Results are paginated in groups of 8, includes an argument to choose page number.

Sample:
$ curl http://127.0.0.1:5000/books

The Books Object:
{
    "books":[
        {
            "id": 1
            "title: "CIRCE",
            "author": "Neil Gaiman"
            "rating": 5
        },
        {
            "id": 2
            "title: "Lullaby",
            "author": "Leila Slimani"
            "rating": 3
        }
        {
            "id": 3
            "title: "The Great Alone",
            "author": "Kristin Hannah"
            "rating": 4
        }
    ], 
    "success":  true,
    "total_books": 3
}
Attributes
    books - array of hashes.
        List of available books.
    
    id - Integer.
        Unique identifier for the object.

    title - String.
        Title of this book

    author - String.
        Author of this book

    rating - Integer.
        Rating value of this book


Update Book Rating

Endpoint: PATCH /books/{book_id}
Updates the specified rating value of a book by setting the value of the parameter passed.
Returns the success value and id of the modified book.

$ curl -X PATCH http://127.0.0.1:5000/books/5 -H "Content-Type: application/json" -d '{"rating":"1"}'

 {
    "success": True
    "id": 1
}
Attributes
    sucess - Boolean.
        Returns True/False.
    
    id - Integer.
        Unique identifier for the object.


Endpoint: DELETE /books/{book_id}

Deletes a book of a given ID. Returns a success value, an id of book deleted, a formatted list of 
remaining books and total number of books.


$ curl -X DELETE http://127.0.0.1:5000/books/5

The Books Object:
 {
    "success": True
    "id": 1,
    "books": [
        {
            "id": 1
            "title: "CIRCE",
            "author": "Neil Gaiman"
            "rating": 5
        },
        {
            "id": 2
            "title: "Lullaby",
            "author": "Leila Slimani"
            "rating": 3
        }
        {
            "id": 3
            "title: "The Great Alone",
            "author": "Kristin Hannah"
            "rating": 4
        }
    ],
    "total_books": 3
}
Attributes
    sucess - Boolean.
        Returns True/False.
    
    id - Integer.
        Unique identifier for the object.

    books - list of objects.
        List of all books.
    
    total_books - Integer.
        Total amount of books.


Endpoint: POST /books

Creates a new book using the submitted title, author and rating. Returns the id of the created book, 
success value, total books, and book list based on current page number to update the frontend.

$ curl http://127.0.0.1:5000/books?page=3 -X POST -H "Content-Type: application/json"
  -d '{"title":"Neverwhere", "author":"Neil Gaiman", "rating":"5"}'

{
  "books": [
    {
      "author": "Neil Gaiman",
      "id": 24,
      "rating": 5,
      "title": "Neverwhere"
    }
  ],
  "created": 24,
  "success": true,
  "total_books": 17
}

Attributes
    books - list of objects.
        List of object containing details of a books.
    
    created - Integer.
        Unique identifier for the object.

    success - Boolean.
        Returns True/False.
    
    total_books - Integer.
        Total amount of books.


Deployment N/A

Authors
Iwuh Ikechukwu Daniel

Acknowledgements
The awesome team at Udacity.