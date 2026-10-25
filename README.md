# Prodigy KS3 Maths

Buildless revision site for Years 7–9. The main route follows the supplied department teaching sequence, checked on 25 October 2026:

- Year 7: 16 units, ordered by the numbered lesson folders and 2026–27 scheme.
- Year 8: 14 units in the same department order. The scheme fills gaps where lesson folders were not supplied.
- Year 9: 19 revision units grouped by the six GCSE units in the **Y9 Combined (H+F)** tab of the supplied combined scheme. Number, Algebra, Fractions/Percentages/Ratio, Angles/Triangles, Data, then Graphs.

The 11 supplementary units remain available through “Show extra revision”. Revision resources consolidate related classroom lessons; this is not a separate resource for every teaching slide. White Rose-style representations and the original content bank are retained, but the site no longer claims to follow White Rose Version 3 block order. All materials are original Prodigy resources, not copied school slides or official White Rose resources. The site is not endorsed by White Rose Education.

All 245 lessons use swipeable slides, with at most three explanation points per slide. Lessons open with a complete worked example: up to four lines of working, with short notes alongside and optional method help underneath. On phones, notes sit directly below their working. Each of the 144 concept types has a labelled visual. Representations include equal-part bars, double number lines, place-value counters, zero pairs, algebra tiles, fraction area models, frequency trees, Venn diagrams, nets, compass constructions and coordinate transformations. Captions connect each model to a calculation or explanation. Buttons and keyboard arrows also navigate the decks.

There are 497 definition cards, four assessed questions per lesson and 60 mixed unit checks. New coverage includes money skills, data types, grouped data, ratio problems with a known difference, constructions, congruence, transformations, sets, expected outcomes and simultaneous equations. The graph plotter, optional Maths keyboard and twelve interactive models remain available.

Each year has one original 30-mark Version 3 review retained as supplementary practice and two retained 30-mark department papers. Papers have saved working, optional timers and printable questions and schemes. No official grades or predictions are attached. Numerical checks verify a final value; method and reasoning marks use indicative schemes, with provisional server-side AI feedback when configured and signed in. Self-marking remains available.

All 142 existing lesson routes and all 1,020 previously published assessment parts retain their original IDs, wording, choices, numeric answers, marks and schemes. New questions append after old unit-check parts so stored answers and existing assignments keep their meaning. Slide positions, word-card ratings and assessed answers use separate Maths course keys. A regression fixture in the shared platform tests checks the previous assessment contract.

Maintain original concept content in scripts/content.py and scripts/revision.py. Calculation-first worked examples for all 144 concepts are authored in scripts/worked_examples.py; keep assessment content unchanged when editing them. The department route and lesson ordering are in scripts/teaching_order.py. The supplementary content bank is in scripts/white_rose.py; new yearly reviews are in scripts/route_papers.py. The review_skills and assessment_skills properties, frozen in scripts/assessment_order.json, preserve every existing unit-check question index while skills controls the visible lesson order. The teaching_source property records the department source. The coverage.json file records the mapping and paper samples.

Rebuild with python scripts/build.py, then run node ../ALevelPhysics/platform/scripts/build-catalogs.cjs KS3Maths from this checkout alongside the other subject repositories. The resulting catalogue has 316 activity pages and 1,749 assessed question parts. Shared account, assignment and marking assets are maintained in the ALevelPhysics platform repository. Preview with a local HTTP server and verify desktop and phone layouts before publishing.
