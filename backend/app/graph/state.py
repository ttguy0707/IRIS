from typing import TypedDict, List, Annotated
import operator

class AgentState(TypedDict):
    """
    Agent 的状态定义。
    这就好比一个共享的文件夹，每个步骤都可以往里面存取东西。
    """
    query: str                # 用户原始问题
    plan: List[str]           # 规划的搜索步骤
    search_results: List[str] # 搜索到的具体内容
    final_report: str         # 最终生成的报告
    critique: str             # 审查意见
    revision_number: int      # 当前修改到了第几版 (防止死循环)
    review_status: str        # "PASS" 或 "FAIL"
    search_mode: str          # 取值: "document" (只查文档) 或 "hybrid" (混合搜索)
    should_stop: bool         # 控制位