---
title: A Reference Architecture for Domain-Specific RAG Assistants
info: Master's Thesis, Stefan Milev, FCSE, December 2026
colorSchema: dark
aspectRatio: 16/9
canvasWidth: 980
transition: fade-out
fonts:
  sans: Inter
  mono: JetBrains Mono
  provider: none
routerMode: hash
layout: hub-cover
drawings:
  persist: false
---

<div class="flex items-center gap-3 mb-14">
  <img src="/ukim-logo-white.png" class="h-11 opacity-85" />
  <img src="/finki-logo-white.png" class="h-6 opacity-85 ml-1" />
  <div class="tiny muted leading-snug ml-3">Ss. Cyril and Methodius University in Skopje<br/>Faculty of Computer Science and Engineering</div>
</div>

<p class="lime !mb-4 font-semibold uppercase tracking-[0.16em] !text-[0.72rem]">Master's Thesis</p>

<h1 class="!text-[1.86rem] !leading-[1.24] !tracking-[-0.025em] !mb-14 !max-w-[36rem]">A reference architecture for building <span class="nowrap">domain-specific</span> <span class="nowrap">retrieval-augmented</span> conversational assistants</h1>

<div class="grid grid-cols-[auto_auto_auto] gap-x-12 gap-y-1 text-sm w-fit">
  <span class="muted tiny">Candidate</span><span class="muted tiny">Mentor</span><span class="muted tiny">Skopje</span>
  <b>Stefan Milev, 249053</b><b>Prof. Dr. Riste Stojanov</b><b>December 2026</b>
</div>

<!--
[0:45] Good morning. I'm Stefan Milev, and my thesis is about chatbots that answer questions from an institution's own documents. More importantly, it's about how we can tell whether their answers are actually right. The case study is a chatbot I built for FCSE students.
-->

---
section: Context
noMark: true
layout: wide
---

<div class="lockup"><b>FINKI Hub</b><span>independent student organization, not affiliated with the faculty</span></div>

# One shared data layer behind the student tools

<HubData />

<p class="caption !mt-2 !mb-0">Other projects include a thesis browser, lecture recordings, faculty announcements and much more.</p>

<div class="maintained">
  <div class="mt-lead">
    <div class="mt-title"><i></i>Actively maintained</div>
    <div class="mt-sub"><b>Fully open source and MIT licensed.</b><br/>Anyone can read, reuse or contribute at <b>github.com/finki-hub</b></div>
  </div>
  <div class="mt-stats">
    <div><b>304</b><span>commits</span></div>
    <div><b>251</b><span>pull requests merged</span></div>
    <div><b>16</b><span>repositories updated</span></div>
  </div>
  <div class="mt-when">in November</div>
</div>

<!--
[1:15] Some context first. FINKI Hub is an independent student organization that builds tools for FCSE students. At the center is Data, a Directus service that brings together what the faculty publishes: courses, staff, rooms, timetables and theses. It is the single source of truth, and the tools read from it through one API: the Discord bot, the course catalog, the timetables and the chatbot, which is the implementation of this thesis. FINKI Hub also runs a thesis browser, lecture recordings, announcements and much more. And the important part: this is actively maintained. In November alone there have been 304 commits and 251 merged pull requests, across all 16 of our active repositories. Everything is fully open source under the permissive MIT license, so anyone can read the code, reuse it or contribute.
-->

---
section: Problem
---

# The answers students need are scattered

<div class="grid grid-cols-[1fr_1fr] gap-11">
<div>
  <div class="label">What students ask, shortened from real emails</div>
  <div class="bubbles">
    <div class="bubble">"I haven't passed Object-Oriented Programming, and Algorithms now shows an unmet prerequisite. Isn't it enough that I attended it?"</div>
    <div class="bubble">"I'll be abroad during enrollment. Can I pay for the new semester before the dates are out, and can someone submit my documents for me?"</div>
    <div class="bubble">"I enrolled in a sixth course with a request. I don't pay tuition because of a special admission quota. Do I owe anything for the sixth course?"</div>
  </div>
</div>
<div class="stack tight">
  <div><h3>Scattered everywhere</h3><p>Regulations, decisions, web pages, announcements and past staff emails.</p></div>
  <div><h3>Sometimes conflicting</h3><p>"Transfer" appears in rules from 2013, 2019 and 2022, each with a different condition.</p></div>
  <div><h3>Often incomplete</h3><p>A rule may leave out the practical steps a student needs.</p></div>
  <div><h3>Some cases are really complicated</h3><p>One question can combine several rules, exceptions and deadlines.</p></div>
  <div><h3>Sometimes only word of mouth</h3><p>Some answers are in no public document. You only learn them by asking staff or older students.</p></div>
  <div><h3>In Macedonian, a low-resource language</h3><p>Few AI models and test sets are built for it, and students mix Cyrillic, Latin letters and English.</p></div>
</div>
</div>

