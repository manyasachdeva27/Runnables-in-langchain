from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate

#initialize the LLM
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", google_api_key="")

#define the prompt template
prompt = PromptTemplate(
    input_variables=["topic"],
    template="Suggest a catchy blog about {topic}?")

#define the topic
topic=input('enter the topic')

#format the prompt manually using PromptTemplate
formatted_prompt=prompt.format(topic=topic)

#call the llm manually
blog_title=llm.predict(formatted_prompt)

#print the output
print("generated blog title:",blog_title)


