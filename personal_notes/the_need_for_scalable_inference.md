# The Need for Scalable Inference

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

[Written by Site 🤓]