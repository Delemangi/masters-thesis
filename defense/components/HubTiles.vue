<script setup lang="ts">
const tiles = [
  { t: 'Announcements', d: 'FINKI Hub Discord', s: 'New faculty posts, delivered to Discord channels as they appear' },
  { t: 'Theses', d: 'theses.finki-hub.com', s: 'Search past bachelor and master theses and their mentors' },
  { t: 'Timetables', d: 'rasporedi.finki-hub.com', s: 'Class schedules, current and past' },
  { t: 'Courses', d: 'predmeti.finki-hub.com', s: 'Every course, plus a semester enrollment planner' },
  { t: 'Recordings', d: 'snimki.finki-hub.com', s: 'Links to lecture and exercise recordings' },
  { t: 'Shell', d: 'shell.finki-hub.com', s: 'A Linux terminal in the browser' },
]
</script>

<template>
  <div class="grid-wrap">
    <div class="hero">
      <div class="tag">This thesis</div>
      <div class="name">Chat</div>
      <div class="dom">chat.finki-hub.com and the Discord bot</div>
      <p>Answers questions about rules, deadlines and procedures from the faculty's own documents, and looks things up in the other FINKI Hub services.</p>
    </div>
    <div v-for="t in tiles" :key="t.t" class="tile">
      <div class="name">{{ t.t }}</div>
      <div class="dom">{{ t.d }}</div>
      <p>{{ t.s }}</p>
    </div>
  </div>
</template>

<style scoped>
.grid-wrap { display: grid; grid-template-columns: 1.55fr 1fr 1fr 1fr; grid-template-rows: 1fr 1fr; gap: .7rem; }
.tile, .hero { padding: .85rem 1rem; background: #0d1d15; border: 1px solid #1e3a2c; border-radius: 10px; }
.hero { grid-row: span 2; position: relative; padding: 1.3rem 1.4rem; border-color: #1ba96e; display: flex; flex-direction: column; justify-content: flex-end; }
.tag { position: absolute; top: 1.2rem; left: 1.4rem; font-size: .7rem; font-weight: 600; color: #8be07a; }
.name { font-family: 'Unbounded', sans-serif; font-weight: 500; font-size: .92rem; color: #ece7da; }
.hero .name { font-size: 1.45rem; line-height: 1.15; }
.dom { font-size: .7rem; color: #9aa59c; margin-top: .2rem; }
p { margin: .45rem 0 0; font-size: .74rem; line-height: 1.4; color: #b2b5aa; }
.hero p { font-size: .9rem; color: #c3c4b8; max-width: 19rem; }
</style>
