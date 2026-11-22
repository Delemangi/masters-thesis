<script setup lang="ts">
import { useNav } from '@slidev/client'
import { computed } from 'vue'

const props = withDefaults(defineProps<{ animate?: boolean }>(), { animate: true })
// The exporter would otherwise capture the strokes partway through the animation.
const { isPrintMode } = useNav()
const play = computed(() => props.animate && !isPrintMode.value && !navigator.webdriver)
// Each instance needs its own gradient id: a shared id resolves to the first copy in the page,
// which may sit on a hidden slide, and the diagonals then render with no paint.
const gid = `diag-${Math.random().toString(36).slice(2, 9)}`
// The FINKI Hub mark redrawn as eight strokes: four chevrons pointing inward and four diagonals
// heading for the centre. On the cover they converge into place once.
const chevrons = [
  { d: 'M265 120 L370 225 L470 120', from: '0,-70' },
  { d: 'M265 540 L370 435 L470 540', from: '0,70' },
  { d: 'M135 235 L240 330 L135 435', from: '-70,0' },
  { d: 'M605 235 L500 330 L605 435', from: '70,0' },
]
const diagonals = [
  { d: 'M135 120 L318 298', from: '-80,-80' },
  { d: 'M605 120 L422 298', from: '80,-80' },
  { d: 'M135 540 L318 362', from: '-80,80' },
  { d: 'M605 540 L422 362', from: '80,80' },
]
</script>

<template>
  <svg viewBox="80 70 580 520" class="logo" :class="{ animate: play }">
    <defs>
      <linearGradient :id="gid" x1="0" y1="0" x2="1" y2="1">
        <stop offset="0" stop-color="#8be07a" />
        <stop offset="1" stop-color="#3fbf73" />
      </linearGradient>
    </defs>
    <path v-for="(c, i) in diagonals" :key="'d' + i" :d="c.d" class="s diag" :stroke="`url(#${gid})`"
      :style="{ '--from': `translate(${c.from.split(',')[0]}px, ${c.from.split(',')[1]}px)`, animationDelay: `${0.15 + i * 0.08}s` }" />
    <path v-for="(c, i) in chevrons" :key="'c' + i" :d="c.d" class="s chev"
      :style="{ '--from': `translate(${c.from.split(',')[0]}px, ${c.from.split(',')[1]}px)`, animationDelay: `${0.45 + i * 0.08}s` }" />
  </svg>
</template>

<style scoped>
.logo { width: 100%; height: auto; overflow: visible; }
.s { fill: none; stroke-width: 44; stroke-linecap: round; stroke-linejoin: round; }

.chev { stroke: #1ba96e; }
.animate .s { animation: converge 1.1s cubic-bezier(.2, .8, .2, 1) both; }
@keyframes converge { from { opacity: 0; transform: var(--from); } to { opacity: 1; transform: none; } }
@media (prefers-reduced-motion: reduce) { .animate .s { animation: none; } }
</style>
