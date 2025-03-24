# Speech AI Demystified Session

**Transcript:** [View on Otter.ai](https://otter.ai/u/uaEm20Z0tm0BAL1DpZSzO4e0Bas?view=transcript)

---

## Overview
This session dives into the **applications** and **technical aspects** of Speech AI. It covers:
- Use cases like **virtual assistants**, **digital avatars**, **car design**, and **robot programming**
- Fundamental components, including **speech recognition**, **synthesis**, **diarization**, **translation**, and **question answering**
- How speech is **encoded** (spectrograms, encoders/decoders)
- **Magpie TTS** (Nvidia’s latest text-to-speech model) using **audio tokens** for high-fidelity voice cloning
- The transition toward **audio-based models** and the importance of **natural voice variations**

---

## Outline

### 1. Introduction and Session Overview
- **Speaker 1** welcomes attendees, reminds them to **mute phones**, and notes that session content will be available on demand via the **GTC app** within 48 hours.
- **Featured Speakers**:
  - **Elena Restor Gayla** (Conversational AI Applied Researcher, Nvidia)  
    - Engineering background and a Master’s degree from the University of Cambridge.
  - **Sven Chilton** (Deep Learning Developer Advocate, Nvidia)  
    - BS from MIT and a PhD from UC Berkeley in nuclear engineering.
- Emphasis on using the **GTC app** to access content and participate in prize draws.

### 2. Applications and Components of Speech AI
- **Speaker 2** highlights various **Speech AI** use cases:
  - **Virtual assistants**, **digital avatars**, **car design**, **robot programming**
- **Key building blocks**:
  - **Speech Recognition** (ASR)
  - **Speech Synthesis** (TTS)
  - **Speaker Diarization**
  - **Speech Translation**
  - **Spoken Question Answering**
- Overview of the **agenda**:
  1. Elena discusses representing speech in computers and speech-to-text systems.
  2. Speaker 2 covers **speech-to-speech pipelines** and how to get started with **Speech AI**.

### 3. Representation of Speech in Computers
- **Speaker 3** explains how computers interpret **sound waves**:
  - **Sound** travels as waves, captured by a **microphone**.
  - **Spectrograms** visually represent frequencies over time.
- Live demonstrations with **pure tones** and **spoken audio** illustrate how audio is digitized into numerical formats.

### 4. Speech-to-Text Systems
- **Typical Flow**:  
  1. **Encoder** transforms complex audio into a **compact vector**.  
  2. **Decoder** maps the vector representation to **text**.
- **Architectures**:
  - **Conformer** and **Fast Conformer** encoders
  - **AED** (Attention-based Encoder-Decoder) decoders
  - **CTC** for faster transcription
- **Performance Metrics**:
  - **Word Error Rate (WER)**
  - **Real-Time Factor (RTF)**
- **Extended Applications**: multi-speaker ASR, speech translation, spoken question answering (e.g., Canary model, speech LLMs).

### 5. Text-to-Speech Systems
- **Evolution** from two-stage (spectrogram intermediate) to **end-to-end** and **LLM-inspired** TTS using **audio tokens**.
- **Audio tokens**: numbers representing chunks of audio signals.
- **Magpie TTS** (Nvidia’s newest model):
  - Generates high-quality, natural-sounding voices.
  - Demonstrated voice **cloning** with impressive accuracy.

### 6. Speech-to-Speech Pipelines
- **Speaker 2**: Building **end-to-end** speech translation:
  1. **Transcribe** audio to text with an ASR.
  2. **Translate** text using an LLM.
  3. **Synthesize** translated text back to audio.
- **James** (a digital human agent) showcased on [build.nvidia.com](https://build.nvidia.com).

#### 6.1 Alternative Pipelines
- **Direct Speech-to-Speech**:
  - Skip explicit transcription, use **speech LMs** on audio tokens for direct translation.
  - Still **early** but promising for a more seamless approach.

### 7. Q&A Highlights
- **Deployment**: Nvidia’s microservices can run on **serverless edge devices** or in **private clouds**.
- **Decoding Spectrograms**: The encoder processes the entire audio; the decoder uses **self-attention** to figure out relevant parts.
- **Realistic Voice Variations**: **Magpie TTS** can capture emotions and subtle inflections better than older systems.

---

