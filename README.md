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

### GET/ questions
1.) If searchTerms is not included in the JSON request parameters
* General:
  * This endpoint is used to return a list of questions (the result is paginated  in groups of 10) <br>
  if searchTerm is not included in the JSON request parameters.  
 * Sample:
   * ``` curl http://127.0.0.1:5000/questions```
2.)  If searchTerms is included in the JSON request parameters
* General:
  *   Return a list of questions based on a text query string.
### POST/quizzes
* General: 
  * This endpoint is used to play the quiz game by returning a question for a given category.
* Sample:
 ````bash
curl http://127.0.0.1:5000/quizzes -X POST --data '{"previous_questions": [20, 21], "quiz_category": {"type": "Science", "id": "1"}}'
curl --header "Content-Type: application/json" --request POST  --data '{"previous_questions": [20, 21], "quiz_category": {"type": "Science", "id": "1"}}'  http://127.0.0.1:5000/quizzes

````
 ````bash
curl http://127.0.0.1:5000/question

````