# Almost a circle

Welcome to "Almost a Circle," an exploration of the art of code serialization and deserialization. In this creative journey, we delve into the intricacies of reusing classes and methods, all explained in a language that everyone can understand. Join the bandwagon as we navigate the fascinating realm where code meets artistry!

## 0.Testing

💡 **If it's not tested, it doesn't work**
Test your files, classes, and methods
Make sure they're unit tested and PEP 8 validated
Run tests with python3 -m unittest discover tests

## 1. Base Class

📁 **Base Class**
Create the foundational class Base
Manage the 'id' attribute for future classes
Handle instantiation and duplication elegantly

## 2. First Rectangle

🔲 **First Rectangle**
Introduce the Rectangle class inheriting from Base
Set private attributes with getters and setters
Protect attributes, validate input

## 3. Validate Attributes

🚨 **Validate Attributes**
Ensure attributes meet requirements
Raise errors for invalid inputs
Maintain robust validation in setter methods

## 4. Area First

📏 **Area First**
Calculate the area of the Rectangle
Add a public method 'area'
Return the area value of the Rectangle instance

## 5. Display #0

🎨 **Display #0**
Print the Rectangle instance with character '#'
Implement the 'display' method
Ignore 'x' and 'y' for now

## 6. \_\_str\_\_

📝 **\_\_str\_\_**
Override the '\_\_str\_\_' method
Return a formatted string representation
Including id, x, y, width, and height

## 7. Display #1

🎨 **Display #1**
Enhance 'display' method to consider 'x' and 'y'
Print the Rectangle instance with character '#'
Properly handle offsets

## 8. Update #0

🔄 **Update #0**
Introduce the 'update' method
Assign arguments to attributes
Handle a series of arguments in order

## 9. Update #1

🔄 **Update #1**
Improve 'update' method with keyword arguments
Assign key-value pairs to attributes
Flexible and unordered argument assignment

## 10. And Now, the Square

🔳 **And Now, the Square!**
Create the Square class inheriting from Rectangle
Share attributes and methods
Maintain the relationship between Square and Rectangle

## 11. Square Size

📏 **Square Size**
Add public getter and setter for 'size'
Set width and height with the same value
Validate size input, follow Rectangle's lead

## 12. Square Update

🔄 **Square Update**
Implement 'update' method for Square
Assign arguments to attributes
Handle id, size, x, and y

## 13. Rectangle Instance to Dictionary Representation

🔍 **Rectangle to Dictionary**
Implement 'to_dictionary' method for Rectangle
Return a dictionary representation
Include id, width, height, x, and y

## 14. Square Instance to Dictionary Representation

🔍 **Square to Dictionary**
Implement 'to_dictionary' method for Square
Return a dictionary representation
Include id, size, x, and y

## 15. Dictionary to JSON String

🔠 **Dictionary to JSON**
Add static method 'to_json_string'
Convert list of dictionaries to JSON string
Handle empty and None cases

## 16. JSON String to File

📁 **JSON String to File**
Add class method 'save_to_file'
Write JSON string to a file
Use class name as the filename

## 17. JSON String to Dictionary

🔠 **JSON String to Dictionary**
Add static method 'from_json_string'
Convert JSON string to a list of dictionaries
Handle empty and None cases

## 18. Dictionary to Instance

🔄 **Dictionary to Instance**
Add class method 'create'
Create an instance from a dictionary
Use 'update' method with **kwargs

## 19. File to Instances

📁 **File to Instances**
Add class method 'load_from_file'
Load instances from a file
Use 'from_json_string' and 'create'

## 20. JSON Ok, but CSV?

🔣 **JSON Ok, but CSV?**
Challenge: CSV Serialization/Deserialization
Add 'save_to_file_csv' and 'load_from_file_csv' methods
Serialize and deserialize in CSV format

Feel the artistry in Python as you explore and master these elegant data structures and algorithms. Enjoy your journey through the world of Python! 🚀🐍 Happy coding! 🎉