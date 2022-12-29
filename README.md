# The AirBnB Clone Project - The COnsole
![AirBnB Logo](https://www.pngitem.com/pimgs/m/132-1322125_transparent-background-airbnb-logo-hd-png-download.png)

## Project Description
This is going to be the frst part of the project where we built a command line interface for the end product using Python's CMD library. The data to be managed are stored in a JSON file and can be managed using the json library. The data are all in form of python objects.

We have the base model from which other data models inherit stuff.

## Description of the command interpreter:
The application has a command line user interface through which the user can seamlessly communicate with the database. Some of the actions this interface will help the user perform include CREATE, UPDATE, READ and DELETE (CRUD). This interface is developed using Object Oriented Programming.

Below are some of the commands reatured by the command line user interface:
- show
- create
- update
- destroy
- count

## How to start it
The following instructions will fetch you a copy of the application to be executed on LINUX machines only.

## Installing
The first step is to clone the repository from github

```
git clone https://github.com/chrishalogen/AirBnB_clone.git
```

## How to use it
It can work in two different modes:


**Interactive** and **Non-interactive**.

In **Interactive mode**, the console will display a prompt (hbnb) indicating that the user can write and execute a command. After the command is run, the prompt will appear again a wait for a new command. This can go indefinitely as long as the user does not exit the program.

```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```

In **Non-interactive mode**, the shell will need to be run with a command input piped into its execution so that the command is run as soon as the Shell starts. In this mode no prompt will appear, and no further input will be expected from the user.


```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```

## Authors

Christian Chi | Email: [chrishalogen](mailto:christackoms@gmail.com) 

Unama Edwin Sunday | Github: [edwinsundayunama](mailto:unamaedwin247@gmail.com)