# Defense Q&A preparation

Likely committee questions, a short answer for each, and where to jump in the deck. Numbers come from the thesis; "slide N" refers to the current 24-slide deck.

## Evaluation and trust

**1. How much of the evaluation is graded by AI, and why should we trust it?**
Almost all of it, which is why I checked it. I graded 100 answers and 317 retrieved passages by hand, without seeing the AI labels. On the live system I agree with the AI grader on 84.8% of answers (κ 0.57); I rated 73.9% correct, Sonnet 80.4%, so it is slightly lenient but close. In the controlled test the graders were much stricter than me, so those rates are probably too low. *Slides 14, 16.*

**2. Why are the controlled numbers (31/96, 53/96) so much lower than the live ~76%?**
They measure different things and are never combined. The controlled test uses a simplified pipeline (one search, one model call, GPT-5.6 Luna), an older corpus (74 FAQs, 19 documents), a strict reference-based judge and a different grading scheme. The live test uses the full agent with tools, GPT-6 Luna, the current corpus (104 FAQs, 65 documents) and a different rubric. The strict judges also explain part of the gap (question 1). *Slide 10.*

**3. Is the held-out test really clean?**
Holdout 3 (298 emails) was never used for any fix, and holdouts 1 and 2 were clean when first measured. The set that drove fixes scores 11.5 points higher than new emails under the same judge, which is exactly why I report the clean sets. *Slide 16 notes.*

**4. Was this pre-registered?**
The controlled experiment was: sample, seed, policies, rubric and analysis were fixed before any answer was generated, and input file hashes were saved. The live evaluation was iterative engineering and is reported as such, separately.

**5. κ is near zero against your grades. Does that make the judges useless?**
Not on its own. κ is low partly because I rated most answers good, which leaves little room for agreement beyond chance; the raw counts (30 good by me vs 12–23 by the judges) show the real issue, which is strictness. The policy comparison still rests on AI labels, because I graded one policy per question.

**6. Are student emails representative of chatbot questions?**
Not fully, and the thesis says so. Emails are written to staff and are longer (median 306 characters) than chat messages (31.5). That is why the controlled test uses both sources and reports them separately. The held-out sets were drawn per topic group across all 24 topics.

## Design choices

**7. Why a context floor of 0.03?**
Long, multi-topic emails get low absolute reranker scores even when the ranking is right: 29 of 30 expected FAQs scored below 0.10. At 0.03 the expected FAQ reached the top 10 for 42.9% of hard emails vs 28.6% at 0.10, close to 0.01 (44.9%) while still dropping the weakest passages. The value only holds for BGE-reranker-v2-m3. *Slide 21.*

**8. Why BGE-M3, given there is no Macedonian benchmark?**
It is multilingual and runs on our own GPU. I measured it on real emails: dense search alone puts a relevant item in the top 10 for 86.2% of them. *Slide 20.*

**9. Why not a knowledge graph (LightRAG)?**
I tested it. It found relevant sources about as often as plain search (hit@10 86.9% vs 87.6%), cost 1,859 model calls to build and added about 2 seconds per question. Students mostly ask about one rule stated in one FAQ or a few passages, so linking entities adds little. *Slides 20, 21.*

**10. Why not fine-tune a model instead of retrieval?**
The rules change every year and answers must point to their source; retrieval lets me update knowledge without retraining and keeps every answer traceable. The thesis also shows the main loss is missing knowledge, which fine-tuning would not fix. (This is reasoning, not something the thesis tested.)

**11. A better reranker ranked better. Why not use it?**
It ranked better by the AI's own labels, not by mine, and the answers got slightly worse: 69.1% vs 74.5% correct (p = 0.24). Under the same floor it removed about 40% of the context. It would need its own threshold before it could help. *Slide 21.*

**12. How do you handle rules that conflict, like the transfer example?**
Documents carry date, validity and authority fields, passed to the model as labeled text, and the prompt prefers an FAQ (current practice) over a general regulation unless a document states a more specific fact. Using validity in ranking is future work.

## Results

**13. Why did more text not help?**
The extra text did reach the model: on the 66 emails with usable references, the share of reference quotes found word for word in the context rose from 48.6% to 66.1%. The answers stayed the same because the failures were incomplete answers and unsupported claims, which are about how the answer is built, not what is retrieved. *Slide 12.*

**14. How often is it wrong, and how do you catch invented details?**
1–3% wrong on clean sets by the AI grader. In the 46 answers we both graded, I marked 4 wrong and the AI 2, so the true rate may be somewhat higher. A script checks every date, amount, URL and email address in an answer against the tool output and confirmed facts; it caught broken announcement links, which were fixed by returning short links from the tool. *Slide 18.*

