# 学习资料助手

这是一个基于 **LangChain** 和大语言模型的小型智能应用。输入学习资料后，可以生成中文要点总结，或针对资料提问。应用通过 LangChain 的提示模板、聊天模型和输出解析器组成处理链。

## 功能

- 总结粘贴的课程笔记或文章，输出 3～5 个要点。
- 根据粘贴的资料回答问题；资料未提及时提示用户。
- 支持在线 OpenAI 模型和本地 Ollama 模型，两种方式任选其一。

## 环境要求

- Python 3.10 或更新版本。
- 在线方式：OpenAI API Key、可访问 OpenAI API 的网络。调用在线模型可能产生费用。
- 本地方式：[Ollama](https://ollama.com/) 和已下载的模型。本地模型运行需要一定内存。

## 运行方法

在项目目录中执行：

```bash
python -m venv .venv
```

Windows PowerShell：

```powershell
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
streamlit run app.py
```

macOS / Linux：

```bash
source .venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

浏览器会打开应用页面，通常是 `http://localhost:8501`。

### 在线模型

侧边栏选择“在线 OpenAI”，输入模型名称和自己的 API Key。示例模型名称为 `gpt-4o-mini`；请确保你的账号有调用该模型的权限。API Key 只用于当前请求，不写入仓库。

### 本地模型

安装并启动 Ollama，然后在终端运行：

```bash
ollama pull qwen2.5:3b
```

侧边栏选择“本地 Ollama”，模型名称填 `qwen2.5:3b`。如果已经安装其他 Ollama 模型，也可以填写对应名称。

## 使用示例

资料：`光合作用是绿色植物利用光能，将二氧化碳和水转化为有机物，并释放氧气的过程。`

- 选择“总结”，可得到光合作用的要点。
- 选择“提问”并输入“光合作用释放什么气体？”，可得到“氧气”。

实际措辞由模型生成，可能有所不同。

## 项目文件

| 文件 | 用途 |
| --- | --- |
| `app.py` | Streamlit 页面、LangChain 模型接入及总结/问答链 |
| `requirements.txt` | Python 依赖 |

## 实现说明

代码使用 `ChatPromptTemplate` 构造指令，通过 `ChatOpenAI` 或 `ChatOllama` 调用大模型，再由 `StrOutputParser` 提取文本。问答时把用户提供的资料放入提示词，让模型以资料为依据作答。这个简易版本没有向量检索，适合篇幅较短的学习资料。

## 注意

请不要把 API Key 写入代码、README 或提交到 GitHub。模型生成的内容可能出错，重要知识点仍需核对原资料。

## 开源协议

本项目采用 MIT License，协议全文如下（仓库中也有单独的 `LICENSE` 文件）：

```text
MIT License

Copyright (c) 2026 hexu-xu

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
