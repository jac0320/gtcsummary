import streamlit as st


def intro():
    st.markdown(
        """
            👋 Hi there! I am Site Wang. This is a summary of my GTC-2024 conference experience. 
            
            NVIDIA GTC 2024 was NVIDIA's flagship annual conference focused on the latest advancements 
            in AI and other cutting-edge technologies.

            I figured the best to summarize the AI conference is to use AI. Hence, leveraging some rudimentary
            learning of the AI technologies, I built this experience to let people interact with my experience using generative AI. **You can directly ask quesitons through the chat interface below. Or visit each tab to explore more information in details.**
        """
        )

    st.write('---')
    
    st.markdown(f"""        
        * 🏆 **Jensen's Keynote**
            * AI summarized transcripts of tshe keynote delivered by Jensen Huang.
            * You can directly ask "What was so exciting about the Jensen's keynote?" or "In Jensen's keynote, what makes NVIDIA Blackwell so powerful?"
        * 📕 **My Notes**
            * Explore my personal notes about the conference. Nothing too fancy here - [almost] all written by me. 
            * You can directly ask "What are some learnings from Site?" or "How should I evaluate Site's note on Retrieval vs Generation?"
        * 🎙️ **Talks**
            * Some AI Summarized transcripts of the technical talks I attended + Scraped talks of my interest.
            * You can ask "Show me some talks about RAG", given the search results, you can further ask "What is the talk Robotics in the age of Generative AI about?" 
        * 🏢 **Companies**
            * Learn about the companies that participated in the conference.
            * You can ask "What are some companies that handles unstructured data?", given the search results, you can further ask "What does this Unstructured do?"    
        * 🤖 **(Alpha)ViewAgent**
            * An experimental agent that generate code to answer your questions about the conference. It works when it works.
            * You can ask "Generate and execute the code that randomly show two notes written by Site side by side." or "Build the code to show the entire transcript of the main Keynote."
                
        Most importantly, don't be limited by the instructions above. Feel free to ask anything about the conference.
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


def keynote_openai_summary():

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


def notes_summary():

    with st.expander("Retrieval vs. Generative"):
        with open(str('personal_notes/retrieval_vs_generation.md'), "r") as file:
            st.markdown(file.read(), unsafe_allow_html=True)
        st.image('pictures/images/rvg.png', caption='Retrieval vs. Generation', use_column_width='always')
    
    with st.expander("The Need for Scalable Inference"):
        with open(str('personal_notes/the_need_for_scalable_inference.md'), "r") as file:
            st.markdown(file.read())

    with st.expander("The Economics of AI"):
        with open(str('personal_notes/the_economics_of_ai.md'), "r") as file:
            st.markdown(file.read())

    with st.expander("Long-context vs. RAG"):
        with open(str('personal_notes/long_context_vs_rag.md'), "r") as file:
            st.markdown(file.read())
    
    with st.expander("Democratizing AI"):
        with open(str('personal_notes/democratizing_ai.md'), "r") as file:
            st.markdown(file.read())

    with st.expander("The World of Agents"):
        with open(str('personal_notes/the_world_of_agents.md'), "r") as file:
            st.markdown(file.read())

    with st.expander("What the heck is this NIM?"):
        with open(str('personal_notes/what_the_heck_is_this_NIM.md'), "r") as file:
            st.markdown(file.read())

def notes_pictures():

    with st.expander("Show me some pictures!"):
        st.markdown("[Sorry this webpage cannot host this much content...](https://github.com/jac0320/gtcsummary/blob/main/pictures/README.md)")