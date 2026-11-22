<script setup lang="ts">
import { onSlideEnter, onSlideLeave, useNav, useSlideContext } from '@slidev/client'
import { ref } from 'vue'

const steps = [
  { t: 'Prepare sources', s: 'Clean, checked text', k: 'gap' },
  { t: 'Store knowledge', s: 'Q&A and documents', k: 'gap' },
  { t: 'Find evidence', s: 'Search and rank', k: 'design' },
  { t: 'Write the answer', s: 'An agent with tools' },
  { t: 'Deliver', s: 'Web and Discord' },
  { t: 'Observe', s: 'Logs and test data' },
]

// The sweep runs only when presenting: the exporter is a headless browser and
// would otherwise capture the nodes mid-animation.
const { $renderContext } = useSlideContext()
const { isPrintMode } = useNav()
const play = ref(false)
onSlideEnter(() => { play.value = $renderContext.value === 'slide' && !isPrintMode.value && !navigator.webdriver })
onSlideLeave(() => { play.value = false })
</script>

<template>
  <div class="flow" :class="{ play }">
    <div class="tag gap"><span>Biggest gap: missing knowledge</span></div>
    <div class="tag design"><span>Most design choices</span></div>

    <div class="rail" />
    <div v-for="(s, i) in steps" :key="s.t" class="step" :class="s.k" :style="{ gridColumn: i + 1, '--i': i }">
      <div class="node">{{ i + 1 }}</div>
      <div class="t">{{ s.t }}</div>
      <div class="d">{{ s.s }}</div>
    </div>

    <div class="back"><span>When an answer is wrong, trace it back to the step that failed</span></div>
  </div>
</template>

<style scoped>
.flow { position: relative; display: grid; grid-template-columns: repeat(6, minmax(0, 1fr)); grid-template-rows: auto auto auto; }

.tag { grid-row: 1; display: flex; flex-direction: column; align-items: center; margin: 0 .5rem .8rem; font-size: .78rem; font-weight: 600; white-space: nowrap; }
.tag::after { content: ''; align-self: stretch; height: .42rem; margin-top: .35rem; border: 1.5px solid currentColor; border-bottom: 0; border-radius: 4px 4px 0 0; }
.tag.gap { grid-column: 1 / 3; color: #8be07a; }
.tag.design { grid-column: 3; color: #36c98a; }

.rail {
  grid-column: 1 / -1; grid-row: 2; align-self: start; height: 3px; margin: calc(1.6rem - 2.5px) calc(100% / 12) 0;
  background: linear-gradient(90deg, #8be07a 0, #8be07a 20%, #36c98a 40%, #2a4536 60%, #2a4536 100%);
  transform-origin: left;
}

.step { grid-row: 2; position: relative; display: flex; flex-direction: column; align-items: center; text-align: center; min-width: 0; }
.node {
  width: 3.2rem; height: 3.2rem; display: flex; align-items: center; justify-content: center; border-radius: 50%;
  background: #12281d; border: 1.5px solid #2f5a44; box-shadow: 0 0 0 5px #07130e;
  font-family: 'Unbounded', sans-serif; font-weight: 500; font-size: 1.15rem; color: #ece7da;
}
.gap .node { background: #8be07a; border-color: #8be07a; color: #07130e; }
.design .node { background: #36c98a; border-color: #36c98a; color: #07130e; }
.t { margin-top: .85rem; font-size: .96rem; font-weight: 600; line-height: 1.3; color: #ece7da; }
.gap .t { color: #8be07a; }
.design .t { color: #36c98a; }
.d { margin-top: .22rem; font-size: .84rem; line-height: 1.4; color: #b8bcb0; }

.back {
  grid-column: 1 / -1; grid-row: 3; position: relative; height: 1.25rem; margin: 1.05rem calc(100% / 12) 0;
  border: 1.5px solid #2f6b4b; border-top: 0; border-radius: 0 0 12px 12px;
}
.back::before {
  content: ''; position: absolute; left: -5px; top: -8px;
  border-left: 5.5px solid transparent; border-right: 5.5px solid transparent; border-bottom: 9px solid #8be07a;
}
.back span {
  position: absolute; left: 50%; bottom: 0; transform: translate(-50%, 50%); padding: 0 1rem; background: #07130e;
  font-family: 'Unbounded', sans-serif; font-weight: 500; font-size: .84rem; line-height: 1.4; color: #8be07a; white-space: nowrap;
}

.play .rail { animation: rail .75s ease both; }
.play .node { animation: pop .4s cubic-bezier(.2, .9, .3, 1.2) both; animation-delay: calc(var(--i) * .11s); }
@keyframes rail { from { transform: scaleX(0); } to { transform: scaleX(1); } }
@keyframes pop { from { opacity: 0; transform: scale(.6); } to { opacity: 1; transform: none; } }
@media (prefers-reduced-motion: reduce) { .play .rail, .play .node { animation: none; } }
</style>
