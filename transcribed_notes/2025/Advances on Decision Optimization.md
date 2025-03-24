# Advances in Decision Optimization (Session S72290)

**Presenters**  
- **Alex Fender, Ph.D.** (Director of Engineering, NVIDIA)  
- **Chris Maes, Ph.D.** (Principal Engineer, NVIDIA)

---

## 1. Overview

This session highlights **NVIDIA’s latest innovations** in **decision optimization** – from **GPU-accelerated** linear and mixed-integer programming (MIP) to integration with **reinforcement learning** (RL) and **large language models** (LLMs). The talk covers progress in **NVIDIA cuOpt** (an optimization solver framework), forthcoming **open-source** plans, and how GPU acceleration is transforming real-world decision-making across **logistics**, **finance**, **manufacturing**, **energy**, and beyond.

---

## 2. Decision Optimization Basics

- **Applications**: scheduling, routing, resource allocation, supply chain, portfolio selection, etc.  
- **Method**: Formulate business problems as an **optimization model** (objective, constraints, decision variables) – solved by advanced **optimization solvers**.

### Dynamic Decision Making
- **Descriptive Analytics** → “What happened?”  
- **Predictive Analytics** → “What will happen?”  
- **Prescriptive Analytics** → “What’s the plan?” (emphasizing optimization)

---

## 3. Acceleration Opportunity

- GPUs can accelerate optimization solvers considerably (from **10×** in PDLP to **10,000×** in some semi-definite programs).  
- Built on **CUDA** and integrated with accelerated data science frameworks (e.g., **RAPIDS**).  

### NVIDIA cuOpt Going Open-Source
- **cuOpt**: GPU-accelerated solver (originally focusing on routing).  
- Plans to **open-source** cuOpt so the optimization community can **collaborate** on large-scale / ultra-fast solvers.

---

## 4. cuOpt Highlights

1. **Routing Engine**  
   - Vehicle routing optimization (TSP, VRP) with multi-constraint, multi-objective.  
   - Up to **~240× speedup** on real-world supply chain use cases.  
   - Achieves **30%** quality improvement in last-mile delivery.

2. **EARLI (Evolutionary Algorithms + RL Initialization)**  
   - Combines **RL** with an **evolutionary** solver to find “good” solutions in **<1 second** for VRP.  
   - Solutions are then refined by cuOpt for near real-time planning.

3. **Open Agentic Decision Intelligence**  
   - Integrates LLM + cuOpt for **natural language** question-answering with advanced optimization.  
   - Example: “Coffee Roasting” demo using supply, demand, shipping cost – solved in near real-time.

4. **NVIDIA Operations**  
   - cuOpt used internally for **NVIDIA supply chain**: ~40K parts, 150+ suppliers, 3K products.  
   - Handling **half a million** variables/constraints in near real time.

5. **cuOpt on Brev**  
   - One-click cuOpt deployment in the cloud with pre-configured GPU stacks.  

**Key takeaway**: RL + LLM frameworks (“Decision Intelligence”) enable broader enterprise adoption of optimization.

---

## 5. Advances in Mixed Integer Programming (MIP)

### Why GPUs for MIP?
- MIP typically uses **branch-and-cut** – a highly **sequential** process.  
- Historically, “GPUs are not helpful for MIP” due to sparse, unstructured data.  
- Today, **massively improved GPU hardware** and new GPU-friendly algorithms (like **PDLP**) create fresh opportunities.

#### Primal-Dual Hybrid Gradient (PDHG) → PDLP
- **PDLP** (Primal-Dual Hybrid Gradient for LP) from Applegate et al. (2021) is a **first-order** method that can be GPU-accelerated.
- **cuOpt** uses PDLP for faster solves:
  - 2 main operations: large **sparse matrix-vector multiplies** + vector operations (memory-bandwidth bound).
  - **H100** or future **B100** with high memory bandwidth → major speedups.

**Benchmarks**:
- Up to **~60×** or more speedups vs. CPU-based MIP solvers on certain large problems.

### Hybrid GPU/CPU Approach (cuOpt 25.02)
1. **GPU**: PDLP-based heuristics refine feasible solutions – quickly improving the **upper bound** (feasible solution quality).  
2. **CPU**: Branch and bound with **dual simplex** to refine the **lower bound** and ensure **optimality**.  
3. **Incumbent Sharing**: GPU solver + CPU solver run in parallel, exchanging feasible solutions for synergy.

**MIPLIB** tests show improvement in final gaps. Large-scale **LP** or **MIP** cases become tractable with GPU acceleration.

---

## 6. Notable Large-Scale Cases

- **LP “zib03”**: 29M variables, 19M constraints, 104M nonzeros – once took days or hours on multi-core CPU.  
  - With GPU-based PDLP, solved in **minutes** at a relative tolerance ~1e-6.
- **Green Energy MIP**: 66M variables, 77M constraints, zero feasible solutions from CPU solvers after 2 days.  
  - GPU-based PDLP heuristics found feasible solutions in ~8 hours with an average gap of 1.5%.

**Implication**: GPU-accelerated solvers open new frontiers for huge optimization problems.

---

## 7. Future Directions

- Open-sourcing **cuOpt** to build a community of contributors and integrators.  
- Deeper **GPU** involvement in **branch-and-cut** (cut generation, node processing).  
- New **algorithmic paradigms** (combining RL, LLMs, HPC) to tackle large-scale optimization.  
- Collaboration with the MIP community on difficult problems, pushing boundaries of what’s possible with GPU acceleration.

---

## 8. Session Info and Additional Resources

- **Session**: S72290 at GTC 2025.  
- More sessions on **accelerated optimization**: S74122, S72603, DLIT71690, etc.  
- Email: [cuopt@nvidia.com](mailto:cuopt@nvidia.com)  
- Check out **NVIDIA GTC** for updates and open collaboration opportunities.

---

## Key Takeaways

1. **GPU Acceleration** in decision optimization is **transformational**, yielding orders-of-magnitude performance gains.  
2. **cuOpt** is moving **open-source**, bringing advanced solvers to the entire optimization community.  
3. Hybrid GPU/CPU solvers (e.g., PDLP + dual simplex) strike a balance between **fast feasibility** and **global optimality**.  
4. Broad **real-world** use cases (logistics, scheduling, supply chain, energy) can leverage these breakthroughs to address **massive** optimization problems in near real time.

