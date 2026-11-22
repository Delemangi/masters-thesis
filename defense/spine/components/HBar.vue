<script setup lang="ts">
const props = withDefaults(defineProps<{
  label: string
  value: number
  max?: number
  suffix?: string
  color?: string
  sub?: string
  labelWidth?: string
}>(), { max: 100, suffix: '', color: 'var(--green)', labelWidth: '11rem' })
const pct = Math.max(0, Math.min(100, (props.value / props.max) * 100))
const fmt = props.value >= 1000 ? props.value.toLocaleString('en-US') : String(props.value)
</script>

<template>
  <div class="hbar" :style="{ gridTemplateColumns: `${labelWidth} 1fr 3.6rem` }">
    <div class="lbl">{{ label }}<span v-if="sub" class="sub">{{ sub }}</span></div>
    <div class="track"><div class="fill" :style="{ width: pct + '%', background: color }" /></div>
    <div class="val">{{ fmt }}{{ suffix }}</div>
  </div>
</template>

<style scoped>
.hbar { display: grid; align-items: center; gap: .6rem; margin: .3rem 0; font-size: .8rem; }
.lbl { color: #d9d6ca; text-align: right; line-height: 1.15; }
.sub { display: block; color: #9aa59c; font-size: .66rem; }
.track { height: .95rem; background: #10241a; clip-path: polygon(0 0, 100% 0, 100% 100%, 0 100%); }
.fill { height: 100%; clip-path: polygon(0 0, 100% 0, calc(100% - 6px) 100%, 0 100%); transform-origin: left; animation: grow .8s cubic-bezier(.2,.8,.2,1) both; }
.val { font-variant-numeric: tabular-nums; color: #ece7da; font-size: .78rem; }
@keyframes grow { from { transform: scaleX(0); } to { transform: scaleX(1); } }
</style>
