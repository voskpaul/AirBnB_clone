Contents
Description
Environment
Further Information
Requirements
Repo Contents
Installation
Usage
Built with
Acknowledgements
Description 📄
TThis is the first step towards building your first full web application: the AirBnB clone. In this first phase a basic console was created using the Cmd Python module, to manage the objects of the whole project, being able to implement the methods create, show, update, all, and destroy to the existing classes and subclasses.

Environment 💻
The console was developed in Ubuntu 20.04 LTS using python3 (version 3.8.5).

Further information 📑
For further information on python version, and documentation visit python.org.

Requirements 📝
Knowledge in python3, how to use a command line interpreter, a computer with Ubuntu 20.04, python3 and pep8 style corrector.

Repo Contents 📋
This repository constains the following files:

File	Description
AUTHORS	Contains info about authors of the project
base_model.py	Defines BaseModel class (parent class), and methods
user.py	Defines subclass User
amenity.py	Defines subclass Amenity
city.py	Defines subclass City
place.py	Defines subclass Place
review.py	Defines subclass Review
state.py	Defines subclass State
file_storage.py	Creates new instance of class, serializes and deserializes data
console.py	creates object, retrieves object from file, does operations on objects, updates attributes of object and destroys object
test_base_model.py	unittests for base_model
test_user.py	unittests for user
test_amenity.py	unittests for amenity
test_city.py	unittests for city
test_place.py	unittests for place
test_review.py	unittests for review
test_state.py	unittests for state
test_file_storage.py	unittests for file_storage
test_console.py	unittests for console
