from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def read_root():
    f = open("mok.txt","rb")
    x = f.read()
    f.close()
    return x
