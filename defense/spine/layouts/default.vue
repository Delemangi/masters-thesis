<template>
  <div class="slidev-layout split">
    <Spine class="sp" />
    <div class="titlecol" />
    <main class="main"><slot /></main>
  </div>
</template>

<style scoped>
.split { padding: 0 !important; display: grid; grid-template-columns: 4.2rem 29% 1fr; position: relative; }
.split::before { display: none; }
.sp, .titlecol { background: linear-gradient(180deg, #0f2219, #0b1912); }
.titlecol { border-right: 1px solid #1e3a2c; }
.main { padding: 3rem 2.8rem 2.4rem; display: flex; flex-direction: column; min-width: 0; }
/* the title sits in the title column, pinned to the same height on every slide */
.main > :deep(h1) {
  position: absolute; left: 5.6rem; width: calc(29% - 3rem); top: 2.85rem;
  font-size: 1.42rem !important; line-height: 1.28 !important; margin: 0 !important; max-width: none !important;
}
</style>
