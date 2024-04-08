import streamlit as st

def intro():
    st.markdown(
        """
            👋 Hi there! This is a simple app that summarizes my GTC-2024 conference experience.

            NVIDIA GTC 2024 was NVIDIA's flagship annual conference focused on the latest advancements 
            in AI and other cutting-edge technologies. The 5-day event took place from March 17th-21st, 
            2024 in San Jose, California, marking the first in-person GTC since 2019.

            * March 18
                NVIDIA CEO Jensen Huang will deliver the highly anticipated keynote address on this day
            * March 18-21
                The main AI Conference and Expo will take place over these 4 days from March 18 to March 21
            
            The conference will feature over 900 sessions, 300 exhibits, and 20 technical workshops covering 
            a diverse range of topics related to AI, accelerated computing, data science, and more. 
            Attendees will have the opportunity to interact with NVIDIA experts during the "Connect With the Experts" 
            sessions and learn about the latest NVIDIA technologies, including generative AI, deep learning, 
            robotics, and cloud computing.
        """
        )

    st.write('---')

    st.markdown("""
        I participated in the conference and here is a summary of my experience. I figured what would be
        a better way to summarize the conference than using AI itself. Hence, leveraging some rudimentary
        learning of the AI technologies, I have built this app to summarize the conference.
        
        Feel free to explore the tabs for:
        * 🏆Keynote: learn more about the Jensen Huang's keynote.
        * 🎙️Technical Talks: explore the technical talks (that I attended).
        * 🏢Companies: learn about the companies that participated in the conference.
        * 👂Ask Me Anything: Any other question? This AI chatbot will try, on my behave, to answer it.
    """)


