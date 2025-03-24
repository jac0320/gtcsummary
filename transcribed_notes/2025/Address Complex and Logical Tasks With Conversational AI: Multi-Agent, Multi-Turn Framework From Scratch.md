# Generative AI Workshop


The session focused on the **development and application of generative AI agents**. Key points included:
- Agents as systems capable of **long-term and short-term planning**.
- The importance of **robust production systems**.
- **Challenges** such as **latency, cost, and determinism**.
- An **agenda** covering formal agent definitions, software engineering patterns, and hands-on sessions.
- Specific examples, including:
  - A **multi-agent system** for e-commerce.
  - Converting unstructured data to **JSONL** format.
  - **Parallel training** and **load balancing** for production-level systems.
- Emphasis on **logging**, **error handling**, and **security measures** for end-to-end reliability.

---


## Outline

### 1. Agenda and Event Code Introduction
- **Speaker 1** welcomes participants and emphasizes the rapid pace of **generative AI** innovation.  
- The **agenda** includes:
  - Formal definition of the agent.
  - Software engineering patterns.
  - Hands-on sessions.
- **Speaker 1** advises to wait 30 minutes before starting the hands-on session to avoid unnecessary GPU time usage.
- The **event code** is provided, with instructions to note it down but not start the session yet.

### 2. Defining Agents and Their Components
- **Formal definition of an agent**: A system that can think, reflect, use tools, and orchestrate tasks with long-term and short-term planning.
- **Agentic phenomenon**: Systems that make decisions independently, often enhanced by agent-based approaches even if not natively part of the LLM.
- **Agents** are software programs designed to **autonomously execute tasks**, serving end users or other systems.
- Highlights the progression from a **proof of concept (POC)** to a **production-level system**.

### 3. Challenges in Agentic Systems
- Ongoing **challenges** include **latency**, **cost-effectiveness**, and **determinism**.
- **Cost** of LLM training and inference is a significant barrier.
- **Larger LLMs** can handle more tasks but at higher computational and resource costs.
- The **core** of any agentic system typically revolves around a **dedicated LLM** handling routing and requests.

### 4. Components of Agentic Systems
- Major components: **tools**, **functions**, and **enterprise data**.
- The **LLM** acts as the **brain**, making decisions based on context and additional information.
- **Short-term and long-term memory** in agentic systems allow for context retention across interactions.
- **Context limits** in LLMs are a bottleneck; **rotary position embedding** and other techniques aim to mitigate these limits.

### 5. Patterns and Hierarchical Agents
- Current **deployment patterns** for LLMs include **single-hop agents** and **multi-actor hierarchical agents**.
- **Multi-turn** and **multi-agent** systems enable agents to converse with themselves or external tools over multiple steps.
- **System messages** differentiate multi-actor/hierarchical agents, allowing structured communication.
- **Human-in-the-loop** scenarios remain crucial, enabling humans to collaborate with or oversee agents.

### 6. Hands-On Session: React Agent
- First hands-on session involves **building a React agent**:
  - Includes library imports and defining the `Agent` class.
  - Creating **functions and tools** for the LLM agent, such as memory calculation utilities.
  - Understanding **intermediate states** vs. **final answers**.

### 7. Multi-Agent System Example
- Second hands-on session covers a **multi-agent system** for an **e-commerce workflow**:
  - The logical flow: checking weather, choosing furniture, and processing orders.
  - Demonstrates **breaking down complex problems** into smaller tasks, assigning each to a specialized agent.
  - Concludes with agents working **cohesively** to deliver a combined solution.

### 8. Real-Life Application: Supervised Fine-Tuning
- Final hands-on session focuses on **converting unstructured data** into **JSONL format** for **supervised fine-tuning**:
  - A **hierarchical agentic system** orchestrates agents to extract concepts, generate questions, and provide answers.
  - Emphasizes maintaining **separate prompt files** to track iterations and prompt versions.
  - Demonstrates how the **JSONL output** is created for downstream training tasks.

### 9. Production-Level System Considerations
- Taking agentic systems to **production** involves:
  - **Parallel training** and **load balancing**.
  - **Long-term planning**, **budget control**, **monitoring**, **logging**, **safety**, and **security**.
- A broader **ecosystem** of agentic orchestration emerges, including fundamental models, storage, and agentic platforms.
- Session ends with a **thank you** to the sponsors and a reminder to provide **feedback**.

---
