# Scaling AI Infrastructure Session

**Transcript:** [View on Otter.ai](https://otter.ai/u/KDmM_8KdfrddI81453OZkxjj7mQ?view=transcript)

---

## Overview
This session discusses **Meta’s approach** to **scaling heterogeneous AI infrastructure** for a wide range of workloads across **3+ billion** daily active users. Speakers **Tyler Graff** and **Albemarle** (Meta) explore hardware co-design, **NPI (New Product Introduction)** processes, automated health checks, and hardware platform selection (GPUs vs. ASICs).

---

## Outline

### 1. Scaling Meta Infrastructure for Heterogeneous AI Use Cases
- **Speaker 1**: Housekeeping announcements (app updates, exhibit hall, surveys).
- **Tyler Graff & Albemarle**: Oversee **large-scale AI systems** at Meta.
- **Speaker 2**: Meta supports **3B+ daily active users** across multiple apps; AI models vary widely, requiring heterogeneous hardware solutions.
- Emphasis on **unified scheduling** and dedicated **supporting services** (data feeding, GPU checkpoints).

### 2. Introduction to AI Infrastructure Challenges
- **Speaker 2**:
  - Internal **unified platform** schedules AI jobs across hardware types.
  - Complexity arises from the wide variety of **AI model** requirements.
- **Speaker 3**:
  - Summarizes the **global scale** – many data centers with diverse hardware SKUs.
  - Minimizing **interruptions** and maximizing **availability** for product teams is critical.

### 3. Early Adoption of New Hardware Platforms
- **Speaker 3**: 
  - Meta’s shift to **early adoption** from being a strategic fast follower.
  - Co-development with **suppliers** helps identify problems quickly and tailor solutions for specific workloads.
  - **Faster time-to-market** and better **hardware utilization** from early engagement.

### 4. Scaling AI Infrastructure Globally
- **Speaker 2**:
  - Large geographic footprint → consistent **NPI process** to validate hardware across sites.
  - Automated processes for **health assessment** and **availability** of AI servers.
  - Ensuring reliability via **automated ingestion** (pre-flight checks, continuous monitoring).

### 5. Maintaining Health of the AI Fleet
- **Speaker 3**:
  - Emphasizes **pre-flight checks** before placing workloads to ensure server viability.
  - Diagnosing/fixing hardware is challenging – especially with large-scale, complex AI servers.
  - Use of **custom tests** and vendor-specific diagnostics to refine **failure signatures** and accelerate remediation.

### 6. Questions and Answers
- **Speaker 5**:
  - Asks about tools for **data corruption detection** beyond PCI / NVIDIA.
  - Wonders about **compute vs. communication** scaling strategies.
  - Asks for examples of **difficult-to-detect** hardware errors.
  - Queries the **trade-offs** between general-purpose GPUs and **ASICs**.
- **Responses**:
  - Need for more advanced, possibly custom solutions beyond PCIe checks.
  - Larger-scale collaboration with suppliers is crucial to handle new failure modes.
  - Weigh **flexibility** (GPUs) vs. **performance** (ASICs), mindful of firmware complexity.

### 7. Choosing Hardware and Future Investments
- **Speaker 7**:
  - Impact of being a **social media** company on hardware strategy? 
  - Shift to **early adoption** partly due to fast-moving product demands.
- **Speaker 3**:
  - Discusses **open-sourcing** hardware platforms (e.g., via OCP).
  - **Co-design** sessions ensure alignment with product roadmaps.
  - ROI considerations drive adoption timelines and hardware selection.

### 8. Early Engagement with Suppliers
- **Speaker 9**:
  - Timelines for introducing new hardware and phasing out older ones.
- **Speaker 3** & **Speaker 2**:
  - Early collaboration with suppliers is key for future requirements.
  - Varying behaviors of hardware → NPI phases exit only when criteria are met.
  - Decision-making is **intentional**, based on ROI and **scalability** needs.

---
