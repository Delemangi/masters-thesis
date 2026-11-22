<script setup lang="ts">
import { useNav, useSlideContext } from '@slidev/client'
const { total } = useNav()
const { $page: page } = useSlideContext()
</script>

<template>
  <div class="slidev-layout plain">
    <main class="body"><slot /></main>
    <div class="num">{{ page }} / {{ total }}</div>
  </div>
</template>

<style scoped>
.plain { padding: 0 !important; position: relative; }
.body { height: 100%; padding: 2.8rem 3.4rem 3.2rem; display: flex; flex-direction: column; }
.body > :deep(h1) { flex: none; font-size: 1.5rem !important; line-height: 1.25 !important; margin: 0 0 1.8rem !important; max-width: 46rem !important; }
.num { position: absolute; right: 3.4rem; bottom: 1.5rem; font-size: .68rem; color: #6b8576; font-variant-numeric: tabular-nums; }
</style>
