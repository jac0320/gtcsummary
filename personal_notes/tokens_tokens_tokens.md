# Tokens, Tokens, Tokens


"Tokens exist only when you look at them." This sentence itself is 8 tokens. It costs money when you use OpenAI's 4o API to generate this sentence.

## Tokens are Free

It sure felt that way at GTC, with Nvidia showing off all their cool projects. There's a feeling that beneath Nvidia lies a reservoir of black gold—tokens endlessly bubbling up from the ground, ready to power innovations.

[IMAGE_PLACEHOLDER:there-will-be-blood-meme.jpg]

The golden solution to building better products, as Jensen Huang demonstrated, is to keep generating more tokens. (I eagerly await the day tokens can solve NP-hard problems.)

Start-up companies desperately hand out tokens to get you hooked on their latest products. They want to show off what they can do with tokens that others can't or won't.

I casually open [chat.com](http://chat.com) daily, generating tokens without thinking much about the $20/month showing up on my credit card statement—until I do. Then I briefly wonder about the cost of tokens popping up on my screen. But the moment I see a newer model on Hacker News, I hop onto that new website and start generating again, even though I could've done the same thing on chat.com. Everything just feels free.

"Tokens exist only when you look at them." This sentence itself is 8 tokens. It costs money when you use OpenAI's 4o API to generate this sentence.


## Tokens are Expensive

Tokens are just numbers, but these numbers come from expensive models and infrastructure. I'm not sure if anyone's paying for the model weights, especially with so many open-source alternatives out there, but infrastructure definitely isn't free.

At work, tokens become a battleground: who gets the best GPU without interruptions to produce tokens that instantly satisfy customers? Tokens equal instant impact. Hence not all tokens are equal for sure.

On personal projects, tokens become painfully expensive, especially when there's no immediate revenue model. It took me three months to realize my React framework was doubling triggering my OpenAI API requests - effectively doubling my costs. Whenever I experiment with new token-based tools, my optimization brain kicks in immediately, searching for ways to cut costs.

Here's a quick cost analysis showing how expensive tokens can get, depending on the GPU used and the models running:

| GPU Type          | Model Example  | Cost per Hour (USD) | Tokens per Second (approx.) | Source |
|-------------------|----------------|---------------------|-----------------------------|--------|
| Nvidia A100       | GPT-4          | $1.00               | 10-30                       | [GPU Rental Costs](https://www.reddit.com/r/LocalLLaMA/comments/1ajnhs1/renting_gpu_time_vast_ai_is_much_more_expensive/) |
| Nvidia H100       | GPT-4o         | $3.00-$3.50         | 20-60                       | [NVIDIA H100 Costs](https://uvation.com/articles/ai-computing-nvidia-h100-and-h200-tensor-core-gpus) |
| Nvidia RTX 4090   | GPT-3.5 Turbo  | $0.80               | N/A          | [LLM Developer Costs](https://www.anyscale.com/blog/num-every-llm-developer-should-know) |
| Cloud TPU v4      | BERT Large     | $3.00               | N/A          | [Cost of Inference](https://blog.dannycastonguay.com/Cost-of-Inference/) |

Maybe there's an economy of scale—more tokens in one place means more efficient infrastructure—but the utilization curve only stretches so far. Will decentralized AI hardware change or eliminate this curve? Too many unanswered questions.

## Tokens are Addictive

It's hard for me to imagine a future without tokens now. I'm constantly obsessed with two questions:

1. Can more tokens solve my problem?
2. Can my problem problem be solvers using fewer and/or cheaper tokens?

I usually don't care which comes first. Tokens alone shouldn't be the focus—things that were complicated 12 months ago now feel essential, thanks to good tooling like Cursor and more.

The demand for tokens will continue to grow, driving improvements in inference and better models. AGI feels distant, but if tokens ever become truly free, that future might actually happen.

Ideally, question #1 would never be a concern. My interactions with AI should simply involve guiding it to the right solution, letting me focus on optimizing costs or watching who else figures out how to do it better.

---

Think of this as Episode 2 of my "Inference" chat from GTC 2024—more casual, less technical. I'm still convinced that better inference will lead us to a brighter future, especially since I'm more interested in practical applications than pure research.

Next year, after attending GTC 2026, I hope to add a third "Tokens" section—though I have no idea yet what I'll write about inference or what inference will become then.
