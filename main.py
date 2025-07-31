from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os

load_dotenv()

def generate_pet_name():
    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",  # ✅ for AI Studio
        temperature=0.7,
        google_api_key=os.getenv("GOOGLE_API_KEY")
    )

    response = llm.invoke("Suggest 5 cool names for my dog.")
    return response.content

if __name__ == "__main__":
    print(generate_pet_name())
