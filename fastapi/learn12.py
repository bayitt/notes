In some cases, you dont really need the return value of a dependency inside your path operation function. Or the dependency does not return a value. But you still need it to be executed/
resolved. In cases like this, instead of declaring a path operation function parameter with Depends, you can add a list of Dependencies to the path operation decorator.

For some types of applications you might want to add dependencies to the whole application. Similarly to the way you can add dependencies to the path operation decorators, you can add
them to the FastAPI application.

FastAPI supports dependencies that do some extra steps after finishing, to do this use yield instead of returning from the dependency

Context Managers are any of those Python objects that you can use in a with statement

Say you want to have a way for your frontend to authenticate with your backend making use of username and password, you can easily do so with FastAPI making use of OAuth2.

OAuth2 specifies that when using the password flow, the client/user must send username and password fields as form data. And the spec specifies that the fields must be named exactly that -
username and password

You can add middleware to FastAPI applications. A "middleware" is a function that works with every request before it is processed by any specific path operation function. And also
with every response before returning it.

To create a middleware, you use the decorator @app.middleware("http") on top of a function. The middleware function receives the request, a function call_next that will receive the
request as a parameter

We can configure CORS in our FastAPI application with CORSMiddleware

