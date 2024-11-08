from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from dotenv import load_dotenv

load_dotenv()

llm = OpenAI()

code_promt = PromptTemplate(
    template="Write a very short {langauge} function that will {task}",
    input_variables=["language","task"]
)

code_chain = LLMChain(
    llm=llm,
    prompt=code_promt
)

result = code_chain({
    "langauge":"python",
    "task":'return a list of numbers'
})

print(result['text'])