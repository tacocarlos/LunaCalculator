import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.matrix import matrix

app = FastAPI(title="Luna Calculator Steps", description="An API for breaking down numerical algorithms into steps for presentation.", version="0.0.1", contact={
    "name": "Carlos Luna",
    "url": "https://personal-site-hazel-five.vercel.app/",
    "email": "carlosluna3801@gmail.com"  
})

origins = ["*"]
# origins = [
#     "https://localhost:8000",
#     "http://localhost:8000",
#     "http://localhost",
#     "https://localhost",

#     "http://localhost:5173/",
#     "http://localhost:5173"
# ]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  
    allow_methods=["*"]
)

# if status is offline then how is it going to return a response?
@app.get("/")
async def ping_status():
    return {
        'version': '0.0.1',
    }

app.include_router(matrix.router)

if __name__ == "__main__":
    print("Launching uvicorn...")
    uvicorn.run(app, host="0.0.0.0", port=8000)