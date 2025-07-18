from agents import Agent,Runner, AsyncOpenAI, OpenAIChatCompletionsModel
from dotenv import load_dotenv
import os
from agents.run import RunConfig

load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")
if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY is not set. Please ensure it is defined in your .env file.")


external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_client
)

config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True
)

writer = Agent(
    name="Writer Agent",
    instructions="You are a translator Agent. Your task is to convert the given text either into English or Urdu",
)
inputer = str(input("Enter text to translate:"))
result =  Runner.run_sync(
    writer, 
    input=inputer,
     run_config= config)
print(result.final_output)
    
