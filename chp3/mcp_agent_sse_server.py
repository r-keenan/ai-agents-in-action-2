from agents import Agent
from agents.mcp import MCPServerSse

async def main():
    async with MCPServerSse(
        name="SSE Python Server",
        params={'url': 'https://localhost:8000/sse'}
    ) as research_server:
        agent = Agent(
            name="Assistant",
            instructions='Use the research tools to perform research.',
            mcp_servers=[research_server]
        ),
