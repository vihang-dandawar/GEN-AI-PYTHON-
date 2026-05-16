# AI Interview Question & Answer Generator

An AI-powered RAG (Retrieval-Augmented Generation) application that extracts content from PDF documents, generates interview questions, creates answers using LLMs, and saves the output into a text file.

---

# Features

- Upload or provide any PDF
- Extracts text from PDF
- Splits large text into chunks
- Creates embeddings using HuggingFace
- Stores embeddings in FAISS vector database
- Generates interview questions using LLM
- Generates answers using RetrievalQA (RAG)
- Saves all questions and answers into `answers.txt`

---

# Tech Stack

- Python
- LangChain
- OpenRouter
- DeepSeek LLM
- HuggingFace Embeddings
- FAISS Vector Database
- PyPDFLoader

---

# Project Workflow

```text
PDF
 ↓
Text Extraction
 ↓
Chunking
 ↓
Embeddings
 ↓
FAISS Vector Store
 ↓
Question Generation
 ↓
RetrievalQA
 ↓
Answer Generation
 ↓
answers.txt
```

---

# Project Structure

```text
Project/
│
├── experiment.py
├── README.md
├── requirements.txt
├── answers.txt
├── .env
└── jd_faiss_index/
```

---

# Installation

## 1. Clone Repository

```bash
git clone https://github.com/yourusername/your-repo-name.git
```

---

## 2. Move Into Project Folder

```bash
cd your-repo-name
```

---

## 3. Create Virtual Environment

### Windows

```bash
python -m venv .venv
```

Activate:

```bash
.venv\Scripts\activate
```

---

## 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Environment Variables

Create a `.env` file in the root folder.

```env
OPENROUTER_API_KEY=your_openrouter_api_key
```

Get API key from:

https://openrouter.ai

---

# Run Project

```bash
python experiment.py
```

Program will ask:

```text
Enter PDF Path:
```

Paste your PDF path.

Example:

```text
C:\Users\YourName\Downloads\resume.pdf
```

---

# Output

The generated questions and answers will be saved in:

```text
answers.txt
```

---

# Example Output

```text
Question:
What is Retrieval-Augmented Generation?

Answer:
Retrieval-Augmented Generation (RAG) combines vector retrieval with LLMs...
```

---

# Important Libraries

| Library | Purpose |
|---|---|
| LangChain | AI orchestration |
| FAISS | Vector database |
| HuggingFace | Embeddings |
| OpenRouter | LLM API |
| PyPDF | PDF extraction |

---

# Future Improvements

- Streamlit UI
- Multi-PDF Support
- MCQ Generation
- DOCX/PDF Export
- Voice Interview Bot
- Chat with PDF
- Resume Analyzer

---

# Author

Vihang Dandawar

---

# License

MIT License