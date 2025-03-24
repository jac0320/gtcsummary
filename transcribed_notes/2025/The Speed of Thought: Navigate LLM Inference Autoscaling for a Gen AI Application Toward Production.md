# LLM Inference Optimization Workshop

---

The discussion focused on **latency**, **throughput**, and **concurrency** in LLM (Language Learning Models) inference:

- **Latency** measures the time to generate the first token (time-to-first-token).
- **Throughput** is the number of tokens per second per deployment or GPU, used for comparison across deployments.
- **Concurrency** is the number of users processing requests simultaneously, distinct from throughput.

A key takeaway is the **trade-off between latency and throughput**:
- Increasing concurrency or batch size can improve throughput but negatively impact latency.
- Auto-scaling strategies (either by increasing concurrency on the same GPU(s) or adding more GPUs) help maintain SLAs.

The session also covered **NIMS (NVIDIA Inference Manager Services)**:
- NIMS optimizes performance and simplifies deployment in Kubernetes.
- The **NIMS Operator** automates GPU management for efficient LLM deployment, handling software components like device plugins and GPU drivers.

---

## Outline

### 1. Latency and Throughput in LLM Inference
- **Speaker 1** explains the importance of **latency** (time to the first token and subsequent tokens) and **throughput** (requests per second per deployment, tokens per second per deployment, or per GPU).
- **Concurrency** is introduced as the number of users processing requests simultaneously, differentiating it from throughput.
- The discussion highlights **trade-offs** between latency and throughput, referencing a plot that illustrates their **inverse relationship**.

### 2. Online vs. Offline Use Cases
- **Speaker 1** distinguishes between:
  - **Online use cases** (e.g., chatbots) requiring **low latency**.
  - **Offline scenarios** (e.g., batch processing) focusing on **high throughput**.
- A plot clarifies the **relationship** between higher batch sizes, improved throughput, and increased latency.
- Various **variables** (input length, context window, model size, latency requirements) influence deployment requirements.

### 3. Auto Scaling in LLM Inference
- **Speaker 1** presents **auto scaling** to handle fluctuating request rates, focusing on:
  1. Increasing concurrency on the **same GPUs** (higher throughput but penalized latency).
  2. **Horizontal scaling** to additional GPUs (maintaining latency SLAs at higher cost).
- The lab training concentrates on **enabling auto scaling** for LLM applications, emphasizing **horizontal auto scaling** strategies.

### 4. Introduction to NIMS
- **Speaker 1** provides an overview of **NIMS**:
  - Offers **optimized performance**, ease of use, and enterprise support for various LLMs.
  - Built with **APIs, inference servers**, and optimizations for different GPUs.
  - **Kubernetes native** and cloud-agnostic, simplifying model deployment workflows.
- Internally, NIMS integrates multiple **backends** and an **LLM executor** that supports various model types.

### 5. Deploying NIMS with NIMS Operator
- **Speaker 1** introduces **NIMS Operator**, a tool based on Nvidia to automate LLM deployments in Kubernetes.
- **NIMS Operator** handles:
  - Software components: device plugins, GPU drivers.
  - Streamlined deployments: from setup to lifecycle management.
  - **NIMS cache** for performance and **NIMS service** for lifecycle coordination.
- This approach provides **full Nvidia control** of application lifecycle and simplifies enterprise-scale LLM deployments.

---
