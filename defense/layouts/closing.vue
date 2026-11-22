<template>
  <div class="slidev-layout dark-slide closing">
    <div class="field" />
    <div class="mark"><LogoMark /></div>
    <div class="content"><slot /></div>
  </div>
</template>

<style scoped>
.closing { position: relative; overflow: hidden; display: flex; flex-direction: column; justify-content: center; }
.closing::before { display: none; }
.field {
  position: absolute; inset: 0;
  background:
    radial-gradient(circle at 79% 50%, rgba(27, 169, 110, .22) 0, rgba(27, 169, 110, 0) 34%),
    repeating-linear-gradient(45deg, rgba(139, 224, 122, .045) 0 1px, transparent 1px 26px),
    repeating-linear-gradient(135deg, rgba(139, 224, 122, .045) 0 1px, transparent 1px 26px);
  mask-image: radial-gradient(ellipse 48% 75% at 79% 50%, black 0%, transparent 78%);
}
.mark { position: absolute; right: 4.2rem; top: 50%; width: 15rem; transform: translateY(-50%); }
.content { position: relative; z-index: 1; }
</style>
