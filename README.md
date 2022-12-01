# Tweet Generator  
Tweet Generator is a web application built for generating posts for social media. In the current scope, the project generates only tweets.  
The functionality that the registered can use include generation of tweets from web articles and plain texts, access to the history of used articles and texts,
as well as the access to all generated posts. Additionally, administrators of the application have access to all users' history and configuration panel.

## Setup  
The set is very easy, but make sure you have docker installed. Navigate to the root folder of the application and run the command:
```
docker-compose up build
```
The frontend will be available on localhost:4200 and the backend will be listening on localhost:5000.

## Stack
* Python using Flask web framework
* Angular 14
* PostgreSQL
* Docker
