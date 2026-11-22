<script setup lang="ts">
const props = withDefaults(defineProps<{
  rows: { label: string; est: number; lo: number; hi: number; hl?: boolean; gap?: boolean }[]
  min?: number
  max?: number
}>(), { min: -12, max: 15 })
const W = 620, rowH = 40, L = 262, R = 72
const offsets: number[] = []
let acc = 0
for (const r of props.rows) { if (r.gap) acc += 14; offsets.push(acc); acc += rowH }
const H = acc + 28
const x = (v: number) => L + ((v - props.min) * (W - L - R)) / (props.max - props.min)
const ticks = [-10, -5, 0, 5, 10, 15].filter(t => t >= props.min && t <= props.max)
</script>

<template>
  <svg :viewBox="`0 0 ${W} ${H}`" class="fp">
    <line v-for="t in ticks" :key="t" :x1="x(t)" :x2="x(t)" y1="0" :y2="H - 20"
      :stroke="t === 0 ? '#7d9085' : '#14291f'" />
    <text v-for="t in ticks" :key="'t' + t" :x="x(t)" :y="H - 5" text-anchor="middle" class="ax">{{ t > 0 ? '+' : '' }}{{ t }}</text>
    <g v-for="(r, i) in rows" :key="i" :transform="`translate(0, ${offsets[i] + 16})`">
      <text :x="L - 12" y="4" text-anchor="end" class="lbl">{{ r.label }}</text>
      <line :x1="x(r.lo)" :x2="x(r.hi)" y1="0" y2="0" :stroke="r.hl ? '#1ba96e' : '#9aa59c'" stroke-width="1.8" stroke-linecap="round" />
      <circle :cx="x(r.est)" cy="0" r="4.5" :fill="r.hl ? '#1ba96e' : '#ece7da'" />
      <text :x="W - R + 10" y="4" class="val" :fill="r.hl ? '#8be07a' : '#9aa59c'">{{ r.est > 0 ? '+' : '' }}{{ r.est.toFixed(2) }}</text>
    </g>
  </svg>
</template>

<style scoped>
.fp { width: 100%; height: auto; }
.ax { fill: #9aa59c; font-size: 14px; }
.lbl { fill: #d9d6ca; font-size: 16px; }
.val { font-size: 15px; font-variant-numeric: tabular-nums; }
</style>
