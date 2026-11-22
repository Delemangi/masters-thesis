<script setup lang="ts">
import { computed } from 'vue'
import { useNav, useSlideContext } from '@slidev/client'

const parts = ['Context', 'Problem', 'How it works', 'Testing', 'Results', 'Findings']
const { total } = useNav()
const { $page: page, $frontmatter: fm } = useSlideContext()
const idx = computed(() => parts.indexOf(fm?.section))
</script>

<template>
  <aside class="spine">
    <div class="mk"><LogoMark :animate="false" /></div>
    <div v-if="fm?.section" class="sec">{{ fm.section }}</div>
    <div class="foot">
      <div class="steps">
        <span v-for="(p, i) in parts" :key="p" :class="{ done: i < idx, now: i === idx }" />
      </div>
      <div class="num">{{ String(page).padStart(2, '0') }}</div>
      <div class="of">of {{ total }}</div>
    </div>
  </aside>
</template>

<style scoped>
.spine { position: relative; height: 100%; display: flex; flex-direction: column; align-items: center; padding: 2.6rem 0 2rem; }
.mk { width: 26px; }
.sec {
  margin-top: 1.4rem; writing-mode: vertical-rl; transform: rotate(180deg);
  font-size: .66rem; font-weight: 600; letter-spacing: .02em; color: #9aa59c; white-space: nowrap;
}
.foot { margin-top: auto; display: flex; flex-direction: column; align-items: center; gap: .55rem; }
.steps { display: flex; flex-direction: column; gap: 4px; margin-bottom: .3rem; }
.steps span { width: 4px; height: 13px; background: #1e3a2c; }
.steps .done { background: #1ba96e; }
.steps .now { background: #8be07a; }
.num { font-family: 'Unbounded', sans-serif; font-size: .9rem; color: #ece7da; line-height: 1; }
.of { font-size: .56rem; color: #7d9085; margin-top: -.3rem; }
</style>
