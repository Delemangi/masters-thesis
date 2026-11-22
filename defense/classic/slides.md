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
  weights: '300,400,500,600,700'
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
Good morning. My thesis is about chatbots that answer questions from an institution's own documents, and about how we can tell whether their answers are any good. The case study is the FINKI Hub chatbot, which I built and run for FCSE students.
-->

---
section: Context
noMark: true
---

<div class="lockup"><div class="lm"><LogoMark :animate="false" /></div><b>FINKI Hub</b><span>independent student organization</span></div>

# Tools FCSE students use every day

<HubTiles />

<p class="caption !mt-4">Not affiliated with the faculty. Every project is open source at <b class="text-[#ece7da]">github.com/finki-hub</b>.</p>

<!--
Some context first. FINKI Hub is a student organization. We build tools on top of public faculty data: an announcements feed on Discord, a thesis browser, timetables, a course planner, lecture recordings and a browser terminal. The chatbot, on the left, is the subject of this thesis. It is also the newest piece, and it reuses the others: when a student asks about a thesis or a timetable, the bot looks it up in those services.
(Backup slide: the full source → service → product map.)
-->

---
section: Problem
---

# Students ask the same questions, and the answers are scattered

<div class="grid grid-cols-[1fr_1.1fr] gap-12 mt-2">
<div>
  <div class="bubble" v-click>
    "I'm transferring from another university. How many of my credits can I bring, and what do I need to submit?"
  </div>
  <p class="small mt-6" v-click>Students ask about situations: enrolling, transferring, fees, deadlines, exams. The answer is spread across regulations, faculty decisions, web pages and what staff wrote back in earlier emails.</p>
</div>
<div v-click class="stack">
  <div><h3>Three rules for the same word</h3><p>"Transfer" appears in the 2013 faculty rules, the 2019 university rules and a 2022 supplement, each with a different condition.</p></div>
  <div><h3>Answered one email at a time</h3><p>The faculty gave us 1,693 anonymized student emails with staff replies, falling into 24 recurring topics.</p></div>
  <div><h3>A confident answer can still be wrong</h3><p>A chatbot that finds a passage about "transfer" can quote the wrong rule, or skip a condition.</p></div>
</div>
</div>

