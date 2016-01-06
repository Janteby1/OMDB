# API Introduction

### Learning Objectives
***Students will be able to...***

* Make request to an external api to grab information

---
### Context 

* Everything on the internet revolves around data. How do we grab it? Where can we get it? What can we do with it? 

---
### Lessons

##### Part 1 - API Intro

* Everything that we've done so far has been about creating and manipulating our own database
* Now we're going to start getting data from somewhere else using APIs
* API stands for Application Programming Interface
* Almost everything is an API 
* For the purposes of this course, and industry talk, people are usually talking about a HTTP API.
* You can think of these as a database somebody else put together that you can pull information from. 

##### Part 2 - REST / CRUD / HTTP VERBS

***Five Min Exercise***

* Do some research on the following
	* REST
	* RESTful API
	* HTTP VERBS / CRUD	

---

* REST stands for Representational State Transfer
* This is NOT an actually programming keyword. It is a term to describe "best practices" when creating HTTP APIs
* The four most common actions when dealing with an API are the CRUD actions

|    | CRUD   | HTTP Method |
|----|--------|-------------|
| C  | Create | POST        |
| R  | Read   | GET         |
| U  | Update | PUT         |
| D  | Delete | DELETE      |

* There are eight HTTP verbs in total but the others are uncommon. 
* Much of what we want to do with an api can be completed using the CRUD HTTP Verbs
* Here are all eight in case you were wondering

```
GET
POST
PUT
DELETE
OPTIONS
HEAD
TRACE
CONNECT
```

##### Part 3 - HTTP Requests

* So we did CRUD in SQL, and now we have CRUD commands with HTTP Verbs, but where do these verbs go? 
* These verbs go into your HTTP Requests
* HTTP works as a `request/response` protocol. Your browser will make `requests` to a server, and that server will serve a `response`
* Python cannot handle requests out of the box so let's install this onto our computers

```
pip3 install requests
```
* Now we have the requests library
* remember `pip3` is our package manager for Python3
* Let's see a list of all our python 3 modules

```
pip3 freeze
```
* A former student of mine built an api for D&D spells called [spell-buddy](http://spell-buddy.herokuapp.com/)
* Let's use this api along with the request library to return some values to us.

```
import requests

print(requests.get("http://spell-buddy.herokuapp.com/api/spells?name=magic%20missile").json())
```
* Maybe put this command inside a method and print the method instead? 
* without .json() will return response 200
* must use .json to get the file in the correct format

##### Part 3 - JSON vs XML

* Notice in the last example we used the method `.json()`
* There are two types of file formats normally supported by API's. They are JSON and XML
* For the purpose of this class, and more recent up to date technologies we will be using JSON
* JSON looks like a dictionary

***NOTE***

* XML is used more in line with big banks or larger coorporations with older technologies. 

##### Part 4 - What are end points?

* Endpoints are a webservice that points us to specific part of an API
* Many API's will have multiple endpoints and you have to target the right one to grab the data you want

##### Resources

* [Tutorial Point for HTTP Request](http://www.tutorialspoint.com/http/http_requests.htm)
* [Andrew Havens Beginners Guide to Creating a REST API](http://www.andrewhavens.com/posts/20/beginners-guide-to-creating-a-rest-api/)
* [Miguel Grinberg Design a RESTful API with Python and Flask](http://blog.miguelgrinberg.com/post/designing-a-restful-api-with-python-and-flask)

