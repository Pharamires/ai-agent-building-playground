import openai
from dotenv import find_dotenv, load_dotenv

load_dotenv()

client = openai.OpenAI()
model = "gpt-4.1"

text_summarizer_agent = Agent(
    name="Summariser",
    instructions="You are summarising the provided text in a concise and simple manner. Different audiences can understand the main points of a text and the main message.",
    model=model
)

print(text_summarizer_agent.id)

thread = Agent