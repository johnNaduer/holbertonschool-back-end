# API Programming
This repository contains code examples and resources related to API programming.

### What Bash scripting should not be used for
Bash scripting is great for automating tasks and creating small scripts, but it should not be used for large, complex projects. Bash scripts lack some of the features and tools available in modern programming languages, such as advanced data structures, libraries, and debugging tools.

### What is an API
API stands for Application Programming Interface. It is a set of protocols and tools for building software applications. An API defines how software components should interact and communicate with each other.
**Example :**
To use the API, you would typically send a request to a specific URL that includes the city name and any other relevant parameters. The API would then respond with the current weather data in a structured format such as JSON.

Here's an example API request in Python using the requests library:
import requests

```python
city = "New York"
url = f"https://api.weatherapi.com/v1/current.json?key=YOUR_API_KEY&q={city}"

response = requests.get(url)
data = response.json()

print(f"Current temperature in {city}: {data['current']['temp_c']}°C")

```
In this example, we're using the WeatherAPI API to get the current weather data for New York. We construct a URL that includes our API key and the city we're interested in, and then send a GET request to that URL using requests.get(). The API responds with JSON data, which we can parse and extract the information we need. In this case, we're printing out the current temperature in Celsius for the specified city.

### What is a REST API
REST stands for Representational State Transfer. A REST API is an API that follows the REST architectural style. It uses HTTP requests to perform operations on data resources and returns data in a standardized format, such as JSON or XML.

### What are microservices
Microservices are a software development approach that structures an application as a collection of small, independent services. Each service performs a specific function and communicates with other services using APIs.

### What is CSV format
CSV stands for Comma-Separated Values. It is a simple file format used to store tabular data, such as spreadsheets or databases. Each line in a CSV file represents a row in the table, and each value within a row is separated by a comma.

### What is JSON format
JSON stands for JavaScript Object Notation. It is a lightweight data format used to exchange data between applications. JSON data is represented as key-value pairs, similar to a dictionary in Python.

### Pythonic style of package and module names
Package and module names in Python should be lowercase, with words separated by underscores. For example, a package name could be my_package, and a module name within that package could be my_module.

### Pythonic Class name style
Class names in Python should be written in CamelCase or CapWords, where the first letter of each word is capitalized. For example, a class name could be MyClass.

### Pythonic Variable name style
Variable names in Python should be lowercase, with words separated by underscores. For example, a variable name could be my_variable.

### Pythonic function name style
Function names in Python should be lowercase, with words separated by underscores. For example, a function name could be my_function.

### Pythonic style of Constant name
Constants in Python should be written in all caps, with words separated by underscores. For example, a constant name could be MY_CONSTANT.

### Meaning of CapWords or CamelCase in Python
CapWords or CamelCase refers to the practice of writing compound words or phrases in which the first letter of each word is capitalized. This style is commonly used in Python for naming classes, functions, and constants.