<style>
.bubbles { display: flex; flex-direction: column; gap: .7rem; }
.bubble { padding: .75rem 1rem; font-size: .88rem; line-height: 1.45; color: #ece7da; background: #0d1d15; border: 1px solid #1e3a2c; border-radius: 14px 14px 14px 4px; }
.stack.tight { gap: .58rem; }
</style>

<!--
[1:30] Here's the problem. Students don't ask "what does article 31 say". They describe their own situation, like these three, shortened from real emails. These are everyday topics, prerequisites, enrollment and fees, but each one has a twist: a course attended but not passed, a student who is abroad, an extra course on a special quota. Cases like these combine several rules, exceptions and deadlines. The information is scattered across regulations, decisions, web pages, announcements and past emails. Some of it conflicts: the word "transfer" alone appears in three rules from 2013, 2019 and 2022, each with a different condition. Some of it is incomplete. And some answers are in no public document at all: you only find out by asking staff or older students. On top of that, all of this is in Macedonian, a low-resource language with few AI models and test sets built for it, and students mix Cyrillic, Latin letters and English. So a chatbot can't simply search the documents and be right every time.
-->

---
section: Problem
---

# What I set out to do

<div class="grid grid-cols-3 gap-4 mt-2 goals">
  <div class="card"><h3>Work out how to build it</h3><p>A step-by-step design that any institution with specific domain knowledge could follow with its own documents.</p></div>
  <div class="card"><h3>Build one for FCSE</h3><p>A chatbot students can use on the web and in Discord.</p></div>
  <div class="card on"><h3>Find out how good it is</h3><p>Test it on real student questions, count how often it's right, and see what still goes wrong.</p></div>
</div>

<div class="grid grid-cols-[1fr_1.45fr] gap-10 mt-8 good">
  <div>
    <h3>What is it tested on?</h3>
    <p>Real student emails, Discord conversations and tickets to FSS, all anonymized.</p>
  </div>
  <div>
    <h3>What counts as a good answer?</h3>
    <p>The right rule, with its conditions, backed by references such as FAQs, documents and links. If the references can't settle it, telling the student which office to ask is also a good answer. The bot can't see grades or personal records, so those questions always go to Student Services.</p>
  </div>
</div>

<style>
.goals .card { padding: 1.1rem 1.2rem 1.25rem; }
.goals h3 { font-family: var(--display); font-weight: 500; font-size: 1rem; line-height: 1.3; margin-bottom: .55rem; }
.goals p { margin: 0; font-size: .88rem; line-height: 1.5; }
.good h3 { font-size: 1rem; margin-bottom: .3rem; }
.good p { margin: 0; font-size: .88rem; line-height: 1.55; }
</style>

<!--
[1:15] So I wanted to do three things. First, work out how to build an assistant like this, in a way any institution with specific domain knowledge could follow with its own documents. Second, build one for FCSE, on the web and in Discord. Third, find out how good it really is. I tested it on real student emails, Discord conversations and tickets to FSS, all anonymized. It helps to say what I mean by a good answer. It's the right rule with its conditions, backed by references like FAQs, documents and links, or, when the references can't settle it, telling the student which office to ask. Sometimes "ask Student Services" is the right answer, and for anything about a student's own grades it's the only one, because the bot can't see them.
-->

---
section: Problem
---

# The questions behind this thesis

<ol class="rq">
  <li><span>1</span>Can this actually work in practice?<em v-click="1">Yes*</em></li>
  <li><span>2</span>What is missing to make it reliable?<em v-click="1">Mostly knowledge*</em></li>
  <li><span>3</span>Can AI do this on its own?<em v-click="1">For most questions*</em></li>
  <li><span>4</span>Does giving it more information help?<em v-click="1">Not by itself*</em></li>
  <li><span>5</span>What actually made it better?<em v-click="1">Data, search, tools, some prompts*</em></li>
  <li><span>6</span>Can we rely on AI to grade the answers?<em v-click="1">Only with care*</em></li>
  <li><span>7</span>Could another institution reuse this?<em v-click="1">Designed to, not yet tried*</em></li>
</ol>

<p v-click="1" class="rq-note"><b>*</b> Mostly good news, but every answer comes with conditions, explained in the next slides.</p>

<style>
.slidev-layout ol.rq { list-style: none; margin: .4rem 0 0; padding: 0; display: flex; flex-direction: column; gap: 1.02rem; }
.slidev-layout ol.rq li { display: grid; grid-template-columns: 2.6rem 1fr 22rem; align-items: baseline; margin: 0; font-size: 1.2rem; line-height: 1.3; color: var(--ink); }
.rq span { font-family: var(--display); font-weight: 500; font-size: 1.2rem; color: var(--lime); }
.rq em { font-style: normal; font-weight: 600; font-size: 1.04rem; color: var(--lime); transition: opacity .55s ease, filter .55s ease !important; }
.rq em.slidev-vclick-hidden { opacity: .6 !important; filter: blur(8px); transform: none; }
.rq li:nth-child(2) em { transition-delay: .1s !important; }
.rq li:nth-child(3) em { transition-delay: .2s !important; }
.rq li:nth-child(4) em { transition-delay: .3s !important; }
.rq li:nth-child(5) em { transition-delay: .4s !important; }
.rq li:nth-child(6) em { transition-delay: .5s !important; }
.rq li:nth-child(7) em { transition-delay: .6s !important; }
.slidev-layout p.rq-note { margin: 1.7rem 0 0; font-size: .95rem; font-weight: 400; color: var(--ink-2); transition: opacity .55s ease .95s, filter .55s ease .95s !important; }
.rq-note b { color: var(--lime) !important; }
.slidev-layout p.rq-note.slidev-vclick-hidden { opacity: .6 !important; filter: blur(8px); transform: none; transition: none !important; }
@media (prefers-reduced-motion: reduce) { .rq em, .slidev-layout p.rq-note { transition: none !important; } }
</style>

<!--
[1:00] That gave me seven basic questions. Can this actually work in practice? What is missing to make it reliable? Can AI do this on its own? Does giving it more information help? What actually made it better? Can we rely on AI to grade the answers? And could another institution reuse this? (click) Here's a quick spoiler: yes, mostly knowledge, for most questions, not by itself, better data, search and tools plus some prompt rules, only with care, and designed to, but not yet tried. So, good news on all seven. But you may have noticed the asterisks: every answer comes with conditions, and that's what the next slides explain. I'll come back to all seven at the end.
-->

---
section: Problem
layout: wide
---

# What already exists, and what this adds

<div class="rw">
<section>
  <h3>Already exists</h3>
  <div><b>Chatbots that answer from documents</b><span>RAG, Lewis et al., 2020</span></div>
  <div><b>AI agents that choose their own searches</b><span>ReAct, Yao et al., 2023</span></div>
  <div><b>AI grading of chatbot answers</b><span>RAGAs, Es et al., 2024</span></div>
  <div><b>University support chatbots</b><span>Marcel, Trienes et al., 2025</span></div>
</section>
<section class="on">
  <h3>What this thesis adds</h3>
  <div><b>A design meant for other institutions to reuse</b></div>
  <div><b>A controlled test of how sources are selected</b></div>
  <div><b>A test of the live chatbot on real emails, in Macedonian</b></div>
  <div><b>A check of how far AI grading can be trusted</b></div>
</section>
</div>

<style>
.rw { display: grid; grid-template-columns: 1fr 1fr; gap: 1.2rem; margin-top: .4rem; }
.rw section { display: flex; flex-direction: column; padding: 1.15rem 1.35rem .7rem; background: var(--panel); border: 1px solid var(--edge); border-radius: 12px; }
.rw section.on { border-color: var(--green); }
.slidev-layout .rw h3 { margin: 0 0 .6rem; font-family: var(--display); font-weight: 500; font-size: 1.12rem; color: var(--ink); }
.slidev-layout .rw .on h3 { color: var(--lime); }
.rw section > div { flex: 1; display: flex; flex-direction: column; justify-content: center; min-height: 4.1rem; border-top: 1px solid var(--edge); }
.rw b { font-size: .98rem; font-weight: 500; line-height: 1.3; color: var(--ink); }
.rw span { margin-top: .12rem; font-size: .78rem; color: var(--ink-3); }
</style>

<!--
[0:45] Before the design, a quick look at what already exists. Chatbots that answer from documents are well known, and so are AI agents that choose their own searches and AI tools that grade answers. The closest work to mine is Marcel, also a university support chatbot tested on anonymized student emails, so testing on emails is not new here. What this thesis adds is the combination: a design meant for other institutions to reuse, though not yet tried elsewhere, a controlled test of how sources are selected, a test of the live chatbot on real emails in Macedonian, and a check of how far AI grading can be trusted.
-->

---
section: How it works
layout: wide
---

# Six steps from documents to answers

<ArchChain class="mt-14" />

<p class="reuse">To reuse it, an institution swaps in its own sources and keeps the six steps.</p>

<style>
.slidev-layout p.reuse { margin: 2.6rem 0 0; text-align: center; font-size: .92rem; color: var(--ink-2); }
</style>

<!--
[1:30] This is the architecture: six steps, left to right. Prepare the sources, store them, find the evidence, write the answer, deliver it, and observe. In my chatbot that means PostgreSQL with pgvector and BGE-M3 embeddings for storage, search plus a reranker to find evidence, and an agent with tools to write the answer. Steps 1 and 2 are highlighted because that's where the biggest gap turned out to be: missing knowledge. Step 3 is highlighted because it has the most design choices, so it's the one the controlled test changes. Each step hands a clear result to the next, so when an answer is wrong, you can trace it back to the step that failed. And to reuse this elsewhere, an institution swaps in its own sources and keeps the same six steps.
-->

---
section: How it works
layout: wide
---

# The agent loop and its tools

<SearchFlow class="mt-1" />

<!--
[1:30] The chatbot is an agent, so it works in a loop. It thinks about what it still needs, calls one or more tools, reads what they returned, and repeats until it can answer. Each answer is capped at 4 searches, 15 tool calls and 10 model calls, and when it hits a limit it's told to answer with what it has. It has two kinds of tools. The first is knowledge search, which is the RAG part: it searches FAQs and documents by meaning with BGE-M3 embeddings, plus keywords for FAQs, the BGE-reranker-v2-m3 model scores the results, anything below 0.03 is dropped, and the best 10 come back with the text around them, along with up to 5 relevant links. That filter is what the controlled test changes. The second kind is live data, mostly through MCP: courses, staff, timetables, rooms, exam sessions, theses and announcements, plus a built-in thesis committee recommender. So it looks these up instead of guessing.
-->

---
section: How it works
layout: wide
---

# What the chatbot can draw on

<div class="draw">
  <section>
    <h3>Written knowledge</h3>
    <p>Found with RAG search</p>
    <div class="big">
      <div><b>104</b><span>frequently asked questions</span></div>
      <div><b>65</b><span>official documents and web pages</span></div>
      <div><b>2,524</b><span>sections of text to search</span></div>
    </div>
    <div class="plus">Plus a catalog of useful links</div>
  </section>
  <section class="live-data">
    <h3>Live data</h3>
    <p>Looked up with tools</p>
    <div class="grid8">
      <div><b>371</b><span>courses</span></div>
      <div><b>44</b><span>study programs</span></div>
      <div><b>137</b><span>staff and collaborators</span></div>
      <div><b>86</b><span>rooms</span></div>
      <div><b>4,268</b><span>bachelor's theses</span></div>
      <div><b>71</b><span>master's theses</span></div>
      <div><b>26</b><span>timetables</span></div>
      <div><b>43</b><span>exam sessions</span></div>
    </div>
    <div class="plus">Plus faculty leadership and announcements</div>
  </section>
</div>

<p class="public">Everything is public. The 1,693 test emails never enter the knowledge base.</p>

<style>
.draw { display: grid; grid-template-columns: .82fr 1.4fr; gap: 1rem; min-height: 18.5rem; margin-top: .3rem; }
.draw section { display: flex; flex-direction: column; padding: 1rem 1.2rem; background: var(--panel); border: 1px solid var(--edge); border-radius: 11px; }
.draw section.live-data { border-color: var(--green); }
.draw h3 { margin: 0 !important; font-family: var(--display); font-weight: 500; font-size: 1.08rem !important; line-height: 1.25; color: var(--lime) !important; }
.draw section > p { margin: .12rem 0 0 !important; font-size: .78rem; color: var(--ink-3); }
.draw b { display: block; font-family: var(--display); font-weight: 500; line-height: 1.1; color: var(--ink); font-variant-numeric: tabular-nums; }
.draw span { display: block; margin-top: .2rem; font-size: .78rem; line-height: 1.25; color: var(--ink-2); }
.big { flex: 1; display: flex; flex-direction: column; justify-content: space-between; gap: .6rem; margin-top: .85rem; }
.big b { font-size: 1.42rem; }
.grid8 { flex: 1; display: grid; grid-template-columns: repeat(4, 1fr); gap: 1.15rem .9rem; align-content: center; margin-top: .95rem; }
.grid8 b { font-size: 1.32rem; }
.plus { margin-top: .9rem; padding-top: .6rem; border-top: 1px solid var(--edge); font-size: .8rem; color: var(--ink-2); }
.slidev-layout p.public { margin: .95rem 0 0; font-size: .86rem; color: var(--ink-2); }
</style>

<!--
[0:45] This is everything it can use. On one side, written knowledge found through RAG: 104 frequently asked questions that I write and maintain, and 65 official documents and web pages, split into about 2,500 sections, plus a catalog of useful links, so each search can also return the most relevant pages. On the other, live data it looks up with tools: courses, study programs, staff, rooms, more than 4,300 theses, timetables and exam sessions. All of it is public, and the 1,693 emails I test on never enter the knowledge base.
-->

---
section: Testing
---

# Two tests, two different questions

<div class="cmp">
  <div></div>
  <div class="head">Controlled test</div>
  <div class="head on">Real-world test</div>

  <div class="k">The question</div>
  <div class="q">Do different search settings give better answers?</div>
  <div class="q on">How good is the real chatbot on questions it has never seen?</div>

  <div class="k">What ran</div>
  <div>A simplified bot: one search, one answer</div>
  <div class="on">The full chatbot with all its tools</div>

  <div class="k">Tested on</div>
  <div><b>192</b> real student questions</div>
  <div class="on"><b>844</b> student emails, in three batches</div>

  <div class="k">What changed</div>
  <div><b>4</b> combinations of two settings:
    <ul class="chg"><li>Minimum document score: 0.10 or 0</li><li>Keep the best result if none pass: on or off</li></ul>
  </div>
  <div class="on"><b>5</b> rounds of fixes, on a separate set of emails:
    <ul class="chg"><li>Lower score cutoff, then agent search</li><li>New tools, link fixes and more FAQs</li></ul>
  </div>
</div>

<p class="graded"><b>Who graded the answers?</b> AI models, checked against my own grades on 100 answers and 317 search results.</p>

<style>
.cmp { display: grid; grid-template-columns: 6.6rem 1fr 1fr; column-gap: 1.6rem; font-size: .92rem; line-height: 1.4; color: var(--ink-2); }
.cmp > div { padding: .62rem 0; border-top: 1px solid var(--edge); }
.cmp > div:nth-child(-n+3) { border-top: 0; padding-top: 0; }
.cmp .head { font-family: var(--display); font-weight: 500; font-size: 1.08rem; color: var(--ink); }
.cmp .head.on { color: var(--lime); }
.cmp .k { font-size: .8rem; color: var(--ink-3); }
.cmp .q { font-size: 1rem; font-weight: 600; color: var(--ink); }
.cmp b { font-family: var(--display); font-weight: 500; color: var(--ink); }
.cmp .on b { color: var(--lime) !important; }
.slidev-layout .cmp ul.chg { margin: .28rem 0 0; padding-left: 1rem; }
.slidev-layout .cmp ul.chg li { margin: .08rem 0; font-size: .84rem; line-height: 1.35; }
.slidev-layout p.graded { margin: 1.15rem 0 0; padding: .65rem 1rem; font-size: .86rem; line-height: 1.45; background: var(--panel); border-left: 3px solid var(--lime); border-radius: 0 8px 8px 0; }
.graded b { color: var(--ink); }
</style>

<!--
[1:30] I ran two tests, because they answer two different questions. The controlled test asks: do different search settings give better answers? So a simplified bot does one search and one answer, on 192 real student questions, and I change two settings: the minimum score a document needs to reach the model, 0.10 or zero, and a fallback that keeps the best result when nothing passes. That gives four combinations, with the plan fixed in advance. The real-world test asks: how good is the actual chatbot on questions it has never seen? That's the full system with all its tools, on 844 student emails in three batches. I improved it in five rounds of fixes, over eleven test runs on a separate set of emails: a lower score cutoff, agent search, new tools, link fixes and more FAQs. AI models graded the answers, so I checked them by grading 100 answers and 317 search results myself, without seeing their grades.
-->

---
section: How it works
---

# Live demo

<div class="live">
  <div class="window">
    <div class="bar"><i></i><i></i><i></i><span>chat.finki-hub.com</span></div>
    <img src="/chat-answer.png" alt="The FINKI Hub chat answering a question about exam sessions, with the regulation it used as a source" />
  </div>
  <div class="try">
    <img src="/qr-chat.svg" alt="QR code for chat.finki-hub.com" />
    <b>Try it yourself</b>
    <span>Scan to open the chatbot on your phone</span>
  </div>
</div>

<style>
.live { display: grid; grid-template-columns: 1.65fr 1fr; gap: 1.6rem; align-items: stretch; }
.window { display: flex; flex-direction: column; overflow: hidden; background: #111; border: 1px solid var(--edge-2); border-radius: 12px; }
.bar { position: relative; display: flex; align-items: center; gap: .32rem; height: 1.9rem; padding: 0 .8rem; background: var(--panel); border-bottom: 1px solid var(--edge); }
.bar i { width: .5rem; height: .5rem; border-radius: 50%; background: var(--edge-2); }
.bar span { position: absolute; left: 50%; transform: translateX(-50%); font-size: .74rem; font-weight: 500; color: var(--lime); }
.window img { display: block; width: 100%; }
.try { display: flex; flex-direction: column; align-items: center; justify-content: center; padding: 1rem; text-align: center; background: #0f2b1f; border: 1px solid var(--green); border-radius: 12px; }
.try img { width: 11.5rem; height: 11.5rem; padding: .4rem; background: #ece7da; border-radius: 8px; }
.try b { margin-top: 1rem; font-family: var(--display); font-weight: 500; font-size: 1.12rem; line-height: 1.25; color: var(--lime) !important; }
.try span { margin-top: .3rem; font-size: .84rem; line-height: 1.35; color: var(--ink-2); }
</style>

<!--
[3:00] Before the results, let me show you the real system. The QR code opens the chatbot if you want to try it yourself. (LIVE DEMO) First a rules question in Cyrillic: watch it search, then answer with sources. The same question in Latin script. A course question, which it looks up with a tool. And "What is my GPA?", which it correctly sends to Student Services. If the network fails, switch to the recorded video.
-->

---
section: Results
---

# Letting in more documents did not help

<p class="setup">The same 192 questions, answered twice. Only one thing changed: the minimum search score a document needs to reach the model, from <b>0.10</b> to <b>0</b>. FAQs kept their 0.10 minimum.</p>

<div class="duo">
<section>
  <div class="big">3 to 6 times</div>
  <div class="sub">more source text reached the model</div>
  <div class="label">Average length of that text, in characters</div>
  <HBar label="Emails, cutoff 0.10" :value="5110" :max="17000" label-width="8.4rem" color="#2e4a3c" />
  <HBar label="Emails, cutoff 0" :value="16481" :max="17000" label-width="8.4rem" />
  <HBar label="Chat, cutoff 0.10" :value="1010" :max="17000" label-width="8.4rem" color="#2e4a3c" />
  <HBar label="Chat, cutoff 0" :value="5808" :max="17000" label-width="8.4rem" />
</section>
<section v-click class="result">
  <div class="big">1 question fewer</div>
  <div class="sub">in each set, too small to count as a real change</div>
  <div class="label">Good answers out of 96, main AI grader</div>
  <HBar label="Emails, cutoff 0.10" :value="31" :max="96" label-width="8.4rem" color="#2e4a3c" />
  <HBar label="Emails, cutoff 0" :value="30" :max="96" label-width="8.4rem" />
  <HBar label="Chat, cutoff 0.10" :value="53" :max="96" label-width="8.4rem" color="#2e4a3c" />
  <HBar label="Chat, cutoff 0" :value="52" :max="96" label-width="8.4rem" />
</section>
</div>

<style>
.slidev-layout p.setup { margin: -.7rem 0 1.25rem; font-size: .92rem; line-height: 1.45; opacity: 1; color: var(--ink-2); }
.duo { display: grid; grid-template-columns: 1fr 1fr; gap: 1.1rem; }
.duo section { padding: 1.15rem 1.25rem 1.05rem; background: var(--panel); border: 1px solid var(--edge); border-radius: 12px; }
.duo section.result { border-color: var(--green); }
.big { font-family: var(--display); font-weight: 500; font-size: 1.42rem; line-height: 1.2; color: var(--ink); }
.result .big { color: var(--lime); }
.sub { margin-top: .22rem; font-size: .86rem; line-height: 1.35; color: var(--ink-2); }
.duo .label { margin: 1rem 0 .3rem; }
.duo :deep(.hbar) { margin: .34rem 0; }
</style>

<div class="check ai"><i></i><span><b>Graded by GPT-5.6 Luna, the main AI grader.</b> A person checked a sample, but not this change.</span></div>

<!--
[1:10] Here's the test. The same 192 questions, answered twice. The only change was the minimum search score a document needs to reach the model: first 0.10, then 0, so even weak document matches get through. FAQs kept their 0.10 minimum. As a result, the model received 3 to 6 times more source text. You'd expect better answers. (click) They didn't improve. Good answers went from 31 to 30 out of 96 emails, and from 53 to 52 out of 96 chat questions. That's one question fewer in each set, about one percentage point, which is within random noise. That is the main AI grader, and I will come back to the other two in a moment. This is the simplified test bot, not the live chatbot.
-->

---
section: Results
---

# Why: the same mistakes remained

<div class="label why-label">How the 96 answers in each set were graded. The two green parts are the good answers.</div>

<div class="why">
<StackBar label="Emails, cutoff 0.10" :total="96" :parts="[{n:9,color:'#1ba96e'},{n:22,color:'#8be07a'},{n:20,color:'#f07a62'},{n:31,color:'#e8b64c'},{n:14,color:'#1e3a2c',light:true}]" />
<StackBar label="Emails, cutoff 0" :total="96" :parts="[{n:10,color:'#1ba96e'},{n:20,color:'#8be07a'},{n:19,color:'#f07a62'},{n:30,color:'#e8b64c'},{n:17,color:'#1e3a2c',light:true}]" />
<StackBar label="Chat, cutoff 0.10" :total="96" :parts="[{n:25,color:'#1ba96e'},{n:28,color:'#8be07a'},{n:12,color:'#f07a62'},{n:22,color:'#e8b64c'},{n:4,color:'#a595e6'},{n:5,color:'#1e3a2c',light:true}]" />
<StackBar label="Chat, cutoff 0" :total="96" :parts="[{n:25,color:'#1ba96e'},{n:27,color:'#8be07a'},{n:11,color:'#f07a62'},{n:24,color:'#e8b64c'},{n:4,color:'#a595e6'},{n:5,color:'#1e3a2c',light:true}]" />
<div class="flex gap-4 tiny mt-4 ml-[9.7rem] text-[#c3c4b8] nowrap">
  <span><span class="swatch bg-[#1ba96e]" />answered from sources</span>
  <span><span class="swatch bg-[#8be07a]" />sent to the right office</span>
  <span><span class="swatch bg-[#f07a62]" />not in the sources</span>
  <span><span class="swatch bg-[#e8b64c]" />left something out</span>
  <span><span class="swatch bg-[#a595e6]" />refused needlessly</span>
  <span><span class="swatch bg-[#1e3a2c]" />could not grade</span>
</div>
</div>

<p class="why-note">More of the facts a correct answer needs did reach the model: <b>49%</b> before, <b>66%</b> after (66 emails). But the answers still left things out or claimed things the sources did not say.</p>

<style>
.why-label { margin: -.2rem 0 .8rem; font-size: .84rem; }
.why :deep(.sb) { margin: .5rem 0; }
.why :deep(.track) { height: 1.9rem; }
.why :deep(.lbl) { font-size: .86rem; }
.why :deep(.seg) { font-size: .82rem; }
.why .tiny { margin-left: 0 !important; justify-content: space-between; gap: .5rem !important; font-size: .76rem; }
.slidev-layout p.why-note { margin: 1.5rem 0 0; font-size: .96rem; line-height: 1.5; color: var(--ink-2); }
</style>

<div class="check ai"><i></i><span><b>AI-graded.</b> A person checked a sample, but not the before and after change.</span></div>

<!--
[0:50] Why didn't it help? Each bar is 96 answers. The two green parts are the good answers, and the red and yellow parts, unsupported claims and incomplete answers, barely moved. For each email, a reference lists the facts a correct answer needs, with a quote from the source. On the 66 emails with usable references, the share of those quotes that reached the model rose from 48.6 to 66.1%. So the model had more of the right facts, but it still left things out or claimed things the sources did not say. The problem was how it used the evidence.
-->

---
section: Results
---

# Can we rely on AI to grade the answers?

<p class="setup">I graded 100 random answers myself, without seeing the AI grades. These are the 50 from the controlled test. The other 50 are from the live system (slide 16).</p>

<div class="duo2">
<section>
  <div class="big">AI graders were harsher</div>
  <div class="label">Answers rated good, out of 36 real questions</div>
  <HBar label="Me (human)" :value="30" :max="36" label-width="8.2rem" color="#8be07a" />
  <HBar label="Claude Sonnet 5.5" :value="23" :max="36" label-width="8.2rem" color="#5e7569" />
  <HBar label="GPT-5.6 Luna" :value="20" :max="36" label-width="8.2rem" color="#5e7569" />
  <HBar label="GPT-6 Luna" :value="12" :max="36" label-width="8.2rem" color="#5e7569" />
</section>
<section v-click>
  <div class="big">And they disagree</div>
  <div class="stat"><b>53–58%</b><span>of the time, two different AI graders give the same grade</span></div>
  <div class="stat"><b>74.5%</b><span>of the time, one AI grader asked twice gives the same grade</span></div>
</section>
</div>

<style>
.slidev-layout p.setup { margin: -.7rem 0 1.25rem; font-size: .92rem; line-height: 1.45; opacity: 1; color: var(--ink-2); }
.duo2 { display: grid; grid-template-columns: 1fr 1fr; gap: 1.1rem; }
.duo2 section { padding: 1.15rem 1.25rem 1.1rem; background: var(--panel); border: 1px solid var(--edge); border-radius: 12px; }
.duo2 .big { font-family: var(--display); font-weight: 500; font-size: 1.22rem; line-height: 1.25; color: var(--lime); }
.duo2 .label { margin: .9rem 0 .4rem; }
.duo2 :deep(.hbar) { margin: .46rem 0; font-size: .86rem; }
.stat { margin-top: 1rem; }
.stat b { display: block; font-family: var(--display); font-weight: 500; font-size: 1.6rem; line-height: 1.15; color: var(--ink); }
.stat span { display: block; margin-top: .25rem; font-size: .84rem; line-height: 1.35; color: var(--ink-2); }
</style>

<div class="check human"><i></i><span><b>Human check:</b> 50 of my 100 graded answers: 37 real questions, 36 also graded by every AI</span></div>

<!--
[1:05] All of this was graded by AI, so can we rely on it? To check, I graded 100 random answers myself, without seeing the AI grades: 50 from this controlled test and 50 from the live system, which come up in a moment. Of the 50 here, 13 weren't real questions, which left 37. The AI graders were harsher than me: on the 36 answers the AI graders could also grade, I rated 30 as good, and they rated between 12 and 23. Across all 37, I rated 31 as good. So the controlled numbers are probably too low. (click) They also disagree with each other. Two different graders give the exact same grade on only 53 to 58% of answers, while the same grader asked twice does so 74.5% of the time. If you only ask whether an answer is good or not, two graders agree 67 to 74% of the time, a kappa of 0.38 to 0.48.
-->

---
section: Results
---

# The grader can change the conclusion

<p class="setup2">Did more text change the share of good answers? The same comparison, graded by each AI.</p>

<div class="matrix">
  <div></div>
  <div class="colh">GPT-5.6 Luna (main)</div>
  <div class="colh">Claude Sonnet 5.5</div>
  <div class="colh">GPT-6 Luna</div>
  <div class="rowh">Emails</div>
  <div class="cell"><b>−1.0</b><span>−8.3 to +6.3</span></div>
  <div class="cell"><b>+1.0</b><span>−7.3 to +9.4</span></div>
  <div class="cell"><b>−2.1</b><span>−9.4 to +5.2</span></div>
  <div class="rowh">Chat</div>
  <div class="cell"><b>−1.0</b><span>−7.3 to +5.2</span></div>
  <div class="cell hot"><b>+7.3</b><span>+1.0 to +13.5</span></div>
  <div class="cell"><b>−1.0</b><span>−5.2 to +3.1</span></div>
</div>

<p class="key">Large numbers: change in good answers, in percentage points. Small numbers: the likely range. If it includes 0, there is no clear change.</p>

<p class="read">Five of six results show <b>no clear change</b>. Only Claude Sonnet found a gain on chat questions: <b>61</b> good answers out of 96, up from <b>54</b>.</p>

<style>
.slidev-layout p.setup2 { margin: -.7rem 0 1.3rem; font-size: .92rem; line-height: 1.45; opacity: 1; color: var(--ink-2); }
.matrix { display: grid; grid-template-columns: 5rem repeat(3, 1fr); gap: .5rem; }
.colh { padding-bottom: .15rem; text-align: center; font-size: .84rem; font-weight: 600; color: var(--ink-2); }
.rowh { display: flex; align-items: center; font-size: .96rem; font-weight: 600; color: var(--ink); }
.cell { display: flex; flex-direction: column; align-items: center; padding: .72rem .5rem .66rem; background: var(--panel); border: 1px solid var(--edge); border-radius: 9px; }
.cell b { font-family: var(--display); font-weight: 500; font-size: 1.4rem; line-height: 1.15; color: var(--ink); }
.cell span { margin-top: .22rem; font-size: .78rem; color: var(--ink-3); font-variant-numeric: tabular-nums; }
.cell.hot { background: #0f2b1f; border-color: var(--lime); }
.cell.hot b { color: var(--lime) !important; }
.cell.hot span { color: var(--ink-2); }
.slidev-layout p.key { margin: .7rem 0 0; font-size: .76rem; color: var(--ink-3); }
.slidev-layout p.read { margin: 1rem 0 0; font-size: 1.04rem; line-height: 1.4; color: var(--ink-2); }
</style>

<div class="check ai"><i></i><span><b>AI-graded.</b> A person checked a sample, but not this comparison.</span></div>

<!--
[0:40] This matters because it can change the conclusion. I repeated the "more text" comparison under all three graders. Five of the six results show no clear change, but one does. With more text, Claude Sonnet rated 61 of the 96 chat answers as good instead of 54, a gain of 7.3 percentage points, and its whole likely range is above zero. The other two graders saw no gain on those same answers. So AI grading is useful, but it has to be checked against people.
-->

---
section: Results
---

# Three in four answers were correct

<div class="grid grid-cols-[0.9fr_1.1fr] gap-12 mt-2 items-center">
<div>
  <div class="hero-num">76%</div>
  <p class="small !mt-2">correct on the last batch of emails, which I never used to improve the system. The AI grader marked only <b>1–3%</b> wrong. The rest were partly right or needed a fact no source has.</p>
</div>
<div>
<div class="label">Correct answers on each new batch, out of those that could be graded</div>
<HBar label="Batch 1" sub="271 emails, 234 graded" :value="70.5" suffix="%" label-width="10.2rem" />
<HBar label="Batch 2" sub="275 emails, 247 graded" :value="77.3" suffix="%" label-width="10.2rem" />
<HBar label="Batch 3" sub="298 emails, 271 graded" :value="76.0" suffix="%" label-width="10.2rem" color="#8be07a" />
<div class="stack mt-5">
  <div class="on"><h3>My own grades were close</h3><p>I graded 50 of these myself. On the 46 we could both grade, we agreed 85% of the time on whether an answer was correct. I rated 74% correct and 4 answers wrong. The AI rated 80% correct and 2 wrong.</p></div>
</div>
</div>
</div>

<style>
.hero-num { font-family: 'Unbounded', sans-serif; font-size: 6rem; font-weight: 500; line-height: .95; letter-spacing: -.04em; color: #8be07a; }
</style>

<div class="check human"><i></i><span><b>Human check:</b> 50 of my 100 graded answers, 85% agreement on the 46 both could grade</span></div>

<!--
[2:00] Now the live system, which is the main result. On the final batch of emails, which no fix ever touched, 76% of answers were correct, and the AI grader marked only 1 to 3% wrong; the rest were partly right or needed a fact no source has. The three batches have 271, 275 and 298 emails, 844 in total. Emails that could not be graded, like thank-you messages, are not counted, which leaves 234, 247 and 271. The three batches agree. And when I graded 50 of these myself, I agreed with the AI grader on whether an answer was correct for 85% of the 46 we could both grade. I was a little stricter: I rated 74% correct and 4 answers wrong, and the AI rated 80% correct and 2 wrong.
-->

---
section: Results
layout: wide
---

# Five rounds of improvement

<p class="setup">I tested the chatbot on the same 334 emails, read the failures, fixed the cause and tested again.</p>

<StageChart />

<p class="caption !mt-3">Dips partly reflect separate grading batches, so rounds 3 and 5 use side-by-side grades. 88% is optimistic: new emails got 76%.</p>

<style>
.slidev-layout p.setup { margin: -.8rem 0 .75rem; font-size: .9rem; line-height: 1.4; opacity: 1; color: var(--ink-2); }
</style>

<div class="check ai"><i></i><span><b>AI-graded only.</b> No human check on this chart.</span></div>

<!--
[1:00] This is how it got there, in five rounds of improvement over eleven test runs on the same 334 emails. Each time I read the failures, fixed the cause and tested again. First, better knowledge: I reviewed all the FAQs. Second, better search: I fixed two faults in how results were filtered and ranked. Third, the chatbot started searching by itself. Fourth, smaller fixes to the live version. Fifth, fixing links and adding FAQs. Correct answers went from 59 to 88%, and wrong ones from 19 to about 1%. The small bump in wrong answers near the end was partly a grading mistake, and the small dips in correct answers partly come from grading runs in separate batches. So for rounds three and five I show runs graded side by side: 76 to 84%, and 84 to 88%. Because I used these emails for fixing, and the grading rules changed along the way, read this as direction. With the same grader, these emails scored 87.8% and new emails 76.3%.
-->

---
section: Results
layout: wide
---

# What made it better, and what did not

<div class="fix">
<section class="yes">
  <h3>Helped</h3>
  <div class="item"><div><b>Letting the chatbot search by itself</b><span>Wrong answers, side-by-side test</span></div><em>8.9% → 1.4%</em></div>
  <div class="item"><div><b>Lower cutoff, ranking on the student's words</b><span>Difficult emails correct, of 49</span></div><em>7 → 20</em></div>
  <div class="item"><div><b>A tool for looking up courses</b><span>Correct, on 24 course questions</span></div><em>21% → 100%</em></div>
  <div class="item"><div><b>Prompt rules for searching and explaining</b><span>Correct, on 96 difficult questions</span></div><em>73% → 84%</em></div>
  <div class="item"><div><b>Having the tool return short links</b><span>Broken links, of about 80</span></div><em>8 → 0</em></div>
</section>
<section class="no">
  <h3>Did not help</h3>
  <div class="item"><div><b>Telling it to copy links exactly</b><span>Broken links, of about 80</span></div><em>8 → 7</em></div>
  <div class="item"><div><b>Telling it to stop being vague</b><span>Mixed results, and it added details not in the sources</span></div></div>
  <div class="item"><div><b>Adding related FAQs</b><span>Distracted it as often as it helped</span></div></div>
</section>
</div>

<p class="lesson">Changes to <b>data</b>, <b>search</b> and <b>tools</b> gave clear gains. <b>Prompt rules</b> helped in some cases and failed in others.</p>

<style>
.fix { display: grid; grid-template-columns: 1.08fr 1fr; gap: 1.1rem; }
.fix section { padding: .95rem 1.15rem .8rem; background: var(--panel); border: 1px solid var(--edge); border-radius: 12px; }
.fix section.yes { border-color: var(--green); }
.slidev-layout .fix h3 { margin: 0 0 .35rem; font-family: var(--display); font-weight: 500; font-size: 1.08rem; color: var(--ink); }
.slidev-layout .fix .yes h3 { color: var(--lime); }
.item { display: flex; align-items: center; justify-content: space-between; gap: .8rem; padding: .48rem 0; border-top: 1px solid var(--edge); }
.item b { display: block; font-size: .86rem; font-weight: 600; line-height: 1.25; color: var(--ink); }
.item span { display: block; margin-top: .08rem; font-size: .74rem; line-height: 1.3; color: var(--ink-3); }
.item em { flex: none; font-family: var(--display); font-style: normal; font-weight: 500; font-size: .86rem; color: var(--ink); white-space: nowrap; }
.yes .item em { color: var(--lime); }
.slidev-layout p.lesson { margin: 1rem 0 0; font-size: 1rem; line-height: 1.4; color: var(--ink-2); }
</style>

<div class="check ai"><i></i><span><b>AI-graded.</b> Each change was tested on its own set of questions.</span></div>

<!--
[1:00] So what actually made the difference? Letting the chatbot search by itself cut wrong answers from 8.9 to 1.4% in a side-by-side test. Lowering the cutoff and ranking on the student's own words took difficult emails from 7 to 20 correct out of 49. A tool for looking up courses took course questions from 21 to 100%. Having the tool return short links took broken links from 8 to 0. Prompt rules were mixed. Rules for how to search and explain took 96 difficult questions from 73 to 84% correct, but difficult sets inflate gains. Telling it to copy links exactly only got from 8 to 7, telling it to stop being vague gave mixed results and added details not in the sources, and adding related FAQs distracted it as often as it helped.
-->

---
section: Results
---

# Finding sources is not the main problem

<div class="grid grid-cols-[1.1fr_0.9fr] gap-10 mt-2 one">
<div>
<div class="label">Last batch: the 275 emails that have a useful source</div>
<HBar label="Useful source found" :value="94.5" suffix="%" label-width="9.5rem" />
<HBar label="Answer correct" :value="72.4" suffix="%" label-width="9.5rem" color="#e8b64c" />
<p class="caption">72.4% counts all 275 emails, including ones that could not be graded, so it is lower than the 76% on slide 16.</p>
<p class="small mt-4">The chatbot searches about 1.7 times per question and finds a useful source for almost every email. Some answers still fall short, for two reasons:</p>
</div>
<div class="stack">
  <div class="on"><h3>The fact is not written anywhere</h3><p>13% of emails ask for something no document says. About a third are in just a few topics, like master's procedures and admissions, where new FAQs would help most.</p></div>
  <div><h3>The answer is written poorly</h3><p>It found the right FAQ, but was too vague or added a detail from a loosely related text.</p></div>
</div>
</div>

<div class="check human"><i></i><span><b>AI-judged. Human check:</b> 317 search results from 20 emails</span></div>

<!--
[1:30] So is finding sources the main problem? No. For 94.5% of emails, a relevant source reached the model. Yet only about 72% of those answers are correct. The gap comes from two places: facts that no document states, about 13% of emails, a third of them in a few topics; and how the answer is written, where the model found the right FAQ but was too vague or added a detail. Search is not perfect: about 9 of the 22 partly correct answers trace back to a source that did not reach the model.
-->

---
section: Results
layout: wide
---

# Comparing search methods

<table class="t">
<thead><tr><th>Method</th><th class="num">Top 1</th><th class="num">Top 3</th><th class="num">Top 5</th><th class="num">Top 10</th><th class="num">Recall, top 10</th><th class="num">Rank score</th></tr></thead>
<tbody>
<tr><td>Keywords (BM25)</td><td class="num">32.0</td><td class="num">52.4</td><td class="num">62.2</td><td class="num">73.5</td><td class="num">50.7</td><td class="num">45.3</td></tr>
<tr><td>Meaning (BGE-M3)</td><td class="num">51.3</td><td class="num">70.2</td><td class="num">77.5</td><td class="num">86.2</td><td class="num">68.6</td><td class="num">62.4</td></tr>
<tr><td>Keywords + meaning</td><td class="num">44.7</td><td class="num">67.6</td><td class="num">78.2</td><td class="num">86.9</td><td class="num">70.5</td><td class="num">58.8</td></tr>
<tr><td>Guess an answer first (HyDE)</td><td class="num">57.5</td><td class="num">76.0</td><td class="num">82.9</td><td class="num">88.4</td><td class="num">72.1</td><td class="num">68.5</td></tr>
<tr><td>Rewrite the question</td><td class="num">50.5</td><td class="num">70.9</td><td class="num">79.3</td><td class="num">88.0</td><td class="num">70.1</td><td class="num">63.3</td></tr>
<tr class="hl"><td>Meaning + reranker (closest to the chatbot)</td><td class="num">52.4</td><td class="num">73.8</td><td class="num">81.1</td><td class="num">86.5</td><td class="num">72.3</td><td class="num">64.5</td></tr>
<tr><td>Keywords + meaning + reranker</td><td class="num">54.5</td><td class="num">76.0</td><td class="num">85.1</td><td class="num">90.2</td><td class="num">75.5</td><td class="num">67.0</td></tr>
<tr><td>Guess an answer + reranker</td><td class="num">56.7</td><td class="num">79.6</td><td class="num">85.8</td><td class="num">91.3</td><td class="num">76.8</td><td class="num">69.0</td></tr>
<tr><td>Rewrite + reranker</td><td class="num">57.1</td><td class="num">78.9</td><td class="num">85.5</td><td class="num">90.9</td><td class="num">74.7</td><td class="num">68.6</td></tr>
</tbody>
</table>

<p class="caption">Top N: how often one search put a useful source in its first N results, out of 275 emails. Highlighted: the closest to the real chatbot, which searches 1.7 times on average to reach 94.5%. Recall reads about 10 points too high. Rank score (MRR×100): higher means the first useful result appears earlier.</p>

<div class="check human"><i></i><span><b>AI-judged. Human check:</b> 317 search results from 20 emails</span></div>

<!--
[0:45] I also compared nine ways of searching on the final batch. Top 10 means a relevant source was among the first ten results. The highlighted row is the closest to what the chatbot uses, at 86.5%. The best method, guessing an answer first and then reranking, reached 91.3%, but the top methods are close together. These are single searches: the agent searches 1.7 times on average, which is how it reaches the 94.5% from the previous slide.
-->

---
section: Results
layout: wide
---

# Tuning search: what helped and what did not

<div class="grid grid-cols-2 gap-10">
<div>
<div class="label">Helped: lowering the cutoff for FAQs too. How often the right FAQ reached the top 10, on the 49 difficult emails from slide 18</div>
<HBar label="Cutoff 0.10" :value="28.6" suffix="%" label-width="6rem" color="#2e4a3c" />
<HBar label="Cutoff 0.03" :value="42.9" suffix="%" label-width="6rem" color="#8be07a" />
<HBar label="Cutoff 0.01" :value="44.9" suffix="%" label-width="6rem" />
<p class="small !mt-4">Long emails get low scores even when the results are right: 29 of 30 correct FAQs scored below 0.10. A cutoff of 0.03 lets more through. Unlike slide 12, it also applies to FAQs.</p>
<p class="caption !mb-0">Students see only sources scoring above 0.30. Half of those are useful.</p>
</div>
<div class="stack">
  <div><h3>Did not help: a knowledge graph</h3><p>LightRAG found useful sources about as often as plain search, but took 1,859 model calls to build and added about 2 seconds per question.</p></div>
  <div><h3>Did not help: a stronger AI reranker</h3><p>Its ranking looked better when AI judged it, but not when I did, and answers did not improve: 69% correct against 74% on 100 emails, within noise.</p></div>
  <div class="on"><h3>Worked well: follow-up questions</h3><p><b>41 of 42</b> answered correctly when the question depended on earlier messages.</p></div>
</div>
</div>

<div class="check human"><i></i><span><b>AI-graded. Human check of the reranker:</b> on 20 emails, a tie at 19 each</span></div>

<!--
[1:15] Lowering the cutoff to 0.03 helped here, unlike on slide 12, because this time it also applied to FAQs, and long emails score low even when the ranking is right. Fancier methods did not: a knowledge graph cost far more for the same results, and a stronger reranker did not improve the answers. The agent did handle follow-up questions well: 41 of 42. One detail on sources: showing only those above 0.30 hides 85% of the useless ones, but also over half of the useful ones.
-->

---
section: Findings
layout: wide
---

# Answers to the seven questions

<table class="t big">
<tbody>
<tr class="hl"><td class="w-[21.4rem]"><b class="muted">1.</b> Can this actually work in practice?</td><td>Yes. About 76% correct on new emails, and few wrong.</td></tr>
<tr><td><b class="muted">2.</b> What is missing to make it reliable?</td><td>Mostly knowledge. 13% of emails need a fact no document has.</td></tr>
<tr><td><b class="muted">3.</b> Can AI do this on its own?</td><td>For most questions, but answers can be vague or add a wrong detail.</td></tr>
<tr><td><b class="muted">4.</b> Does giving it more information help?</td><td>Not by itself. Five of six comparisons showed no clear change.</td></tr>
<tr><td><b class="muted">5.</b> What actually made it better?</td><td>Better data, search and tools, and some prompt rules.</td></tr>
<tr><td><b class="muted">6.</b> Can we rely on AI to grade the answers?</td><td>Only with care. Graders disagree with each other and with me.</td></tr>
<tr><td><b class="muted">7.</b> Could another institution reuse this?</td><td>Designed to, but not yet tried elsewhere.</td></tr>
</tbody>
</table>

<style>
table.t.big { font-size: .95rem; }
table.t.big td { padding: .68rem .6rem; line-height: 1.3; }
</style>

<!--
[1:45] Back to the seven questions. One: yes, it works in practice. On real emails it had never seen, about three in four answers were correct, and the AI grader marked 1 to 3% wrong. In the sample I graded, I found a few more wrong answers: 4 of 46, against 2 for the AI. Two: what's missing is mostly knowledge, facts no document states. Three: AI handles most questions, and it finds a useful source for 94.5% of the emails that have one, but it can still be too vague or add a wrong detail. Four: more information alone doesn't help. In the controlled test, about a third of email answers and half of chat answers were good by the AI grader, likely more by a person, and three to six times more text made no difference under the main grader. One of the two other graders did see a gain on chatbot questions. Five: what made it better was better data, search and tools, like letting the agent search. Some prompt rules helped too, and others did not. Six: AI grading needs checking against people. The graders were far stricter than me in the controlled test and slightly more lenient on the live system. And seven: the design is meant to be reused by other institutions, but that hasn't been tried yet.
-->

---
section: Findings
layout: wide
---

# What this means for anyone building one

<div class="grid grid-cols-3 gap-4 mt-1">
  <div class="card !p-5"><div class="fig muted">1</div><h3 class="mt-3">Write down the knowledge</h3><p class="small">Having the facts written down matters more than fine-tuning search.</p></div>
  <div class="card !p-5"><div class="fig muted">2</div><h3 class="mt-3">Check the AI grader against people</h3><p class="small">A different AI grader can give different numbers and even a different conclusion.</p></div>
  <div class="card !p-5"><div class="fig muted">3</div><h3 class="mt-3">Fix the data before the prompts</h3><p class="small">If the data is wrong, telling the model to be careful will not fix it.</p></div>
</div>

<div class="grid grid-cols-2 gap-10 mt-6 small">
<div>
<h3 class="red">Limits</h3>

- Mostly graded by AI. I checked 100 answers myself, and I built the system
- The live system changed between test runs
- Not yet tried at a second institution

</div>
<div>
<h3 class="green">Next</h3>

- Grading by faculty staff, the most important step
- New FAQs for the topics where knowledge is missing
- Trying the same approach at a second institution

</div>
</div>

<!--
[1:30] Three lessons for anyone building one. Write down the knowledge: confirmed facts matter more than tuning search. Check your AI grader against people. And fix the data before the prompts. The limits: grading is mostly AI with one human checker, the live system changed between runs, and it's not yet tried elsewhere. Next is grading by faculty staff, filling the knowledge gaps, and trying the same approach at a second institution. Thank you.
-->

---
layout: closing
---

<h1 class="!text-[2.6rem] !mb-3">Thank you</h1>
<p class="text-lg !mt-0">Questions are welcome.</p>

<div class="mt-14 text-sm grid grid-cols-[auto_auto_auto] gap-x-12 gap-y-1 w-fit">
  <span class="muted">Chatbot</span><span class="muted">FINKI Hub</span><span class="muted">Source code</span>
  <b>chat.finki-hub.com</b><b>finki-hub.com</b><b>github.com/finki-hub</b>
</div>

<p class="tiny muted !mt-16">Stefan Milev, mentored by Prof. Dr. Riste Stojanov, FCSE, Ss. Cyril and Methodius University in Skopje</p>
