from fastapi import FastAPI
app = FastAPI()

@app.get("/data")
def read_root():
    f = open("mok.txt","r")
    x = f.read()
    f.close()
    return x
