from langchain_core.messages import HumanMessage
from app.graph.state import AgentState
from app.utils.llm import get_llm

# 用一个小模型即可，速度快
router_llm = get_llm()

def route_query(state: AgentState):
    """
    判断用户输入是“新查询”还是“修改指令”
    """
    query = state["query"]
    # 获取当前是否已有报告
    has_report = bool(state.get("final_report", "").strip())

    print(f"--- [Router] 正在分析意图: '{query}' (已有报告: {has_report}) ---")

    # 如果根本没有历史报告，肯定是新任务，直接去 planner
    if not has_report:
        return "planner"

    # 如果有报告，让 LLM 判断
    prompt = f"""
    当前系统已经生成了一份研究报告。
    用户的最新输入是: "{query}"
    
    请判断用户的意图：
    1. "NEW_TOPIC": 用户想要开始一个全新的研究课题（例如："帮我查一下量子计算"）。
    2. "REFINE": 用户想要基于现有的报告进行修改、润色或补充（例如："第一章写详细点"、"改通俗点"）。
    
    只输出 "NEW_TOPIC" 或 "REFINE"。
    """
    
    result = router_llm.invoke([HumanMessage(content=prompt)]).content.strip().upper()
    print(f"--- [Router] LLM 判定结果: {result} ---")
    
    if "REFINE" in result:
        return "refiner"  # 去专门的修改节点
    else:
        return "planner"  # 开启新课题