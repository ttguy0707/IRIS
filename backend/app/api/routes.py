from fastapi import APIRouter, UploadFile, File, HTTPException
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
from typing import List
from app.graph.graph import create_graph
import json
import asyncio
import os
import shutil
from app.rag.engine import process_documents, reset_knowledge_base, UPLOAD_DIR
from langgraph.checkpoint.sqlite.aio import AsyncSqliteSaver

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(CURRENT_DIR, "checkpoints.db")
print(f"📁 记忆数据库将保存在当前运行目录: {DB_PATH}")
router = APIRouter()

# 定义请求体：前端只需要传一个 query
class ChatRequest(BaseModel):
    query: str
    search_mode: str = "hybrid" # 默认为混合搜索
    thread_id: str               # 必须传入当前会话 ID

@router.post("/clear")
async def clear_endpoint():
    try:
        reset_knowledge_base() # 调用我们之前写好的安全清空函数
        return {"message": "知识库已重置", "status": "success"}
    except Exception as e:
        print(f"清空失败: {e}")
        return {"message": f"清空失败: {str(e)}", "status": "error"}

@router.post("/upload")
async def upload_files(files: List[UploadFile] = File(...)):
    """
    批量上传接口
    """
    # 1. 数量限制校验
    if len(files) > 5:
        raise HTTPException(status_code=400, detail="一次最多只能上传 5 个文件")

    try:
        # 2. 每次上传前，重置知识库 (保证是当前任务的文档)
        reset_knowledge_base()
        
        saved_paths = []
        # 3. 保存文件到本地磁盘
        for file in files:
            # 防止文件名重复或乱码，这里简单处理，直接拼接
            file_path = os.path.join(UPLOAD_DIR, file.filename)
            with open(file_path, "wb") as buffer:
                shutil.copyfileobj(file.file, buffer)
            saved_paths.append(file_path)
            
        # 4. 调用 RAG 引擎进行处理 (切片 + 入库)
        chunks_num = process_documents(saved_paths)
        
        return {
            "status": "success",
            "file_count": len(files), 
            "chunks_stored": chunks_num,
            "message": "文档解析完成，知识库构建成功"
        }
    except Exception as e:
        print(f"上传处理失败: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/chat")
async def chat_endpoint(request: ChatRequest):
    config = {"configurable": {"thread_id": request.thread_id}}
    async def event_generator():
        # 初始化状态，把前端传来的 search_mode 塞进去
        initial_state = {
            "query": request.query, 
            "revision_number": 1,
            "search_mode": request.search_mode 
        }
        
        print(f"🚀 新任务开启 | 模式: {request.search_mode} | 问题: {request.query}")

        async with AsyncSqliteSaver.from_conn_string(DB_PATH) as memory:
            app = create_graph(memory=memory)
            
            async for event in app.astream(initial_state, config=config):
                 for node_name, state_update in event.items():
                    data = json.dumps({"step": node_name, "data": state_update}, ensure_ascii=False)
                    yield f"data: {data}\n\n"
                    await asyncio.sleep(0.1) 
        
        yield "data: [DONE]\n\n"

    return StreamingResponse(event_generator(), media_type="text/event-stream")