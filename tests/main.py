# 加上 FastAPI 裝飾器後
from fastapi import FastAPI

app = FastAPI()

@app.get("/hello")  # 裝飾器：把這個函式註冊為 GET /hello 的處理器
def say_hello():
    return {"message": "Hello!"}

print("加上裝飾器後，這個函式變成了 API 端點！")
print(f"已註冊的路由: {[route.path for route in app.routes if hasattr(route, 'path')]}")