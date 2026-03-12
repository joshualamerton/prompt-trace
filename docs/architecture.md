# PromptTrace Architecture

PromptTrace sits between an application and its LLM calls.

It records prompts and responses as structured events.

Core components:

Application  
Sends prompts.

PromptTrace  
Captures prompt-response interactions.

Trace Store  
Maintains history for inspection and debugging.
