from fastapi import FastAPI

# Initialize FastAPI app
app = FastAPI()

# Sample data for each endpoint
data = {
    "api1": {
        "text1": "Virat Kohli",
        "text2": "Rohit Sharma",
        "text3": "MS Dhoni",
        "text4": "R. Ashwin"
    },
    "api2": {
        "text1": "Lionel Messi",
        "text2": "Cristiano Ronaldo",
        "text3": "Neymar jr",
        "text4": "Iniesta"
    },
   "api3": {
    "text1": "Roger Federer",
    "text2": "Rafael Nadal",
    "text3": "Novak Djokovic",
    "text4": "Serena Williams"
}
,
   "api4": {
    "text1": "Michael Jordan",
    "text2": "LeBron James",
    "text3": "Kobe Bryant",
    "text4": "Stephen Curry"
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
