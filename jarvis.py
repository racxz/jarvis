from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.prompts import PromptTemplate
from langchain_ollama import OllamaLLM

llm = OllamaLLM(model="mistral")
chat_history = ChatMessageHistory()

prompt = PromptTemplate(
    input_variables=["chat_history","qes"],
    template="Previous convo: {chat_history}\nUser: {qes}\nJARVIS:"
)
#func to run ai chat with memory
def run_chain(qes):
    #retrive chat history
    chat_history_text="\n".join([f"{msg.type.capitalize()}:{msg.content}" for msg in chat_history.messages])
    #Run the AI response
    res = llm.invoke(prompt.format(chat_history=chat_history_text, qes=qes))

    #store new user input and AI response in memory
    chat_history.add_user_message(qes)
    chat_history.add_ai_message(res)

    return res

print("\n ask...")
print("\n type exit for stop")
while True:
    user_input=input("\n you: ")
    if user_input.lower()=="exit":
        print("\n bye bye...")
        break
    ai_res=run_chain(user_input)
    print(f"\n JARVIS: {ai_res}")
