<script setup lang="ts">
defineProps<{ num?: string }>()
</script>

<template>
  <div class="slidev-layout dark-slide section">
    <img class="mark" src="/finki-hub-logo.png" alt="" />
    <div class="inner">
      <div class="num">{{ num }}</div>
      <div class="body"><slot /></div>
    </div>
  </div>
</template>

<style scoped>
.section { position: relative; overflow: hidden; display: flex; align-items: center; }
.inner { position: relative; z-index: 1; }
.num { font-size: 5.5rem; font-weight: 700; line-height: 1; letter-spacing: -.05em; color: #22c55e; margin-bottom: 1rem; font-variant-numeric: tabular-nums; }
.body :deep(h1) { font-size: 2.6rem; line-height: 1.12; margin: 0 0 .7rem; max-width: 38rem; }
.body :deep(p) { color: #9d9d98; font-size: 1.1rem; max-width: 36rem; margin: 0; }
.mark { position: absolute; right: -5rem; top: 50%; transform: translateY(-50%) rotate(8deg); width: 28rem; opacity: .06; }
</style>
