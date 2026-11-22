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

<div class="lockup"><b>FINKI Hub</b><span>independent student organization</span></div>

# Tools FCSE students use every day

<HubTiles />

<p class="caption !mt-4">Not affiliated with the faculty. Every project is open source at <b class="text-[#ece7da]">github.com/finki-hub</b>.</p>

<!--
[1:30] Some context first. FINKI Hub is an independent student organization. We build tools on top of public faculty data: a Discord feed of faculty announcements, a thesis browser, timetables, a course planner, lecture recordings and a browser terminal. The chatbot on the left is the subject of this thesis. It's the newest piece, and it reuses the others: when you ask it about a thesis or a timetable, it looks it up in those services.
-->

---
section: Problem
---

# The answers students need are scattered

<div class="grid grid-cols-[1fr_1.1fr] gap-12 mt-2">
<div>
  <div class="bubble">
    "I'm transferring from another university. How many of my credits can I bring, and what do I need to submit?"
  </div>
  <p class="small mt-6">Students ask about situations: enrolling, transferring, fees, deadlines, exams. The answer is spread across regulations, faculty decisions, web pages and what staff wrote back in earlier emails.</p>
</div>
<div class="stack">
  <div><h3>Three rules for the same word</h3><p>"Transfer" appears in the 2013 faculty rules, the 2019 university rules and a 2022 supplement, each with a different condition.</p></div>
  <div><h3>Answered one email at a time</h3><p>The faculty gave us 1,693 anonymized student emails with staff replies, falling into 24 recurring topics.</p></div>
  <div><h3>A confident answer can still be wrong</h3><p>A chatbot that finds a passage about "transfer" can quote the wrong rule, or skip a condition.</p></div>
</div>
</div>

