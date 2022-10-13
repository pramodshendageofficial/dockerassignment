from fastapi import FastAPI
import uvicorn
app=FastAPI()

@app.get('/')
def root():
    return "Hello World. Welcome to FASTAPI Application"

if __name__=="__main__":
    uvicorn.run("main:app", port=8000, reload=True)