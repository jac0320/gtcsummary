TOOLS = [
        {
            "type": "function",
            "function": {
                "name": "keynote_rag",
                "description": "Use this for questions about the content, announcements, and details from Jensen Huang's GTC 2025 Keynote. This tool searches through the keynote transcript and summaries. Do NOT use this for code generation or data manipulation tasks.",
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
                "description": "Use this for questions about the content and insights from Site's personal notes and blog posts. This tool searches through Site's written content. Do NOT use this for code generation, data manipulation, or display formatting tasks.",
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
                "description": "Use this to find companies from GTC 2025 sponsors that are most relevant to a specific topic or technology. This tool ranks companies based on their descriptions. Do NOT use this for code generation or data manipulation tasks.",
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
                "description": "Use this to get detailed information about a specific GTC 2025 sponsor company. This tool searches through company descriptions. Do NOT use this for code generation or data manipulation tasks.",
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
                "description": "Use this to find specific GTC 2025 technical talks and their URLs. This tool searches through talk titles and descriptions. Do NOT use this for code generation or data manipulation tasks.",
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
                "description": "Use this to find technical talks from GTC 2025 that are most relevant to a specific topic. This tool ranks talks based on their content. Do NOT use this for code generation or data manipulation tasks.",
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
                "description": "Use this for ANY task that requires code generation, data manipulation, or custom display formatting in Streamlit. This includes but is not limited to: displaying random content, converting text to different formats (like morse code), creating custom visualizations, or any other task that needs Python code execution. This is the ONLY tool that should be used for code generation tasks.",
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
                "description": "Use this for questions about the content of talks that Site attended and transcribed in person at GTC 2025. This tool searches through the transcribed content. Do NOT use this for code generation or data manipulation tasks.",
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