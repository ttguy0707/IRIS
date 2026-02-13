from langchain_core.messages import HumanMessage
from app.graph.state import AgentState
from app.utils.llm import get_llm

llm = get_llm()

def refine_node(state: AgentState):
    query = state["query"]               # 修改指令，例如 "把第一章改详细点"
    old_report = state.get("final_report", "")
    
    print(f"--- [Refiner] 正在根据指令修改报告: {query} ---")
    
    prompt = f"""
    你是一个专业的报告编辑。
    
    【原始报告】
    {old_report}
    
    【用户修改指令】
    {query}
    
    请根据用户的指令，对原始报告进行修改。
    注意：
    1. 保持原有的 Markdown 结构。
    2. 只修改用户要求的部分，其余部分尽量保持原汁原味。
    3. 直接输出修改后的完整报告，不要有任何前言后语。
    """
    
    response = llm.invoke([HumanMessage(content=prompt)])
    new_report = response.content
    
    return {
        "final_report": new_report,
        "review_status": "PASS" # 修改后默认通过，直接给用户看
    }