<script setup lang="ts">
const loop = [
  { t: 'Think', s: 'The model decides what it still needs' },
  { t: 'Act', s: 'It calls one or more tools' },
  { t: 'Observe', s: 'It reads what they returned' },
]
const tools = [
  { k: 'Courses', v: 'Courses, study programs' },
  { k: 'People', v: 'Staff, faculty leadership' },
  { k: 'Schedules', v: 'Timetables, rooms, exam sessions' },
  { k: 'Theses', v: 'Theses, statistics, committee picks' },
  { k: 'News', v: 'Faculty announcements' },
]
</script>

<template>
  <div class="wrap">
    <div class="left">
      <div class="end">Student question</div>
      <i class="down" />
      <div class="loop">
        <div v-for="(s, i) in loop" :key="s.t" class="step">
          <div class="n">{{ i + 1 }}</div>
          <div><b>{{ s.t }}</b><span>{{ s.s }}</span></div>
        </div>
        <div class="back"><span>Need more?</span></div>
      </div>
      <i class="down" />
      <div class="end on">Answer with sources</div>
      <p class="limits">Limits per answer: <b>4</b> searches, <b>15</b> tool calls, <b>10</b> model calls</p>
    </div>

    <div class="right">
      <div class="label">Tools the agent can call</div>
      <section class="rag">
        <h3>Knowledge search (RAG)</h3>
        <p>FAQs, documents and useful links</p>
        <ol>
          <li><b>Search</b><span class="nw">BGE-M3 embeddings,<br>keyword search<br>(FAQs only)</span></li>
          <li><b>Rank</b><span class="nw">BGE-reranker-v2-m3</span></li>
          <li class="hot"><b>Filter</b><span>Under 0.03 dropped</span></li>
          <li><b>Select</b><span>Best 10, up to 5 links</span></li>
        </ol>
      </section>
      <section class="data">
        <h3>Live data tools</h3>
        <p class="sub">Through MCP, plus a built-in committee recommender</p>
        <div v-for="t in tools" :key="t.k" class="row"><b>{{ t.k }}</b><span>{{ t.v }}</span></div>
      </section>
    </div>
  </div>
</template>

<style scoped>
.wrap { display: grid; grid-template-columns: .82fr 1.18fr; gap: 2.2rem; align-items: start; }

.end { padding: .42rem .8rem; text-align: center; font-size: .9rem; font-weight: 600; color: #ece7da; background: #0d1d15; border: 1px solid #2a4536; border-radius: 9px; margin-right: 3.1rem; }
.end.on { color: #07130e; background: #8be07a; border-color: #8be07a; }
.down { display: block; width: 2px; height: .62rem; margin: 0 calc(50% + 1.55rem - 1px) 0 auto; background: #2f6b4b; }

.loop { position: relative; display: flex; flex-direction: column; gap: .62rem; padding: .78rem .8rem; margin-right: 3.1rem; background: #0f2b1f; border: 1px solid #1ba96e; border-radius: 11px; }
.step { display: grid; grid-template-columns: 1.9rem 1fr; gap: .55rem; align-items: center; }
.n { width: 1.9rem; height: 1.9rem; display: flex; align-items: center; justify-content: center; border-radius: 50%; background: #36c98a; font-family: 'Unbounded', sans-serif; font-size: .8rem; font-weight: 500; color: #07130e; }
.step b { display: block; font-size: .92rem; font-weight: 600; line-height: 1.2; color: #ece7da; }
.step span { display: block; font-size: .76rem; line-height: 1.25; color: #c3c4b8; }

.back { position: absolute; top: 1.7rem; bottom: 1.7rem; right: -1.75rem; width: 1.75rem; border: 1.5px solid #8be07a; border-left: 0; border-radius: 0 10px 10px 0; }
.back::before { content: ''; position: absolute; left: -1px; top: -6.5px; border-top: 5.5px solid transparent; border-bottom: 5.5px solid transparent; border-right: 9px solid #8be07a; }
.back span { position: absolute; top: 50%; left: 100%; transform: translate(-50%, -50%) rotate(90deg); padding: 0 .4rem; background: #07130e; font-size: .72rem; font-weight: 600; color: #8be07a; white-space: nowrap; }

.limits { margin: .7rem 0 0 !important; font-size: .76rem; line-height: 1.35; color: #aeb4a9; }
.limits b { color: #8be07a !important; }

.label { margin-bottom: .42rem; font-size: .76rem; color: #9aa59c; }
section { padding: .65rem .9rem; background: #0d1d15; border: 1px solid #1e3a2c; border-radius: 10px; }
section + section { margin-top: .55rem; }
section.rag { border-color: #1ba96e; }
section h3 { margin: 0 !important; font-size: .94rem !important; font-weight: 600; line-height: 1.25; color: #8be07a !important; }
.rag p, p.sub { margin: .04rem 0 0 !important; font-size: .76rem; color: #aeb4a9; }
.rag li span.nw { white-space: nowrap; }
.rag ol { list-style: none; display: grid; grid-template-columns: 1.3fr 1.25fr .85fr .8fr; gap: .4rem; margin: .45rem 0 0 !important; padding: 0 !important; }
.rag li { margin: 0 !important; padding-left: .45rem; border-left: 2px solid #2f5a44; }
.rag li.hot { border-left-color: #36c98a; }
.rag li b { display: block; font-size: .8rem; font-weight: 600; line-height: 1.25; color: #ece7da; }
.rag li.hot b { color: #36c98a; }
.rag li span { display: block; font-size: .75rem; line-height: 1.25; color: #aeb4a9; }

.row { display: grid; grid-template-columns: 5.2rem 1fr; padding: .17rem 0; font-size: .8rem; line-height: 1.3; }
.sub + .row { margin-top: .22rem; }
.row b { font-weight: 600; color: #ece7da; }
.row span { color: #c3c4b8; }
</style>
