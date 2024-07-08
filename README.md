This is a simple app that collect feedback in the form of rating with values from 1-5

Consist of backend and frontend with different tech stack

BACKEND = FastAPI - python
Frontend = Vue - javascript

Backend documentation handled by swagger and served in [address]:8000/docs
Frontend served by vite in [address]:5173

Environment settings should be place in app folder. This is the content of env files:
DATABASE_HOSTNAME = 
DATABASE_PORT = 
DATABASE_NAME = 
DATABASE_USERNAME = 
DATABASE_PASSWORD = 

Database and orm handled by sqlalchemy. Target database using postgresql

Unit test for API located in app/test and can be executed using pytest
