# Vision, Speech, Text, and What else?

## Did I mention who won the arms race?

Nah. Doesn't even matter anymore. Everyone's throwing their best models into the ring and honestly, good for us—we now have more powerful tools for way more useful (and weirdly specific) applications.

I think it all started when **Sora** came out swinging and spooked Google enough to throw Gemini into fifth gear. On my way home that day, I had this random-but-useful idea:  
**"Descriptive notifications for my Ring camera."**  

Because, let me tell you, Ring notifications are *something else*. I get bombarded with them daily. Half the time it's my wife just wandering around our garden, which somehow generates like 6 different alerts. The other half is people walking past our front door like it's Times Square.  
What if the notifications actually said things like:

- "A casually dressed woman (who appears to be working from home) is strolling in your garden."  
- "A bird just landed on your mailbox. Harmless vibes."  
- "Mailman dropped a package with the care of a bedtime story."  
- "There's a very angry dude at your front door. He's holding a machete. Might wanna check that."

Tell me that's not a solid hackathon idea.

Cut to GTC 2025, I was sitting in the **AI Agents for Real-Time Video Understanding and Summarization** talk. And yeah—it's all real now. These folks are doing sorcery with video clips. Let's talk numbers for a second:

- **60-min video summary in 30 seconds**  
- **Q&A-ready in 50 seconds**  
...With the catch being it's powered by:
- 8× H100s (~$200K just for the GPUs)
- 192 kWh/day → ~$1K/month on power
- Data center cooling (~1.5K/month if you assume 1.75 PUE)
- Hosting costs? Around $2K/month

So yeah, it's fast. But it's also, like, "mortgage a second house" expensive.

---

[IMAGE_PLACEHOLDER:video_ingestion.jpeg]

---

## Use cases? Plenty. And some are pretty dope:

- **ASOCS**: forklift, AGV, drone awareness in factories  
- **VAST**: analyzing sports videos (aka reading LeBron's mind in real-time)  
- **DataRobot**: supply chain logistics (because of course)  
- **ITMAX**: multi-modal traffic event response scheduling  
- **Linker Vision**: real-time incident alerts  
- **Accenture**: real-time disaster assessment through their NAV AI platform  
- **Reka AI**: watching warehouses/shops with multimodal AI  
- **Some managers**: yeah... they're trying to use this to track how "efficient" workers are (lol okay, very chill)

All of this? Very cool in demos. Very powerful in practice. But here's the thing—

Not everything needs to be multimodal.

Yes, that sounds obvious. But you'd be surprised. Just because your production line has cameras doesn't mean you need an LLM + vision + audio + haptics model to check if a screw's in the wrong place. Maybe a simple image classifier does the trick. Maybe just RFID.

Sure, there's no shortage of models out there—some of which can reduce costs dramatically. But we need to *actually think* before reaching for the biggest hammer in the toolbox. It's too easy to say "multimodal" when we really just mean "overkill."

---

Where this gets *really* interesting is how these multi-modal models start feeding into **Physical AI**—especially for training embodied agents (a.k.a. general-purpose robots). Think about it: we now have systems that can interpret YouTube videos, learn how humans interact with the physical world, and then use that data to train robotic systems.  

Simulations? Check. Reinforcement learning? Check.  
Data showing how humans use appliances, walk through doors, pour wine? Coming in hot.  

This whole pipeline—from video summarization to robot training—is laying out a long, long runway for the kind of robots we only see in sci-fi. And while we're not in Westworld yet, we're definitely building the airport.

So yeah—I'm watching closely.