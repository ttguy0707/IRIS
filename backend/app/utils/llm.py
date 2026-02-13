import os
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

# 加载 .env 环境变量
load_dotenv()

def get_llm(model_type="fast"):
    """
    模型工厂函数。
    :param model_type: "fast" (用于生成) 或 "smart" (用于审查)
    """
    
    # --- 配置 A: 快速模型 (DeepSeek-V3 / GPT-4o-mini) ---
    # 用于：Planner, Writer (需要速度和流利度)
    if model_type == "fast":
        return ChatOpenAI(
            model="qwen3-max", 
            temperature=0.7, # 稍微有点创造力
            base_url=os.getenv("OPENAI_API_BASE"), 
            api_key=os.getenv("OPENAI_API_KEY")
        )
    
    # --- 配置 B: 聪明模型 (DeepSeek-R1 / GPT-4o / Claude-3.5) ---
    # 用于：Reviewer (需要严谨逻辑)
    elif model_type == "smart":
        return ChatOpenAI(
            # 建议用 DeepSeek-R1 (推理能力强) 或 GPT-4o
            model="deepseek-r1",
            temperature=0,   # 绝对理性，不要创造力
            base_url=os.getenv("OPENAI_API_BASE"), 
            api_key=os.getenv("OPENAI_API_KEY")
        )