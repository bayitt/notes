If you have a path operation that receives a path parameter, but you want the possible valid path parameter values to be predefined, we can make use of a standard Python Enum.
We can get the actual value of an enum by accessing the value property on the enum

It may be possible that you need a dynamic path parameter to include other slashes (/). In this case, we can declare the path as 
@app.get('/files/{file_path:path}'). file_path is the name of the path parameter while :path tells it I'm guessing that it should be catch all and just grab everything specified after
files

When you declare other function parameters that are not part of the path parameters, they are automatically interpreted as "query" parameters

Apparently you can declare path parameters and query parameters in any order and FastAPI is smart enough to detect which is a path parameter and which is a query parameter

To declare request bodies in FastAPI, you make use of Pydantic models with all their powers and benefits.

Thinking about it, this FastAPI concept of defining classes with Pydantic and making use of that to define your request body and validate all that, its quite similar to Nest JS's concept
of DTOs

Apparently with FastAPI, there is one big request body in which you can list out all the parameters and then in your path operation function, FastAPI will compose the request body
into the different parameters you have specified on the function

FastAPI is also smart enough to detect whether a path operation function parameter is from the path, query or request body. The function parameters are recognized as below:
- If the parameter is also declared in the path, it will be used as a parameter
- If the parameter is of a single type (link int, float, str, bool) it will be interpreted as a query parameter
- If the parameter is declared to be of the type of a Pydantic model, it will be interpreted as a request body