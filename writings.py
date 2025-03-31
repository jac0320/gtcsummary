import streamlit as st


def intro():
    st.markdown(
        """
            Hi there! My name is sfcarrot 🥕 and this is about my experience at GTC 2024 & 2025.

            I figured the best to summarize the AI conference is to use AI. Hence, leveraging some rudimentary learnings of how code works, I built this little app to let people interact with GTC though my eyes. 

            **You can directly ask quesitons through the chat interface below. Or visit each tab to explore more information in details.**
        """
        )

    st.write('---')
    
    st.markdown(f"""        
        * 🏆 **Jensen's Keynote**
            * AI summarized transcripts of tshe keynote delivered by Jensen Huang.
            * Try ask "What was so exciting about the Jensen's keynote?" or "In Jensen's keynote, what makes NVIDIA Blackwell so powerful?"
        * 📕 **My Blogs**
            * Explore my personal notes about the conference. Nothing too fancy here - [almost] all written by me. 
            * Try ask "What are some learnings from Site?" or "How should I evaluate Site's note on Retrieval vs Generation?"
        * 🎙️ **Talks**
            * Some AI Summarized transcripts of the technical talks I attended + Scraped talks of my interest.
            * Try ask "Show me some talks about RAG", given the search results, you can further ask "What is the talk Robotics in the age of Generative AI about?" 
        * 🏢 **Companies**
            * Learn about the companies that participated in the conference.
            * Try ask "What are some companies that handles unstructured data?", given the search results, you can further ask "What does this Unstructured do?"    
        * 🤖 **(Alpha) ViewAgent**
            * An experimental agent that generate code to answer your questions about the conference. It works when it works.
            * Try ask "Generate and execute the code that randomly show two notes written by Site side by side." or "Build the code to show the entire transcript of the main Keynote."
    """)


def keynote_perplexity_summary():

    with st.expander("Perplexity's Summary of the Event News Resources 🗞️ [by AI 🤖s]"):
        st.markdown("""
            GTC 2024 was NVIDIA's premier AI conference, showcasing the latest breakthroughs in hardware, software, and services for accelerating AI development. The event kicked off with a keynote by NVIDIA CEO Jensen Huang, where he unveiled the powerful new Blackwell GPUs, including the flagship GB200 chip designed for raw compute gains in AI. 
            Huang emphasized that we have entered the "Era of AI," with accelerated computing being crucial for driving simulations and digital twins across industries. He highlighted NVIDIA's Omniverse platform as the "soul" of the company, enabling collaboration and integration of generative AI for interactive visualization and physics-based rendering. 
            Key announcements included the integration of NVIDIA AI and Omniverse technologies into Siemens' TeamCenter X software for unified engineering data visualization and AI-generated 3D objects/backgrounds. Partnerships with companies like Hyundai for sustainable shipbuilding were also showcased, leveraging Omniverse for massive engineering datasets. 
            NVIDIA positioned itself as a full-stack AI development engine, with offerings spanning hardware like the Blackwell GPUs, software like the Omniverse platform, and services for data management and computing tailored to AI requirements. 
            The conference highlighted NVIDIA's central role in powering the AI revolution across various industries.
        """)