<style>
.bubble { position: relative; padding: 1rem 1.2rem; font-size: 1.05rem; line-height: 1.5; color: #ece7da; background: #12281d; border: 1px solid #2a5a3f; clip-path: polygon(14px 0, 100% 0, 100% 100%, 0 100%, 0 14px); }
</style>

<!--
[1:30] Here's the problem. Students don't ask "what does article 31 say". They describe their situation, like this student who is transferring. To answer that you need several sources: the word "transfer" alone appears in three different rules from 2013, 2019 and 2022, each with a different condition. Today these questions go to staff by email; the faculty gave us 1,693 of them. And a chatbot can easily find a passage about transfers and still quote the wrong rule.
-->

---
section: Problem
---

# What I set out to do

<div class="grid grid-cols-3 gap-4 mt-2">
  <div class="card"><div class="fig">Design</div><p class="small mt-3">A blueprint for assistants that answer from an institution's documents, where every step can be checked.</p></div>
  <div class="card"><div class="fig">Build</div><p class="small mt-3">The FINKI Hub chatbot as a working example, used by real students on the web and in Discord.</p></div>
  <div class="card on"><div class="fig">Measure</div><p class="small mt-3">Honestly test how often its answers are right, and find out what actually limits them.</p></div>
</div>

<div class="mt-8 small">
<p class="!m-0"><b>A good answer</b> either gives the correct rule with its conditions, backed by the sources, or sends the student to the right office when the documents can't settle it. Questions about a student's own records, like grades, only need the right referral: the bot never sees personal data.</p>
</div>

<!--
[1:15] So the work had three parts. Design: a general blueprint for this kind of assistant, where every step can be checked. Build: the FINKI Hub chatbot, used by real students. And measure: honestly, how often it's right. Note what counts as a good answer: either the correct rule with its conditions, or sending the student to the right office. Sometimes "ask Student Services" is the right answer.
-->

---
section: Problem
---

# Five questions the thesis answers

<div class="grid grid-cols-2 gap-8 mt-1">
<div class="stack">
  <div><h3>Test 1, controlled</h3><p class="!text-[.68rem] !text-[#849086]">Same questions, one setting changed at a time</p></div>
  <div><p><b class="muted">1.</b> How often does it give a good answer, and what goes wrong?</p></div>
  <div><p><b class="muted">2.</b> Does giving the model more of the documents help?</p></div>
  <div><p><b class="muted">3.</b> Can we trust AI to grade the answers?</p></div>
</div>
<div class="stack">
  <div class="on"><h3>Test 2, the live system</h3><p class="!text-[.68rem] !text-[#849086]">The deployed chatbot on emails it had never seen</p></div>
  <div><p><b class="muted">4.</b> How often is it right on real student emails, and where does it fail?</p></div>
  <div><p><b class="muted">5.</b> Is finding the right documents the bottleneck?</p></div>
</div>
</div>

<!--
[1:00] That gives five questions. Three come from a controlled experiment: how often is it good, does more text help, and can AI grade it. Two come from the live system: how often is it right on real emails, and is finding documents the bottleneck. I'll come back to all five at the end.
-->

---
section: How it works
layout: wide
---

# The blueprint: six steps, each one checkable

<ArchChain class="mt-2" />

<p class="small mt-8">Step 3 is where most of the design choices are, so it is the step the controlled test varies. Because each step hands a clear result to the next, a wrong answer can be traced to the step where it went wrong.</p>

<!--
[2:00] This is the architecture: six steps, left to right. Prepare the sources, store them, find the evidence, write the answer, deliver it, and observe. The top line says what each step does, the bottom line how my chatbot does it. Step 3, finding evidence, is highlighted because that's where most design choices are, and it's what the controlled experiment varies. Because each step hands a clear result to the next, a wrong answer can be traced back to the step where it went wrong.
-->

---
section: How it works
---

# What the chatbot knows

<div class="figs mt-2">
  <div><div class="fig">104</div><div class="fig-label">FAQ answers I wrote and maintain</div></div>
  <div><div class="fig">65</div><div class="fig-label">official documents and faculty web pages</div></div>
  <div><div class="fig">2,524</div><div class="fig-label">searchable passages</div></div>
  <div><div class="fig">1,693</div><div class="fig-label">real student emails, used only for testing</div></div>
</div>

<div class="grid grid-cols-2 gap-12 mt-8 small">
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
[1:15] What does it know? 104 FAQ answers that I write and maintain, 65 official documents and faculty pages, split into about 2,500 searchable passages. The 1,693 emails are only used for testing; they never enter the knowledge base. Everything is public, and search runs on our own GPU server.
-->

---
section: How it works
---

# The chatbot, live

<div class="demo">
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
[3:00] Let me show it. (LIVE DEMO) First a rules question in Cyrillic: watch it search, then answer with sources. The same question in Latin script. A course question, which it looks up with a tool. And "What is my GPA?", which it correctly sends to Student Services. If the network fails, switch to the recorded video.
-->

---
section: Testing
---

# Two ways to test it

<div class="grid grid-cols-2 gap-6 mt-2">
<div class="card !p-5">
  <h3 class="!text-[1.05rem]">Test 1: a controlled experiment</h3>
  <p class="small">A simplified bot does one search and writes one answer. I change one retrieval setting at a time and compare.</p>
  <div class="grid grid-cols-2 gap-3 mt-4">
    <div><div class="fig !text-[1.6rem]">192</div><div class="fig-label">questions: real emails and chatbot messages</div></div>
    <div><div class="fig !text-[1.6rem]">4</div><div class="fig-label">settings compared, plan fixed in advance</div></div>
  </div>
</div>
<div class="card on !p-5">
  <h3 class="!text-[1.05rem]">Test 2: the real system</h3>
  <p class="small">The deployed chatbot, with all its tools, answers student emails it has never seen.</p>
  <div class="grid grid-cols-2 gap-3 mt-4">
    <div><div class="fig !text-[1.6rem]">844</div><div class="fig-label">unseen emails in three batches</div></div>
    <div><div class="fig !text-[1.6rem]">11</div><div class="fig-label">versions of the system along the way</div></div>
  </div>
</div>
</div>

<p class="small mt-6">AI models graded the answers. To check them, <b>I graded 100 answers and 317 retrieved passages by hand</b>, without seeing the AI grades.</p>

<!--
[1:30] I tested it two ways. Test 1 is controlled: a simplified bot does one search and one answer, and I change one retrieval setting at a time on 192 real questions, with the plan fixed in advance. Test 2 is the real system on 844 emails it had never seen. AI models graded the answers, so I checked them by grading 100 answers and 317 passages myself.
-->

---
section: Results
---

# More text did not help

<div class="grid grid-cols-[1fr_1fr] gap-12 mt-2 one">
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
[1:30] First surprise. Letting more documents through gave the model three to six times more text. (click) The share of good answers changed by about minus one point, which is noise. More evidence did reach the model, but the answers didn't improve; what held them back was incomplete answers and claims the sources didn't support.
-->

---
section: Results
---

# AI graders were stricter than me

<div class="grid grid-cols-[1fr_1fr] gap-12 mt-2 one">
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
[1:30] Second finding: you can't blindly trust an AI grader. Out of about 36 answers I rated 30 as good; the three AI graders rated between 12 and 23. (click) They also disagree with each other, on about a quarter to a third of answers, and one of them even saw an improvement the others didn't. So the controlled numbers are probably too low.
-->

---
section: Results
---

# Three in four answers were correct

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
<div class="stack mt-5">
  <div class="on"><h3>My grades agree</h3><p>On 50 of these answers I agreed with the AI grader 85% of the time. I rated 74% correct.</p></div>
</div>
</div>
</div>

<style>
.hero-num { font-family: 'Unbounded', sans-serif; font-size: 6rem; font-weight: 500; line-height: .95; letter-spacing: -.04em; background: linear-gradient(135deg, #8be07a, #1ba96e); -webkit-background-clip: text; background-clip: text; color: transparent; }
</style>

<!--
[2:00] Now the live system, which is the main result. On the final batch of emails, which no fix ever touched, 76% of answers were correct, and only 1 to 3% were wrong; the rest were partly right or honest referrals. The three batches agree. And when I graded 50 of these myself, I agreed with the AI grader 85% of the time.
-->

---
section: Results
layout: wide
---

# How it got there: eleven versions, from 59% to 88%

<StageChart />

<p class="caption">Measured on the 334 emails used for fixing, so the final number is optimistic; the grading also changed over time. Read it for direction, not exact values.</p>

<!--
[1:15] This is how it got there, over eleven versions. Correct answers went from 59 to 88% and wrong ones from 19 to about 1%. The big steps: version 3 fixed how passages are scored, and version 5 let the agent search for itself. This is measured on the emails I used for fixing, so read it as direction, not as the final number.
-->

---
section: Results
layout: wide
---

# What made it better, and what did not

<div class="grid grid-cols-2 gap-8 mt-2">
<div>
<div class="label">Kept</div>
<div class="stack">
  <div><h3>Let the agent search for itself</h3><p>Wrong answers fell from 8.9% to 1.4%</p></div>
  <div><h3>Keep weakly matching passages, judged against the student's own words</h3><p>Hard emails answered correctly went from 7 to 20 of 49</p></div>
  <div><h3>Look courses up with a tool</h3><p>Course questions went from 21% to 100% correct</p></div>
  <div><h3>Return short links from the tool</h3><p>Broken links went from 8 to 0</p></div>
</div>
</div>
<div>
<div class="label">Dropped</div>
<div class="stack">
  <div><h3>Tell the model to copy links exactly</h3><p>Broken links: 8 → 7. Fixing the data worked; the instruction did not</p></div>
  <div><h3>Tell it not to hedge</h3><p>Less hedging, but new unsupported details and no more correct answers</p></div>
  <div><h3>Pull in extra linked FAQs</h3><p>Distracted the model as often as it helped</p></div>
</div>
</div>
</div>

<!--
[1:30] What worked: letting the agent search, keeping weakly matching passages but judging them against the student's own words, and giving it real tools. What didn't: telling the model in the prompt to copy links exactly, or not to hedge. The lesson: when the problem is in the data, fix the data; an instruction won't.
-->

---
section: Results
---

# Sources are found; facts are missing

<div class="grid grid-cols-[1.1fr_0.9fr] gap-10 mt-2 one">
<div>
<div class="label">Final batch, 275 emails with a relevant source</div>
<HBar label="Relevant source found" :value="94.5" suffix="%" label-width="9.5rem" />
<HBar label="Answer correct" :value="72.4" suffix="%" label-width="9.5rem" color="#e8b64c" />
<p class="small mt-5">The agent searches about twice per question and finds a relevant source for almost every email. The gap between finding and answering comes from two places:</p>
</div>
<div class="stack">
  <div class="on"><h3>Facts no document states</h3><p>13% of emails. They cluster in a few topics, like master's procedures and admissions, which new FAQs can fill.</p></div>
  <div><h3>How the answer is written</h3><p>The right FAQ was found, but the model hedged or added a detail from a loosely related passage.</p></div>
</div>
</div>

<!--
[1:30] So is retrieval the bottleneck? No. For 94.5% of emails, a relevant source reached the model. Yet only about 72% of those answers are correct. The gap comes from two places: facts that no document states, about 13% of emails, clustered in a few topics; and how the answer is written, where the model found the right FAQ but hedged or added a detail.
-->

---
section: Results
layout: wide
---

# Fancier retrieval did not make answers better

<div class="grid grid-cols-3 gap-4 mt-2">
<div class="card !p-5">
  <h3>A knowledge graph</h3>
  <p class="small">LightRAG found relevant sources about as often as plain search, cost 1,859 model calls to build and added about 2 seconds per question.</p>
</div>
<div class="card !p-5">
  <h3>An AI reranker</h3>
  <p class="small">Ranked sources better by the AI's own labels, not by mine, and answers got slightly worse: 69% correct against 74%.</p>
</div>
<div class="card on !p-5">
  <h3>Follow-up questions</h3>
  <div class="fig lime !text-[2.2rem] mt-2">41 / 42</div>
  <p class="small">answered correctly when the question only made sense with the earlier conversation.</p>
</div>
</div>

<!--
[1:15] I also tried fancier retrieval. A knowledge graph found sources about as well as plain search, at much higher cost. A stronger AI reranker ranked better by its own standards but answers got slightly worse. On the positive side, the agent handled follow-up questions well: 41 of 42.
-->

---
section: Findings
layout: wide
---

# Answers to the five questions

<table class="t big">
<tbody>
<tr><td class="w-[16rem]"><b class="muted">1.</b> How often is it good?</td><td>In the controlled test, a third of email answers and half of chat answers by the AI grader, likely more by a person. The weak spots are incomplete answers and unsupported claims.</td></tr>
<tr><td><b class="muted">2.</b> Does more text help?</td><td>No. Three to six times more text, no change.</td></tr>
<tr><td><b class="muted">3.</b> Can AI grade it?</td><td>Only with care. Graders disagree with each other and are far stricter than a person.</td></tr>
<tr class="hl"><td><b class="muted">4.</b> Is it right on real emails?</td><td>About three in four correct, 1–3% wrong, confirmed by my own grading.</td></tr>
<tr><td><b class="muted">5.</b> Is retrieval the bottleneck?</td><td>No. The sources are found for 94.5% of emails; missing knowledge and answer writing matter more.</td></tr>
</tbody>
</table>

<style>
table.t.big { font-size: .92rem; }
table.t.big td { padding: .62rem .6rem; }
</style>

<!--
[1:30] Back to the five questions. One: in the controlled test, about a third to a half are good by the AI grader, likely more. Two: more text doesn't help. Three: AI grading needs checking against people. Four: on real emails, about three in four are correct and very few wrong. Five: retrieval is not the bottleneck.
-->

---
section: Findings
layout: wide
---

# What this means for anyone building one

<div class="grid grid-cols-3 gap-4 mt-1">
  <div class="card on !p-5"><div class="fig muted">1</div><h3 class="mt-3">Write down the knowledge</h3><p class="small">Confirmed facts matter more than tuning search.</p></div>
  <div class="card on !p-5"><div class="fig muted">2</div><h3 class="mt-3">Check the AI grader against people</h3><p class="small">Its numbers, and sometimes its conclusions, change with the grader.</p></div>
  <div class="card on !p-5"><div class="fig muted">3</div><h3 class="mt-3">Fix data, not prompts</h3><p class="small">When the problem is in the data, an instruction will not fix it.</p></div>
</div>

<div class="grid grid-cols-2 gap-10 mt-6 small">
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

<!--
[1:30] Three lessons for anyone building one. Write down the knowledge: confirmed facts matter more than tuning search. Check your AI grader against people. And fix data, not prompts. The limits: grading is mostly AI with one human checker, the live system changed between runs, and it's not yet tried elsewhere. Next is grading by faculty staff and filling the knowledge gaps. Thank you.
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

---
section: Backup
layout: wide
---

# Backup: how each platform is built

<HubMap />

<p class="caption !mt-2">Docker images built by GitHub Actions run on two servers (apps, GPU); web apps and small APIs run on Cloudflare.</p>

---
section: Backup
layout: wide
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
layout: wide
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
layout: wide
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
layout: wide
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
