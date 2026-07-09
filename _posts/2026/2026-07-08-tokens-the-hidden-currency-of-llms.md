---
author: vitraag
comments: true
date: 2026-07-08T00:00:00Z
layout: post
slug: tokens-the-hidden-currency-of-llms
title: "Tokens: The Hidden Currency of LLMs"
categories:
    - ai
    - education
---

You've probably hit a token limit error at some point and wondered what a token even is. The model never reads your sentence the way you typed it. It reads **tokens**, small chunks of text that a tokenizer slices your words into before the model gets its hands on anything. Tokens are how these systems see, how they get billed, and why they eventually run out of room to keep listening to you.

This post is the deep-dive version: what a token actually is, why every provider counts them differently, how images and audio get tokenized too, and whether any of this survives the next few years of model design.

---

## What is a token, really?

Not a word. Not a character. Whatever chunk of text a specific tokenizer decided deserved its own slot in the dictionary, usually somewhere between a letter and a full word.

```
"unbelievable" → ["un", "believ", "able"]     (3 tokens)
"ChatGPT"      → ["Chat", "G", "PT"]          (3 tokens)
"👍"           → 1 to 3 tokens depending on the tokenizer
```

Picture an old predictive-text keyboard. There's a shortcut button for "the," another for "ing," maybe even "tion" if you text enough. Common patterns earn a button. Your cousin's unusual last name, a typo, a random string, none of that gets a button, so it's spelled out letter by letter. That keyboard is basically the tokenizer, and every button press is one token.

Nearly every modern tokenizer works the same way, whether it's OpenAI's flavor of Byte Pair Encoding or Google's SentencePiece: start with raw bytes, scan a mountain of training text for whichever pair of tokens appears together most often, merge that pair into a new token, and repeat tens of thousands of times. The result is a compression dictionary trained on the internet. Common stuff gets a short code. Rare stuff gets spelled out the hard way.

That's why `unbelievable` splits into three pieces instead of staying whole. `believ` shows up constantly in training text (believe, believed, believer), so it earned its own token long before the full word "unbelievable" ever did.

---

## Why every provider counts tokens differently

Each company trains its own tokenizer on its own text, with its own vocabulary size. Feed the same sentence to five different models and you'll likely get five different token counts.

| Provider | Tokenizer family | Vocabulary size | How you count it |
|---|---|---|---|
| OpenAI | BPE (`o200k_base`) | ~200K | `tiktoken`, runs locally |
| Anthropic (Claude) | Proprietary BPE | not published | `count_tokens` API call |
| Google (Gemini) | SentencePiece | ~256K | `count_tokens` in the Gemini SDK |
| Meta (Llama 3/4) | BPE, tiktoken-based | ~128K | Hugging Face `tokenizers` |
| Mistral | BPE (tekken / SentencePiece) | ~32K–150K | Hugging Face `tokenizers` |
| DeepSeek (V3) | Byte-level BPE | ~128K | Hugging Face `tokenizers` |
| GLM-4.6 (Zhipu / Z.ai) | Unigram | ~160K | Z.ai tokenizer API / Hugging Face |

Worth noticing: the Chinese labs, DeepSeek and GLM included, both lean toward larger vocabularies and pretokenizers tuned for multilingual compression. English-centric tokenizers tend to waste tokens on Chinese, Japanese, and Korean text, so a bigger, differently-trained vocabulary is a direct fix rather than an accident.

A bigger vocabulary usually means fewer tokens per sentence, since more whole words get a dedicated slot. It also means a heavier model underneath. That's a deliberate trade-off, not a random one.

If you're building on Claude, don't reach for `tiktoken` to estimate token counts. It's OpenAI's tokenizer, and it will undercount Claude tokens by 15 to 20 percent on ordinary English, more on code. Anthropic hasn't published its tokenizer, so `count_tokens` is the only honest number. It also changes between model generations: Sonnet 5's tokenizer runs about 30 percent heavier than Sonnet 4.6's on identical text.

---

## Count tokens yourself

```python
# OpenAI, entirely offline
import tiktoken
enc = tiktoken.encoding_for_model("gpt-4o")
print(len(enc.encode("Tokenization is the hidden currency of LLMs.")))

# Anthropic, via the API (never estimate this with tiktoken)
from anthropic import Anthropic
client = Anthropic()
resp = client.messages.count_tokens(
    model="claude-opus-4-8",
    messages=[{"role": "user", "content": "Tokenization is the hidden currency of LLMs."}],
)
print(resp.input_tokens)

# Open-weight models, via Hugging Face
from transformers import AutoTokenizer
tok = AutoTokenizer.from_pretrained("meta-llama/Llama-3.1-8B")
print(len(tok.encode("Tokenization is the hidden currency of LLMs.")))
```

Run the same sentence through all three and line up the counts. The gap between them is the literal, physical reason identical prompts cost different amounts and fill up a context window at different rates depending on which model is reading.

If you'd rather click than code, two browser tools do this visually:

