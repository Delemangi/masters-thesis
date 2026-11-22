<script setup lang="ts">
const layers = [
  { l: 'Faculty sources', c: ['finki.ukim.mk', 'EduPage timetables', 'Thesis records', 'Moodle', 'BigBlueButton', 'Official documents'] },
  { l: 'Collectors', c: ['services-scraper', 'courses-scraper', 'timetables API', 'bachelors and masters APIs', 'finki-auth'] },
  { l: 'Shared data', c: ['Data (Directus)', 'data.finki-hub.com', 'documents'], on: true },
  { l: 'Chatbot', c: ['api: agent and RAG', 'gpu-api: BGE-M3', 'mcp: tools', 'PostgreSQL with pgvector'], on: true },
  { l: 'What students use', c: ['Chat', 'Discord bot', 'Courses', 'Timetables', 'Theses', 'Recordings', 'Shell'] },
]
</script>

<template>
  <div class="map">
    <div v-for="r in layers" :key="r.l" class="row" :class="{ on: r.on }">
      <div class="l">{{ r.l }}</div>
      <div class="c"><span v-for="x in r.c" :key="x">{{ x }}</span></div>
    </div>
  </div>
</template>

<style scoped>
.map { display: flex; flex-direction: column; gap: .55rem; }
.row { display: grid; grid-template-columns: 9.5rem 1fr; align-items: center; padding: .62rem .9rem; background: #0d1d15; border: 1px solid #1e3a2c; border-radius: 9px; }
.row.on { border-color: #1ba96e; background: #0f2b1f; }
.l { font-size: .84rem; font-weight: 600; color: #ece7da; }
.on .l { color: #8be07a; }
.c { display: flex; flex-wrap: wrap; gap: .34rem; }
.c span { padding: .14rem .5rem; font-size: .74rem; line-height: 1.4; color: #c3c4b8; background: #10241a; border: 1px solid #24432f; border-radius: 5px; }
.on .c span { color: #ece7da; border-color: #2f6b4b; }
</style>