<style>
.bubble { position: relative; padding: 1rem 1.2rem; font-size: 1.05rem; line-height: 1.5; color: #ece7da; background: #12281d; border: 1px solid #2a5a3f; clip-path: polygon(14px 0, 100% 0, 100% 100%, 0 100%, 0 14px); }
</style>

<!--
Here is the problem. A student does not ask "what does article 31 say". They describe their situation. The answer usually needs several sources, and they don't always agree. Today these questions go to staff by email, one at a time.
-->

---
section: Problem
---

# What I set out to do

<div class="grid grid-cols-3 gap-4 mt-2">
  <div class="card" v-click><div class="fig green">Design</div><p class="small mt-3">A blueprint for assistants that answer from an institution's documents, where every step can be checked.</p></div>
  <div class="card" v-click><div class="fig green">Build</div><p class="small mt-3">The FINKI Hub chatbot as a working example, used by real students on the web and in Discord.</p></div>
  <div class="card on" v-click><div class="fig lime">Measure</div><p class="small mt-3">Honestly test how often its answers are right, and find out what actually limits them.</p></div>
</div>

<div class="mt-8 small" v-click>
<p class="!m-0"><b>A good answer</b> either gives the correct rule with its conditions, backed by the sources, or sends the student to the right office when the documents can't settle it. Questions about a student's own records, like grades, only need the right referral: the bot never sees personal data.</p>
</div>

<!--
So the work had three parts. Design a general blueprint, build a real system with it, and measure it carefully. "Good" includes a correct referral: sometimes the honest answer is "ask Student Services".
-->

---
section: Problem
---

# Five questions the thesis answers

<div class="grid grid-cols-2 gap-8 mt-1">
<div class="stack">
  <div v-click><h3>Test 1, controlled</h3><p class="!text-[.68rem] !text-[#849086]">Same questions, one setting changed at a time</p></div>
  <div v-click><p><b class="lime">1.</b> How often does it give a good answer, and what goes wrong?</p></div>
  <div v-click><p><b class="lime">2.</b> Does giving the model more of the documents help?</p></div>
  <div v-click><p><b class="lime">3.</b> Can we trust AI to grade the answers?</p></div>
</div>
<div class="stack">
  <div v-click class="on"><h3>Test 2, the live system</h3><p class="!text-[.68rem] !text-[#849086]">The deployed chatbot on emails it had never seen</p></div>
  <div v-click><p><b class="lime">4.</b> How often is it right on real student emails, and where does it fail?</p></div>
  <div v-click><p><b class="lime">5.</b> Is finding the right documents the bottleneck?</p></div>
</div>
</div>

<!--
Formally these are RQ1 to RQ3 and LQ1 to LQ2 in the thesis. The first three come from a controlled experiment, the last two from the live system.
-->

---
section: How it works
---

# The blueprint: six steps, each one checkable

<ArchChain class="mt-2" />

<p class="small mt-8" v-click>Step 3 is where most of the design choices are, so it is the step the controlled test varies. Because each step hands a clear result to the next, a wrong answer can be traced to the step where it went wrong.</p>

<!--
The architecture is six responsibilities with explicit handoffs. Top line: what each step does. Bottom line: how the FINKI Hub chatbot does it. Finding evidence is highlighted because that's where the thresholds and rerankers live.
-->

---
section: How it works
---

# It answers from the faculty's own documents

<div class="figs mt-2">
  <div v-click><div class="fig green">104</div><div class="fig-label">FAQ answers I wrote and maintain</div></div>
  <div v-click><div class="fig">65</div><div class="fig-label">official documents and faculty web pages</div></div>
  <div v-click><div class="fig">2,524</div><div class="fig-label">searchable passages</div></div>
  <div v-click><div class="fig lime">1,693</div><div class="fig-label">real student emails, used only for testing</div></div>
</div>

<div class="grid grid-cols-2 gap-12 mt-8 small" v-click>
<div>

- Everything it knows is public
- Each document was converted to text and read against the original
- Students write in Macedonian, Cyrillic or Latin script, or English

</div>
<div>

- Search and ranking run on our own GPU server
- The test emails never enter the knowledge base
- Besides documents, it can look up courses, timetables, theses and announcements

</div>
</div>

<!--
Embeddings are BGE-M3; reranker is BGE-reranker-v2-m3. There is no published Macedonian benchmark for BGE-M3, so I measured it: dense search alone puts a relevant item in the top 10 for 86.2% of real emails.
-->

---
section: How it works
---

# The chatbot, live

<div class="grid grid-cols-[1.4fr_1fr] gap-8 items-center">
<div>
  <img src="/chat-crop.png" class="w-full border border-[#1e3a2c] rounded-lg" />
  <p class="caption">chat.finki-hub.com; the same service answers in Discord</p>
</div>
<div class="stack">
  <div><h3>Ask in Cyrillic</h3><p>A question about the rules: watch it search, then answer with sources</p></div>
  <div><h3>Ask the same in Latin script</h3><p>It understands both</p></div>
  <div><h3>Ask about a course</h3><p>It looks the course up instead of guessing</p></div>
  <div class="on"><h3>Ask "What is my GPA?"</h3><p>It sends you to Student Services</p></div>
</div>
</div>

<!--
LIVE DEMO, 2–3 minutes. If the network fails, play the recorded video.
-->

---
section: Testing
---

# Two ways to test it

<div class="grid grid-cols-2 gap-6 mt-2">
<div class="card !p-5" v-click>
  <h3 class="!text-[1.05rem]">Test 1: a controlled experiment</h3>
  <p class="small">A simplified bot does one search and writes one answer. I change one retrieval setting at a time and compare.</p>
  <div class="grid grid-cols-2 gap-3 mt-4">
    <div><div class="fig !text-[1.6rem]">192</div><div class="fig-label">questions: real emails and chatbot messages</div></div>
    <div><div class="fig !text-[1.6rem]">4</div><div class="fig-label">settings compared, plan fixed in advance</div></div>
  </div>
</div>
<div class="card on !p-5" v-click>
  <h3 class="!text-[1.05rem]">Test 2: the real system</h3>
  <p class="small">The deployed chatbot, with all its tools, answers student emails it has never seen.</p>
  <div class="grid grid-cols-2 gap-3 mt-4">
    <div><div class="fig !text-[1.6rem] lime">844</div><div class="fig-label">unseen emails in three batches</div></div>
    <div><div class="fig !text-[1.6rem]">11</div><div class="fig-label">versions of the system along the way</div></div>
  </div>
</div>
</div>

<p class="small mt-6" v-click>AI models graded the answers. To check them, <b>I graded 100 answers and 317 retrieved passages by hand</b>, without seeing the AI grades.</p>

<!--
Test 1 isolates one decision. Test 2 measures the real thing. The numbers from the two are never combined.
-->

---
section: Results
---

# Giving the model three to six times more text did not help

<div class="grid grid-cols-[1fr_1fr] gap-12 mt-2">
<div>
<div class="label">Text the model received, in characters</div>
<HBar label="Emails, before" :value="5110" :max="17000" label-width="8rem" color="#2e4a3c" />
<HBar label="Emails, after" :value="16481" :max="17000" label-width="8rem" />
<HBar label="Chat, before" :value="1010" :max="17000" label-width="8rem" color="#2e4a3c" />
<HBar label="Chat, after" :value="5808" :max="17000" label-width="8rem" />
</div>
<div v-click>
<div class="label">Change in good answers</div>
<div class="fig !text-[3rem]">−1 <span class="!text-[1.2rem] muted">point</span></div>
<p class="small mt-3">in both question sets, within noise. A fallback setting and a rewritten prompt did not help either.</p>
<p class="small">What held answers back was not missing text: it was incomplete answers and claims the sources did not support.</p>
</div>
</div>

<!--
RQ1 and RQ2. Under the baseline, the main judge rated 31 of 96 email answers and 53 of 96 chatbot answers as good. Lowering the document threshold (0.10 → 0.00) gave the model far more context; the difference was −1.04 points in both samples, 95% intervals [−8.3, 6.3] and [−7.3, 5.2]. Backup: outcome breakdown.
-->

---
section: Results
---

# The AI graders disagreed, and were much stricter than a person

<div class="grid grid-cols-[1fr_1fr] gap-12 mt-2">
<div>
<div class="label">Answers rated good, out of about 36</div>
<HBar label="Me" :value="30" :max="37" label-width="7.5rem" color="linear-gradient(90deg,#1ba96e,#8be07a)" />
<HBar label="Claude Sonnet" :value="23" :max="37" label-width="7.5rem" color="#5e7569" />
<HBar label="GPT-5.6 Luna" :value="20" :max="37" label-width="7.5rem" color="#5e7569" />
<HBar label="GPT-6 Luna" :value="12" :max="37" label-width="7.5rem" color="#5e7569" />
</div>
<div class="stack" v-click>
  <div><h3>They disagree with each other</h3><p>Two graders agree on only 67–74% of answers. One of the three even saw a gain where the others saw none.</p></div>
  <div class="on"><h3>They are harsher than someone who knows the rules</h3><p>They called answers incomplete that I would accept, so the true share of good answers is probably higher.</p></div>
</div>
</div>

<!--
RQ3. Agreement with my grades was at chance level (kappa near zero). The comparison between settings still rests on AI labels, because I graded one setting per question. Backup: judge intervals.
-->

---
section: Results
---

# On emails it had never seen, about three in four answers were correct

<div class="grid grid-cols-[0.9fr_1.1fr] gap-12 mt-2 items-center">
<div>
  <div class="hero-num">76%</div>
  <p class="small !mt-2">correct on the final batch, which no fix ever touched. Only <b>1–3%</b> were wrong; the rest were partly right or honest referrals.</p>
</div>
<div>
<div class="label">Correct, on each unseen batch</div>
<HBar label="Batch 1" :value="70.5" suffix="%" label-width="5rem" />
<HBar label="Batch 2" :value="77.3" suffix="%" label-width="5rem" />
<HBar label="Batch 3" :value="76.0" suffix="%" label-width="5rem" color="linear-gradient(90deg,#1ba96e,#8be07a)" />
<div class="stack mt-5" v-click>
  <div class="on"><h3>My grades agree</h3><p>On 50 of these answers I agreed with the AI grader 85% of the time. I rated 74% correct.</p></div>
</div>
</div>
</div>

<style>
.hero-num { font-family: 'Unbounded', sans-serif; font-size: 6rem; font-weight: 500; line-height: .95; letter-spacing: -.04em; background: linear-gradient(135deg, #8be07a, #1ba96e); -webkit-background-clip: text; background-clip: text; color: transparent; }
</style>

<!--
LQ1. Clean runs: 70.5% (batch 1), 77.0/77.3% (batch 2, two runs), 76.5/76.0% (batch 3, two runs); wrong 0.8–3.0%. Graded by Claude Sonnet under one rubric. Identical runs differ by up to about 3 points. The set used for fixes scored 87.8%, 11.5 points higher than new emails: tuning on a set flatters it.
-->

---
section: Results
---

# How it got there: eleven versions, from 59% to 88%

<StageChart />

<p class="caption">Measured on the 334 emails used for fixing, so the final number is optimistic; the grading also changed over time. Read it for direction, not exact values.</p>

<!--
Early gains came from filling knowledge gaps. S3 is the retrieval repair: lower context floor (0.10 → 0.03) and scoring passages against the student's own words. S5 moved search into the agent, which removed most wrong answers.
-->

---
section: Results
---

# What made it better, and what did not

<div class="grid grid-cols-2 gap-8 mt-2">
<div>
<div class="label">Kept</div>
<div class="stack">
  <div v-click><h3>Let the agent search for itself</h3><p>Wrong answers fell from 8.9% to 1.4%</p></div>
  <div v-click><h3>Keep weakly matching passages, judged against the student's own words</h3><p>Hard emails answered correctly went from 7 to 20 of 49</p></div>
  <div v-click><h3>Look courses up with a tool</h3><p>Course questions went from 21% to 100% correct</p></div>
  <div v-click><h3>Return short links from the tool</h3><p>Broken links went from 8 to 0</p></div>
</div>
</div>
<div>
<div class="label">Dropped</div>
<div class="stack">
  <div v-click><h3>Tell the model to copy links exactly</h3><p>Broken links: 8 → 7. Fixing the data worked; the instruction did not</p></div>
  <div v-click><h3>Tell it not to hedge</h3><p>Less hedging, but new unsupported details and no more correct answers</p></div>
  <div v-click><h3>Pull in extra linked FAQs</h3><p>Distracted the model as often as it helped</p></div>
</div>
</div>
</div>

<!--
Hard sets contain emails that earlier versions got wrong, so their gains are inflated and can't be ranked against each other. The 0.10 floor problem: long emails get low reranker scores even when the ranking is right (backup slide).
-->

---
section: Results
---

# The right documents are usually found; missing knowledge is the gap

<div class="grid grid-cols-[1.1fr_0.9fr] gap-10 mt-2">
<div>
<div class="label">Final batch, 275 emails with a relevant source</div>
<HBar label="Relevant source found" :value="94.5" suffix="%" label-width="9.5rem" />
<HBar label="Answer correct" :value="72.4" suffix="%" label-width="9.5rem" color="#e8b64c" />
<p class="small mt-5">The agent searches about twice per question and finds a relevant source for almost every email. The gap between finding and answering comes from two places:</p>
</div>
<div class="stack">
  <div v-click class="on"><h3>Facts no document states</h3><p>13% of emails. They cluster in a few topics, like master's procedures and admissions, which new FAQs can fill.</p></div>
  <div v-click><h3>How the answer is written</h3><p>The right FAQ was found, but the model hedged or added a detail from a loosely related passage.</p></div>
</div>
</div>

<!--
LQ2. Recall: one production search finds a relevant item for 85.5%, the agent's searches together 94.5%. Only 13 of 298 emails had a relevant item that never reached the model. With my own relevance labels on 317 passages, retrieval looks even better.
-->

---
section: Results
---

# Fancier retrieval did not make answers better

<div class="grid grid-cols-3 gap-4 mt-2">
<div class="card !p-5" v-click>
  <h3>A knowledge graph</h3>
  <p class="small">LightRAG found relevant sources about as often as plain search, cost 1,859 model calls to build and added about 2 seconds per question.</p>
</div>
<div class="card !p-5" v-click>
  <h3>An AI reranker</h3>
  <p class="small">Ranked sources better by the AI's own labels, not by mine, and answers got slightly worse: 69% correct against 74%.</p>
</div>
<div class="card on !p-5" v-click>
  <h3>Follow-up questions</h3>
  <div class="fig green !text-[2.2rem] mt-2">41 / 42</div>
  <p class="small">answered correctly when the question only made sense with the earlier conversation.</p>
</div>
</div>

<!--
Students mostly ask about one rule stated in one FAQ or a few passages, so linking entities across documents adds little. Decision-model test: 100 emails, p = 0.24, within chance.
-->

---
section: Findings
---

# Answers to the five questions

<table class="t big">
<tbody>
<tr v-click><td class="w-[16rem]"><b class="lime">1.</b> How often is it good?</td><td>In the controlled test, a third of email answers and half of chat answers by the AI grader, likely more by a person. The weak spots are incomplete answers and unsupported claims.</td></tr>
<tr v-click><td><b class="lime">2.</b> Does more text help?</td><td>No. Three to six times more text, no change.</td></tr>
<tr v-click><td><b class="lime">3.</b> Can AI grade it?</td><td>Only with care. Graders disagree with each other and are far stricter than a person.</td></tr>
<tr v-click class="hl"><td><b class="lime">4.</b> Is it right on real emails?</td><td>About three in four correct, 1–3% wrong, confirmed by my own grading.</td></tr>
<tr v-click><td><b class="lime">5.</b> Is retrieval the bottleneck?</td><td>No. The sources are found for 94.5% of emails; missing knowledge and answer writing matter more.</td></tr>
</tbody>
</table>

<style>
table.t.big { font-size: .92rem; }
table.t.big td { padding: .62rem .6rem; }
</style>

---
section: Findings
---

# What this means for anyone building one

<div class="grid grid-cols-3 gap-4 mt-1">
  <div class="card on !p-5" v-click><div class="fig green">1</div><h3 class="mt-3">Write down the knowledge</h3><p class="small">Confirmed facts matter more than tuning search.</p></div>
  <div class="card on !p-5" v-click><div class="fig green">2</div><h3 class="mt-3">Check the AI grader against people</h3><p class="small">Its numbers, and sometimes its conclusions, change with the grader.</p></div>
  <div class="card on !p-5" v-click><div class="fig green">3</div><h3 class="mt-3">Fix data, not prompts</h3><p class="small">When the problem is in the data, an instruction will not fix it.</p></div>
</div>

<div class="grid grid-cols-2 gap-10 mt-6 small" v-click>
<div>
<h3 class="red">Limits</h3>

- Mostly AI-graded; 100 answers checked by one person, who also built it
- The live system changed between test runs
- Not yet tried at a second institution

</div>
<div>
<h3 class="green">Next</h3>

- Grading by faculty staff, the most important step
- New FAQs for the topics where knowledge is missing
- A test with retrieval switched off, as a baseline

</div>
</div>

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

---
section: Backup
---

# Backup: how each platform is built

<HubMap />

<p class="caption !mt-2">Docker images built by GitHub Actions run on two servers (apps, GPU); web apps and small APIs run on Cloudflare.</p>

---
section: Backup
---

# Backup: controlled test, answers by category

<StackBar label="Emails, before" :total="96" :parts="[{n:9,color:'#1ba96e'},{n:22,color:'#8be07a'},{n:20,color:'#f07a62'},{n:31,color:'#e8b64c'},{n:14,color:'#1e3a2c',light:true}]" />
<StackBar label="Emails, after" :total="96" :parts="[{n:10,color:'#1ba96e'},{n:20,color:'#8be07a'},{n:19,color:'#f07a62'},{n:30,color:'#e8b64c'},{n:17,color:'#1e3a2c',light:true}]" />
<div class="h-3" />
<StackBar label="Chat, before" :total="96" :parts="[{n:25,color:'#1ba96e'},{n:28,color:'#8be07a'},{n:12,color:'#f07a62'},{n:22,color:'#e8b64c'},{n:4,color:'#a595e6'},{n:5,color:'#1e3a2c',light:true}]" />
<StackBar label="Chat, after" :total="96" :parts="[{n:25,color:'#1ba96e'},{n:27,color:'#8be07a'},{n:11,color:'#f07a62'},{n:24,color:'#e8b64c'},{n:4,color:'#a595e6'},{n:5,color:'#1e3a2c',light:true}]" />

<div class="flex gap-4 tiny mt-3 ml-[9.7rem] text-[#c3c4b8] nowrap">
  <span><span class="swatch bg-[#1ba96e]" />supported answer</span>
  <span><span class="swatch bg-[#8be07a]" />useful referral</span>
  <span><span class="swatch bg-[#f07a62]" />unsupported claim</span>
  <span><span class="swatch bg-[#e8b64c]" />incomplete</span>
  <span><span class="swatch bg-[#a595e6]" />unneeded refusal</span>
  <span><span class="swatch bg-[#1e3a2c]" />not gradable</span>
</div>

<p class="caption !mt-5">96 questions per row, main AI grader. "Before" is the baseline (document threshold 0.10), "after" the lower threshold (0.00).</p>

---
section: Backup
---

# Backup: the controlled result under each AI grader

<div class="grid grid-cols-[1.2fr_0.8fr] gap-8">
<div>
<div class="label">Lower threshold minus baseline, percentage points, 95% interval</div>
<ForestPlot :rows="[
  { label: 'Emails, GPT-5.6 Luna (main)', est: -1.04, lo: -8.3, hi: 6.3 },
  { label: 'Emails, Claude Sonnet 5.5', est: 1.04, lo: -7.3, hi: 9.4 },
  { label: 'Emails, GPT-6 Luna', est: -2.08, lo: -9.4, hi: 5.2 },
  { label: 'Chat, GPT-5.6 Luna (main)', est: -1.04, lo: -7.3, hi: 5.2, gap: true },
  { label: 'Chat, Claude Sonnet 5.5', est: 7.29, lo: 1.0, hi: 13.5, hl: true },
  { label: 'Chat, GPT-6 Luna', est: -1.04, lo: -5.2, hi: 3.1 },
]" />
</div>
<div class="small">
<p>Pairs of graders agree on whether an answer is good for 67–74% of answers (κ 0.38–0.48).</p>
<p>The same grader, given the same input twice, agrees with itself on 74.5% of categories.</p>
</div>
</div>

---
section: Backup
---

# Backup: retrieval methods on the final batch

<table class="t">
<thead><tr><th>Method</th><th class="num">hit@1</th><th class="num">hit@3</th><th class="num">hit@5</th><th class="num">hit@10</th><th class="num">recall@10</th><th class="num">MRR×100</th></tr></thead>
<tbody>
<tr><td>BM25</td><td class="num">32.0</td><td class="num">52.4</td><td class="num">62.2</td><td class="num">73.5</td><td class="num">50.7</td><td class="num">45.3</td></tr>
<tr><td>Dense (BGE-M3)</td><td class="num">51.3</td><td class="num">70.2</td><td class="num">77.5</td><td class="num">86.2</td><td class="num">68.6</td><td class="num">62.4</td></tr>
<tr><td>Hybrid (RRF)</td><td class="num">44.7</td><td class="num">67.6</td><td class="num">78.2</td><td class="num">86.9</td><td class="num">70.5</td><td class="num">58.8</td></tr>
<tr><td>HyDE</td><td class="num">57.5</td><td class="num">76.0</td><td class="num">82.9</td><td class="num">88.4</td><td class="num">72.1</td><td class="num">68.5</td></tr>
<tr><td>Rewrite</td><td class="num">50.5</td><td class="num">70.9</td><td class="num">79.3</td><td class="num">88.0</td><td class="num">70.1</td><td class="num">63.3</td></tr>
<tr><td>Dense + rerank</td><td class="num">52.4</td><td class="num">73.8</td><td class="num">81.1</td><td class="num">86.5</td><td class="num">72.3</td><td class="num">64.5</td></tr>
<tr><td>Hybrid + rerank</td><td class="num">54.5</td><td class="num">76.0</td><td class="num">85.1</td><td class="num">90.2</td><td class="num">75.5</td><td class="num">67.0</td></tr>
<tr class="hl"><td>HyDE + rerank</td><td class="num">56.7</td><td class="num">79.6</td><td class="num">85.8</td><td class="num">91.3</td><td class="num">76.8</td><td class="num">69.0</td></tr>
<tr><td>Rewrite + rerank</td><td class="num">57.1</td><td class="num">78.9</td><td class="num">85.5</td><td class="num">90.9</td><td class="num">74.7</td><td class="num">68.6</td></tr>
</tbody>
</table>
<p class="caption">Percent of the 275 emails with a relevant item, pooled AI labels. Recall values are about 10 points too high (shown by deeper judging); hit rates are reliable.</p>

---
section: Backup
---

# Backup: choosing the 0.03 context floor

<div class="grid grid-cols-[1fr_1fr] gap-12">
<div>
<div class="label">Expected FAQ in the top 10, 49 wrongly answered emails</div>
<HBar label="Floor 0.10" :value="28.6" suffix="%" label-width="6rem" color="#2e4a3c" />
<HBar label="Floor 0.03" :value="42.9" suffix="%" label-width="6rem" />
<HBar label="Floor 0.01" :value="44.9" suffix="%" label-width="6rem" color="#8be07a" />
</div>
<div class="small">

- Long emails get low reranker scores even when the ranking is right
- 29 of 30 expected FAQs among the candidates scored below 0.10
- 0.03 comes close to 0.01 while still dropping the weakest passages
- At the 0.30 display threshold, half of the shown sources are relevant and 85% of irrelevant ones are hidden

</div>
</div>
