from langchain_core.prompts import ChatPromptTemplate
from app.utils.llm import get_llm
from app.graph.state import AgentState

llm = get_llm()

# 提示词：教 AI 怎么做计划
PLAN_PROMPT = ChatPromptTemplate.from_template(
    """你是一个专业的调研助手。
    针对用户的问题：{query}
    请生成 3-5 个简短的搜索关键词，用于在 Google 上查找相关信息。
    已有审查意见（如果有）：{critique}
    如果存在审查意见，请务必针对意见中提到的缺失信息生成关键词。
    只返回关键词，用逗号分隔，不要有其他废话。
    例如：关键词1, 关键词2, 关键词3
    """
)

def plan_node(state: AgentState):
    print("--- [节点] 正在规划搜索路径 ---")
    query = state["query"]
    critique = state.get("critique", "") # 获取审查意见
    
    # 调用 LLM
    response = llm.invoke(PLAN_PROMPT.format(query=query, critique=critique))
    
    # 解析结果：把 "A, B, C" 变成 ["A", "B", "C"]
    plans = [p.strip() for p in response.content.split(",")]
    
    # 更新状态
    return {"plan": plans}