// frontend/src/services/api.js

const API_BASE = "http://localhost:8000/api";

function generateUUID() {
  return 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, function(c) {
      var r = Math.random() * 16 | 0, v = c == 'x' ? r : (r & 0x3 | 0x8);
      return v.toString(16);
  });
}

// 会话级 ID：页面一刷新就重置，满足"单次会话记忆"需求
const SESSION_THREAD_ID = generateUUID();
/**
 * 批量上传文件
 * @param {Array<File>} files - 文件对象数组
 */
export async function uploadFiles(files) {
    const formData = new FormData();
    // 遍历文件数组，把它们都塞进 'files' 字段里
    files.forEach(file => {
        formData.append('files', file);
    });

    // 发送 POST 请求到 /upload
    const response = await fetch(`${API_BASE}/upload`, {
        method: "POST",
        body: formData
    });
    
    if (!response.ok) {
        const errorData = await response.json();
        throw new Error(errorData.detail || "Upload failed");
    }
    
    return await response.json();
}
export async function clearContext() {
  const response = await fetch(`${API_BASE}/clear`, {
      method: "POST"
  });
  if (!response.ok) throw new Error("Failed to clear context");
  return await response.json();
}

/**
 * 流式聊天
 * @param {string} query - 问题
 * @param {string} searchMode - 'hybrid' | 'document'
 * @param {function} onMessage - 接收消息回调
 * @param {function} onDone - 完成回调
 * @param {function} onError - 错误回调
 */
export async function streamChat(query, search_mode, onData, onDone, onError) {
  try {
      const response = await fetch(`${API_BASE}/chat`, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ 
              query: query, 
              search_mode: search_mode,  // 严格使用 search_mode
              thread_id: SESSION_THREAD_ID 
          }),
      });
      
      if (!response.ok) throw new Error('Network error');

      const reader = response.body.getReader();
      const decoder = new TextDecoder('utf-8');
      
      while (true) {
          const { done, value } = await reader.read();
          if (done) break;
          const chunk = decoder.decode(value);
          const lines = chunk.split('\n');
          for (const line of lines) {
              if (line.startsWith('data: ')) {
                  const dataStr = line.replace('data: ', '').trim();
                  if (dataStr === '[DONE]') {
                      onDone(); return;
                  }
                  try { onData(JSON.parse(dataStr)); } catch(e){}
              }
          }
      }
  } catch (error) { onError(error); }
}