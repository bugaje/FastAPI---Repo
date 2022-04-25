from fastapi import FastAPI, Path
from pydantic import BaseModel
from typing import Optional

tags_metadata = [
    {
        "name": "users",
        "description": "Operations with users. The **login** logic is also here.",
    },
    {
        "name": "items",
        "description": "Manage items. So _fancy_ they have their own docs.",
        "externalDocs": {
            "description": "Items external docs",
            "url": "https://fastapi.tiangolo.com/",
        },
    },
]

app = FastAPI(openapi_tags=tags_metadata)

class Students(BaseModel):
    name: str
    age: int
    State: str
    
class UpdateStudent(BaseModel):
    name: Optional[str] = None
    age: Optional[str] = None
    State: Optional[str] = None

student_lists = {
    1: {
        "name": "Haidar",
        "age": 26,
        "State": "Katsina"
    },
    2: {
        "name": "Hadiza",
        "age": 30,
        "State": "Kaduna"
    }
}

@app.get('/')
def home():
    return {"Message": "Welcome here."}

@app.get('/get-student/{student_id}')
def get_student(student_id: int = Path(None, description="Provide the student ID.")):
    return student_lists[student_id]

@app.get('/get-by-name/{student_id}')
def get_student(student_id: int, student: Students):
    for student_id in student_lists:
        if student_lists[student_id]["name"] == name:
            return student_lists[student_id]
        
    return {"Data": "No student record found!"}

@app.put('/update-student/{student_id}')
def update_student(student_id: int, student: UpdateStudent):
    if student_id not in student_lists:
        return {"Error": "Student does not exist."}
    if student.name != None:
        student_lists[student_id].name = student.name
    if student.age != None:
        student_lists[student_id].age = student.age
    if student.State != None:
        student_lists[student_id].State = student.State
        
    return student_list[student_id]
    
@app.post('/create-student/{student_id}')
def create_student(student_id: int, student: Students):
    if student_id in student_lists:
        return {"Error": "Student already exist"}
    student_lists[student_id] = student
    return student_lists[student_id]

@app.delete('/delete-student/{student_id}')
def delete_student(student_id: int):
    if student_id not in student_lists:
        return {"Error": "Student does not exist."}
    
    del student_lists[student_id]
    return {"Message": "Record deleted succesfully."}