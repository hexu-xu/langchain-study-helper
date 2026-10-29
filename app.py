"""A small LangChain study helper with online and local model options."""

import streamlit as st
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import ChatOllama
from langchain_openai import ChatOpenAI


SUMMARY_PROMPT = ChatPromptTemplate.from_messages(
    [
        ("system", "你是学习助手。请用中文概括资料，列出三到五个要点；只依据给定资料，不要编造。"),
        ("human", "资料：\n{material}"),
    ]
)

QUESTION_PROMPT = ChatPromptTemplate.from_messages(
    [
        ("system", "你是学习助手。请只根据给定资料回答问题。资料没有答案时，明确说“资料中没有提到”。"),
        ("human", "资料：\n{material}\n\n问题：{question}"),
    ]
)


def make_model(provider: str, model_name: str, api_key: str):
    """Create a LangChain chat model from the user's settings."""
    if provider == "在线 OpenAI":
        if not api_key.strip():
            raise ValueError("请填写 OpenAI API Key。")
        return ChatOpenAI(model=model_name, api_key=api_key.strip())
    return ChatOllama(model=model_name)


def run_task(model, task: str, material: str, question: str = "") -> str:
    """Run one prompt → model → text parser chain."""
    if not material.strip():
        raise ValueError("请先输入学习资料。")
    if task == "提问" and not question.strip():
        raise ValueError("请输入问题。")

    prompt = SUMMARY_PROMPT if task == "总结" else QUESTION_PROMPT
    chain = prompt | model | StrOutputParser()
    return chain.invoke({"material": material.strip(), "question": question.strip()})


def main() -> None:
    st.set_page_config(page_title="学习资料助手", page_icon="📚")
    st.title("📚 学习资料助手")
    st.caption("粘贴学习资料，让大模型帮你总结或回答问题。")

    with st.sidebar:
        st.header("模型设置")
        provider = st.radio("运行方式", ["在线 OpenAI", "本地 Ollama"])
        default_model = "gpt-4o-mini" if provider == "在线 OpenAI" else "qwen2.5:3b"
        model_name = st.text_input("模型名称", value=default_model)
        api_key = (
            st.text_input("OpenAI API Key", type="password", help="只用于本次模型请求，不写入文件。")
            if provider == "在线 OpenAI"
            else ""
        )

    with st.form("study_form"):
        material = st.text_area("学习资料", height=250, placeholder="在这里粘贴课程笔记或文章……")
        task = st.radio("要做什么", ["总结", "提问"], horizontal=True)
        question = st.text_input("你的问题（选择“提问”时填写）")
        submitted = st.form_submit_button("开始", type="primary")

    if submitted:
        try:
            if not model_name.strip():
                raise ValueError("请填写模型名称。")
            model = make_model(provider, model_name.strip(), api_key)
            with st.spinner("正在生成……"):
                result = run_task(model, task, material, question)
            st.subheader("结果")
            st.write(result)
        except ValueError as exc:
            st.warning(str(exc))
        except Exception as exc:
            st.error(f"模型调用失败：{exc}")
            st.info("请检查 API Key、模型名称和网络，或确认 Ollama 已启动并下载了该模型。")


if __name__ == "__main__":
    main()
