from fastapi import FastAPI
import uvicorn


app = FastAPI()

students = [
    {
        "userName": "Mubeen",
        "rollNo": 2342
    },
    {
        "userName": "Arsalan",
        "rollNo": 6467
    }
]
@app.get("/students")
def getStudents():
    return students


@app.get("/addStudent")
def addStudent(userName:str, rollNo:str):
    global studentss
    students.append({"userName": userName, "rollNo":rollNo})
    return students
    


@app.get("/")
def helloWorld():
    return "Hello World"

# path variables
@app.get("/gettodos/{id}")
def getTodos(id):
    print("Get todos called", id)
    return id

@app.post("/gettodos")
def getTodos():
    print("Get post method todos called")
    return "post gettodos called"

# query parms
@app.get("/getSingleTodo")
def getSingleTodo(userName:str, rollNo:str):
    print("Get getSingleTodo called", userName, rollNo)
    return "Get getSingleTodo"

@app.put("/updateTodo")
def updateTodo():
    return "updateTodo called"




def start():
    uvicorn.run("todos.main:app",host="127.0.0.1", port=8080, reload=True)