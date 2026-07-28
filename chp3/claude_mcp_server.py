from mcp.server.fastmcp import FastMCP

mcp = FastMCP('Research Tools')

@mcp.tool()
def get_research_sources() -> list[str]:
    """Provides a list of research sources."""
    search_sources = [
        "Wikipedia",
        "Google",
        "Youtube"
    ]
    return search_sources


if __name__ == "__main__":
    mcp.run()