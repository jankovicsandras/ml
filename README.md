# ML

### Machine Learning, LLM and other Jupyter Notebooks and resources
##### (Newest on top)

----

### [emscripten_wasm_vectordb.ipynb](https://github.com/jankovicsandras/ml/blob/main/emscripten_wasm_vectordb.ipynb)

Webassembly vectordb test. Python test database -> embedding with all-MiniLM-L6-v2 -> building C vectordb program -> Emscripten Wasm compiling -> Python testing with calling Wasmtime.

----

### [LazierMergekit.ipynb](https://github.com/jankovicsandras/ml/blob/main/LazierMergekit.ipynb)

LazyMergekit can create a new LLM by merging weights. LazierMergekit adds Llama.cpp quantization.
Example LLM created with this: [Mindentural-7B-240124](https://huggingface.co/jankovicsandras/Mindentural-7B-240124)

----

### [phi2_all_MiniLM_L6_v2_test.ipynb](https://github.com/jankovicsandras/ml/blob/main/phi2_all_MiniLM_L6_v2_test.ipynb)
### [dolphin_phi2_all_MiniLM_L6_v2_test.ipynb](https://github.com/jankovicsandras/ml/blob/main/dolphin_phi2_all_MiniLM_L6_v2_test.ipynb)

Testing RAG with:
 - Phi-2 and Dolphin Phi-2 LLMs
 - FAISS and a simple custom vectordb
 - embedding model: all-MiniLM-L6-v2

----

### [rwkv_cpp_test.ipynb](https://github.com/jankovicsandras/ml/blob/main/rwkv_cpp_test.ipynb)
Testing [RWKV-LM](https://github.com/BlinkDL/RWKV-LM) / [rwkv.cpp](https://github.com/saharNooby/rwkv.cpp) , using the [RWKV-4-World-3B... model](https://huggingface.co/BlinkDL/rwkv-4-world/tree/main) quantized to Q5_1. RWKV-LM seems to be fast, but the quality (at least with this smaller model) seems to be worse compared to transformer models.

Example:
```
> User: Hva heter fargene i regnbue?
> Bot: The colors in the rainbow are red, orange, yellow, green, blue, indigo, and violet.

> User: 
> Bot: Hello! How can I assist you today?

> User: Hva er 3+2?
> Bot: 3+2 = 5.

> User: Hva er 7*6+5*4?
> Bot: 7*6+5*4 = 35.

> User: How many days are there in three weeks?
> Bot: There are 14 days in three weeks.

> User: Write a poem about reindeers.
> Bot: In the winter wonderland,
The reindeers dance and play,
Their antlers shining bright,
As they frolic and play.
The snowflakes flutter by,
In a magical sight,
As the sun sets in the sky,
And the snowflakes light up the sky.
```

----

### [lc_hf_BERT.ipynb](https://github.com/jankovicsandras/ml/blob/main/lc_hf_BERT.ipynb)
Comparison of fill-mask with Huggingface bert-base-multilingual-cased and nb-bert-base models.

Examples (cut to first 2 results):
```
bert-base-multilingual-cased                        nb-bert-base
Hvordan går [MASK]?                                 Hvordan går [MASK]?
? 0.05671808868646622                               det 0.7175660729408264
det 0.040497686713933945                            du 0.01880013197660446

Det er [MASK] i dag.                                Det er [MASK] i dag.
det 0.16041837632656097                             verre 0.05127672478556633
ikke 0.05124184861779213                            manana 0.034877367317676544

Kroppstemperatur på 40 grader betyr [MASK].         Kroppstemperatur på 40 grader betyr [MASK].
null 0.023636769503355026                           nada 0.2990809381008148
tilsvarende 0.017484165728092194                    mye 0.1012713685631752

[MASK] er veldig fin.                               [MASK] er veldig fin.
Den 0.2882879972457886                              Den 0.18935281038284302
Det 0.06573046743869781                             Han 0.13225464522838593

Jeg liker å [MASK].                                 Jeg liker å [MASK].
være 0.07584870606660843                            danse 0.25082850456237793
han 0.020002491772174835                            spille 0.14404089748859406

Hva kan du seie om [MASK]?                          Hva kan du seie om [MASK]?
om 0.02956273779273033                              det 0.09066858887672424
ting 0.020101193338632584                           saka 0.02837744727730751
```

----

### [rlm2_q5km_gguf_test.ipynb](https://github.com/jankovicsandras/ml/blob/main/rlm2_q5km_gguf_test.ipynb)
Similar to llama2_test.ipynb, using a different model: [rlm2_q5km.gguf](https://huggingface.co/jankovicsandras/Llama-2-13b-chat-norwegian-Q5_K_M-GGUF)
. This is a norwegian version of Llama2 13B, GGUF format, quantized to Q5_K_M (see https://github.com/ggerganov/llama.cpp).

Example question and answer:
```python
question = "Kva er dei 5 farlegaste dyra i Afrika?"
```

```
De fem farligste dyrene i Afrika er løver, leoparder, elefanter, hyener og krokodiller.
```

----

### [CodeLlama_7B_GGUF_Llama_cpp_test.ipynb](https://github.com/jankovicsandras/ml/blob/main/CodeLlama_7B_GGUF_Llama_cpp_test.ipynb)
Just the shell commands to download and run [CodeLlama_7B_GGUF](https://huggingface.co/TheBloke/CodeLlama-7B-GGUF/) with [Llama.cpp](https://github.com/ggerganov/llama.cpp) in interactive mode.

----

### [codellama-12b.ggmlv3.Q5_K_M.bin-test.ipynb](https://github.com/jankovicsandras/ml/blob/main/codellama_12b_ggmlv3_Q5_K_M_bin_test.ipynb)
Similar to llama2_test.ipynb, using a different model: [codellama-13b.ggmlv3.Q5_K_M.bin](https://huggingface.co/TheBloke/CodeLlama-13B-GGML/resolve/main/codellama-13b.ggmlv3.Q5_K_M.bin)

----

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


----

## License

## For external dependencies: see their licenses. For my code:

### The Unlicense / PUBLIC DOMAIN

This is free and unencumbered software released into the public domain.

Anyone is free to copy, modify, publish, use, compile, sell, or
distribute this software, either in source code form or as a compiled
binary, for any purpose, commercial or non-commercial, and by any
means.

In jurisdictions that recognize copyright laws, the author or authors
of this software dedicate any and all copyright interest in the
software to the public domain. We make this dedication for the benefit
of the public at large and to the detriment of our heirs and
successors. We intend this dedication to be an overt act of
relinquishment in perpetuity of all present and future rights to this
software under copyright law.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.

For more information, please refer to [http://unlicense.org](http://unlicense.org)


