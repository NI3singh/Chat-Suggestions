# # WITH LOCAL MODEL
# from langchain_community.llms import Ollama

# llm = Ollama(model="llama3.2:1b")
# def chat_reply_suggestons(user_input):
#     prompt = f"generate 3 chat reply suggestions for the user input in human chatting language. here is the user input : {user_input} and remember just reply with the suggestions only nothing else and all three suggestions in single python list format"
    
#     response = llm.invoke(prompt)
#     return response

# user_input = "Hello, how are you?"
# suggestions = chat_reply_suggestons(user_input)
# print(suggestions)

#-----------------------------------------------------------------------------------------

# WITH GROQ API
# from groq import Groq

# client = Groq(api_key=")

# def chat_reply_suggestons(user_input):
#    prompt = f"generate 3 chat reply suggestions for the user input in human chatting language. here is the user input : {user_input} and remember just reply with the suggestions only nothing else and all three suggestions in single python list format"
#    response = client.chat.completions.create(
#        model="llama-3.3-70b-versatile",
#        messages=[{"role": "user", "content": prompt}],
#        temperature=0.3
#    )

#    try:
#         suggestions = response.choices[0].message.content.strip()
#         return suggestions
#    except Exception as e:
#         return {"Error" : str(e)}

# user_input = "Hello, how are you?"
# suggestions = chat_reply_suggestons(user_input)
# print(suggestions)

#-----------------------------------------------------------------------------------------

# LIVE API
# from fastapi import FastAPI, HTTPException
# from pydantic import BaseModel
# from groq import Groq

# # Initialize the Groq client
# client = Groq(api_key="")

# # FastAPI app initialization
# app = FastAPI()

# # Pydantic model for incoming user input
# class UserInput(BaseModel):
#     user_input: str

# # Function to get chat reply suggestions
# def chat_reply_suggestions(user_input):
#     prompt = f"""
#         Your task is to generate **exactly 3 chat reply suggestions** for the user input. The replies must be written in a natural, human-friendly tone. **Do not act as a chatbot** — respond as a person would in a real-life conversation.

#         **Strict instructions**:
#         1. Each suggestion must feel like a response from a real human, not a chatbot.
#         2. Do not include any explanations, disclaimers, or introductory text in your response. **Only provide the suggestions.**
#         3. The 3 suggestions should be listed in a single Python list format.
#         4. Make sure the suggestions sound natural and conversational, just as a person would respond to the given input not as chatbot.
#         5. **Do not include anything else** in the response (no extra sentences, no instructions, etc.), just the suggestions in list format.

#         Here is the user input: {user_input}

#         **Output Format**: [“suggestion 1”, “suggestion 2”, “suggestion 3”]
#         """
    
#     try:
#         # Call the Groq API
#         response = client.chat.completions.create(
#             model="llama-3.3-70b-versatile",
#             messages=[{"role": "user", "content": prompt}],
#             temperature=0.3
#         )

#         # Extract the suggestions from the response
#         suggestions = response.choices[0].message.content.strip()
#         return suggestions
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=f"Error: {str(e)}")

# # FastAPI endpoint to receive user input and return chat suggestions
# @app.post("/generate-chat-suggestions/")
# async def generate_chat_suggestions(user_input: UserInput):
#     suggestions = chat_reply_suggestions(user_input.user_input)
#     return {"suggestions": suggestions}



from groq import Groq

client = Groq(api_key="")

def chat_reply_suggestions(user_input):
    prompt = f"""
        Your task is to generate *exactly 4 chat reply suggestions* for the user input. The replies must be written in a natural, human-friendly tone. *Do not act as a chatbot* — respond as a person would in a real-life conversation.

        **Strict instructions**:
        1. Make sure the suggestions sound natural, casual, and conversational—like how people text.  
        2. Each reply should be *very short (3-5 words max)*, like quick chat suggestions.  
        3. Keep replies friendly, expressive, and engaging. Use emojis if they fit.  
        4. Do not include any explanations, disclaimers, or introductory text in your response. *Only provide the suggestions.*  
        5. The 4 suggestions should be listed in a single Python list format.  
        6. *Do not include anything else* in the response (no extra sentences, no instructions, etc.), just the suggestions in list format.  

        Here is the user input: {user_input}  

        **Output Format**: ["suggestion 1", "suggestion 2", "suggestion 3", "suggestion 4"]
        """

    try:
    
        response = client.chat.completions.create(
            # model="llama-3.3-70b-versatile",
            model="llama-3.3-70b-specdec",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3
        )

        suggestions = response.choices[0].message.content.strip()
        return suggestions
    except Exception as e:
        return {"Error" : str(e)}
    

user_input = input("Enter chat : ")
suggestions = chat_reply_suggestions(user_input)
print(suggestions)
