TOOLS = [
        {
            "type": "function",
            "function": {
                "name": "keynote_rag",
                "description": "Retrieve answers to questions about Jensen Huang's Keynote at GTC 2025.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "query": {
                            "type": "string",
                            "description": "A question about Jensen Huang's Keynote Presentation.",
                        }
                    },
                    "required": ["query"],
                },
            }
        },
        {
            "type": "function",
            "function": {
                "name": "personal_note_rag",
                "description": "Answer questions based on personal notes by Site Wang from GTC 2025.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "query": {
                            "type": "string",
                            "description": "A question about Site Wang's personal notes.",
                        }
                    },
                    "required": ["query"],
                },
            }
        },
        {
            "type": "function",
            "function": {
                "name": "company_rerank",
                "description": "Rank GTC 2025 sponsor companies by relevance to a user query.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "query": {
                            "type": "string",
                            "description": "A query about company descriptions.",
                        },
                        "k": {
                            "type": "integer",
                            "description": "Number of top results to return.",
                            "default": 5
                        }
                    },
                    "required": ["query"],
                },
            }
        },
        {
            "type": "function",
            "function": {
                "name": "company_info_search",
                "description": "Provide information about a specific GTC 2025 sponsor company.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "query": {
                            "type": "string",
                            "description": "A query about a specific sponsor company.",
                        }
                    },
                    "required": ["query"],
                },
            }
        },
        {
            "type": "function",
            "function": {
                "name": "talk_info_search",
                "description": "Fetch the URL for a specific GTC 2025 talk based on a user query.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "query": {
                            "type": "string",
                            "description": "A query about a specific technical talk.",
                        }
                    },
                    "required": ["query"],
                },
            }
        },
        {
            "type": "function",
            "function": {
                "name": "talk_rerank",
                "description": "Rank GTC 2025 technical talks by relevance to a user query.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "query": {
                            "type": "string",
                            "description": "A query about research topics for technical talks.",
                        },
                        "k": {
                            "type": "integer",
                            "description": "Number of top results to return.",
                            "default": 5
                        }
                    },
                    "required": ["query"],
                },
            }
        },
        {
            "type": "function",
            "function": {
                "name": "alpha_view_agent",
                "description": "Generate code to fulfill complex user requests using Streamlit.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "query": {
                            "type": "string",
                            "description": "A request for a code generation task.",
                        }
                    },
                    "required": ["query"],
                },
            }
        },
        {
            "type": "function",
            "function": {
                "name": "transcribed_talks_rag",
                "description": "Provide detailed information on transcribed talks attended in person at GTC 2025.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "query": {
                            "type": "string",
                            "description": "A question about the transcribed talks attended in person.",
                        }
                    },
                    "required": ["query"],
                },
            }
        }
    ]