**15. What is the single biggest remaining problem?**
Missing knowledge: about 13% of emails ask for a fact no source states. About a third fall in a few topics (master's procedures, admissions, degree verification, open days), which new confirmed FAQs can fill. *Slide 19.*

## Practical

**16. What about privacy?**
The knowledge base holds only public documents, web pages and my FAQs. The bot cannot see any student's records. The test emails were anonymized by the faculty and never enter the knowledge base. Usage analytics store metadata only, no question text, and users can delete their conversations.

**17. What does it cost and how fast is it?**
Retrieval runs on our own GPU server. In live runs, the first words of an answer appeared after a median of 5.0–5.4 seconds. The two controlled campaigns cost an estimated USD 31 in model calls; the decision-model ranking test cost about USD 0.20.

**18. Does the architecture work for other institutions?**
It is designed to: an institution replaces its corpus, source review and data connections and keeps the six steps. It has not yet been tried at a second institution; that is a stated limitation.

**19. What would you do next?**
Grading by faculty staff to calibrate the AI judges (most important), new FAQs for the gap topics with validity metadata used in ranking, and trying the same approach at a second institution. The thesis also lists a live test with search turned off as possible future work. *Slide 23.*

## About the deck itself

**20. Slide 2 shows a Data service. Why isn't it in the thesis?**
Data (Directus at data.finki-hub.com) was added after the thesis text and its evaluation runs were finished, so it does not affect any reported result. It is on the slide because it is now how the FINKI Hub tools share data. *Slide 2.*

**21. How do your seven questions relate to the thesis research questions?**
The thesis states three formal questions: how often responses are supported or usefully routed, how retrieval thresholds affect that, and what limits the results (question choice, references, AI judge). The seven on the slide are the same work in plain language, plus the live evaluation. *Slides 5, 22.*

**22. Who maintains all of this?**
I am the main maintainer: I authored almost all recent pull requests. Everything is MIT licensed and open to contributions. *Slide 2.*

**23. Why not compare every answer with the staff replies?**
The staff replies are the closest thing to a gold standard, but the thesis treats them as a hint because they can be stale or partial. A correct current answer could be marked wrong for disagreeing with an old reply. In the live evaluation the AI judges see them alongside the current FAQs, official links, syllabi, answer rules and confirmed facts. *Slide 16.*

**24. How much was checked by a person?**
I graded 100 answers (50 controlled, 50 live) and 317 search results from 20 emails, without seeing the AI labels. On the live system that is 50 of 844 answers, about 6%. I agree with the AI grader on 84.8% of the answers we could both grade (46). The eleven-version chart is AI-graded only. The most important next step is independent grading by faculty staff, because I built the system. *Slides 14, 16, 23.*

**25. The thesis says you rated 30 of 37 as good. Is that right?**
Precisely: 31 of the 37 real questions, and 30 of the 36 that the main AI graders could also grade. The comparison table in the thesis uses the 30 of 36. GPT-6 Luna could grade 34 of them, also with 30 good by me. *Slide 14.*

**26. How much do the AI graders agree?**
On the exact grade, two different graders agree on 53.0 to 57.9% of answers, and one grader repeated on the same input agrees with itself on 74.5% (35 of 47). On the simpler question of good or not good, two graders agree on 66.8 to 74.0% (κ 0.38 to 0.48). *Slide 14.*

**27. Why do I see 76%, 72.4% and 88% correct?**
They use different bases. 76% is the last clean batch, out of the emails that could be graded (run b: 76.0%, run a: 76.5%). 72.4% is the same batch out of all 275 emails that have a relevant source, including ones that could not be graded. 87.8% is the 334 emails used for fixing, so it is optimistic. With the same grader (Opus), those emails scored 87.8% and the first clean batch 76.3%. *Slides 16, 17, 19.*

**28. Slide 12 says a lower cutoff did not help, but slide 20 says it did. Which is it?**
They are different changes. The controlled test lowered the cutoff for documents only and kept FAQs at 0.10. The live fix lowered one shared cutoff to 0.03, so it also let low-scoring FAQs through, and it also ranked against the student's original words. On 49 hard emails, that took correct answers from 7 to 20. The two parts of the live fix were not fully separated. *Slides 12, 21.*

**29. Why is 94.5% higher than the best method in the search table (91.3%)?**
The table measures one search, and the row closest to the chatbot reaches 86.5%. The agent searches 1.7 times per answer on average, and its first search alone reaches 86.5%, the second 93.1%. *Slides 19, 20.*

