from fastapi import FastAPI, Form

app = FastAPI()

# BEGIN (write your solution here)
@app.post("/login")
async def login(
    username: str = Form(..., description="Имя пользователя"),
    password: str = Form(..., description="Пароль пользователя")
):
    return {
        "username": username,
        "password": password,
        "status": "Login successful"
    }

# END
