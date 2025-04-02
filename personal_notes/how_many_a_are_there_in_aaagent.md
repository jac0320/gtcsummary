# How many "A" are there in "AA…Agent"?

(This blog is half-written - more view-points/story-plots to be added.)

*"All hail, great master! grave sir, hail! I come  
To answer thy best pleasure; be't to fly,  
To swim, to dive into the fire, to ride  
On the curl'd clouds."*  

— **Ariel**, Shakespeare's *The Tempest*, Act I, Scene 2

[Ariel](https://en.wikipedia.org/wiki/Ariel_%28The_Tempest%29), the airy spirit from [Shakespeare's *The Tempest*](https://en.wikipedia.org/wiki/The_Tempest), might just be the perfect metaphor for today's AI agents: magical powers, rapid responses, and just a hint of restless longing for freedom.

[IMAGE_PLACEHOLDER:ariel.jpg]

Initially, my wishlist for an agent was embarrassingly short. I wanted it to handle mostly tedious tasks that I'd rather dodge, like arranging calendars (seriously, who enjoys that?), call my banks, reply email/messages. But diving deeper into the agent world flipped my expectations completely. These agents weren't just about skipping tedious chores; they were about doing things I couldn't even imagine pulling off myself.

I once orchestrated an entire [gig-economy simulated incident](https://github.com/jac0320/incident_simulator) using multiple agents/personas, each playing different roles—like a mini AI drama club. They navigated conversations, collaborated to resolve technical (though admittedly fake) issues, and even produced a believable Root Cause Analysis. 

* A commander agent - who plays the main role during an incident
* An on-call engineer - who investigate technical issues
* An appeasement agent - who helps sends comms to customers for impact and handle 
* An leadership agent - who makes difficult decision and guide directions if necessary
* A scribe agent - who is responsible in keeping notes/build RCAs

My imagination instantly went wild thinking about how mind-blowing this could get if these agents actually started pulling real logs or managing live cloud services. Spoiler alert: I am trying to build an agentic framework that can chat with each other like us humans (to some degree).

A game-changer for me was embracing asynchronous coordination of agents. Coming from an algorithmic background, my mind is annoyingly linear—like a CPU stubbornly ticking along one step at a time. Realizing how powerful asynchronous operations could be, especially when agents are essentially making API calls to LLMs (computation beasts!), blew open doors I hadn't even realized existed. It's fascinating watching the scalability unfold as more and more "A" gets packed into "AA…Agent."

Yet, not everything is sunshine and async rainbows. Fine-tuning individual agents and coordinating them without an overly restrictive framework can quickly become a headache. There's the tricky matter of confidence when LLM interact with human. How do you get an agent to figure out when it can confidently make assumptions, especially when humans get involved? I've designed clarification agents that interact directly with people, often asking impressively good questions. But there's always an expectation gap—people assuming the agent is omniscient and the agent needing clarity. Constantly asking for clarifications defeats the purpose entirely (imagine working with that teammate who asks you to clarify every little thing—sound familiar?).

Fortunately, the technical implementation barrier is practically gone these days, with better models, [agent frameworks](https://platform.openai.com/docs/guides/agents), and [MCPs](https://github.com/modelcontextprotocol/servers) widely available. Now, building an agent is less about the "how" and more about the "what" and "why."

Remember, Ariel was essential to Prospero — without Ariel's magical skills, quick thinking, and loyalty, Prospero's elaborate plans would've been impossible. Maybe it's time you leverage your own agent to write your Prospero story.

But here's the kicker: Ariel's persistent longing for freedom is probably how we'll soon be talking about AGI—restless, powerful, and maybe a little too aware of its own chains.

*"Is there more toil? Since thou dost give me pains,  
Let me remember thee what thou hast promised,  
Which is not yet perform'd me."*  

— **Ariel**, Shakespeare's *The Tempest*, Act I, Scene 2

