from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from app.api.routes import router

# 1. 创建 FastAPI 实例
app = FastAPI(title="IRIS Agent API")

# 2. 配置 CORS (允许前端访问)
# 允许所有来源，或者指定 ["http://localhost:5173"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 3. 注册路由
app.include_router(router, prefix="/api")

@app.get("/")
def health_check():
    return {"status": "running", "model_config": "Qwen-Max + DeepSeek-R1"}

if __name__ == "__main__":
    print("🚀 后端服务正在启动...")
    # 启动服务器，监听 8000 端口
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)





'''
    测试Agent功能是否正常
'''
# def main():
#     print("🚀 IRIS Agent 启动中...")
    
#     # 1. 创建图
#     app = create_graph()
    
#     # 2. 模拟用户输入
#     user_input = "2026年 AI Agent 的主要技术趋势是什么？"
#     initial_state = {"query": user_input}
    
#     # 3. 运行图
#     # invoke 会同步运行整个流程直到结束
#     result = app.invoke(initial_state)
    
#     # 4. 打印最终结果
#     print("\n" + "="*50)
#     print("✅ 最终报告生成完毕：")
#     print("="*50 + "\n")
#     print(result["final_report"])

# if __name__ == "__main__":
#     main()