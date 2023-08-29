# ML test


### [llama2_test.ipynb](https://github.com/jankovicsandras/ml/blob/main/llama2_test.ipynb)
This is a minimal demo of [LLM question answering](https://en.wikipedia.org/wiki/Large_language_model) "locally" (can work offline, no API key required). Implemented in [Google Colab](https://en.wikipedia.org/wiki/Google_Colab), using [LangChain](https://en.wikipedia.org/wiki/LangChain) and this [Llama2](https://en.wikipedia.org/wiki/LLaMA) model: [huggingface.co/TheBloke/Llama-2-13B-chat-GGML/resolve/main/llama-2-13b-chat.ggmlv3.q2_K.bin](huggingface.co/TheBloke/Llama-2-13B-chat-GGML/resolve/main/llama-2-13b-chat.ggmlv3.q2_K.bin) . This works in the free version of Google Colab (as of aug. 2023). Downloading the model takes ca. 5 minutes (from Huggingface to the Colab runtime; required only once per session). Question answering takes ca. 2 minutes.

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

### [codellama-12b.ggmlv3.Q5_K_M.bin-test.ipynb](https://github.com/jankovicsandras/ml/blob/main/codellama_12b_ggmlv3_Q5_K_M_bin_test.ipynb)
Similar to llama2_test.ipynb, using a different model: [codellama-13b.ggmlv3.Q5_K_M.bin](https://huggingface.co/TheBloke/CodeLlama-13B-GGML/resolve/main/codellama-13b.ggmlv3.Q5_K_M.bin)

### [CodeLlama_7B_GGUF_Llama_cpp_test.ipynb](https://github.com/jankovicsandras/ml/blob/main/CodeLlama_7B_GGUF_Llama_cpp_test.ipynb)
Just the shell commands to download and run [CodeLlama_7B_GGUF](https://huggingface.co/TheBloke/CodeLlama-7B-GGUF/) with [Llama.cpp](https://github.com/ggerganov/llama.cpp) in interactive mode.
