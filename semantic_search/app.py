# Build a semantic search engine with LangChain

# 1.Document Preparation
from langchain_core.documents import Document

document = [
     Document(
        page_content="Dogs are great companions, known for their loyalty and friendliness.",
        metadata={"source": "mammal-pets-doc"},
    ),
    Document(
        page_content="Cats are independent pets that often enjoy their own space.",
        metadata={"source": "mammal-pets-doc"},
    ),
    Document(
    page_content="LangChain is a framework for developing applications powered by language models.",
    metadata={"source": "https://langchain.com/docs/"}
    ),
]

# 2. Load Documents from PDFs
from langchain_community.document_loaders import PyPDFLoader

path = "nke-10k-2023.pdf"
loader = PyPDFLoader(path)
docs = loader.load()

print(f"Loaded {len(docs)} documents from the PDF.")
