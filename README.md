# GTC 2024: Learning Notes 🤖📚

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## TL;DR: 

This Streamlit app provides a summary of Site Wang's learnings from GTC 2024.

Deployed at [streamlit community cloud](https://jac0320-gtcsummary-gtc-summary-igftof.streamlit.app/)


## Running this App Locally


1. Switch to a new virtualenv
2. Install dependencies: `pip install -r requirements.txt`
3. Make sure you have env var set LLM calls
    * `OPENAI_API_KEY` for OpenAI calls
    * `API_KEY` for Google's Gemini
4. Kick off the app by doing `streamlit run gtc_summary.py`


## Default Model Usage

Generally, the spending of all models below shouldn't be more than $0.1 for 1 day of extensive tuning/optimization.

1. Embedding Model: OpenAI's embedding with interface from LlamaIndex
2. RAG: LlamaIndex's RAG model with GPT3.5Turbo + OpenAI Embedding
3. Keyword Search: OpenAI's embedding
4. Company Search: Google's Gemini 1.5Pro
5. Code Generation
    * Blockers: GPT-3.5-Turbo
    * Code Planner: GPT-3.5-Turbo
    * Code Writer: Google Gemini
    * Code Reviewer: GPT-4-Turbo


## Hacking

Please try not to hack it. Trust me you won't get much. 
If you are successful, I appreciate let me know. I would love to learn from you and block your hack.