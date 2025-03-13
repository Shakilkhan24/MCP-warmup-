# First look to MCP (model context protocol)

    Expose data through Resources (think of these sort of like GET endpoints; they are used to load information into the LLM's context)
    Provide functionality through Tools (sort of like POST endpoints; they are used to execute code or otherwise produce a side effect)
    Define interaction patterns through Prompts (reusable templates for LLM interactions)
    And more!


## Install MCP  

### With `uv`:  
```sh
uv add "mcp[cli]"
```

### Or With `pip`:  
```sh
pip install mcp
```

### Install this repo:  
```sh
git clone <repo-url>
cd <repo-directory>
```

### Run MCP Inspector:  
```sh
mcp dev main.py
```  

---
