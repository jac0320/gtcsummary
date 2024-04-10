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
        st.markdown("""
            This was mentioned in the keynote by Jensen Huang. He said
                    
            > The way that computing was done is Retrieval, you would grab your phone and touch something. And some signals go off basically
            to some source somewhere that is PRE-RECORDED content somebody wrote, like a story, image, or video. Then Pre-recorded content is streamed back to the phone and recomposed in a way based on a recommender system to present the information to you. The future of the vast majority of the content will not be retrieved and the reason is those pre-recorded content was made by somebody 
            who doesn't understand the context which is the reason why we retrieve so much content. If you can work with an AI that understands the context, like who you are, for what reason you're fetching this information, and produce the information for you just the way you like it. The amount of energy we save, the amount of resource we save, the amount of wasted time we save will be tremendous."
                    
            Take the following example when I want to know which fasteners (diameter and length) to use for an outdoor deck with 2x6 redwood:
            
            1. My first try was to look it up on Google, but I ended up on several DIY websites. The overwhelming number of ads made it tough to find the information I needed.
            2. I tried watching a tutorial on YouTube. It was a 10-minute video. Nah, who knows if it has my answer or not? I am too impatient.
            3. Then I hopped on perplexity.ai and asked the same questions, and I got the AI-generated answer in less than 5 seconds (with references).
            
            What struck me was how the AI seemed to intuitively understand what I was looking for amidst a sea of diverse information. While I still value the depth and quality of pre-recorded tutorials and guides, I'm increasingly convinced of the potential of generative AI. It's about connecting people with the right information in the right context - and that's where I put my money at.
            
            [Written by Human 🤓]
        """)
    
    with st.expander("The Need for Scalable Inference"):
        st.markdown("""
            Nvidia is really up their game with their FP4/FP6/FP8 performance with Blackwell GPU. feeling a bit puzzled by all these "FPs"? Don't worry; it's simpler than it sounds.
            
            Think of FP-X as a sort of 'size' for the data points the GPU handles - kind of like choosing the right-sized container for your leftovers. The "X" in FP-X tells you how big that container is. A bigger number means you're getting more detail (precision) but at the cost of needing more space and time (memory bandwidth and slower processing). On the flip side, a smaller number means less detail, but you save on space and speed things up.
                            
            Now, it is important to note that we are talking about inference here, not training. Inference is the process of using a trained model to make predictions on new data. And hence, the majority of the applications, are driven by a bunch of inference. Hence, the speed of inference is crucial for real-time applications. For example:
                    
            * If you want to deploy a large model on a robot for it to complete a series of tasks based on a high-level commander, you want the inference to be as fast as possible. 
            * The self-driving vehicle needs to make real-time decisions based on the input from the sensors. And you don't want your model still running after running over a pedestrian. The faster the inference, the safer this vehicle maneuvers. 
            * Phone support agent system using LLM: you want your support agent model to have fast inference to respond to the customer on the phone in a very natural and human-like way.
                    
            But here's the catch: speed isn't everything. As AI gets more advanced and takes on more tasks, it's going to gobble up more power. Imagine having a top-notch AI support agent that answers customers flawlessly but drains so much power that the costs go through the roof - not exactly ideal for business.
                    
            Hence, the crucial demand for scalable inference is to have a:
            * Fast Computation (driven by cloud/local architecture, algorithm, and hardware)
            * Cheaper Operations (energy, infra, and maintenance)
            
            So who do you think runs a better game here?
            
            [Written by Human 🤓]
        """)

    with st.expander("The Economics of AI"):
        st.markdown("""
            I was chatting with bria.ai, which is a visual generative AI platform for creators, and we got into this discussion about how much to train a model. They have a multimodal model that is claimed to be trained from the ground up. For that, it took 280 A100 for 2 weeks to train the model. And if you go to lambdalabs.com to rent an A100, it will cost you \$2.5 per hr. So, the total cost to train the model once is \$2.5 per hr x 280 x 24 x 14 = \$235k
            
            So, let's do some math. If you've got 10k users forking over $10 each month, you'd break even on just the training cost in a smidge over two months. That's not even touching the iceberg of data costs, salaries, marketing... you get the point.
                    
            So what'd a start-up do?:
            1. Hack up the price? Sure, if you want to put the breaks on growth and enjoy the melodious screams of your VCs.
            2. Figure out more growth as MidJourney riding the AI hype with their 1.5M-2.6M active users. Tempting, with all that AI mania money floating around.
            3. Or maybe, just maybe, use some of that sweet investor cash to bring in the brainiacs who can fine-tune the model, cutting costs without skimping on quality. Sounds smart, right?
    
            I could be naive but I'd bet option 2 is the easiest way to go now with the all AI hype that floods \$\$\$ into the AI startups. But eventually, option 3 is the option that leads you into the final round of the sustainable business game.
                    
            And let's not forget the AI value debate. Sure, for complex, creative tasks, AI's a no-brainer, outperforming traditional code by achieving something that regular logic just couldn't handle at scale. But for the simple stuff? It's a harder sell. Why go AI for a task as simple as 1+1 (using \$\$ inference) when a basic function would do the trick unless you're keen on splurging on software engineering talent?
                    
            Yet, there's a twist. Even for these 'simple' tasks, when you bundle them up and look at the big picture, AI starts making a whole lot of sense. What matters is the value of integrated automation. Your SWEs built a good abstraction and architecture for a platform to be scalable. AI can help augment/maintain the system with less cost and less time from people. And this is where the value of AI comes in for even simpler tasks. Independently, simpler tasks are not worth the cost of AI, but when you integrate them, the table can be turned. 
            
            So, it's not just about the hefty upfront cost of training an AI model. It's about weighing the ongoing costs (infrastructure, maintenance, talent, etc.) against the value AI brings in terms of customizable, integrated automation. Don't fire all your SWEs. Have AI augment their lives and support them in maintaining the system to free up their tedious on-call live at least.
                                        
            [Written by Human 🤓]
        """)

    with st.expander("Long-context vs. RAG"):
        st.markdown("""
            Everyone is doing RAG. Literally, everyone. RAG is a model that is designed to retrieve the section information from a long and dedicated context, and then use it to generate the answer. Think of it as an open-book exam. You have a book that contains all the information you need to answer the question. You read the book, then you answer the question. 
                    
            In my opinion, the key to a successful RAG model is the quality of the context. And for a business model, it is about the proprietary data that each company has - the documentation. Documentation quality and quantitive is a necessary condition for a successful RAG. Sufficiently, you will also need a good generative algorithm to generate the answer, which incorporates context retrieval tuning, structured LLM prompt engineering, and strong validation schemas. There is no shortage of papers on how to do this since the framework is cost-effective and easy to implement. In the technical talks, I have seen quite a few companies trying to apply RAG internally. Companies like LlamaIndex, Perplexity, and Glen all build part of their business pillars based on a RAG framework. I don't doubt the potential of RAG, but is RAG the only way to go?
            
            No. Long-context model stands as another viable option. Long context is a model that is designed to take a long context and generate the answer (Google has the >1M token model). Think of it as a closed-book exam. You have a book that contains all the information you need to answer the question. You "memorize" the book, and then you answer the question. As these models tend to be a lot harder and more to train, the key to a long-context model is your machine learning engineers + enough capital. It can outperform RAG on certain tasks like handling complex queries and constructing detailed narratives.
                    
            Is it an either-or situation? Not necessarily. Some studies found RAG combined with a 32k-token LLM can outperform providing full context directly to the LLM. In my chat with few friends, all agreed that RAG is not going away any time soon. The understanding of both RAG and the long-context model is still early. The best track is to keep trying and learning.
                    
            [Written by Human 🤓]
        """)
    
    with st.expander("Democratizing AI"):
        st.markdown(
            """
            Ironically, the first person to mention the term "democratizing AI" was OpenAI's COO Brad Lightcap. He emphasized the importance of enabling a wide range of users to leverage AI technologies for diverse applications. To me, that almost sounds like "We should scoop more users from Google into our closed environment". On the other hand, Mistral, which company open-sources a high-quality smaller talked about how to give AI to users' hands without mentioning "Democratizing AI" once for 45 minutes.

            Jokes aside, my takeaways on Democratizing AI is about two things:
            1. Enable more people to use and benefit from AI in a non-harms way
            2. Don't have AI controlled by a few powerful entities
            At least, I am convinced that this will be my mission in helping people build AI products.
            
            Often the time, I ran into such discussion on how can AI solve this question. And I'd always answer, it may not. But, let's think it through. What is the rule of thumb that you may consider AI:
            1. **Does your problem have some sort of pattern?** For example, is your task somehow repetitive but not the same every time you do it? Like reply an email, classifying a document, or categorizing a file into the Box folder.
            2. **Does your decision require some logic that cannot be explicitly written?** For example, the email you are reading does not always follow the same pattern, but you can tell if it is spam or not. Or, the document you are reading does not always have the same structure, but you can tell if it is a legal document or not.
            
            if you answer yes/maybe to both questions, then you may consider using AI. And if you don't know how to use it, I can help people learn about what AI can do and how to leverage it based on my knowledge and experience. I won't be able to solve all the problems, but I can help you think through the problem and see if you can build an AI solution. Maybe my future wish is to give people the platform to build AI without knowing how to code. But, that is a long way to go. Or is it?

            [Written by Human 🤓]
            """
        )

    with st.expander("The World of Agents and Simulation"):
        st.markdown("""
            Two days before I wrote this sentence down, this paper called [More Agents Is All You Need](https://arxiv.org/pdf/2402.05120.pdf) came out. Besides these, there are about 7 blogs in my reading list talking about Agents. There are also people using [AI agents build Operating Systems](https://github.com/agiresearch/AIOS). And I just finished talking to a start-up that leverages agents to automate website browsing flows. Last weekend, I boarded my wife to death while discussing how I am thinking about a critic agent that leverages bigger models to tame lower-level agents to prompt task success rate. Hopefully, you get the idea at this point.
                    
            But, interestingly, when you hop on perplexity and ask what is an AI agent it will tell you:
            > Based on the search results, there does not appear to be a clear, defined "AI agent framework" being discussed. The sources cover various topics related to AI, intelligent agents, and their potential applications, but do not describe a specific framework or approach.
            
            My take on an AI agent is an inference unit that can perform one or a series of tasks subject to a pre-defined goal. Keeping it at a high level, the AI agent is software that can do things for you. It can be as simple as a chatbot that can answer your questions, or as complex as a robot that can do your laundry. The key is to define the **goal** and **decompose** that goal into logical steps (note that the logical steps are not fixed, as there can be many ways to complete the goal. You can think of an agent designed solely to generate a series of tasks. And this other agent is designed to attribute these tasks to dedicated agents. Then some agents are critical of the workflow and may ask certain parts to be re-done and observe an alternative. And you have other agents helping you summarize and validate the outcome. As the tasks differ, the models/prompts/logic designed for each agent can be different. Here, there is your army of minions, please be the best villain and go dominate the world. 
                    
            At this point, you don't want all of your agents to sit on top of an OpenAI API as it can be \$\$\$ when you turn on the machine. It becomes fascinating to leverage a variety of different models, fine-tuned/pre-trained on specific tasks, to drive down your cost of operation. And to let this system run, you will also need scalable inference... wait a second... am I recalling my previous section now? It must be important.
                    
            [Written by Human 🤓]
        """)

    with st.expander("What the heck is this NIM?"):
        st.markdown("""
            NIM is everything you'd want to enterprise AI. It optimizes a bunch of things for you. It is like a magic box that you can put your AI model in and it will run faster and cheaper.... as long as you buy the hardware from NVIDIA. Feel free to read below if you want to continue [Written by Human 🤓 until here and summarized by AI 🤖 below):
            
            NIM is a powerful tool from NVIDIA that helps organizations accelerate their journey to production AI. It is designed to bridge the gap between the complex world of AI development and the operational needs of enterprises.
                    
            NIM provides optimized inference microservices that allow developers to access AI models through industry-standard APIs. This simplifies the development and deployment of AI applications, enabling rapid scaling within enterprises.
                    
            NIM packages domain-specific NVIDIA CUDA libraries and specialized code tailored to various domains like language, speech, video processing, healthcare, and more. This ensures the AI applications are accurate and relevant to their specific use cases.
                    
            NIM leverages optimized inference engines for each model and hardware setup, providing the best possible latency and throughput on accelerated infrastructure. This reduces the cost of running inference workloads as they scale. 

            NIM is part of the NVIDIA AI Enterprise software platform, which provides enterprise-grade AI capabilities. It allows developers to experiment with NIM microservices and deploy production-grade NIM microservices on various NVIDIA-powered environments. 
        """)

def notes_pictures():

    with st.expander("Show me some pictures!"):
        st.markdown("[Sorry this webpage cannot host this much content...](https://github.com/jac0320/gtcsummary/blob/main/pictures/README.md)")