<template>
  <div class="slidev-layout wide">
    <Spine class="sp" />
    <main class="wmain"><slot /></main>
  </div>
</template>

<style scoped>
.wide { padding: 0 !important; display: grid; grid-template-columns: 4.2rem 1fr; }
.sp { background: linear-gradient(180deg, #0f2219, #0b1912); border-right: 1px solid #1e3a2c; }
.wmain { padding: 2.85rem 2.8rem 2.2rem 2.4rem; display: flex; flex-direction: column; min-width: 0; }
.wmain > :deep(h1) { flex: none; font-size: 1.42rem !important; line-height: 1.28 !important; margin: 0 0 1.4rem !important; }
</style>
