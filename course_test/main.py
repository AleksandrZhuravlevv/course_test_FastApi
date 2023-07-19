from datetime import datetime, timedelta
from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

app = FastAPI(
    title="Test App"
)
security = HTTPBearer()

# Пример пользователя
username = "user"
password = "password"

# Пример данных о зарплате и дате следующего повышения
salary = 5000
next_promotion = datetime.now() + timedelta(days=365)


# Функция для проверки валидности токена
def authorize_token(token: HTTPAuthorizationCredentials = Depends(security)):
    if token != "your_access_token":
        raise HTTPException(status_code=401, detail="Invalid token")
    return token


# Получение токена авторизации
@app.post("/token")
def get_token(username_: str, password_: str):
    if username_ == "user" and password_ == "password":
        return {"access_token": "your_access_token", "token_type": "bearer"}
    raise HTTPException(status_code=401, detail="Invalid credentials")


# Получение данных о зарплате
@app.get("/salary")
def get_salary():
    return {"salary": salary, "next_promotion": next_promotion.strftime("%Y-%m-%d")}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