def keynote_2025_openai_summary():

    with st.expander("OpenAI's Summary of the Keynote 🗞️ [by AI 🤖s]"):
        st.markdown("""
# GTC 2025 Keynote Summary

Below is a concise overview of the main topics and announcements Jensen Huang covered during the GTC 2025 keynote.

---

## 1. The Evolution of AI

- **Generative AI**: Emphasis on the industry's transition from perception AI (vision/speech) to generative AI (text-to-anything, amino acids-to-proteins, etc.).  
- **Agentic AI**: New wave of AI systems that can reason step-by-step and plan/execute actions. Major leaps in compute demands stem from these capabilities.  
- **Physical AI & Robotics**: Expansion from purely digital AI to AI that understands and interacts with the physical world (autonomous vehicles, factory robots, etc.).

---

## 2. Surging Demand for AI Infrastructure

- **Scaling Law & Compute**: "Reasoning" tokens can multiply training and inference requirements by as much as 100× vs. previous assumptions.  
- **Data Center Investment**: Data center spending to reach trillions by 2030, shifting toward accelerated computing rather than traditional CPU servers.

---

## 3. New Hardware Roadmap: Blackwell, Reuben, and Beyond

### Blackwell GPU Architecture
- **Full Production**: Blackwell succeeds Hopper with major performance gains.  
- **Disaggregated MVLink 72 & Liquid Cooling**: Separating the NVLink switches from motherboards and liquid cooling each rack to achieve 1 exaflop in a single rack.  
- **Inference Focus**: Up to 40× faster on "reasoning" inference (large-token outputs) vs. Hopper.

### Annual Release Cadence
- **Vera Reuben (2026)**: Introduces next-gen CPU, GPU (CX9), memory (HBM4), and NVLink 144.  
- **Reuben Ultra (2027)**: Scales to NVLink 576, enabling extremely large GPU clusters (hundreds of thousands or millions of GPUs).

---

## 4. Networking Advances

- **Spectrum X + Infiniband**: Making Ethernet behave more like Infiniband with low latency, congestion control, etc.  
- **Silicon Photonics**: 1.6 Tb/s co-packaged photonics that can drastically cut data center transceiver costs and power usage. Crucial to scaling to millions of GPUs.

---

## 5. Full-Stack for Enterprises & Edge

- **DGX Spark**: A compact personal AI workstation featuring a CPU/GPU with 1 petaFLOP of compute.  
- **DGX Station**: A liquid-cooled, 20 petaFLOP "desktop supercomputer" for data scientists.  
- **Edge & 5G**: Partnerships with Cisco, T-Mobile, and more to bring accelerated and AI-driven networking to telecom edges.

---

## 6. AI Software & Frameworks

- **Nvidia Dynamo**: "Operating system" for AI factories, orchestrating model parallelism (pipeline, tensor, expert) and dynamic resource allocation.  
- **Nvidia NIMS**: Open-source AI model framework for advanced reasoning.  
- **Semantic Storage**: Future enterprise storage will continuously embed data (not just store/retrieve) for more intelligent querying.

---

## 7. Robotics & Physical AI

- **Omniverse + Cosmos**: Large-scale synthetic data generation and simulation for robotics training.  
- **Newton Physics Engine**: Partnership among Nvidia, DeepMind, and Disney Research, providing real-time, GPU-accelerated rigid/soft body simulation.  
- **Groot N1**: A dual-system ("fast" vs. "slow" thinking) generalist humanoid-robot model. Announced as open-sourced for developers.

---

## 8. Notable Partnerships & Industry Adoption

- **GM**: Uses Nvidia platforms for next-gen autonomous driving (training, simulation, in-car computation).  
- **Cisco & T-Mobile**: Collaborations on edge AI and 5G radio networks.  
- **Enterprise Ecosystem**: Mentions of Dell, HP, Lenovo, Accenture, SAP, ServiceNow, Box, and more adopting Nvidia's AI infrastructure/software stacks.

---

## 9. Key Takeaways

1. **Massive Growth**: AI computation needs will continue skyrocketing, driven by reasoning-based workloads.  
2. **Nvidia's Full-Stack Approach**: GPUs, CPUs, networking, software frameworks, and digital-twin simulations all aim to create "AI factories."  
3. **Annual Innovation**: New hardware every year, each generation designed to keep pace with exponential AI demands.  
4. **Robotics & Physical AI**: Accelerated physics-based simulation, reinforcement learning, and shared "foundation robot models."  
5. **Broad Industry Impact**: Cloud, enterprise, automotive, manufacturing, telecom—accelerated AI is becoming the default across all segments.

---

        """)


def keynote_2024_openai_summary():

    with st.expander("OpenAI's Summary of the Keynote Transcript 📝 [by AI 🤖]"):

        st.markdown("""
        GTC 2024, hosted by NVIDIA, was a pivotal event that showcased groundbreaking advancements in AI and computing. The conference featured a mix of technical presentations, panels, and discussions that emphasized the transformative potential of AI across various sectors.

        **Key Highlights and Innovations:**

        1. **Blackwell Architecture**: NVIDIA introduced its new Blackwell architecture, which is designed for the generative AI era. This architecture underpins NVIDIA's latest GPUs and is set to boost AI performance significantly, especially for tasks involving massive AI models【7†source】【10†source】.

        2. **Generative AI and Software Development**: NVIDIA's CEO Jensen Huang discussed the shift in software development towards using generative AI. Instead of traditional coding, companies are expected to assemble AI models and manage them through examples and feedback, a process facilitated by NVIDIA's NIMs (NVIDIA Inference Microservices)【7†source】【8†source】.

        3. **Sustainability and Efficiency**: Despite the high power consumption of GPUs, Huang highlighted the efficiency improvements AI can bring, such as more effective battery charging and grid management. These advancements present a net positive impact on energy use and sustainability【8†source】.

        4. **Applications in Diverse Fields**: Panels and discussions at the conference explored AI's role in various domains, from automotive and healthcare to digital media and robotics. For example, the use of AI in drug discovery and patient care was discussed as transforming healthcare delivery【6†source】.

        5. **Networking and Supercomputing Capabilities**: The event showcased enhancements in networking and supercomputing, such as the integration with Quantum-X800 InfiniBand and Spectrum-X800 Ethernet platforms, supporting speeds up to 800Gb/s, crucial for handling extensive AI workloads【10†source】.

        6. **Project Groot and Robotics**: Project Groot was unveiled, marking NVIDIA's venture into humanoid robotics aimed at creating more adaptable and interactive AI systems. This initiative aligns with NVIDIA's broader vision of integrating AI with real-world applications【10†source】.

        The conference not only highlighted technological advances but also emphasized NVIDIA's central role in the AI industry's future, with significant endorsements from major tech leaders and widespread adoption of the Blackwell platform【7†source】【10†source】. Overall, GTC 2024 set the stage for the next leaps in AI technology, promising profound impacts across various industries.
        """)


