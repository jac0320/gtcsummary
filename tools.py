TOOLS = [
        {
            "type": "function",
            "function": {
                "name": "keynote_rag",
                "description": "Answer question about Jensen Huang's Keynote presentation at GTC 2025. The questions/query only applies to the keynote information.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "query": {
                            "type": "string",
                            "description": "Question string about with Jensen Huang's Keynote Presentation",
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
                "description": "Answer question about personal notes written by Site Wang based on his experience at GTC 2025. These notes are all written by Site Wang himself with fresh opinion about several new AI topics about the conferece.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "query": {
                            "type": "string",
                            "description": "Question string about personal notes written by Site Wang",
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
                "description": "Rank sponsor companies at GTC 2025 based on the user query relevance to the company description.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "query": {
                            "type": "string",
                            "description": "Question string about general description of a company",
                        },
                        "k": {
                            "type": "integer",
                            "description": "how many top results to be returned",
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
                "description": "Answer question about a specific sponsor company at GTC 2025. It is only used when a sepcific company name is mentioned/asked by the user.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "query": {
                            "type": "string",
                            "description": "Question string about a specific sponsor company at GTC 2025",
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
                "description": "Conduct a searched to fetch the url about a specific talk based on the user query. It is only applicable when user is asking about a specific talk.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "query": {
                            "type": "string",
                            "description": "Title string about a specific technical talk at GTC 2025",
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
                "description": "Rank technical talks at GTC 2025 based on the user query relevance to talks' title.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "query": {
                            "type": "string",
                            "description": "Question string about a general direction of research topics to be used for searching for relevant technical talks at GTC 2025",
                        },
                        "k": {
                            "type": "integer",
                            "description": "how many top results to be returned",
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
                "description": "This function is used to generate code to fulfill a users request. The requests is not a typically information retrieval request but a more complex tasks that requires code generation. The function will generate a plan of steps to address the user question by coding in the streamlit interface.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "query": {
                            "type": "string",
                            "description": "User requests for a code generation task",
                        }
                    },
                    "required": ["query"],
                },
            }
        }
    ]