<script setup lang="ts">
import { onSlideEnter, onSlideLeave, useNav, useSlideContext } from '@slidev/client'
import { ref } from 'vue'

const correct = [59.0, 70.4, 78.0, 75.9, 83.8, 78.9, 80.6, 80.5, 81.9, 81.7, 87.8]
const wrong = [19.0, 18.9, 11.7, 8.9, 1.4, 3.1, 2.4, 1.4, 1.6, 6.9, 1.3]
const rounds = [
  { from: 0, to: 1, t: 'Better knowledge', s: 'Reviewed all the FAQs', r: '59% → 70%' },
  { from: 1, to: 3, t: 'Better search', s: 'Fixed two search faults', r: '70% → 78%' },
  { from: 3, to: 4, t: 'Agent search', s: 'Searches by itself', r: '76% → 84%' },
  { from: 4, to: 9, t: 'Fine-tuning', s: 'Smaller live fixes', r: '79% → 82%' },
  { from: 9, to: 10, t: 'Links and FAQs', s: 'Links, more FAQs', r: '84% → 88%' },
]
const W = 870, H = 238, L = 44, R = 104, T = 34, B = 8
const x = (i: number) => L + (i * (W - L - R)) / 10
const y = (v: number) => T + ((100 - v) * (H - T - B)) / 100
const path = (arr: number[]) => arr.map((v, i) => `${i ? 'L' : 'M'}${x(i)},${y(v)}`).join(' ')
const grid = [0, 25, 50, 75, 100]

// The lines draw in only when presenting: the exporter would capture them half drawn.
const { $renderContext } = useSlideContext()
const { isPrintMode } = useNav()
const play = ref(false)
onSlideEnter(() => { play.value = $renderContext.value === 'slide' && !isPrintMode.value && !navigator.webdriver })
onSlideLeave(() => { play.value = false })
</script>

<template>
<div>
  <svg :viewBox="`0 0 ${W} ${H}`" class="chart" :class="{ play }" role="img" aria-label="Over five rounds of improvement, correct answers rose from 59 to 88 percent and wrong answers fell from 19 to 1 percent">
    <g v-for="(r, i) in rounds" :key="r.t">
      <rect :x="x(r.from)" :y="T" :width="x(r.to) - x(r.from)" :height="H - T - B" :fill="i % 2 ? '#0c1c15' : '#102a1e'" />
      <circle :cx="(x(r.from) + x(r.to)) / 2" :cy="15" r="11" fill="#8be07a" />
      <text :x="(x(r.from) + x(r.to)) / 2" :y="19.5" text-anchor="middle" class="pin">{{ i + 1 }}</text>
    </g>
    <g v-for="g in grid" :key="g">
      <line :x1="L" :x2="W - R" :y1="y(g)" :y2="y(g)" stroke="#1d3a2b" />
      <text :x="L - 9" :y="y(g) + 4" text-anchor="end" class="ax">{{ g }}%</text>
    </g>
    <path :d="path(correct)" fill="none" stroke="#1ba96e" stroke-width="3" class="draw" />
    <path :d="path(wrong)" fill="none" stroke="#f07a62" stroke-width="2.6" class="draw d2" />
    <circle v-for="(v, i) in correct" :key="'c' + i" :cx="x(i)" :cy="y(v)" r="4" fill="#1ba96e" />
    <circle v-for="(v, i) in wrong" :key="'w' + i" :cx="x(i)" :cy="y(v)" r="3.4" fill="#f07a62" />
    <text :x="x(0) + 8" :y="y(59) + 20" class="pt g">59%</text>
    <text :x="x(0) + 8" :y="y(19) - 9" class="pt r">19%</text>
    <text :x="x(9) - 8" :y="y(6.9) - 8" text-anchor="end" class="note">partly a grading mistake</text>
    <text :x="x(10) + 11" :y="y(87.8) + 5" class="end g">Correct 88%</text>
    <text :x="x(10) + 11" :y="y(1.3) + 5" class="end r">Wrong 1%</text>
  </svg>
  <div class="rounds">
    <div v-for="(r, i) in rounds" :key="r.t">
      <i>{{ i + 1 }}</i>
      <b>{{ r.t }}</b>
      <span>{{ r.s }}</span>
      <em>{{ r.r }}</em>
    </div>
  </div>
</div>
</template>

<style scoped>
.chart { display: block; width: 100%; height: auto; overflow: visible; }
.ax { fill: #9aa59c; font-size: 12px; }
.pin { fill: #07130e; font-size: 13px; font-weight: 700; }
.note { fill: #f07a62; font-size: 12.5px; }
.pt, .end { font-size: 14px; font-weight: 600; font-variant-numeric: tabular-nums; }
.g { fill: #8be07a; } .r { fill: #f07a62; }
.play .draw { stroke-dasharray: 2000; stroke-dashoffset: 2000; animation: draw 1.8s ease forwards; }
.play .d2 { animation-delay: .3s; }
@media (prefers-reduced-motion: reduce) { .play .draw { animation: none; stroke-dashoffset: 0; } }
@keyframes draw { to { stroke-dashoffset: 0; } }
.rounds { display: grid; grid-template-columns: repeat(5, minmax(0, 1fr)); gap: .55rem; margin-top: .6rem; }
.rounds > div { position: relative; padding: .42rem .4rem .42rem 1.65rem; background: #0d1d15; border: 1px solid #1e3a2c; border-radius: 8px; }
.rounds i { position: absolute; left: .45rem; top: .48rem; width: 1rem; height: 1rem; display: flex; align-items: center; justify-content: center; border-radius: 50%; background: #8be07a; font-style: normal; font-size: .75rem; font-weight: 700; color: #07130e; }
.rounds b { display: block; font-size: .8rem; font-weight: 600; line-height: 1.25; color: #ece7da; }
.rounds span { display: block; margin-top: .08rem; font-size: .75rem; line-height: 1.25; color: #aeb4a9; }
.rounds em { display: block; margin-top: .18rem; font-style: normal; font-size: .8rem; font-weight: 600; color: #8be07a; }
</style>
