# AirBnB (clone) - The console


## Description
This is a mock of the infamous AirBnB website. This clone website is created for educational purposes only.

### The console
- create your data model
- manage (create, update, destroy, etc) objects via a console / command interpreter
- store and persist objects to a file (JSON file)
The first piece is to manipulate a powerful storage system. This storage engine will give us an abstraction between “My object” and “How they are stored and persisted”. This means: from your console code (the command interpreter itself) and from the front-end and RestAPI you will build later, you won’t have to pay attention (take care) of how your objects are stored.

This abstraction will also allow you to change the type of storage easily without updating all of your codebase.

The console will be a tool to validate this storage engine
___

## Directories and Files
___
### Directories
| Directory | Description |
| ------ | ------ |
| [models] | This directory contains the modules and classes to create an object|
| [engine] | This directory contains the modules file storage|
| [tests] | This directory contains all the test for models|

### Files
| File | Description |
| ------ | ------ |
| [console.py] | The console file|
| [AUTHORS] | This file contains all the authors of this project|

##### Files models directory
| File | Description |
| ------ | ------ |
| [base_model.py] | BaseModel superclass|
| [amenity.py] | Amenity subclass|
| [city.py] | City subclass|
| [place.py] | Place subclass|
| [review.py] | Review subclass|
| [state.py] | State subclass|
| [user.py] | User subclass|

##### Files engine directory
| File | Description |
| ------ | ------ |
| [file_storage.py] | FileStorage class|

##### Files tests directory
| File | Description |
| ------ | ------ |
| [test_models/test_base_model.py] | Unittest module for file storage|
| [test_engine/test_file_storage.py] | Unittest module for file storage|
___

### Installation
```sh
$ git clone https://github.com/abelabebayehu/AirBnB_clone.git
```

### Examples
Display help command
___
```sh
AirBnB_clone$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

(hbnb) 
(hbnb) quit
AirBnB_clone$
```
___

### Developed with
- Ubuntu 20.04 LTS using python3 (version 3.8.5)
___

### Author
- Abel Abebayehu <abelperspectives@gmail.com>
