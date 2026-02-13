<template>
    <transition name="slide-down">
        <div v-if="showWarning" class="fixed top-24 left-1/2 transform -translate-x-1/2 z-50 bg-amber-50 border border-amber-200 text-amber-800 px-6 py-3 rounded-full shadow-lg flex items-center gap-3">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-amber-500" viewBox="0 0 20 20" fill="currentColor">
                <path fill-rule="evenodd" d="M8.257 3.099c.765-1.36 2.722-1.36 3.486 0l5.58 9.92c.75 1.334-.213 2.98-1.742 2.98H4.42c-1.53 0-2.493-1.646-1.743-2.98l5.58-9.92zM11 13a1 1 0 11-2 0 1 1 0 012 0zm-1-8a1 1 0 00-1 1v3a1 1 0 002 0V6a1 1 0 00-1-1z" clip-rule="evenodd" />
            </svg>
            <span class="text-sm font-medium">{{ warningMessage }}</span>
            <button @click="showWarning = false" class="text-amber-500 hover:text-amber-700">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" viewBox="0 0 20 20" fill="currentColor"><path fill-rule="evenodd" d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z" clip-rule="evenodd" /></svg>
            </button>
        </div>
    </transition>
  <div class="min-h-screen bg-gray-50 text-gray-900 font-sans relative overflow-x-hidden selection:bg-blue-100 selection:text-blue-900">
    
    <div class="fixed top-0 left-0 w-full h-full overflow-hidden -z-10 pointer-events-none">
        <div class="absolute top-[-10%] left-[-10%] w-[40%] h-[40%] bg-purple-300/30 rounded-full blur-[120px] mix-blend-multiply animate-blob"></div>
        <div class="absolute top-[-10%] right-[-10%] w-[40%] h-[40%] bg-blue-300/30 rounded-full blur-[120px] mix-blend-multiply animate-blob animation-delay-2000"></div>
        <div class="absolute bottom-[-20%] left-[20%] w-[40%] h-[40%] bg-indigo-300/30 rounded-full blur-[120px] mix-blend-multiply animate-blob animation-delay-4000"></div>
    </div>

    <header class="sticky top-0 z-50 border-b border-white/20 bg-white/70 backdrop-blur-xl">
      <div class="max-w-7xl mx-auto px-6 py-4 flex items-center justify-between">
        <div class="flex items-center gap-3">
          <div class="relative w-10 h-10 flex items-center justify-center bg-gradient-to-tr from-blue-600 to-purple-600 rounded-xl shadow-lg shadow-blue-500/20 text-white">
            <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="M12 2a14.5 14.5 0 0 0 0 20 14.5 14.5 0 0 0 0-20"/><path d="M2 12h20"/></svg>
          </div>
          <div class="flex flex-col">
            <h1 class="text-2xl font-black tracking-tighter bg-gradient-to-r from-blue-700 via-purple-600 to-indigo-600 bg-clip-text text-transparent" style="font-family: 'Orbitron', sans-serif;">
              IRIS
            </h1>
            <span class="text-[10px] font-semibold text-gray-500 tracking-[0.05em] uppercase -mt-1">
              Intelligent Research Insight System
            </span>
          </div>
        </div>
      </div>
    </header>

    <main class="max-w-7xl mx-auto p-6 lg:p-8 grid grid-cols-1 lg:grid-cols-12 gap-8 mt-4">
      
      <div class="lg:col-span-4 space-y-6">
        
        <div class="bg-white/80 backdrop-blur-xl p-6 rounded-2xl shadow-xl border border-white/40 space-y-5">
          
            <div>
                <div class="flex justify-between items-center mb-2">
                    <label class="text-xs font-bold text-gray-400 uppercase tracking-wider">Knowledge Base</label>
                    <span class="text-[10px] text-gray-400 bg-gray-100 px-2 py-0.5 rounded-full">Max 5 PDFs</span>
                </div>
                
                <div 
                    @dragover.prevent="isDragging = true"
                    @dragleave.prevent="isDragging = false"
                    @drop.prevent="handleDrop"
                    class="relative group cursor-pointer border-2 border-dashed rounded-xl p-4 transition-all duration-300 flex flex-col items-center justify-center text-center min-h-[100px]"
                    :class="isDragging ? 'border-blue-500 bg-blue-50/50' : 'border-gray-300 hover:border-blue-400 hover:bg-gray-50/50'"
                >
                    <input type="file" multiple accept=".pdf" class="absolute inset-0 opacity-0 cursor-pointer" @change="handleFileSelect" />
                    
                    <div v-if="uploadedFiles.length === 0" class="pointer-events-none flex flex-col items-center">
                        <div class="w-8 h-8 mb-2 rounded-full bg-blue-50 flex items-center justify-center text-blue-500">
                            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="17 8 12 3 7 8"/><line x1="12" y1="3" x2="12" y2="15"/></svg>
                        </div>
                        <p class="text-xs text-gray-500 font-medium">Drop PDFs here</p>
                    </div>

                    <div v-else class="w-full space-y-2 pointer-events-none z-10">
                        <div v-for="(file, i) in uploadedFiles" :key="i" class="flex items-center justify-between bg-white px-3 py-2 rounded-lg shadow-sm border border-gray-100 text-xs animate-fade-in-up">
                            <div class="flex items-center gap-2 overflow-hidden">
                                <span class="text-red-500">
                                    <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14.5 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V7.5L14.5 2z"/><polyline points="14 2 14 8 20 8"/></svg>
                                </span>
                                <span class="truncate max-w-[150px] text-gray-700 font-medium">{{ file.name }}</span>
                            </div>
                            <span class="text-green-500">
                                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg>
                            </span>
                        </div>
                    </div>
                </div>
            </div>

            <div class="bg-gray-100/80 p-1 rounded-xl flex items-center relative">
                <div 
                    class="absolute top-1 bottom-1 w-[48%] bg-white rounded-lg shadow-sm transition-all duration-300 ease-out z-0"
                    :class="searchMode === 'document' ? 'left-1' : 'left-[51%]'"
                ></div>

                <button 
                    @click="setMode('document')"
                    :disabled="uploadedFiles.length === 0"
                    class="flex-1 py-2 text-[10px] font-bold tracking-wide rounded-lg z-10 transition-colors duration-300 uppercase flex items-center justify-center gap-1.5"
                    :class="[
                        searchMode === 'document' ? 'text-blue-600' : 'text-gray-400 hover:text-gray-600',
                        uploadedFiles.length === 0 ? 'opacity-50 cursor-not-allowed' : ''
                    ]"
                >
                    <svg xmlns="http://www.w3.org/2000/svg" width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14.5 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V7.5L14.5 2z"/><polyline points="14 2 14 8 20 8"/><path d="M16 13H8"/><path d="M16 17H8"/><path d="M10 9H8"/></svg>
                    Doc Only
                </button>
                <button 
                    @click="setMode('hybrid')"
                    class="flex-1 py-2 text-[10px] font-bold tracking-wide rounded-lg z-10 transition-colors duration-300 uppercase flex items-center justify-center gap-1.5"
                    :class="searchMode === 'hybrid' ? 'text-purple-600' : 'text-gray-400 hover:text-gray-600'"
                >
                    <svg xmlns="http://www.w3.org/2000/svg" width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><line x1="2" y1="12" x2="22" y2="12"/><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/></svg>
                    Hybrid
                </button>
            </div>

            <div>
                <div class="relative group">
                    <div class="absolute -inset-0.5 bg-gradient-to-r from-blue-600 to-purple-600 rounded-xl opacity-20 group-hover:opacity-40 transition duration-500 blur"></div>
                    <textarea 
                    v-model="query" 
                    class="relative w-full p-4 bg-white border-0 rounded-xl shadow-inner text-gray-700 placeholder-gray-400 focus:ring-0 text-sm leading-relaxed resize-none transition-all"
                    rows="3"
                    placeholder="Enter research topic..."
                    :disabled="isLoading"
                    ></textarea>
                </div>
            
                <button 
                    @click="startResearch"
                    :disabled="isLoading || !query"
                    class="mt-4 w-full group relative overflow-hidden rounded-xl bg-gray-900 px-8 py-3.5 text-white shadow-lg transition-all hover:bg-gray-800 hover:shadow-xl hover:-translate-y-0.5 disabled:cursor-not-allowed disabled:opacity-50 disabled:shadow-none disabled:translate-y-0"
                >
                    <div class="absolute inset-0 bg-gradient-to-r from-blue-600 to-purple-600 opacity-0 group-hover:opacity-100 transition-opacity duration-500"></div>
                    <span class="relative flex items-center justify-center gap-2 font-medium tracking-wide text-xs uppercase">
                        <span v-if="isLoading">Processing...</span>
                        <span v-else>Initiate Research</span>
                        <svg v-if="!isLoading" xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14"/><path d="m12 5 7 7-7 7"/></svg>
                    </span>
                </button>
            </div>
        </div>

        <StatusFlow :currentStep="currentStep" />

        <div class="rounded-2xl bg-[#0F172A] border border-slate-800 shadow-2xl overflow-hidden ring-1 ring-white/10">
            <div class="flex items-center gap-1.5 px-4 py-2 bg-slate-900/50 border-b border-slate-800">
                <div class="w-2.5 h-2.5 rounded-full bg-red-500/80"></div>
                <div class="w-2.5 h-2.5 rounded-full bg-yellow-500/80"></div>
                <div class="w-2.5 h-2.5 rounded-full bg-green-500/80"></div>
                <span class="ml-2 text-[10px] font-mono text-slate-500">terminal@iris-core:~</span>
            </div>
            <div ref="logsContainer" class="h-32 p-4 overflow-y-auto font-mono text-[11px] leading-5 space-y-1 scrollbar-thin scrollbar-thumb-slate-700 scrollbar-track-transparent">
                <div v-if="logs.length === 0" class="text-slate-600 italic">System ready. Waiting for input...</div>
                <div v-for="(log, i) in logs" :key="i" class="flex gap-2">
                    <span class="text-blue-500 shrink-0">➜</span>
                    <span class="text-slate-300 break-all">{{ log }}</span>
                </div>
                <div v-if="isLoading" class="animate-pulse text-blue-500 mt-2">_</div>
            </div>
        </div>
      </div>

      <div class="lg:col-span-8 flex flex-col h-full min-h-[700px]">
        <div class="flex-1 bg-white/80 backdrop-blur-xl rounded-2xl shadow-xl border border-white/40 p-8 lg:p-12 relative overflow-hidden flex flex-col">
            
            <div class="absolute top-0 right-0 p-8 opacity-[0.03] pointer-events-none">
                 <h1 class="text-9xl font-black font-sans" style="font-family: 'Orbitron';">IRIS</h1>
            </div>

            <div v-if="!displayedReport && !isLoading" class="flex-1 flex flex-col items-center justify-center text-gray-400 space-y-4">
                <div class="w-20 h-20 rounded-3xl bg-gradient-to-tr from-gray-100 to-gray-200 flex items-center justify-center shadow-inner">
                    <svg class="w-10 h-10 text-gray-300" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M19.5 14.25v-2.625a3.375 3.375 0 00-3.375-3.375h-1.5A1.125 1.125 0 0113.5 7.125v-1.5a3.375 3.375 0 00-3.375-3.375H8.25m0 12.75h7.5m-7.5 3H12M10.5 2.25H5.625c-.621 0-1.125.504-1.125 1.125v17.25c0 .621.504 1.125 1.125 1.125h12.75c.621 0 1.125-.504 1.125-1.125V11.25a9 9 0 00-9-9z"></path></svg>
                </div>
                <div class="text-center">
                    <h3 class="text-lg font-medium text-gray-900">Awaiting Assignment</h3>
                    <p class="text-sm">Upload docs or enter a topic to begin.</p>
                </div>
            </div>

            <div v-else-if="isLoading && !displayedReport" class="flex-1 flex flex-col items-center justify-center relative">
                <div class="relative w-40 h-40 flex items-center justify-center">
                    <div class="absolute inset-0 bg-gradient-to-tr from-blue-500 to-purple-600 rounded-full blur-[60px] opacity-60 animate-pulse"></div>
                    
                    <div class="absolute top-0 -left-4 w-24 h-24 bg-cyan-400 rounded-full blur-[40px] opacity-50 mix-blend-screen animate-blob"></div>
                    <div class="absolute -bottom-4 -right-4 w-24 h-24 bg-indigo-500 rounded-full blur-[40px] opacity-50 mix-blend-screen animate-blob animation-delay-2000"></div>
                    <div class="absolute -bottom-8 left-8 w-20 h-20 bg-purple-400 rounded-full blur-[40px] opacity-50 mix-blend-screen animate-blob animation-delay-4000"></div>

                    <div class="relative z-10 w-3 h-3 bg-white rounded-full shadow-[0_0_20px_rgba(255,255,255,0.8)] animate-ping" style="animation-duration: 2s;"></div>
                </div>

                <div class="mt-12 text-center space-y-2 relative z-10">
                    <h3 class="text-xl font-bold bg-clip-text text-transparent bg-gradient-to-r from-blue-600 to-purple-600 tracking-widest animate-pulse">
                        THINKING
                    </h3>
                    <p class="text-xs text-slate-400 font-mono uppercase tracking-[0.2em]">
                        Analyze & Plan Strategy...
                    </p>
                </div>
            </div>

            <div v-else class="prose prose-slate max-w-none prose-headings:font-display prose-headings:font-bold prose-headings:tracking-tight prose-a:text-blue-600 prose-img:rounded-xl">
                <div v-html="renderedReport"></div>
                <span v-if="isTyping" class="inline-block w-2 h-5 bg-blue-600 ml-1 animate-pulse align-middle"></span>
            </div>

        </div>
      </div>

    </main>
  </div>
