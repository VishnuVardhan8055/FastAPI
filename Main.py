from fastapi import FastAPI

app = FastAPI()

data = [1,2,3,4,5,6,7,8,9,0]

@app.get("/")
def home():
    return "Hello welcome to the Home Page"

@app.get("/listdata")
def get_data():
    # Convert list to string before concatenation
    return "Getting the List Data: " + str(data)


@app.get("/post")
@app.post("/post")
def post():
    data.sort()
    return "Sorted list updated in the page: " + str(data)

@app.get("/put")

@app.put("/put")
def put():
    if -1 in data:
        return "Already exists in the data. No duplicates allowed. Data: " + str(data)
    else:
        data.append(-1)
        return "Data is appended: " + str(data)




@app.get("/Delete")
@app.delete("/Delete")
def delete():
    if 2 in data:
        data.remove(2)
        print("Data after removal:", data)
        return "Removed successfully: " + str(data)
    else:
        return "data is not avilable in the list"



from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In dev mode only — allows all origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