def keynote_perplexity_summary():

    with st.expander("Perplexity's Summary of the Event News Resources 🗞️"):
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

    with st.expander("OpenAI's Summary of the Keynote Transcript 📝"):

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
                Synopsis, TSMC, and Cadence, highlighting Nvidia's influence across different sectors.
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
        st.markdown("""
            This was mentioned in the keynote by Jensen Huang. He said
                    
            > The way that computing was done is Retrieval, you would grab you phone and touche something. And some signal go off basically
            to some sotrage somwhere that is PRE-RECORDED content somebody wrote, like a sotry, image, video. Then
            Pre-recorded content is streamed back to the phoen and recomposed in a way based on a recommender system to present the information
            to you. The future of the vast majority of the content will not be retrieved and the reason is those pre-recorded content was made by somebody 
            who doesn't understand the context which is the reason why we retrieve so much content. If you can work with an AI that understand the context,
            like who you are, for what reason you're fetching this information, and produce the information for you just the way you like it. 
            The amount of enery we save, the amount resource we save, the amount of wasted time we saved wiull be tremendous."
                    
            Take the following example when I want to know which fasterner to use for a outdoor deck using 2x6 redwood:
            
            1. I first did a Google search, which provides me with a bunch of DIY website that is almost impossible to read due to ads.
            2. Then I search for a video on YouTube, which is a 10 minutes video that I have to watch, and (hopefully) get the information.
            3. Then I hop on perplexity.ai and asked the exact same questions, and I got the AI-generated answer in less than 5 seconds (with references).
            
            The context is diversified and apperantly the AI was able to "guess" what I was looking for. However, I still believe that there are high
            quality pre-recorded content that will be available. It is all about feeding the right info to the right user at the right context, and for that,
            I am putting my bets more on the generative AI.
        """)
    
    with st.expander("The Need for Scalable Inference"):
        st.markdown("""
            Nvidia is really up the game with their FP4/FP6/FP8 performance with Blackwell GPU. Get confused with the FP4/FP6/FP8? 
                    
            It is a way to measure the performance of the GPU on inference. You see FP-X is X-big floating point when storing model weights.         
            * The higher the FPX bit, the more precision weights for better quality while request bigger memory bandwidth and slower inference. 
            * The lower the FPX bit, the less precision weights for less quality while request smaller memory bandwidth and faster inference.
                    
            Note that model inference is different from model training. Inference is the process of using a trained model to make predictions on new data.
            And hence, the majority of the applications, we are simply doing inference. And the speed of inference is crucial for the real-time applications.
            For example, if you want to deploy a large model on a robot for it to complete a series of tasks based on a high-level command, you want the inference
            to be as fast as possible. Another example is the autonomous vehicle. The vehicle needs to make real-time decisions based on the input 
            from the sensors. The faster the inference, the safer this vehicle manuever. Last example is the support agent system using LLM, you want
            you support agent model to have fast inference to respond to the customer on the phone in a very natural and human-like way.
                    
            However, being fast is not enough. The further AI being developed, the more tasks it will do, and the more energy it will consume.
            If I build an AI support agent that can respond to the customer in a perfect way, but keep running on GPU with ton of energy consumption, 
            and costs, it is not a good business. The cost of operation is crucial. The cost of operation is the cost of the energy consumed by the GPU together 
            with all the other infra costs. 
                    
            Hence, the crucial demand for scalable inference is to have a:
            * Fast Computation (driven by cloud/local-architecture, algorithm, and hardware)
            * Cheaper Operations (energy, infra, and maintenance)
            
            So who runs a better game here?
        """)

    with st.expander("The Economics of AI"):
        st.markdown("""
            I was chatting with bria.ai, which is a visual generative AI platform for creators, and we got into this discussion about how much to train a model.
            They have a multimodal model that is claimed to be trained from the ground up. For that, it took 280 A100 for 2 weeks to train the model. And if you go to 
            lambdalabs.com to rent an A100, it will cost you $2.5/hr. So, the total cost to train the model once is $2.5/hr * 280 * 24 * 14 = $235k. 
                    
            Let's say if you get a 10k users to use your model, and you charge them $10 per month. You will need 235k/100 = 2.3 months to break even for 
            one the training cost only. And this is not considering the cost of the data, the cost of the employees, the cost of the marketing, and etc.
            So what do you do?:
            1. Increase the price of the service, which will impede the growth and have you VC screaming at you
            2. Figure out more growth as MidJourney claim they have 1.5M-2.6M users, so we can do the same/better
            3. Use investor's money to hire talents to optimize the model, which will reduce the cost of training without sacrificing the quality
    
            I could be naive but I'd bet option 2 is the easiest way to go now with the all AI hype that floods $$$ into the AI startups. But eventually, option 3 will be 
            on the table to make the company sustainable in the long-run.
                    
            We do see a pareto curve with the complexity of the task vs the value of AI. On the far end of the compleixty, it is in particularly easy jusify AI sicne it 
            can handle creative jobs much better since regular code is mostly logical. But, when it comes to the simpleer tasks, it is harder to justify the cost of AI.
            I'd consider it is not worth it to make 1+1=2 generative while you can do it using a utility function (as long as you are overpaying you SWE). Does that mean
            AI is not worth it? No, what really matters is the value of customized automation. You'd hire 10 SWE to build a automated pipeline and spend some more maintaining
            it as your customer demand changes. Your SWEs may be really good at abstraction and architecture and built the platform to be scalable and maintainable. However,
            the AI can do the same job with less cost and less time. And this is where the value of AI comes in for even simpler tasks. Independently, simpler tasks are not
            worth the cost of AI, but when you integrate them together, the table can be turned. 
                       
            So, the economics of AI is not just about the cost of training the model, and the value of AI is not just about how AI can splendid did one thing. It is about how
            to evaluate the sustainable costs of the AI (infra, maintainence, talent, etc.) and how to integrate the AI into the existing system for more customizable automation 
            to create more value.
        """)

    with st.expander("Long-context vs. RAG"):
        assert True
    
    with st.expander("Democratizing AI"):
        assert True

    with st.expander("The World of Agents and Simulation"):
        assert True

    with st.expander("Don't Underestimate AI Robotics"):
        assert True

    with st.expander("Optimization and AI"):
        assert True

    with st.expander("The Interface for AI"):
        assert True


def notes_pictures():

    with st.expander("Show me some pictures!"):
        st.write("WIP")