JARVIS: LangChain + Ollama Conversational AI

This project is a simple conversational AI assistant using LangChain, Ollama, and a local LLM (default: mistral). It features chat memory, so the assistant ("JARVIS") can remember previous exchanges in the current session.
Features

    Conversational Memory: Remembers previous messages in the session for context-aware responses.

    Local LLM: Uses Ollama to run open-source language models locally (default: mistral).

    Customizable Prompt: Easily adjust the prompt template for different personalities or tasks.

Requirements

    Python 3.8+

    Ollama installed and running locally with the desired model pulled (e.g., ollama run mistral)

    Python packages:

        langchain-core

        langchain-community

        langchain-ollama

Install dependencies with:

bash
pip install langchain-core langchain-community langchain-ollama

Usage

    Ensure Ollama is running with your chosen model (e.g., mistral):

bash
ollama run mistral

Run the script:

bash
python agent.py

Chat with JARVIS!
Type your questions or prompts. Type exit to stop the conversation.

    text
    ask...

    type exit for stop

    you: What is your name?
    JARVIS: I am JARVIS, your AI assistant!

How it Works

    The script uses ChatMessageHistory to store the conversation.

    Each user message and AI response is added to memory.

    The prompt template includes the full conversation history for context.

    The model generates context-aware responses.

Customization

    Change the model:
    Edit llm = OllamaLLM(model="mistral") to use another model available in Ollama.

    Modify the prompt:
    Adjust the PromptTemplate to change JARVIS’s personality or response style.
