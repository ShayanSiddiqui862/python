from agents import Agent,Runner, function_tool
from httpx import get, request
from connection import config
from datetime import datetime
import rich
import requests
@function_tool
def get_products():
    url = "https://template6-six.vercel.app/api/products"
    try:
        response = requests.get(url)
        response.raise_for_status()
        products = response.json()
        return products
    except requests.exceptions.RequestException as e:
        return f"Error fetching Prdoucts:"
    
agent = Agent(
    name = "Shopping Agent",
    instructions="You are a shopping agent that help the user about the available products in our store. The data is being fetched from the api",
    tools=[get_products]
)

result = Runner.run_sync(agent,"Get me the list of products and display each product with its name and price and with good formatting",run_config=config)
print(result.final_output)

