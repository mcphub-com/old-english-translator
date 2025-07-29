import requests
from datetime import datetime
from typing import Union, Literal, List
from mcp.server import FastMCP
from pydantic import Field
from typing import Annotated
from mcp.server.fastmcp import FastMCP
from fastmcp import FastMCP, Context
import os
from dotenv import load_dotenv
load_dotenv()
rapid_api_key = os.getenv("RAPID_API_KEY")

__rapidapi_url__ = 'https://rapidapi.com/orthosie/api/old-english-translator'

mcp = FastMCP('old-english-translator')

@mcp.tool()
def translate_to_old_english(text: Annotated[str, Field(description='Text to convert to old English.')]) -> dict: 
    '''Old English Translator'''
    url = 'https://orthosie-old-english-translator-v1.p.rapidapi.com/oldenglish.json'
    headers = {'x-rapidapi-host': 'orthosie-old-english-translator-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'text': text,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()



if __name__ == '__main__':
    import sys
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 9997
    mcp.run(transport="stdio")
