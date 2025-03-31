**Revisiting NIM after One Year**  

My first session at GTC 2025 was all about auto-scaling inference on NIM (NVIDIA Inference Microservices). Honestly, I’ve barely touched NIM so far—because, let’s face it, most of my personal projects run just fine on vLLM/Ollama. But now I’m intrigued, because even though NVIDIA GPUs often live on some fancy pedestal far from my everyday tasks, NIM seems to make bridging that gap super easy.

Apparently, NIM was first rolled out during GTC 2024, headlined by Jensen Huang himself (naturally). The pitch? “Go from messing around with your AI toy to actually deploying it in production” in just a few clicks. Or, well, a few commands. Here’s what that might look like:

```bash
ngc registry image info --format_type ascii ${Repository}:latest

# Choose a LLM NIM Image from NGC
export IMG_NAME="nvcr.io/nim/meta/llama3-8b-instruct:latest"

# Choose a path on your system to cache the downloaded models
export LOCAL_NIM_CACHE=~/.cache/nim
mkdir -p "$LOCAL_NIM_CACHE"

# Start the LLM NIM
docker run -it --rm --name=Llama3-8B-Instruct \
  --runtime=nvidia \
  --gpus all \
  --shm-size=16GB \
  -e NGC_API_KEY=$NGC_API_KEY \
  -v "$LOCAL_NIM_CACHE:/opt/nim/.cache" \
  -u $(id -u) \
  -p 8000:8000 \
  $IMG_NAME
```

And boom, you get your own LLM, happily running away.  

It was already surprisingly straightforward last year (I might try hooking this up with Lightning AI sometime). Apparently, a bunch of big companies (including all three major cloud providers) now embrace NIM. Fast forward 12 months, and the training session I attended focused on how NIM handles scaling in production. The system is crazy mature for something that debuted a year ago—though it’s not rocket science, and apparently hooking up NIM to your Kubernetes stack for auto-scaling, monitoring, and alerting is just a few lines of commands. (In the modern tech world, a year is practically a lifetime. Don’t remind me how my side projects are still in alpha after three years.)

As an applied engineer, I’m naturally obsessed with inference. Actually serving generative AI stuff to customers can be…frustrating. You don’t want your app to feel clunky and slow. And it needs to be up basically all the time, because people love complaining when it’s not.  

I’m hoping to answer a few questions here:
1. Why should anyone care about inference?
2. What do you really need to know about inference?
3. What did NIM accomplish in the past year?

### Some Not-So-Boring Concepts

- **TTFT (Time-to-First-Token)**: How long does it take before you see that first word pop out?
- **E2E Latency**: The total time from sending a request to getting the entire response.
- **Throughput, Cost, RPS/GPU**: How many requests can you handle per second on a single GPU (and how broke will that leave you)?
- **Concurrency / Batch Size**: Because GPUs love bigger batches…except that can slow down each individual request.

Bigger batch sizes mean higher throughput—sweet if you have a ton of users. But it can also slow down each user’s response. Smaller batches speed up individual replies, but you can’t handle as many users at once. Decisions, decisions.

Then there’s the extra “fun” part: context. How big is your model? Is it a chatbot, a classifier, or something spitting out code? Does your traffic spike like crazy, or is it super steady? Do people prefer streaming token-by-token, or is it more of a batch job? And what GPU are you even using?

### The Reality Check: Auto-Scaling and Cost

Eventually, you’ll find some “sweet spot” for your particular use case…until you outgrow it. Then it’s time to scale. Auto-scaling is not exactly a novel concept—EC2’s been doing it forever—but doing this for GPUs isn’t quite as trivial. GPU scaling requires rules of its own, though the underlying principle is the same: monitor your usage (Prometheus is your buddy here), watch the load, and spin up more GPUs when your app is about to break under the weight of incoming requests. It’s a bit of engineering black magic—but when it all connects, it’s glorious. One moment you see your requests surging, and the next, your GPU cluster automatically bumps up capacity. No frantic Slack messages from your manager at midnight, no meltdown on Reddit.

So why doesn’t everyone do it? Spoiler alert: **cost**. In a magical world where money grows on GPUs, each user would get a dedicated monstrous GPU cluster. If that’s not enough, throw in 10 more. But GPUs are still expensive, especially if you’re running them 24/7. There are data center overheads, insane energy bills, and some sweaty CFO breathing down your neck.

But hey, that’s also what makes inference optimization interesting. If you’ve ever had to tweak algorithms to handle cost/performance trade-offs, you know the feeling: find the right hyperparameters, watch your utilization, keep the latency in check, and don’t make your finance team cry.

### The Future

Is inference going to get cheaper? Eventually, yes—just like how the first computers filled an entire room, and now we carry one around in our pockets for cat memes. Model innovations, better algorithms, hardware improvements…these things keep moving forward. We’re nowhere near peak AI usage yet, and the demand for inference will only keep growing (someone once said “exponentially” with a straight face). But be mindful: don’t lump inference demand in with training. They’re two different beasts.  

So, for all you applied engineers out there (or the people who just want stuff to work so they can watch Netflix in peace): keep an eye on what’s happening in inference land. Cheaper, faster, more reliable inference is coming, but until then, you’ll probably want to keep a close eye on your GPU usage—and your wallet. After all, running the next big chat app on a single GPU might be comfy…until thousands of users show up. Then you can watch NIM do its auto-scaling magic and save you from yet another “why is our app down?” Slack thread. Enjoy!