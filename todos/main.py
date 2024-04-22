from fastapi import FastAPI
import uvicorn


app = FastAPI()

@app.get("/")
def helloWorld():
    return "Hello World"

@app.get("/gettodos")
def getTodos():
    print("Get todos called")
    return "gettodos called"

@app.post("/gettodos")
def getTodos():
    print("Get post method todos called")
    return "post gettodos called"

@app.get("/getSingleTodo")
def getSingleTodo():
    print("Get getSingleTodo called")
    return "getSingleTodo called sdf"

@app.put("/updateTodo")
def updateTodo():
    return "updateTodo called"




def start():
    uvicorn.run("todos.main:app",host="127.0.0.1", port=8080, reload=True)