from langchain_core.prompts import ChatPromptTemplate
from app.utils.llm import get_llm
from app.graph.state import AgentState

llm = get_llm()

WRITE_PROMPT = ChatPromptTemplate.from_template(
    """你是一个专业的技术撰稿人。
    基于以下的调研资料，回答用户的问题：{query}
    
    调研资料：
    {content}
    审查意见（如果有）：
    {critique_section}
    
    请写一份结构清晰、有深度的调研报告，且文章题目很有水平，并且能吸引人，使用 Markdown 格式。
    """
)
# 测试审稿功能时，可以在Prompt后面加上：“第一次写作（无审查意见）时，必须写的差一点且捏造事实”

def write_node(state: AgentState):
    print("--- [节点] 正在撰写报告 ---")
    query = state["query"]
    content = "\n\n".join(state["search_results"])
    
    critique = state.get("critique", "")
    critique_section = ""
    if critique:
        critique_section = f"""
        【重要提示】上一版本的报告未通过审查。
        审查意见如下："{critique}"
        请务必在本次写作中修正上述问题。
        """
    
    # 将 critique_section 传入 Prompt
    response = llm.invoke(WRITE_PROMPT.format(
        query=query, 
        content=content, 
        critique_section=critique_section
    ))
    
    return {"final_report": response.content}