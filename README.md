# 🚀 FastAPI Foundation - 給程式新手的 FastAPI 基礎教材

**循序漸進、淺顯易懂的 FastAPI 學習教材**

> 📖 使用 Jupyter Notebook 互動式教學，搭配 Python 實作範例

## 🎯 專案特色

- **👶 新手友善** - 從零開始，無需後端開發經驗
- **📓 互動學習** - Jupyter Notebook 邊學邊做
- **🔄 循序漸進** - 10 個章節由淺入深
- **💻 可運行範例** - 每個章節都有完整實作
- **📚 開源免費** - 歡迎貢獻與分享

## 📋 教學大綱

| 章節 | 主題 | 內容概述 |
|------|------|----------|
| 01 | **FastAPI 入門** | 安裝環境、Hello World、基本概念介紹 |
| 02 | **基礎概念** | Python 類型提示、Pydantic 資料驗證、依賴注入 |
| 03 | **路由設計** | 路徑操作、APIRouter、路由組織最佳實踐 |
| 04 | **請求與回應** | 請求體處理、回應模型、資料驗證 |
| 05 | **資料庫操作** | SQLite、PostgreSQL、MongoDB、ORM 整合 |
| 06 | **認證與授權** | JWT 認證、OAuth2、密碼雜湊、權限控制 |
| 07 | **檔案處理** | 檔案上傳/下載、靜態檔案、雲端儲存 |
| 08 | **WebSocket** | 即時通訊、聊天室實作、推送通知 |
| 09 | **測試** | pytest 基礎、單元測試、整合測試 |
| 10 | **部署** | Docker 容器化、雲端部署、CI/CD |

## 🚀 快速開始

### 1. 複製專案
```bash
git clone https://github.com/yourusername/fastapi_foundation.git
cd fastapi_foundation
```

### 2. 建立虛擬環境
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
```

### 3. 安裝依賴
```bash
pip install -r requirements.txt
```

### 4. 啟動 Jupyter Notebook
```bash
jupyter notebook
```

### 5. 開始學習
打開 `notebooks/01_intro/` 開始第一章！

## 📁 專案結構

```
fastapi_foundation/
├── README.md              # 專案說明（本檔案）
├── CLAUDE.md              # Claude Code 協作規則
├── requirements.txt       # Python 依賴套件
├── notebooks/             # 📓 Jupyter 教學章節
│   ├── 01_intro/          # 第一章：FastAPI 入門
│   ├── 02_basics/         # 第二章：基礎概念
│   ├── 03_routing/        # 第三章：路由設計
│   ├── 04_request_response/ # 第四章：請求與回應
│   ├── 05_database/       # 第五章：資料庫操作
│   ├── 06_authentication/ # 第六章：認證與授權
│   ├── 07_file_handling/  # 第七章：檔案處理
│   ├── 08_websocket/      # 第八章：WebSocket
│   ├── 09_testing/        # 第九章：測試
│   └── 10_deployment/     # 第十章：部署
├── src/                   # 💻 Python 實作範例
│   ├── examples/          # 完整範例程式碼
│   ├── utils/             # 共用工具
│   ├── models/            # 資料模型
│   └── api/               # API 端點
├── docs/                  # 📚 額外文件
├── tests/                 # 🧪 測試檔案
└── output/                # 📤 輸出檔案
```

## 🛠️ 開發環境需求

- Python 3.9+
- pip (Python 套件管理器)
- Jupyter Notebook
- Git

### 主要依賴套件

```
fastapi>=0.100.0
uvicorn>=0.23.0
pydantic>=2.0.0
sqlalchemy>=2.0.0
python-jose[cryptography]
passlib[bcrypt]
python-multipart
pytest
httpx
```

## 📖 如何使用本教材

1. **按順序學習** - 建議從第一章開始，循序漸進
2. **動手實作** - 每個 Notebook 都有練習題，請務必動手做
3. **執行程式碼** - 使用 Shift+Enter 執行 Notebook 中的程式碼
4. **參考範例** - `src/examples/` 有完整的實作範例可供參考
5. **提問交流** - 歡迎在 Issues 中提問

## 🤝 貢獻指南

歡迎貢獻！您可以：

1. 🐛 回報問題 (Issues)
2. 📝 改善文件或教材內容
3. 💡 提供新的範例或練習題
4. 🌍 翻譯成其他語言

### 貢獻流程

1. Fork 這個專案
2. 建立新分支 (`git checkout -b feature/amazing-feature`)
3. 提交變更 (`git commit -m 'feat: 新增某某功能'`)
4. 推送到分支 (`git push origin feature/amazing-feature`)
5. 開啟 Pull Request

## 📜 授權

本專案採用 MIT 授權條款 - 詳見 [LICENSE](LICENSE) 檔案

## 🙏 致謝

- [FastAPI](https://fastapi.tiangolo.com/) - 現代、快速的 Python Web 框架
- [Pydantic](https://pydantic.dev/) - 資料驗證庫
- [SQLAlchemy](https://www.sqlalchemy.org/) - Python SQL 工具包
- 所有貢獻者和學習者

---

**Happy Learning! 🎉**

> 💡 如果這個教材對您有幫助，歡迎給個 ⭐ Star！
