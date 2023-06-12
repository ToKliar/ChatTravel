# ChatTravel

使用大语言模型制定旅游计划

安装步骤
```
pip install gpt4all
```

上述安装失败的话，本地安装步骤如下
```
git clone --recurse-submodules https://github.com/nomic-ai/gpt4all
cd gpt4all/gpt4all-backend/
mkdir build
cd build
cmake ..
cmake --build . --parallel
cd ../../gpt4all-bindings/python
pip3 install -e .
```

使用步骤
```
from gpt4all import GPT4All

gptj = GPT4All("ggml-gpt4all-j-v1.3-groovy", model_path)
gptj.generate('Name three colors')
```