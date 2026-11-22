<script setup lang="ts">
const sources = ['Faculty website', 'Timetables', 'Thesis records', 'Moodle courses']
const stats = [
  { n: '371', l: 'courses' },
  { n: '137', l: 'staff' },
  { n: '4,339', l: 'theses' },
  { n: '86', l: 'rooms' },
]
const apps = [
  { t: 'Chat', s: 'The implementation of this thesis', on: true },
  { t: 'Discord bot', s: 'Course, staff and exam lookups' },
  { t: 'Courses', s: 'Catalog and semester planner' },
  { t: 'Timetables', s: 'Schedules and exam sessions' },
]
const ys = [12.5, 37.5, 62.5, 87.5]
const appYs = [13, 35, 53.5, 72, 90.5]
</script>

<template>
  <div class="flow">
    <div class="col">
      <div class="head">From the faculty</div>
      <div class="rows">
        <div v-for="s in sources" :key="s" class="src">{{ s }}</div>
      </div>
    </div>

    <svg class="wire" viewBox="0 0 100 100" preserveAspectRatio="none" aria-hidden="true">
      <path v-for="y in ys" :key="y" :d="`M0 ${y} C50 ${y} 50 50 100 50`" />
    </svg>

    <div class="hub">
      <div class="name">Data</div>
      <div class="dom">data.finki-hub.com</div>
      <p>One source of truth, built on Directus. These tools all read it through the same API.</p>
      <div class="stats">
        <div v-for="s in stats" :key="s.l"><b>{{ s.n }}</b><span>{{ s.l }}</span></div>
      </div>
    </div>

    <svg class="wire" viewBox="0 0 100 100" preserveAspectRatio="none" aria-hidden="true">
      <path v-for="y in appYs" :key="y" :class="{ lit: y === appYs[0], more: y === appYs[4] }" :d="`M0 50 C50 50 50 ${y} 100 ${y}`" />
    </svg>

    <div class="col">
      <div class="head">Read by</div>
      <div class="rows five">
        <div v-for="a in apps" :key="a.t" class="app" :class="{ on: a.on }">
          <b>{{ a.t }}</b><span>{{ a.s }}</span>
        </div>
        <div class="app more">
          <div class="dots" aria-label="and more"><i /><i /><i /></div>
          <span>MCP tools, the open API and more</span>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.flow { display: grid; grid-template-columns: 9.5rem 3.6rem 1fr 3.6rem 14.5rem; height: 15rem; }
.col { display: flex; flex-direction: column; min-height: 0; }
.head { height: 1.5rem; flex: none; font-size: .76rem; color: #9aa59c; }
.rows { flex: 1; display: grid; grid-template-rows: repeat(4, 1fr); min-height: 0; }
.rows.five { grid-template-rows: 1.4fr 1fr 1fr 1fr 1fr; }
.src { display: flex; align-items: center; font-size: .9rem; color: #c3c4b8; }
.app { display: flex; flex-direction: column; justify-content: center; padding-left: .85rem; border-left: 2px solid #2a4536; margin: .14rem 0; }
.app b { font-size: .9rem; font-weight: 600; color: #ece7da; line-height: 1.25; }
.app span { font-size: .76rem; color: #9aa59c; line-height: 1.3; }
.app.on { margin: 0 0 .2rem; padding: 0 .85rem; background: rgba(27, 169, 110, .2); border: 1px solid #8be07a; border-radius: 9px; }
.app.more { border-left-style: dashed; }
.dots { display: flex; gap: .24rem; height: 1.05rem; align-items: center; }
.dots i { width: .3rem; height: .3rem; border-radius: 50%; background: #8be07a; }
.app.on b { font-family: 'Unbounded', sans-serif; font-weight: 500; font-size: 1.05rem; color: #8be07a; }
.app.on span { margin-top: .1rem; font-size: .76rem; font-weight: 500; color: #ece7da; }
.wire { width: 100%; height: calc(100% - 1.5rem); margin-top: 1.5rem; overflow: visible; }
.wire path { fill: none; stroke: #2a4536; stroke-width: 1.25; vector-effect: non-scaling-stroke; }
.wire path.more { stroke-dasharray: 3 4; }
.wire path.lit { stroke: #8be07a; stroke-width: 2.25; }
.hub { margin-top: 1.5rem; padding: .85rem 1.35rem; background: #0d1d15; border: 1px solid #1ba96e; border-radius: 12px; display: flex; flex-direction: column; min-width: 0; }
.name { font-family: 'Unbounded', sans-serif; font-weight: 500; font-size: 1.45rem; line-height: 1.1; color: #ece7da; }
.dom { font-size: .76rem; color: #8be07a; margin-top: .3rem; }
.hub p { margin: .6rem 0 0; font-size: .84rem; line-height: 1.42; color: #c3c4b8; }
.stats { margin-top: auto; display: grid; grid-template-columns: repeat(4, auto); justify-content: space-between; gap: .6rem; padding-top: .7rem; border-top: 1px solid #1e3a2c; }
.stats b { display: block; font-family: 'Unbounded', sans-serif; font-weight: 500; font-size: .92rem; line-height: 1.2; color: #ece7da; font-variant-numeric: tabular-nums; }
.stats span { display: block; font-size: .76rem; line-height: 1.2; margin-top: .15rem; color: #9aa59c; }
</style>
