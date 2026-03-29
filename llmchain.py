from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain.chains import LLMChain

#initialize the LLM
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", google_api_key="")

#define the prompt template
prompt = PromptTemplate(
    input_variables=["topic"],
    template="Suggest a catchy blog about {topic}?")

#create a LLMChain
chain=LLMChain(llm=llm,prompt=prompt)

#define the topic
topic=input('enter the topic')
output=chain.run(topic)

#print the output
print("generated blog title:",output)


5
