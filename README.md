# Full Stack API Final Project

This was the first project for the Full Stack Web Developer Nanodegree from udacity <br>( https://www.udacity.com/course/full-stack-web-developer-nanodegree--nd0044).
The task was to create an webapplication and test suite for implementing the following functionality:

1) Display questions - both all questions and by category. Questions should show the question, category and difficulty rating by default and can show/hide the answer. 
2) Delete questions.
3) Add questions and require that they include question and answer text.
4) Search for questions based on a text query string.
5) Play the quiz game, randomizing either all questions or within a specific category. 

Completing this trivia app will give you the ability to structure plan, implement, and test an API - skills essential for enabling your future applications to communicate with others. 



## Getting Started

### Backend

Create a python3 virtual environment. Then install all dependencies by running 
```bash
pip install -r /backend/requirements.txt
```
To run the server, execute:
```bash
python /flaskr/__init__.py
```
### Frontend

The `./frontend` directory contains a complete React frontend to consume the data from the Flask server. Y

The frontend app was built completely in React. In order zo run the app you need to install npm and all packages in package.json
To run the React app, execute:
```bash
npm start
```
Open [http://localhost:3000]  to view it in the browser

## API Reference
The API will return three types of errors:

* 400 – bad request
* 404 – resource not found
* 422 – unprocessable

## Endpoints
### POST/questions
Creates a new question or returns a search result
1.) If searchTerms is not included in the JSON request parameters
* General:
    * Creates a new question
* Sample
    ```
    curl http://127.0.0.1:5000/questions -X POST -H "Content-Type: application/json" 
    -d '{ "question": "Which currency has germany", "answer": "euro", "difficulty": 3, "category": "3" }'
    ```
2.)  If searchTerms is included in the JSON request parameters
* General:

* Sample:
    ``` curl http://127.0.0.1:5000/questions -X POST -d '{"searchTerm": "what"}'```
* Response:
  ``{
  "categories": {
    "1": "Science", 
    "2": "Art", 
    "3": "Geography", 
    "4": "History", 
    "5": "Entertainment", 
    "6": "Sports"
  }, 
  "questions": [
    {
      "answer": "Mona Lisa", 
      "category": "2", 
      "difficulty": 3, 
      "id": 13, 
      "question": "La Giaconda is better known as what?"
    }, 
    {
      "answer": "Blood", 
      "category": "1", 
      "difficulty": 4, 
      "id": 18, 
      "question": "Hematology is a branch of medicine involving the study of what?"
    }
  ], 
  "success": true, 
  "total_questions": 2
}`` 
### GET/ questions
* General:
  * This endpoint return a search result based on proved search tearm
* Sample:
  *  ``curl -g http://127.0.0.1:5000/questions -X GET`` 
* Response: <br>
  ``
  {
  "categories": {
    "1": "Science", 
    "2": "Art", 
    "3": "Geography", 
    "4": "History", 
    "5": "Entertainment", 
    "6": "Sports"
  }, 
  "questions": [
    {
      "answer": "Maya Angelou", 
      "category": "4", 
      "difficulty": 2, 
      "id": 1, 
      "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
    }, 
    {
      "answer": "Muhammad Ali", 
      "category": "4", 
      "difficulty": 1, 
      "id": 2, 
      "question": "What boxer's original name is Cassius Clay?"
    }, 
    {
      "answer": "Apollo 13", 
      "category": "5", 
      "difficulty": 4, 
      "id": 3, 
      "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
    }, 
    {
      "answer": "Tom Cruise", 
      "category": "5", 
      "difficulty": 4, 
      "id": 4, 
      "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
    }, 
    {
      "answer": "Edward Scissorhands", 
      "category": "5", 
      "difficulty": 3, 
      "id": 5, 
      "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
    }, 
    {
      "answer": "Brazil", 
      "category": "6", 
      "difficulty": 3, 
      "id": 6, 
      "question": "Which is the only team to play in every soccer World Cup tournament?"
    }, 
    {
      "answer": "Uruguay", 
      "category": "6", 
      "difficulty": 4, 
      "id": 7, 
      "question": "Which country won the first ever soccer World Cup in 1930?"
    }, 
    {
      "answer": "George Washington Carver", 
      "category": "4", 
      "difficulty": 2, 
      "id": 8, 
      "question": "Who invented Peanut Butter?"
    }, 
    {
      "answer": "Lake Victoria", 
      "category": "3", 
      "difficulty": 2, 
      "id": 9, 
      "question": "What is the largest lake in Africa?"
    }, 
    {
      "answer": "The Palace of Versailles", 
      "category": "3", 
      "difficulty": 3, 
      "id": 10, 
      "question": "In which royal palace would you find the Hall of Mirrors?"
    }
  ], 
  "success": true, 
  "total_questions": 20
}
  ``
#### DELETE /questions/\<int:id\>

* General:
  * Deletes a given question which is identified by the id 
* Sample: 
  *  `curl http://127.0.0.1:5000/questions/6 -X DELETE`<br>

#### GET /categories

* General: 
  * Returns a list of all available categories in the database .
* Sample: 
  * `curl http://127.0.0.1:5000/categories`<br>
* Respone:
  * ``{
  "categories": {
    "1": "Science", 
    "2": "Art", 
    "3": "Geography", 
    "4": "History", 
    "5": "Entertainment", 
    "6": "Sports"
  }, 
  "success": true
}``
### GET /categories/<int:id>/questions
* General:
  * Return all questions of a given category
* Sample:
  * curl http://127.0.0.1:5000/categories/1/questions
* Response:
  ``
  {
  "categories": {
    "1": "Science", 
    "2": "Art", 
    "3": "Geography", 
    "4": "History", 
    "5": "Entertainment", 
    "6": "Sports"
  }, 
  "current_category": {
    "id": 1, 
    "type": "Science"
  }, 
  "questions": [
    {
      "answer": "The Liver", 
      "category": "1", 
      "difficulty": 4, 
      "id": 16, 
      "question": "What is the heaviest organ in the human body?"
    }, 
    {
      "answer": "Alexander Fleming", 
      "category": "1", 
      "difficulty": 3, 
      "id": 17, 
      "question": "Who discovered penicillin?"
    }, 
    {
      "answer": "Blood", 
      "category": "1", 
      "difficulty": 4, 
      "id": 18, 
      "question": "Hematology is a branch of medicine involving the study of what?"
    }, 
    {
      "answer": "I am good", 
      "category": "1", 
      "difficulty": 1, 
      "id": 22, 
      "question": "How are you"
    }
  ], 
  "success": true, 
  "total_questions": 20}``
  
### /quizzes
* General: 
  * This endpoint is used to play the quiz game by returning a question for a given category.
* Sample:
  * ````curl http://127.0.0.1:5000/quizzes -X POST --data '{"previous_questions": [14, 15], "quiz_category": {"type": "Science", "id": "1"}}'````
* Response:
``
{
  "question": {
    "answer": "The Liver", 
    "category": "1", 
    "difficulty": 4, 
    "id": 16, 
    "question": "What is the heaviest organ in the human body?"
  }, 
  "success": true
}``