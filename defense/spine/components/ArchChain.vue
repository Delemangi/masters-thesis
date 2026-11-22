<script setup lang="ts">
const steps = [
  { t: 'Prepare sources', s: 'Official documents turned into checked text', i: 'PDF and Word → Markdown, read against the original' },
  { t: 'Store knowledge', s: 'FAQs and document passages, ready to search', i: 'PostgreSQL with pgvector, BGE-M3 embeddings' },
  { t: 'Find evidence', s: 'Pick the passages that answer the question', i: 'Search, then a reranker scores each passage', on: true },
  { t: 'Write the answer', s: 'The model answers from that evidence only', i: 'An agent that can search and call tools' },
  { t: 'Deliver', s: 'Same answer on the web and in Discord', i: 'chat.finki-hub.com and the Discord bot' },
  { t: 'Observe', s: 'Logs and test data kept apart', i: 'Stored chats, usage metadata, private test sets' },
]
</script>

<template>
  <div class="chain">
    <div v-for="(s, i) in steps" :key="s.t" class="col" :class="{ on: s.on }">
      <div class="chev"><span>{{ i + 1 }}</span></div>
      <div class="t">{{ s.t }}</div>
      <div class="s">{{ s.s }}</div>
      <div class="i">{{ s.i }}</div>
    </div>
  </div>
</template>

<style scoped>
.chain { display: grid; grid-template-columns: repeat(6, 1fr); gap: .35rem; }
.chev {
  height: 2.6rem; display: flex; align-items: center; padding-left: 1.4rem; margin-bottom: .8rem;
  background: linear-gradient(90deg, #12281d, #1a3a2a);
  clip-path: polygon(0 0, calc(100% - 14px) 0, 100% 50%, calc(100% - 14px) 100%, 0 100%, 14px 50%);
  font-family: 'Unbounded', sans-serif; font-size: .9rem; color: #9aa59c;
}
.col:first-child .chev { clip-path: polygon(0 0, calc(100% - 14px) 0, 100% 50%, calc(100% - 14px) 100%, 0 100%); padding-left: .9rem; }
.on .chev { background: linear-gradient(90deg, #1ba96e, #8be07a); color: #07130e; }
.t { font-weight: 600; font-size: .9rem; color: #ece7da; }
.on .t { color: #8be07a; }
.s { font-size: .78rem; color: #c3c4b8; margin-top: .3rem; line-height: 1.4; }
.i { font-size: .68rem; color: #9aa59c; margin-top: .55rem; padding-top: .5rem; border-top: 1px solid #1e3a2c; line-height: 1.4; }
</style>