- **[platform.openai.com/tokenizer](https://platform.openai.com/tokenizer)**, OpenAI's own page. Type a sentence and it comes back color-coded, one color per token.
- **[tiktokenizer.vercel.app](https://tiktokenizer.vercel.app)**, a community tool that switches between GPT, Claude, Llama, and Mistral tokenizers on the same input so you can watch the token boundaries redraw as you change models.

Anthropic hasn't published a web visualizer for Claude, which tracks with the tokenizer itself being unpublished. The `count_tokens` call above is the closest thing to a playground you'll get.

---

## Will tokenizers eventually disappear?

A lot of researchers hope so, and it's genuinely unresolved.

Andrej Karpathy, who's trained models at Tesla, OpenAI, and briefly at Anthropic, made a well-known lecture on this called [Let's Build the GPT Tokenizer](https://www.youtube.com/watch?v=zduSFxRajkE). His argument, roughly: most of a model's strangest failures trace back to tokenization decisions made once, early, by a separate algorithm the language model itself never gets to weigh in on. The strawberry letter-counting problem, shaky arithmetic on long numbers, a model feeling sharp in English and clumsy in Korean for reasons that have nothing to do with understanding. A lot of that traces back to how the tokenizer chopped things up before the model ever saw a sentence.

The alternative some researchers are chasing is tokenizer-free, byte-level modeling: feed the model raw bytes directly and let the network learn its own notion of "chunk" end to end. Early architectures exist. Whether they can match BPE's efficiency at frontier scale is still unresolved, since byte sequences run much longer than token sequences for the same text, and transformers get more expensive as sequences get longer.

So no, tokenizers haven't gone anywhere yet. But the field treats tokenization as a known wart rather than a permanent feature.

---

## Tokens beyond text

Text isn't the only thing that gets tokenized. Multimodal models like GPT-4o, Claude, and Gemini also read images, and increasingly audio and video, and all of it becomes tokens before the model touches it.

**Images** get sliced into a grid of small patches, often 16 by 16 pixels, and each patch is flattened and run through a small network that turns it into a vector. That vector is the image's version of a token. A single photo might turn into a few hundred to a few thousand of these patch tokens depending on resolution. Higher resolution costs more tokens for the same reason a longer paragraph does: more patches, more tokens, more cost. There isn't a mainstream click-and-see visualizer for this the way there is for text, but the [Keras vision transformer tokenization guide](https://keras.io/examples/vision/token_learner/) is a good hands-on walkthrough if you want to see the patches get cut and embedded step by step.

**Audio** works a bit differently again. Rather than patches, models like MusicGen or AudioLM run raw audio through a neural codec (EnCodec, SoundStream) that compresses it into a sequence of discrete codes, and those codes function as audio tokens. Same underlying idea as text BPE: turn a continuous signal into a manageable sequence of discrete symbols a transformer can attend over.

**Video** stretches the image approach across time: sample frames, slice each one into patches, and you get a lot of tokens very fast. That's a big reason video-understanding models cost so much more to run than a plain chatbot.

**What "multimodal" actually means**: text tokens, image patch tokens, and audio codec tokens all get mapped into the same shared vector space, so one transformer can pay attention across all of them at once. A word in your prompt can attend to a patch of your uploaded photo exactly the way it attends to another word. There's no separate vision module handing off a summary to a language module. It's one model, one attention mechanism, reading a mixed sequence of tokens regardless of which modality they came from.

---

## Tokens are your invoice too

Every provider prices by the token, and input and output are usually priced differently since generating text costs more than reading it.

| Model | Input $ / 1M tokens | Output $ / 1M tokens |
|---|---|---|
| Claude Opus 4.8 | $5.00 | $25.00 |
| Claude Sonnet 5 | $3.00 | $15.00 |
| Claude Haiku 4.5 | $1.00 | $5.00 |

*(Anthropic's rates as of this writing, check the pricing page before budgeting against them.)*

The same English sentence can cost different amounts on different models purely from tokenizer differences, before the per-token price even enters the math. Context windows, rate limits, and caching are all denominated in tokens too, so a million-token window doesn't hold a fixed word count. It holds fewer words of French than English, and fewer still of dense code or non-Latin scripts.

---

## A few quirks worth knowing

The "how many Rs are in strawberry" stumper exists largely because of tokenization. The model doesn't see individual letters, it sees two or three sub-word chunks, so counting a specific letter means reasoning about something it can't directly see.

Numbers tokenize inconsistently, which is part of why LLMs historically fumble arithmetic on long figures. Some tokenizers turn `380` into one token but split `3801` into `380` plus `1`. That's pattern-matching over chunks that don't line up with place value, not digit-by-digit math.

Leading whitespace is invisible but never free. `"Hello"` and `" Hello"` are different tokens in most BPE tokenizers, so a stray leading space from a copy-paste quietly inflates your token count.

Non-English text usually costs more, since training data skews English. The same sentence in Hindi or Korean can take two to three times as many tokens as its English equivalent, a real latency and cost tax that rarely shows up in an English-speaking team's testing.

---

## The takeaway

A token is whatever the tokenizer decided to chunk your text into, and every provider trained a different tokenizer with different opinions about what deserves a shortcut. This mechanism is the actual fuel these models run on, and hopefully you now have a better sense of what's in the tank: why the same prompt costs differently across models, why context windows don't map cleanly to word counts, why non-English and code-heavy text costs more, and why counting Claude tokens with `tiktoken` gives you the wrong number every time.

When it actually matters, count with the real tokenizer for the specific model you're calling. Not a guess, and not a rule of thumb from a blog post.
