from creewi_tools import Basetool
\
    class Duckduckgosearch_tool(Basetool):
        name:str ="Duckduckgosearch_tool"
        description:str = "This tool is used to search the internet."
        
        def _run(self, argument:str) -> str:
            
        