</template>

<script setup>
import { ref, computed, nextTick } from 'vue';
import { uploadFiles, streamChat, clearContext } from './services/api';
import StatusFlow from './components/StatusFlow.vue';
import MarkdownIt from 'markdown-it';
// 【修复步骤 1】引入数学公式插件 (必须先 npm install markdown-it-katex)
import mk from 'markdown-it-katex';

// 【修复步骤 2】挂载插件
const md = new MarkdownIt({
    html: true,
    linkify: true,
    typographer: true
});
md.use(mk);
const showWarning = ref(false);
const warningMessage = ref('');
const triggerWarning = (msg) => {
    warningMessage.value = msg;
    showWarning.value = true;
    // 5秒后自动消失
    setTimeout(() => {
        showWarning.value = false;
    }, 5000);
};


// 状态变量
const query = ref('');
const isLoading = ref(false);
const currentStep = ref('idle'); 
const logs = ref([]);
const logsContainer = ref(null);
const uploadedFiles = ref([]); 
const isDragging = ref(false);
const searchMode = ref('hybrid'); 

// 打字机变量
const displayedReport = ref('');
const isTyping = ref(false);

// 【修复步骤 3】增强渲染逻辑：把后端返回的 \[...\] 替换成插件能识别的 $$...$$
const renderedReport = computed(() => {
    let raw = displayedReport.value || '';
    
    // 1. 预处理：修复 LaTeX 定界符
    // 将 \[ ... \] 替换为 $$ ... $$ (块级公式)
    raw = raw.replace(/\\\[/g, '$$$').replace(/\\\]/g, '$$$');
    
    // 将 \( ... \) 替换为 $ ... $ (行内公式)
    raw = raw.replace(/\\\(/g, '$').replace(/\\\)/g, '$');

    // 2. 额外补丁：有些模型会输出不带反斜杠的 [ formula ]，这比较少见但要防备
    // 注意：这里需要小心不要误伤 Markdown 链接 [text](url)
    // 简单的策略是：如果 [ 后面跟着 \text 或 \frac 等 LaTeX 关键字，就认为是公式
    raw = raw.replace(/\[\s*(\\text|\\frac|\\sum|\\int)/g, '$$$$ $1'); 
    // 对应的闭合 ] 很难精准匹配，通常标准的 \[ \] 替换就够了。
    
    // 3. 渲染
    return md.render(raw);
});

const scrollToBottom = async () => {
    await nextTick();
    if (logsContainer.value) logsContainer.value.scrollTop = logsContainer.value.scrollHeight;
};

// --- 文件处理逻辑 ---
const handleFileSelect = async (event) => {
    processFiles(event.target.files);
};

const handleDrop = async (event) => {
    isDragging.value = false;
    processFiles(event.dataTransfer.files);
};

const processFiles = async (files) => {
    if (files.length > 5) {
        alert("Maximum 5 files allowed!");
        return;
    }
    
    uploadedFiles.value = Array.from(files);
    
    if (uploadedFiles.value.length > 0) {
        logs.value.push(`[SYSTEM] Uploading ${files.length} document(s)...`);
        try {
            const res = await uploadFiles(uploadedFiles.value);
            logs.value.push(`[SYSTEM] Knowledge base built. ${res.chunks_stored} chunks indexed.`);
        } catch (e) {
            logs.value.push(`[ERROR] Upload failed: ${e.message}`);
            alert("Upload failed: " + e.message);
            uploadedFiles.value = []; 
        }
    }
};

const setMode = (mode) => {
    searchMode.value = mode;
};

let typingInterval = null;
const typeWriterEffect = (text) => {
    isTyping.value = true;
    
    // 【关键修复】：如果当前有正在运行的打字机，立刻干掉它！防止文字重叠并发
    if (typingInterval) {
        clearInterval(typingInterval);
    }
    
    let index = 0;
    typingInterval = setInterval(() => {
        if (index < text.length) {
            displayedReport.value += text.slice(index, index + 3);
            index += 3;
        } else {
            clearInterval(typingInterval);
            typingInterval = null; // 清空记录
            isTyping.value = false;
        }
    }, 10);
};

// --- 开始研究 ---
const startResearch = async () => { 
    if (!query.value) return;
    
    isLoading.value = true;
    currentStep.value = 'planner'; 
    logs.value = []; 
    logs.value.push(`[INIT] System initialized. Mode: ${searchMode.value.toUpperCase()}`);
    displayedReport.value = '';
    
    const actualMode = uploadedFiles.value.length === 0 ? 'hybrid' : searchMode.value;

    try {
        if (uploadedFiles.value.length > 0) {
            logs.value.push(`[SYSTEM] Uploading ${uploadedFiles.value.length} document(s)...`);
            const res = await uploadFiles(uploadedFiles.value);
            logs.value.push(`[SYSTEM] Knowledge base built. ${res.chunks_stored} chunks indexed.`);
        } else {
            logs.value.push(`[SYSTEM] Clearing previous knowledge base...`);
            await clearContext();
            logs.value.push(`[SYSTEM] Context cleared. Running in pure Web Search mode.`);
        }

        streamChat(
            query.value,
            actualMode,
            (data) => {
                    // 1. 同步后端当前步骤
                    if (data.step) currentStep.value = data.step;

                    // --- 步骤 1: 规划 (Planner) ---
                    if (data.step === 'planner') {
                        currentStep.value = 'researcher'; // 视觉上跳到下一步
                        logs.value.push(`[PLANNER] Strategy: [${data.data.plan.join(', ')}]`);
                    }

                    // --- 步骤 2: 搜索 (Researcher) ---
                    else if (data.step === 'researcher') {
                        const results = data.data.search_results || [];
                        const resultsStr = JSON.stringify(results);

                        // [核心修改] 检测严重警告（熔断停止）
                        if (resultsStr.includes("流程已终止")) {
                            triggerWarning("⛔️ 文档与问题无关，任务已强制停止");
                            logs.value.push(`[SYSTEM] Task terminated: Context irrelevant in Doc-Only mode.`);
                            currentStep.value = 'done'; // 强制结束状态
                            return; // 关键：直接返回，不再执行下面的代码，防止跳到 writer
                        }

                        // 检测普通警告（自动切换等）
                        if (resultsStr.includes("自动切换为全网搜索")) {
                            triggerWarning("⚠️ 文档与问题无关，已自动切换为全网搜索");
                        } else if (resultsStr.includes("Document Only 模式")) {
                            triggerWarning("⚠️ 文档与问题无关，无法回答");
                        }

                        // 如果没有停止，则正常流转到 writer
                        currentStep.value = 'writer';
                        logs.value.push(`[RESEARCHER] Data acquisition complete. Items: ${results.length}`);
                    }

                    // --- 步骤 3: 写作 (Writer) ---
                    else if (data.step === 'writer') {
                        currentStep.value = 'reviewer';
                        logs.value.push(`[WRITER] Drafting content...`);
                        if (data.data.final_report) {
                            displayedReport.value = '';
                            typeWriterEffect(data.data.final_report);
                        }
                    }

                    // --- 步骤 4: 审查 (Reviewer) ---
                    else if (data.step === 'reviewer') {
                        if (data.data.review_status === 'FAIL') {
                            logs.value.push(`[QA] Review FAILED: ${data.data.critique} -> Rerolling`);
                            currentStep.value = 'planner';
                        } else {
                            logs.value.push(`[QA] Review PASSED.`);
                        }
                    }
                    else if (data.step === 'refiner') {
                    currentStep.value = 'writer'; // UI上复用写作状态
                    logs.value.push(`[REFINER] Modifying report based on feedback...`);
                    if (data.data.final_report) {
                        displayedReport.value = '';
                        // 重新打字输出修改后的报告
                        typeWriterEffect(data.data.final_report);
                    }
                }

                    scrollToBottom();
                },
            () => {
                isLoading.value = false;
                currentStep.value = 'done';
                logs.value.push('[DONE] Process complete.');
                scrollToBottom();
            },
            (err) => {
                isLoading.value = false;
                logs.value.push(`[ERROR] ${err.message}`);
                scrollToBottom();
            }
        );
    } catch (e) {
        isLoading.value = false;
        logs.value.push(`[ERROR] Initialization failed: ${e.message}`);
        alert("System Error: " + e.message);
    }
};
</script>

<style>
/* 保持原有的动画样式 */
.slide-down-enter-active,
.slide-down-leave-active {
  transition: all 0.3s ease;
}
.slide-down-enter-from,
.slide-down-leave-to {
  transform: translate(-50%, -100%);
  opacity: 0;
}
@keyframes blob {
    0% { transform: translate(0px, 0px) scale(1); }
    33% { transform: translate(30px, -50px) scale(1.1); }
    66% { transform: translate(-20px, 20px) scale(0.9); }
    100% { transform: translate(0px, 0px) scale(1); }
}
.animate-blob {
    animation: blob 7s infinite;
}
.animation-delay-2000 { animation-delay: 2s; }
.animation-delay-4000 { animation-delay: 4s; }

/* 简单的淡入动画 */
@keyframes fadeInUp {
    from { opacity: 0; transform: translateY(5px); }
    to { opacity: 1; transform: translateY(0); }
}
.animate-fade-in-up {
    animation: fadeInUp 0.3s ease-out;
}
@import 'https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css';

/* 2. 关键修复：解决 Tailwind 与 KaTeX 的样式冲突 */
/* Tailwind 默认将所有元素设为 border-box，这会破坏 KaTeX 的布局算法 */
.katex * {
    box-sizing: content-box !important;
}

/* 3. 公式滚动条优化 */
.katex-display {
    overflow-x: auto;
    overflow-y: hidden;
    padding: 0.5em 0;
    margin: 1em 0 !important; /* 修正外边距 */
}

/* --- 全局字体优化 --- */
body {
  font-family: theme('fontFamily.sans');
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

/* --- 舒适阅读风格 --- */
.prose {
  font-size: 1.05rem;
  color: #374151;
  line-height: 1.75;
}

/* 标题 */
.prose h1 {
  @apply text-3xl font-bold text-gray-900 mb-8 pb-4 border-b border-gray-100;
  font-family: theme('fontFamily.sans');
  line-height: 1.3;
}

.prose h2 {
  @apply text-xl font-bold text-gray-800 mt-10 mb-4 flex items-center;
  font-family: theme('fontFamily.sans');
  position: relative;
  padding-left: 1rem;
}
.prose h2::before {
  content: '';
  position: absolute;
  left: 0;
  top: 50%;
  transform: translateY(-50%);
  width: 4px;
  height: 1em;
  @apply bg-blue-600 rounded-full;
}

.prose h3 {
  @apply text-lg font-bold text-gray-800 mt-8 mb-3;
  font-family: theme('fontFamily.sans');
}

/* 正文 */
.prose p {
  @apply text-justify mb-5 leading-relaxed text-gray-700;
}

/* 重点文字 */
.prose strong {
  @apply font-bold text-gray-900;
}

/* 摘要/引用块 */
.prose blockquote {
  font-style: normal !important;
  @apply my-8 pl-6 pr-4 py-5;
  @apply bg-gray-50 rounded-r-lg border-l-4 border-blue-500;
  @apply text-gray-700 text-base leading-relaxed; 
}

/* 列表 */
.prose ul {
  @apply list-disc list-outside ml-6 space-y-2 mb-6 text-gray-700;
}
.prose ol {
  @apply list-decimal list-outside ml-6 space-y-2 mb-6 text-gray-700;
}

/* 表格 */
.prose table {
  @apply w-full text-left border-collapse my-8 rounded-lg overflow-hidden border border-gray-200;
}
.prose thead {
  @apply bg-gray-50;
}
.prose th {
  @apply px-4 py-3 font-semibold text-gray-900 text-sm uppercase tracking-wide border-b border-gray-200;
}
.prose td {
  @apply px-4 py-3 text-sm text-gray-600 border-b border-gray-100;
}
.prose tr:hover td {
  @apply bg-blue-50/30 transition-colors;
}

/* 代码块 */
.prose pre {
  @apply bg-[#1e293b] text-gray-100 rounded-xl p-5 my-6 overflow-x-auto shadow-lg;
  font-family: 'Menlo', 'Monaco', 'Courier New', monospace;
  font-size: 0.9em;
}
.prose code {
  @apply text-blue-600 bg-blue-50 px-1.5 py-0.5 rounded text-sm font-medium mx-0.5;
  font-family: 'Menlo', 'Monaco', 'Courier New', monospace;
}
.prose pre code {
  @apply bg-transparent text-gray-100 p-0 text-xs;
}

/* KaTeX 字体微调 */
.katex {
  font-size: 1.15em;
  font-family: 'Times New Roman', serif;
}
</style>