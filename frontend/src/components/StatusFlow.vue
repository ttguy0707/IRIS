<template>
  <div class="relative overflow-hidden rounded-2xl border border-white/20 bg-white/60 backdrop-blur-xl shadow-xl p-6 transition-all hover:shadow-2xl">
    <div class="absolute -top-10 -right-10 w-32 h-32 bg-blue-400/20 rounded-full blur-3xl"></div>
    <div class="absolute bottom-0 left-0 w-24 h-24 bg-purple-400/20 rounded-full blur-3xl"></div>

    <h3 class="relative text-xs font-bold text-gray-400 mb-6 uppercase tracking-[0.2em] font-sans">
      Workflow Engine
    </h3>
    
    <div class="relative space-y-8 pl-2">
      <div class="absolute left-[19px] top-4 bottom-4 w-0.5 bg-gray-200/50 rounded-full"></div>

      <div 
        v-for="(step, index) in steps" 
        :key="step.id"
        class="relative flex items-center gap-5 group"
      >
        <div class="relative z-10 flex items-center justify-center w-10 h-10 rounded-xl border transition-all duration-500"
          :class="getIconStyles(index)"
        >
          <div v-if="currentStepIndex === index && currentStep !== 'done'" 
               class="absolute inset-0 rounded-xl bg-blue-500 blur-lg opacity-40 animate-pulse">
          </div>

          <component 
            :is="step.icon" 
            class="w-5 h-5 transition-all duration-300" 
            :class="currentStepIndex === index && currentStep !== 'done' ? 'animate-bounce-slight text-white' : ''" 
          />
        </div>

        <div class="flex flex-col">
          <span 
            class="text-sm font-bold tracking-wide transition-all duration-300"
            :class="getTextStyles(index)"
          >
            {{ step.label }}
          </span>
          <span class="text-[10px] text-gray-400 font-medium tracking-wider uppercase">
             {{ step.desc }}
          </span>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { computed } from 'vue';
import { CheckIcon, Loader2Icon, BrainCircuitIcon, SearchIcon, FileTextIcon, ShieldCheckIcon } from 'lucide-vue-next';

const props = defineProps({
  currentStep: { type: String, default: 'idle' }
});

const steps = [
  { id: 'planner', label: 'TASK PLANNING', desc: '拆解任务与路径规划', icon: BrainCircuitIcon },
  { id: 'researcher', label: 'DEEP SEARCH', desc: '全网数据检索与聚合', icon: SearchIcon },
  { id: 'writer', label: 'CONTENT GENERATION', desc: '多维信息整合与写作', icon: FileTextIcon },
  { id: 'reviewer', label: 'QUALITY ASSURANCE', desc: '逻辑校验与反思修正', icon: ShieldCheckIcon },
];

const currentStepIndex = computed(() => {
    if (props.currentStep === 'idle') return -1;
    if (props.currentStep === 'done') return steps.length;
    return steps.findIndex(s => s.id === props.currentStep);
});

// 样式辅助函数
const getIconStyles = (index) => {
    // 已完成
    if (props.currentStep === 'done' || currentStepIndex.value > index) {
        return 'bg-gradient-to-br from-green-400 to-emerald-600 border-transparent text-white shadow-lg shadow-green-500/30 scale-100';
    }
    // 进行中
    if (currentStepIndex.value === index) {
        return 'bg-gradient-to-br from-blue-500 to-indigo-600 border-transparent text-white shadow-lg shadow-blue-500/40 scale-110';
    }
    // 未开始
    return 'bg-white border-gray-200 text-gray-300 scale-90';
};

const getTextStyles = (index) => {
    if (props.currentStep === 'done' || currentStepIndex.value > index) return 'text-green-600';
    if (currentStepIndex.value === index) return 'text-blue-700 scale-105 origin-left';
    return 'text-gray-300';
};
</script>

<style scoped>
/* 自定义微动效 */
@keyframes bounce-slight {
    0%, 100% { transform: translateY(0); }
    50% { transform: translateY(-2px); }
}
.animate-bounce-slight {
    animation: bounce-slight 2s infinite;
}
</style>