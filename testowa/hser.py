from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def read_root():
    f = open("mok.txt","r")
    x = f.read()
    f.close()
    return x
