from fastapi import FastAPI

# Initialize FastAPI app
app = FastAPI()

# Sample data for each endpoint
data = {
    "api1": {
        "text1": "Welcome to API 1!",
        "text2": "This is the first value",
        "text3": "This is a description for API 1",
        "text4": "Here is some more info on API 1"
    },
    "api2": {
        "text1": "Welcome to API 2!",
        "text2": "This is the second value",
        "text3": "This is a description for API 2",
        "text4": "Here is some more info on API 2"
    },
    "api3": {
        "text1": "Welcome to API 3!",
        "text2": "This is the third value",
        "text3": "This is a description for API 3",
        "text4": "Here is some more info on API 3"
    },
    "api4": {
        "text1": "Welcome to API 4!",
        "text2": "This is the fourth value",
        "text3": "This is a description for API 4",
        "text4": "Here is some more info on API 4"
    }
}

# API 1: Returns 4 different text values
@app.get("/api1")
async def get_api1():
    return data["api1"]

# API 2: Returns 4 different text values
@app.get("/api2")
async def get_api2():
    return data["api2"]

# API 3: Returns 4 different text values
@app.get("/api3")
async def get_api3():
    return data["api3"]

# API 4: Returns 4 different text values
@app.get("/api4")
async def get_api4():
    return data["api4"]
