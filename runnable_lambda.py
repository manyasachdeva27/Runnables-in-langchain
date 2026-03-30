from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableSequence,RunnablePassthrough,RunnableParallel, RunnableLambda

load_dotenv

prompt=PromptTemplate(
    template="write a joke about {topic}",
    input_variables=["topic"]
)

model=ChatOpenAI()

parser=StrOutputParser()

joke_gen_chain=RunnableSequence(prompt,model,parser)

# def word_count(text):
#     return len(text.split())

# parallel_chain=RunnableParallel({
#     'joke':RunnablePassthrough(),
#     'word_count':RunnableLambda(word_count)
# })

#or 

parallel_chain=RunnableParallel({
    'joke':RunnablePassthrough(),
    'word_count':RunnableLambda(lambda x: len(x.split()))
})

final_chain=RunnableSequence(joke_gen_chain,parallel_chain)

result=final_chain.invoke({'topic':'AI'})

print(result)
