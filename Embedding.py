from langchain.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from dotenv import load_dotenv

load_dotenv()
text_splitter = CharacterTextSplitter(
    separator="\n", # second priority
    chunk_size=200, # first priority
    chunk_overlap=0
)

loader = TextLoader("Data/facts.txt")
docs = loader.load_and_split(
    text_splitter=text_splitter
)
for doc in docs:
    print(doc.page_content)
    print("\n")

