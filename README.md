# 🩺 Medical RAG Chatbot

An end-to-end **Medical Retrieval-Augmented Generation (RAG) Chatbot** built with **FastAPI**, **React**, **LangChain**, **ChromaDB**, **Groq LLM**, and **HuggingFace Embeddings**.

The chatbot answers medical questions by retrieving relevant information from trusted medical PDF documents before generating responses, improving factual accuracy and providing source references.

---

# 🚀 Features

- 📄 Upload Medical PDFs
- 🤖 AI-powered Medical Question Answering
- 🔍 Retrieval-Augmented Generation (RAG)
- 🧠 Conversation Memory
- 📚 Source Citation Support
- ⚡ Streaming Responses
- 🗂 ChromaDB Vector Database
- 🧬 HuggingFace Sentence Embeddings
- 🚀 Groq LLM Integration
- 🎨 Modern React Frontend
- 📝 Structured Logging
- 🛡 Global Exception Handling
- ✅ Request Validation
- 🐳 Docker Support
- 📦 Docker Compose
- 🔄 GitHub Actions CI
- 🧪 Automated Testing
- ☁️ Render Deployment Ready

---

# 🏗 Project Architecture

```text
                User
                  │
                  ▼
          React Frontend
                  │
                  ▼
          FastAPI Backend
                  │
        ┌─────────┴─────────┐
        │                   │
        ▼                   ▼
  Conversation Memory   PDF Retriever
        │                   │
        └─────────┬─────────┘
                  ▼
             ChromaDB
                  │
                  ▼
     HuggingFace Embeddings
                  │
                  ▼
             Groq LLM
                  │
                  ▼
             Final Response
```

---

# 🛠 Tech Stack

## Frontend

- React
- Axios
- CSS

## Backend

- FastAPI
- Python
- LangChain
- ChromaDB
- Groq
- HuggingFace Embeddings
- Pydantic

## DevOps

- Docker
- Docker Compose
- GitHub Actions
- Render

---

# 📂 Project Structure

```text
medical-rag-chatbot/
│
├── backend/
│   ├── app/
│   ├── tests/
│   ├── Dockerfile
│   └── requirements.txt
│
├── frontend/
│   ├── src/
│   └── public/
│
├── docs/
│
├── .github/
│   └── workflows/
│
└── README.md
```

---

# ⚙ Installation

## Clone Repository

```bash
git clone <repository-url>
cd medical-rag-chatbot
```

---

## Backend

```bash
cd backend

python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt

uvicorn app.main:app --reload
```

---

## Frontend

```bash
cd frontend

npm install

npm run dev
```

---

# 🐳 Docker

Build Docker Image

```bash
docker build -t medical-rag-backend .
```

Run Docker Compose

```bash
docker compose up --build
```

---

# 🧪 Testing

```bash
pytest

pytest --cov=app --cov-report=term-missing
```

---

# ☁ Deployment

Configured for:

- Render
- Docker
- GitHub Actions

---

# 📈 Future Improvements

- User Authentication
- Multi-user Chat History
- PostgreSQL Integration
- Medical Image Analysis
- Voice Input
- Citation Highlighting
- Admin Dashboard
- Kubernetes Deployment

---

# 📄 License

This project is developed for educational and portfolio purposes.

---

# 👨‍💻 Author

**Mannem Bindu Madhav**

B.Tech Computer Science Engineering

AI / Machine Learning Enthusiast

GitHub:
https://github.com/MannemMadhav

LinkedIn:
https://www.linkedin.com/in/bindu-madhav-mannem-5037602b