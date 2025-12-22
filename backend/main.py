from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from database import users_collection


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/login")
def login(username: str = Form(...), password: str = Form(...)):
    user = users_collection.find_one({"username": username, "password": password})
    if user:
        user["_id"] = str(user["_id"])
        return user
    return JSONResponse(status_code=401, content={"message": "Invalid credentials"})


@app.post("/signup")
def signup(
    username: str = Form(...),
    password: str = Form(...),
    firstname: str = Form(...),
    lastname: str = Form(...),
    age: int = Form(...),
    email: str = Form(...),
    phone: str = Form(...),
    address: str = Form(...),
    
):
    if users_collection.find_one({"username": username}):
        return JSONResponse(status_code=400, content={"message": "Username already exists"})

    users_collection.insert_one({
        "username": username,
        "password": password,
        "firstname": firstname,
        "lastname": lastname,
        "age": age,
        "email": email,
        "phone": phone,
        "address": address,
        "photo": "https://via.placeholder.com/150"
    })
    return {"message": "Signup successful"}
