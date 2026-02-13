from langchain_core.prompts import ChatPromptTemplate
from app.utils.llm import get_llm
from app.graph.state import AgentState

llm = get_llm(model_type="smart")

# 审查官的提示词
REVIEW_PROMPT = ChatPromptTemplate.from_template(
    """你是一个严厉的审核员。
    请检查以下报告是否充分回答了用户的问题：{query}
    
    报告内容：
    {report}
    
    请严格按照以下 JSON 格式返回结果（不要包含 Markdown 代码块）：
    {{
        "status": "PASS" 或 "FAIL",
        "feedback": "如果是 PASS，这里留空。如果是 FAIL，请列出 1 个具体的改进建议或需要补充搜索的方向。"
    }}
    """
)

def review_node(state: AgentState):
    print("--- [节点] 正在审查报告质量 ---")
    query = state["query"]
    report = state["final_report"]
    # 获取当前的循环次数，如果没有则默认为 1
    num = state.get("revision_number", 1)
    
    # 简单的 JSON 解析逻辑 (生产环境建议用 Pydantic OutputParser)
    response = llm.invoke(REVIEW_PROMPT.format(query=query, report=report))
    content = response.content.strip().replace("```json", "").replace("```", "")
    
    import json
    try:
        result = json.loads(content)
    except:
        # 如果 LLM 抽风没返回 JSON，默认让它通过，防止报错
        result = {"status": "PASS", "feedback": ""}

    return {
        "critique": result.get("feedback",""),
        "revision_number": num + 1,
        "review_status": result.get("status", "PASS")
    }