from fastapi import FastAPI

app = FastAPI()

# BEGIN (write your solution here)
from fastapi import FastAPI

app = FastAPI()

@app.get("/reverse/{text}")
def reverse_text(text: str):
    reversed_text = text[::-1]
    return {"reversed": reversed_text}
# END
