from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain,SequentialChain
from dotenv import load_dotenv

load_dotenv()

llm = OpenAI()

#Code Template
code_prompt = PromptTemplate(
    template="Write a very short {langauge} function that will {task}",
    input_variables=["language","task"]
)

# Test Template
test_prompt = PromptTemplate(
    template="Write a test for following {langauge} code:\n {code}",
    input_variables=["langauge","code"]
)


# code chain
code_chain = LLMChain(
    llm=llm,
    prompt=code_prompt,
    output_key="code"
)

# test chain
test_chain = LLMChain(
    llm=llm,
    prompt=test_prompt,
    output_key="test"
)

chain = SequentialChain(
    chains=[code_chain,test_chain],
    input_variables=["task","langauge"],
    output_variables=["code","test"]
)


result = chain({
    "langauge":"python",
    "task":'return a list of numbers'
})

print(result)