<script setup lang="ts">
import { computed } from 'vue'
import { useNav, useSlideContext } from '@slidev/client'

const parts = ['Context', 'Problem', 'How it works', 'Testing', 'Results', 'Findings']
const { total } = useNav()
const { $page: currentPage, $frontmatter } = useSlideContext()
const hidden = computed(() => ['hub-cover', 'closing'].includes($frontmatter?.layout))
const idx = computed(() => parts.indexOf($frontmatter?.section))
</script>

<template>
  <div v-if="!hidden && !$frontmatter?.noMark" class="corner"><LogoMark :animate="false" /></div>
  <footer v-if="!hidden" class="foot">
    <div class="left" />
    <div class="track" v-if="idx >= 0 || $frontmatter?.section">
      <span v-for="(p, i) in parts" :key="p" class="seg" :class="{ done: i < idx, now: i === idx }" />
      <span class="sec">{{ $frontmatter?.section }}</span>
    </div>
    <div class="right">{{ currentPage }}<span class="of">/{{ total }}</span></div>
  </footer>
</template>

<style scoped>
.foot {
  position: absolute; left: 3.2rem; right: 3.2rem; bottom: 0;
  height: 2.1rem; display: grid; grid-template-columns: 1fr auto 1fr; align-items: center;
  font-size: .64rem; color: #849086;
}
.left { display: flex; align-items: center; gap: .45rem; }
.corner { position: absolute; top: 2.55rem; right: 3.2rem; width: 34px; }
.track { display: flex; align-items: center; gap: 4px; }
.seg { width: 22px; height: 4px; background: #1e3a2c; clip-path: polygon(3px 0, 100% 0, calc(100% - 3px) 100%, 0 100%); }
.seg.done { background: #1ba96e; opacity: .55; }
.seg.now { background: #8be07a; }
.sec { margin-left: .6rem; color: #c3c4b8; }
.right { justify-self: end; font-family: 'Unbounded', sans-serif; font-size: .62rem; color: #8be07a; }
.of { color: #4c6255; margin-left: 1px; }
</style>
