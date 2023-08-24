# ML test


### [llama2_test.ipynb](https://github.com/jankovicsandras/ml/blob/main/llama2_test.ipynb)
This is a minimal demo of [LLM question answering](https://en.wikipedia.org/wiki/Large_language_model) "locally" (can work offline, no API key required). Implemented in [Google Colab](https://en.wikipedia.org/wiki/Google_Colab), using [LangChain](https://en.wikipedia.org/wiki/LangChain) and this [Llama2](https://en.wikipedia.org/wiki/LLaMA) model: [huggingface.co/TheBloke/Llama-2-13B-chat-GGML/resolve/main/llama-2-13b-chat.ggmlv3.q2_K.bin](huggingface.co/TheBloke/Llama-2-13B-chat-GGML/resolve/main/llama-2-13b-chat.ggmlv3.q2_K.bin) . This works (as of aug. 2023) in the free version of Google Colab. Downloading the model (required only once per session) takes ca. 5 minutes. Question answering takes ca. 2 minutes.

Example question and answer:
```python
question = "What is the number of the days of the week squared?"
```

```
If we have the number of days in a week, and we square it, what would be the result?

Let's start with the assumption that there are 7 days in a week.

If we take 7 and square it, we get:

7^2 = 7 × 7 = 49

So, the number of days in a week squared is 49.
```
