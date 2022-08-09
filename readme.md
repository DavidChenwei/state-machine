# A simple way to implement State machine
## How to run the code
- First: Run server.py
It will generate a PNG file, which is the image of the State machine structure.  
Every time run the server.py, it will generate a new image and it will cover the previous image.
- Second: Run the client.py  
In the file, the client will automatically send a request every 3 seconds.
The range of request value is '1', '2', '3'

## Result
- Check the result of the server.py, you can find out the result as follows:  
Connection established  
Server:A  
Client:2  
Server:Q    
Client:3  
Server:K  
Client:3  
Server:Y  
Client:1  
Server:V  
Client:2  
Server:E  
Client:3  
Server:O  
Client:3  
Server:W  
Client:1  
Server:S  
Client:3  
Server:D  
Client:2  
Server:J  
......
Client:2  
Server:Z
Server:A 

- The result of image named State machine structure.png in the current folder.

## Notes:
- If you don't want use graphviz, just run the server_without_graphviz at first.
- Change your own host in server and client
- If you want to run server.py, it needs to install graphviz on your computer and install the python package
