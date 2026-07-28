from agents import Agent, Runner
from agents.parts import MCPServerStdio, MCPServerStdioParams
import asyncio
from pathlib import Path


SCRIPT = Path(__file__).with_name('claude_mcp_server.py').resolve()

async def main():
    async with MCPServerStdio(
        name='Research Tools',
        params=MCPServerStdioParams(
            command='mcp',
            args=['run', str(SCRIPT)]
        )
    ) as research_server:
        agent = Agent(
            name='Assistant',
            instructions='Use the research tools to perform research.',
            mcp_servers=[research_server]
        )

        print('Running: Get the available research sources')
        result = await Runner.run(
            agent,
            "Get the available research sources"
        )
        print(result.final_output)

if __name__ == 'main':
    asyncio.run(main())

