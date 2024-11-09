from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from langchain.memory import ConversationBufferMemory,FileChatMessageHistory,ConversationSummaryMemory
from langchain.prompts import MessagesPlaceholder, HumanMessagePromptTemplate, ChatPromptTemplate
from dotenv import load_dotenv

load_dotenv()

chat = ChatOpenAI()

memory = ConversationSummaryMemory(
    # chat_memory=FileChatMessageHistory("messages.json"),
    memory_key="messages",
    llm=chat,
    return_messages=True)  #message here is the key of the dictionary (it can be anything) return meesages = True make sure that old messages are not stored as just strings but as objects


prompt = ChatPromptTemplate(
    input_variables=["content","messages"],
    messages=[
        MessagesPlaceholder(variable_name="messages"),
        HumanMessagePromptTemplate.from_template("{content}")
    ]
)

chain = LLMChain(
    llm=chat,
    prompt=prompt,
    memory=memory,
    verbose=True
)

while True:
    content = input(">> ")
    result = chain({"content": content})
    print(result["text"])
