# 📚 第二章：FastAPI 基礎概念

> 掌握 FastAPI 的三大核心基石：類型提示、Pydantic、依賴注入

---

## 🎯 章節目標

完成本章後，你將能夠：

- ✅ 使用 Python 類型提示撰寫清晰的程式碼
- ✅ 用 Pydantic 建立資料模型並自動驗證
- ✅ 運用依賴注入設計模組化、可測試的 API

---

## 📖 章節內容

### 2.1 Python 類型提示 (Type Hints)

**📁 檔案**：[01_type_hints.ipynb](01_type_hints.ipynb)

**學習重點**：
- 什麼是類型提示？為什麼重要？
- 基本類型：`str`、`int`、`float`、`bool`
- 容器類型：`list[T]`、`dict[K,V]`、`set[T]`、`tuple[T,...]`
- typing 模組：`Optional`、`Union`、`Any`、`Callable`
- 類型提示在 FastAPI 中的實際應用

**為什麼需要學這個？**
> FastAPI 的「魔法」來自類型提示。它讓框架能自動解析參數、驗證資料、生成文檔。沒有類型提示，就沒有 FastAPI 的強大功能。

---

### 2.2 Pydantic 資料驗證

**📁 檔案**：[02_pydantic.ipynb](02_pydantic.ipynb)

**學習重點**：
- `BaseModel` 基礎用法與模型方法
- `Field` 欄位驗證（長度、範圍、正則表達式）
- `@field_validator` 自訂驗證邏輯
- 模型繼承：建立 Create/Update/Response 模型
- 巢狀模型：處理複雜的資料結構

**為什麼需要學這個？**
> 真實世界的 API 必須驗證輸入資料。Pydantic 讓你用宣告式的方式定義資料規則，FastAPI 會自動執行驗證並回傳清楚的錯誤訊息。

---

### 2.3 依賴注入 (Dependency Injection)

**📁 檔案**：[03_dependency_injection.ipynb](03_dependency_injection.ipynb)

**學習重點**：
- 依賴注入的概念與優點
- `Depends()` 基本用法
- 類別作為依賴
- 依賴鏈（巢狀依賴）
- `yield` 依賴：資源管理
- 全域依賴：跨端點共用

**為什麼需要學這個？**
> 依賴注入是編寫可維護程式碼的關鍵。它讓你能輕鬆重用認證邏輯、資料庫連線、分頁參數等，而不用在每個端點重複寫一樣的程式碼。

---

## 🔗 三者的關係

```
┌─────────────────────────────────────────────────────────────┐
│                      FastAPI 端點                            │
│  @app.get("/users/{user_id}")                               │
│  def get_user(                                               │
│      user_id: int,              ← 類型提示：自動轉換參數      │
│      user: User = Depends(...), ← 依賴注入：提供共用邏輯      │
│  ) -> UserResponse:             ← Pydantic：定義回應格式      │
└─────────────────────────────────────────────────────────────┘
```

| 技術 | 負責什麼 |
|------|----------|
| **類型提示** | 告訴 FastAPI 參數和回傳值的類型 |
| **Pydantic** | 定義資料結構、驗證規則 |
| **依賴注入** | 提供可重用的邏輯（認證、資料庫、設定等） |

---

## 📋 前置知識

開始本章前，請確保你已經：

- [x] 完成第一章：FastAPI 入門
- [x] 了解 Python 基本語法（函式、類別、字典）
- [x] 知道如何執行 Jupyter Notebook

---

## 🛠️ 環境準備

```bash
# 確認已安裝必要套件
pip install fastapi pydantic
```

---

## 📝 學習建議

### 推薦學習順序

```
01_type_hints.ipynb → 02_pydantic.ipynb → 03_dependency_injection.ipynb
```

> ⚠️ **請按順序學習！** 後面的內容會使用前面學到的概念。

### 學習方法

1. **閱讀說明** - 理解概念和原理
2. **執行程式碼** - 觀察輸出結果
3. **修改實驗** - 改變參數看看會發生什麼
4. **完成練習** - 鞏固所學

### 學習時間估計

| 單元 | 預估時間 | 難度 |
|------|----------|------|
| 2.1 類型提示 | 30-45 分鐘 | ⭐ 入門 |
| 2.2 Pydantic | 45-60 分鐘 | ⭐⭐ 基礎 |
| 2.3 依賴注入 | 45-60 分鐘 | ⭐⭐ 基礎 |

---

## ❓ 常見問題

### Q: Python 3.9 以下版本怎麼辦？

類型提示的語法在不同版本有差異：

```python
# Python 3.9+
def func(items: list[str]) -> dict[str, int]: ...

# Python 3.8 及以下
from typing import List, Dict
def func(items: List[str]) -> Dict[str, int]: ...
```

### Q: Pydantic v1 和 v2 有什麼差別？

本教材使用 **Pydantic v2**，主要差異：

| v1 寫法 | v2 寫法 |
|---------|---------|
| `.dict()` | `.model_dump()` |
| `.json()` | `.model_dump_json()` |
| `@validator` | `@field_validator` |

### Q: 依賴注入和直接呼叫函式有什麼不同？

| 直接呼叫 | 依賴注入 |
|----------|----------|
| 你自己呼叫函式 | FastAPI 幫你呼叫 |
| 無法自動處理參數 | 自動從請求解析參數 |
| 不容易測試 | 容易替換為測試用的假資料 |

---

## ⏭️ 下一步

完成本章後，前往：

👉 **[第三章：路由設計](../03_routing/)** - 學習如何組織 API 路由

---

## 📚 延伸資源

- [Python 類型提示官方文件](https://docs.python.org/3/library/typing.html)
- [Pydantic 官方文件](https://docs.pydantic.dev/)
- [FastAPI 依賴注入文件](https://fastapi.tiangolo.com/tutorial/dependencies/)
