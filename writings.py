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
            * You can directly ask "What was so exciting about the Jensen's keynote?"
        * 📕 **My Notes**
            * Explore my personal notes about the conference. Nothing fancy here - [almost] all written by me. 
            * You can directly ask "What are some learnings from Site?"
        * 🎙️ **Talks**
            * Some AI Summarized transcripts of the technical talks I attended + Scraped talks of my interest.
            * You can ask "Show me some talks about RAG", given the search results, you can further ask "What is the talk Robotics in the age of Generative AI about?" 
        * 🏢 **Companies**
            * Learn about the companies that participated in the conference.
            * You can ask "What are some companies that handles unstructure data?", given the search results, you can further ask "What does this Unstructured do?"    
        * 🤖 **(Alpha)ViewAgent**
            * An experimental agent that generate code to answer your questions about the conference. It works when it works.
            * You can ask "Randomly choose a note written by Site and show it." or "Can I see all the companies what starts with Letter D?"
                
        Most importantly, don't be limited by the instructions above. Feel free to ask anything about the conference.
    """)


def keynote_perplexity_summary():

    with st.expander("Perplexity's Summary of the Event News Resources 🗞️ [by AI 🤖s]"):
        st.markdown("""
            Jensen Huang's GTC 2024 keynote highlighted several major announcements and developments from NVIDIA:

            NVIDIA's Blackwell Architecture: Huang announced the Blackwell architecture, which he said will accelerate AI products in late 2024. Blackwell is designed to run real-time generative AI on trillion-parameter large language models (LLMs) at 25x less cost and energy compared to current solutions[4].

            NVIDIA GB200 Grace Blackwell Superchip: Alongside the Blackwell GPUs, NVIDIA unveiled the GB200 Grace Blackwell Superchip, which connects multiple Blackwell GPUs[4].

            Partnerships and Integrations: Huang detailed major partnerships and integrations with cloud providers and enterprise companies:

            - NVIDIA's full-stack AI platform will be integrated into Oracle's Enterprise AI[4].
            - AWS will provide access to NVIDIA Grace Blackwell GPU-based Amazon EC2 instances and NVIDIA DGX Cloud with Blackwell[4].
            - NVIDIA will accelerate Google Cloud with the Grace Blackwell AI computing platform and NVIDIA DGX Cloud service[4].
            - Microsoft will adopt the NVIDIA Grace Blackwell Superchip to accelerate Azure[4].
            - Dell will use NVIDIA's AI infrastructure and software, and will eventually incorporate the Grace Blackwell Superchip into its PowerEdge servers[4].
            - SAP will add NVIDIA's retrieval-augmented generation capabilities into its Joule copilot and use NVIDIA NIMs and other joint services[4].

            Other Announcements:
            - NVIDIA announced cuPQC, a library to accelerate post-quantum cryptography[4].
            - NVIDIA unveiled its X800 series of network switches to accelerate AI infrastructure[4].

            The keynote was widely praised, with Bloomberg calling NVIDIA the center stage of the "AI Era"[2] and Forbes describing it as the "Woodstock of AI"[2]. Overall, Huang's keynote showcased NVIDIA's leadership in AI and its deep partnerships across the technology industry[1][2][3][4][5].
        """)


        st.markdown("""
            Citations:
            1. https://www.nvidia.com/gtc/keynote/
            2. https://www.nvidia.com/gtc/
            3. https://www.investopedia.com/what-to-expect-from-nvidia-gpu-technology-conference-2024-8609090
            4. https://www.techrepublic.com/article/nvidia-gtc-2024-keynote/
            5. https://www.technewsworld.com/story/gtc-2024-the-brilliant-insanity-of-nvidias-ceo-and-which-ai-vendors-stood-out-179082.html              
        """)


def keynote_openai_summary():

    with st.expander("OpenAI's Summary of the Keynote Transcript 📝 [by AI 🤖]"):

        st.markdown("""
            The GTC 2024 keynote by Nvidia's CEO Jensen Huang covered a wide range of 
            topics showcasing Nvidia's vision and advancements in AI and computing. Here's a 
            detailed summary of the key points discussed:
        """)

        st.markdown("##### AI's Impact Across Various Domains")
        st.write("""
            Nvidia's AI is portrayed as transformative across multiple sectors, including astronomy, 
            healthcare, energy, robotics, and more. The keynote emphasized AI's role in improving our 
                understanding of the universe, assisting the disabled, revolutionizing energy storage, 
                and enhancing patient care, among other benefits.
        """)

        st.markdown("##### Conference Overview")
        st.write("""
            The GTC event was highlighted as a convergence of experts from diverse scientific fields, 
            aiming to leverage AI for innovative applications such as next-gen 6G technologies and 
            robotic cars. The conference also showcased the involvement of major companies from various 
            industries, emphasizing the broad impact of accelerated computing.
        """)

        st.markdown("##### Nvidia's Journey and Achievements")
        st.write("""
            The keynote touched upon significant milestones in Nvidia's history, from the introduction of 
                CUDA in 2006 to the revolutionary advancements brought about by AlexNet in 2012, the development 
                of the DGX-1 AI supercomputer in 2016, and the emergence of generative AI in 2023.
        """)

        st.markdown("##### The Evolution and Future of AI and Computing")
        st.write("""
            Huang discussed the shift towards generative AI, where computers are used to create new software, 
                offering a novel approach to software development. This section also explored the concept of
                "AI factories" that produce AI models and the potential transformations in various industries 
                due to fundamental changes in computing.
        """)

        st.markdown("##### Partnerships and Collaborations")
        st.write("""
            Nvidia announced collaborations with significant industry players to accelerate their ecosystems 
                and connect them to Nvidia's Omniverse for creating digital twins. Partners include Ansys, 
                Synopsis, TSMC, and Cadence, highlight Nvidia's influence across different sectors.
        """)

        st.markdown("##### Advancements in Large Language Models and AI Supercomputing")
        st.write("""
            The keynote covered the exponential growth of AI models, requiring more substantial computing capabilities. 
                Nvidia introduced a new GPU platform named "Blackwell," designed to cater to the demands of generative 
                AI and large language models.
        """)
        
        st.markdown("##### Nvidia's Vision for AI-Driven Industries")
        st.write("""
            The discussion extended to the transformation of various industries through AI, including weather forecasting 
                with Nvidia's CORDI model, healthcare innovations with Nvidia's BioNeMo, and the development of AI co-pilots 
                for enhancing productivity in chip design and other domains.
        """)

        st.markdown("##### The Future of Robotics and Digital Twins")
        st.write("""
            Huang explored the next wave of robotics powered by AI, requiring a synergy of multiple computing systems
                for training, simulating, and operating robots. Nvidia's Omniverse was presented as a crucial platform 
                for creating sophisticated digital twins for various applications, including industrial and warehouse operations. 
        """)
        
        st.markdown("##### Collaborations with Industry Giants")
        st.write("""
            The keynote concluded with announcements of strategic partnerships with companies like Siemens, aiming to integrate Nvidia's 
                AI and Omniverse technologies into their platforms, thus enabling more efficient and collaborative workflows across industries.
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