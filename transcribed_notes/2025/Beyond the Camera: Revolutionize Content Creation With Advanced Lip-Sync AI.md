# Beyond the Camera: Revolutionizing Content Creation With Advanced Lip-Sync AI

**Presenter**: Anshul (Co-founder, InVideo AI)  
**Event**: NVIDIA GTC 2025  
**Date**: March 18, 2025  

---

## 1. Introduction to InVideo AI

- **InVideo AI**:
  - Creates publish-ready videos from text prompts.
  - Over **30 million users** across **190+ countries**.
  - Generates fully edited videos (30 seconds to 30 minutes) in multiple languages.
  - Achieved **$65M+ ARR** in the first 18 months.
  - Currently processing **3 new videos per second** (over 6.5 million videos in the last 30 days).

---

## 2. InSyncVideo: The Lip-Sync Model

- **Purpose**:
  - Generate **convincing lip sync** for both **AI-generated** and **real** human characters.
  - Enable **digital twins** from minimal user footage (as little as 12 seconds).
  - Reduce the need for expensive cinematography and facilitate new storytelling possibilities.

### 2.1 Key Features
- Works well for **dubbing existing videos** into multiple languages.
- Integrates with **fully generative content** and digital human avatars.
- Handles **face occlusions**, **lighting changes**, and **movement** reasonably well.

### 2.2 Performance Benchmarks
| Model        | FID ↓  | SSIM ↑ | Sync Conf. ↑ | FVD ↓    |
|--------------|--------|--------|--------------|----------|
| wav2lip      | 14.33  | 0.58   | 8.2          | 304.35   |
| video ReTalking | 10.89 | 0.62   | 7.2          | 207.56   |
| DINet        | 9.2    | 0.66   | 7.4          | 208.93   |
| MuseTalk     | 10.71  | 0.61   | 6.5          | 246.75   |
| latentSync   | 8.06   | 0.66   | 7.83         | 192.74   |
| **InSyncVideo (ours)** | **6.56**   | **0.751**  | **8.03**         | **163.08**   |

*(Lower FID, higher SSIM/Sync Confidence, and lower FVD indicate better performance.)*

---

## 3. Production Deployment Lessons

- **Initial Inference**:
  - Near real-time performance on A100/H100 GPUs in PyTorch.
- **Optimizations**:
  - Custom CUDA kernel for a key operation → **1.8× speed-up**.
  - **ONNX** ~10% faster than base PyTorch.
  - **TensorRT** ~40% faster than base PyTorch.
  - **FP32** used due to visual artifacts with FP16.
- **Scaling**:
  - Working towards seamless integration with existing infrastructure at large scale.

---

## 4. Data Collection Process

- **Early Attempts**:
  - Initial model trained on ~10 hours of data (simple architecture) → Didn’t generalize well.
  - Scaling up to **250 hours** improved results but remained insufficient for production.
- **Data-Driven Approach**:
  - Realized **data quality** and **quantity** were paramount.
  - Deployed **camera crews** to collect **1000s of hours** of diverse, high-quality footage.
  - Built an **internal data curation tool** to ensure top-tier dataset integrity.
- **Outcome**:
  - Over **1000 hours** of curated, high-fidelity video → substantially better lip-sync results.

---

## 5. Model Architecture

### 5.1 Design Goals
1. **High Synchronization Accuracy**  
2. **Efficient Inference**  
3. **Robust to Occlusions**  
4. **Handles Various Lighting Conditions**  

### 5.2 Architecture Components

- **Encoder**:
  - Selective Frame Sampler (explores variations in pose/lip positions).
  - Non-Facial Feature Encoder (helps with background reconstruction).
  - Audio Projection Layer (stronger audio signal processing).

- **Mixer**:
  - Alignment Network + AdaAT (inspired by DINet).
  - Audio Mapping Network (enhances audio signals for generation).

- **Decoder** (GAN-based):
  - Inpainter for mouth/face regions.
  - Multiple discriminators (local + global) for realism, influenced by NVIDIA StyleGAN.
  - Custom SyncNet to ensure lip-sync accuracy.

### 5.3 Lessons Learned
- **Data Quality**: Often trumps architecture choices once training is sufficiently robust.  
- **Architecture & Inference Costs**: Must be carefully balanced for large-scale, real-time demands.  
- **Iterative Refinement**: Multiple architecture iterations led to incremental improvements, but data improvements were decisive.

---

## 6. Future Plans: v4 Release

- **Lip Sync + AI Avatars**:
  - **AI twins** (digital doubles in under 5 minutes).
  - **AI actors** for learning & development, presentations, ads, and more.
- **Continued Focus**: Enhancing realism, efficiency, and user-driven customization for next-gen content creation.

---

## 7. Conclusion & Contact

- **InSyncVideo** transforms AI-generated or user-generated content with high-quality lip sync at scale.
- **Takeaway**: Cutting-edge AI models **rely** on robust data pipelines, specialized architectures, and optimized inference stacks (PyTorch → ONNX → TensorRT).
- **Feedback & Links**:
  - [InVideo](https://invideo.io/)
  - Anshul’s handle: **@_anshulk**  
  - Released at **GTC 2025** (March 18, 2025)

---  

