In Golang, the built in os package provides methods for reading and writing to files. Earlier it used to be handled by the io/util package.

os.WriteFile() will create a new file if it doesn't exist and write to it or it will override it with new content if it does exist. The first parameter is the path to the file which is a 
string, bytes to be written to the file, and the permission the file should have

Use os.Getwd() to get the current working directory of a file. Also use the Join method on the path/filepath package to join a file path with the appropriate separator based on the 
operating system

There are 2 ways to append to an existing file, either you first read the file, append the content and then write the file