def display_markdown_with_image(file_path, image_caption=None, image_width=50):
    """Helper function to display markdown content with optional image.
    
    Args:
        file_path (str): Path to the markdown file
        image_caption (str, optional): Caption for the image
        image_width (int, optional): Width of the image as percentage of container width. Defaults to 50.
    """
    with open(str(file_path), "r") as file:
        content = file.read()
        # Split content by image placeholder
        parts = content.split('[IMAGE_PLACEHOLDER:')
        if len(parts) > 1:
            # Display first part
            st.markdown(parts[0], unsafe_allow_html=True)
            # Extract image name and remaining content
            image_name, remaining = parts[1].split(']', 1)
            # Display image with specified width
            col1, col2, col3 = st.columns([(100-image_width)/2, image_width, (100-image_width)/2])
            with col2:
                st.image(f'personal_notes/images/{image_name}', caption=image_caption)
            # Display remaining content
            st.markdown(remaining, unsafe_allow_html=True)
        else:
            st.markdown(content, unsafe_allow_html=True)

def notes_summary():
    st.subheader("2025 Blogs")
    
    # 2025 Blog Posts
    blog_posts_2025 = [
        ("💻 The Vibe of Vibe Coding", "the_vibe_of_vibe_coding.md", "Vibe Coding Twitter from Andrej Karpathy", 50),
        ("🔤 Tokens, Tokens, Tokens", "tokens_tokens_tokens.md", "There Will Be Blood meme", 50)
        ("🤔 How Many A's are There in AAAgent?", "how_many_a_are_there_in_aaagent.md", "Ariel from The Tempest", 50),
        ("🤖 Keeping an Eye on Physical AI", "keeping_an_eye_on_physical_ai.md", "Shakey the robot", 50),
        ("👁️ Vision, Speech, Text and the Rests", "vision_speech_text_and_the_rests.md", "Video Ingestion", 50),
        ("🔄 Revisit NIM After One Year", "revisit_nim_after_one_year.md", None, 50),
    ]

    for title, filename, image_caption, image_width in blog_posts_2025:
        with st.expander(title):
            display_markdown_with_image(f'personal_notes/{filename}', image_caption, image_width)

    st.write('---')
    st.subheader("2024 Blogs")

    # 2024 Blog Posts
    blog_posts_2024 = [
        ("🔄 Retrieval vs Generation", "retrieval_vs_generation.md", None, 50),
        ("❓ What the Heck is This NIM?", "what_the_heck_is_this_NIM.md", None, 50),
        ("📚 Long Context vs RAG", "long_context_vs_rag.md", None, 50),
        ("🌍 Democratizing AI", "democratizing_ai.md", None, 50),
        ("💰 The Economics of AI", "the_economics_of_ai.md", None, 50),
        ("⚡ The Need for Scalable Inference", "the_need_for_scalable_inference.md", None, 50),
        ("🤖 The World of Agents", "the_world_of_agents.md", None, 50)
    ]

    for title, filename, image_caption, image_width in blog_posts_2024:
        with st.expander(title):
            display_markdown_with_image(f'personal_notes/{filename}', image_caption, image_width)
            # Special case for Retrieval vs Generation which has an additional image
            if filename == "retrieval_vs_generation.md":
                col1, col2, col3 = st.columns([25, 50, 25])
                with col2:
                    st.image('pictures/images/rvg.png', caption='Retrieval vs. Generation')

def notes_pictures():

    with st.expander("Show me some pictures!"):
        st.markdown("[Sorry this service cannot host many image content. Using this one](https://github.com/jac0320/gtcsummary/blob/main/pictures/README.md)")