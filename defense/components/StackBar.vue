<script setup lang="ts">
defineProps<{
  label: string
  parts: { n: number; color: string; light?: boolean }[]
  total: number
}>()
</script>

<template>
  <div class="sb">
    <div class="lbl">{{ label }}</div>
    <div class="track">
      <div
        v-for="(p, i) in parts" :key="i" class="seg"
        :style="{ width: (p.n / total) * 100 + '%', background: p.color, color: p.light ? '#d9d6ca' : '#07130e' }"
      >
        <span v-if="p.n / total > 0.05">{{ p.n }}</span>
      </div>
    </div>
  </div>
</template>

<style scoped>
.sb { display: grid; grid-template-columns: 9rem 1fr; gap: .7rem; align-items: center; margin: .3rem 0; }
.lbl { text-align: right; font-size: .8rem; color: #d9d6ca; }
.track { display: flex; height: 1.5rem; border-radius: 4px; overflow: hidden; }
.seg { display: flex; align-items: center; justify-content: center; font-size: .72rem; font-weight: 600; font-variant-numeric: tabular-nums; border-right: 1px solid #07130e; }
</style>
