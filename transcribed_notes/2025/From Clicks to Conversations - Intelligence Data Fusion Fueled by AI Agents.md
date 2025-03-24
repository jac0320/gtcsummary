# From Clicks to Conversations – Intelligence Data Fusion Fueled by AI Agents

## Overview
A **proof-of-concept (POC)** developed by **Saab AB** in collaboration with **NVIDIA** demonstrates how **large language models (LLMs)** and **agent-based systems** can transform intelligence data analysis. The project focuses on **maritime data fusion**, using **ship transponder data** (AIS) to highlight how **natural language** conversations can replace traditional click-based user interfaces.

---

## Key Points

### 1. Massive Data Fusion Platform
- **Saab’s platform** aggregates diverse **data sources** (e.g., active/passive sensors, satellite feeds, open-source intel).
- Historically relied on **graphical UIs**, requiring manual steps (“clicks”) to retrieve and filter data.
- The new approach: **conversation-based** queries that let users ask, “Which ships were anchored outside coastline X for 30+ minutes?”

### 2. Shift from Clicks to Conversations
- **Intent-Based Interaction**:
  - Inspired by the concept of an **AI UI Paradigm** (Batch → Commands → Intent).
  - Users specify **high-level outcomes** or questions; AI interprets, refines, and executes tasks.
- **Trust & Transparency**:
  - Emphasis on **trustworthy AI** with clear accountability and guardrails.
  - Human-AI teaming ensures the user can validate, override, or refine AI-driven outcomes.

### 3. Multi-Agent Architecture
- **AI Agents**:
  1. **Search** – Locates relevant data (ship IDs, positions).
  2. **Filter** – Reduces the dataset based on specific criteria (anchoring duration, location).
  3. **Rendezvous Detection**, **Anomaly Detection** – Specialized analytics for advanced intelligence tasks.
  4. **Supervisor**, **Finisher**, **Judge** – Manage or validate agent outputs, enforce **NeMo** guardrails, and orchestrate multi-agent collaboration.
- **Backend Microservices**:
  - Connect to a **Massive Data Fusion** engine (the data lake house), returning structured results in response to agent queries.

### 4. NVIDIA NIM Integration
- **NVIDIA** provided guidance on:
  - **LLMs** and **NeMo** guardrails for content filtering and compliance.
  - **Agent orchestration** best practices, ensuring reliable multi-agent communication.

### 5. User Workflow
1. User types a **natural language request**:  
   *“Show me all ships that stopped longer than 30 min outside coastline X in the last six months.”*
2. The **AI assistant** delegates queries to relevant **agents** (Search, Filter, etc.).
3. The **Supervisor** orchestrates results and enforces **guardrails** with a **Judge** agent, if needed.
4. The user receives a **refined answer**, potentially refining the conversation further:  
   *“Which of these 432 ships visited country Y?”*

### 6. Benefits and Challenges
- **Benefits**:
  - Faster, more **intuitive** data queries using conversational AI.
  - Multi-agent architecture handles complex requests with minimal manual “clicks.”
  - Enhances **situational awareness** for defense or security use cases.
- **Challenges**:
  - Ensuring **trust** (correctness, security) in AI recommendations.
  - **Guardrails** to prevent hallucinations or unauthorized data exposure.
  - Complexity of coordinating multiple specialized agents and verifying outputs.

### 7. Future Directions
- **Refining** the multi-agent system with more domain-specific tools and advanced analytics.
- **Scaling** to handle additional data feeds (satellite imagery, sensor data).
- **Iterating** on user experience to improve explainability and confidence in AI-driven results.

---

## Key Takeaways
1. **Generative AI** greatly **impacts user interface design**, shifting from point-and-click to **conversational** interactions.
2. **Agent-based systems** bring both **opportunities** (modularity, specialization) and **challenges** (complex orchestration, trust).
3. **Massive data fusion** for maritime or intelligence applications benefits from an **intent-based** approach, letting operators ask high-level questions rather than manually navigating complex data structures.

---
