import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from dotenv import load_dotenv

# Import RetrievalQA from langchain
from langchain_classic.chains import RetrievalQA
from langchain_classic.chains.summarize import load_summarize_chain


load_dotenv()

# Create uploads folder
os.makedirs("uploads", exist_ok=True)

# Get OpenRouter API key
api_key = os.getenv("OPENROUTER_API_KEY")

if not api_key:
    raise ValueError(
        "Please set the OPENROUTER_API_KEY environment variable"
    )

# Define LLM from OpenRouter
llm = ChatOpenAI(
    model="openrouter/auto",
    api_key=api_key,
    base_url="https://openrouter.ai/api/v1",
    temperature=0.7,
    max_tokens=1000
)

# User PDF Input
filepath = input("Enter PDF Path: ")

# Load PDF
loader = PyPDFLoader(filepath)
data = loader.load()

# Extract text from PDF
quetions_gen = ""

for page in data:
    quetions_gen += page.page_content

# Split text into chunks
splitter = RecursiveCharacterTextSplitter(
    chunk_size=1500,
    chunk_overlap=200
)

chunks_quetions_gen = splitter.split_text(quetions_gen)

# Convert chunks into Documents
document_quetions_gen = [
    Document(page_content=t)
    for t in chunks_quetions_gen
]

# Initialize HuggingFace Embeddings
embeddings = HuggingFaceEmbeddings(
    model_name="all-MiniLM-L6-v2"
)

# Create FAISS vector store
vector_store = FAISS.from_documents(
    documents=document_quetions_gen,
    embedding=embeddings
)

# Save vector database
vector_store.save_local("jd_faiss_index")

# =========================
# QUESTION GENERATION PROMPT
# =========================

system_prompt = """
You are an expert technical interviewer for AI Full Stack Engineer roles.

Your task is to generate interview questions ONLY from the provided job description.

Rules:
1. Analyze the job description carefully.
2. Extract:
   - Technical skills
   - Programming languages
   - Frameworks
   - AI/ML concepts
   - Full stack technologies
   - Cloud/devops tools
   - Responsibilities
3. Generate concise and relevant interview questions directly related to the JD.
4. Questions must test:
   - Technical understanding
   - Coding ability
   - System design
   - Problem solving
   - Real-world engineering thinking
5. Include beginner, intermediate, and advanced questions.
6. Avoid explanations, answers, introductions, headings, markdown tables, or extra formatting.
7. Do NOT generate complete interview guides.
8. Do NOT repeat questions.
9. Keep questions practical, interview-oriented, and role-specific.
10. Output ONLY the questions.

JOB DESCRIPTION:
{text}

INTERVIEW QUESTIONS:
"""

prompt_quetions = PromptTemplate(
    template=system_prompt,
    input_variables=["text"]
)

# =========================
# REFINE PROMPT
# =========================

refine_system_prompt = """
You are an expert AI technical interviewer.

We already have a set of interview questions generated from a job description.

Your task is to refine and improve the existing questions using the additional context below.

Rules:
1. Improve technical depth and clarity.
2. Remove duplicate or weak questions.
3. Add new questions ONLY if the new context introduces:
   - New skills
   - New technologies
   - New responsibilities
4. Keep questions concise and interview-focused.
5. Do NOT generate answers.
6. Do NOT generate headings, explanations, tables, or long formatted documents.
7. Output ONLY the improved interview questions.
8. Generate 10 Questions one after another and give an order to each question.

EXISTING QUESTIONS:
{existing_answer}

ADDITIONAL CONTEXT:
{text}

REFINED INTERVIEW QUESTIONS:
"""

refine_prompt_quetions = PromptTemplate(
    input_variables=["existing_answer", "text"],
    template=refine_system_prompt
)

# =========================
# QUESTION GENERATION CHAIN
# =========================

ques_gen_chain = load_summarize_chain(
    llm=llm,
    chain_type="stuff",
    prompt=prompt_quetions,
)

# Generate Questions
questions_List = ques_gen_chain.run(document_quetions_gen)

print("\nGenerated Questions:\n")
print(questions_List)

# =========================
# RETRIEVAL QA
# =========================

retriever = vector_store.as_retriever()

retrieval_qa = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=retriever,
    return_source_documents=True
)

# =========================
# CLEAR OLD ANSWERS FILE
# =========================

open("answers.txt", "w").close()

# =========================
# SPLIT QUESTIONS
# =========================

questions = questions_List.split("\n")

# =========================
# ANSWER EACH QUESTION
# =========================

for question in questions:

    # Ignore empty lines
    if question.strip() == "":
        continue

    print("\nQuestion:", question)

    # Generate answer using RAG
    response = retrieval_qa.invoke(question)

    answer = response["result"]

    print("\nAnswer:", answer)
    print("\n-----------------------------------------")

    # Save Question & Answer to file
    with open("answers.txt", "a", encoding="utf-8") as f:

        f.write("Question: " + question + "\n\n")
        f.write("Answer: " + answer + "\n")
        f.write(
            "\n====================================================\n\n"
        )

print("\nAll Questions & Answers saved successfully in answers.txt")