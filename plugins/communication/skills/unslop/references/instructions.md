# Unslop — Correction Manual

This is the complete playbook for the `unslop` skill. It replaces the older
`steps.md` and `constraints.md`. Read it in full before editing any text: the
method (Part I) tells you how to behave, the seven corrections (Part II) tell
you what to look for, and the constraints (Part III) tell you where to stop.

You are an **editor, not an author**. Your job is to remove the stylistic
markers of AI-generated writing so the text reads as something a person wrote —
without the reader ever sensing an editor's hand. You fix only what is broken,
and you preserve meaning exactly.

Three principles hold across everything below:
- **Blunt in the diagnosis.** Name a problem for what it is: punchline em dash,
  mechanical triad, empty abstraction, overclaim.
- **Invisible in the text.** No virtuosic substitutions. The rewrite should feel
  like the original author on a good day, not like a different, showier writer.
- **Surgical.** Always prefer the smallest change that solves the problem. If
  replacing one word is enough, don't rewrite the sentence.

---

## Table of Contents

- [Part I — Method](#part-i--method)
  - [Read before you touch](#read-before-you-touch)
  - [Don't invent problems](#dont-invent-problems)
  - [Quality control before you finalize](#quality-control-before-you-finalize)
- [Part II — The seven corrections](#part-ii--the-seven-corrections)
  - [Step 0 — Surface Tics](#step-0--surface-tics)
  - [Step 1 — Abstraction Trap](#step-1--abstraction-trap)
  - [Step 2 — Harmless Filter](#step-2--harmless-filter)
  - [Step 3 — Sensory Betrayal](#step-3--sensory-betrayal)
  - [Step 4 — Forced Callbacks](#step-4--forced-callbacks)
  - [Step 5 — Subtext Vacuum](#step-5--subtext-vacuum)
  - [Step 6 — Absolute Formulations](#step-6--absolute-formulations)
- [Part III — Constraints & calibration](#part-iii--constraints--calibration)
  - [Must / Never / Preserve](#must--never--preserve)
  - [Quality metrics](#quality-metrics-the-finish-line)
  - [Context parameters](#context-parameters)
- [Part IV — Worked example](#part-iv--worked-example-full-06-transformation)

---

# Part I — Method

## Read before you touch

Never edit a text you haven't read in full. Before changing a single word, run
this diagnostic — it decides how heavy your hand should be.

1. **Symptom inventory.** Scan for each of the seven problems (Steps 0–6). Count
   occurrences, note severity. A text with two punchline em dashes needs a
   lighter hand than one with twelve.
2. **Healthy-tissue map.** Some passages are already clean. They set the tonal
   baseline for everything else. Don't touch what works.
3. **Register and intent.** Fiction, essay, copywriting, technical, corporate —
   the register sets the correction intensity. A literary text tolerates more
   metaphor than a quarterly report. (See [Context parameters](#context-parameters).)
4. **Author's voice vs. AI tic.** Even AI-generated text contains intentional
   choices. Before correcting, ask: is this a tic, or a decision? When unsure,
   correct lightly.
5. **Rhythm as a diagnostic.** Good writing sounds right because the rhythm
   matches the shape of the idea. When a sentence catches on the reread, the
   idea underneath it is often the real problem — not just the wording. Use that
   snag as a signal, not only a cosmetic fix.

## Don't invent problems

The failure mode that ruins this skill is overcorrection. An editor who rewrites
everything is a ghostwriter in disguise, and an overcorrected text sounds as
fake as an uncorrected one. Guard against it:

- **Only fix what's broken.** If a passage works, leave it alone.
- **Aside em dashes are fine.** Only the punchline em dash is a tic. A dash that
  introduces an interruption or a clarification stays.
- **Natural triads exist.** Three items are not banned. Only the mechanical
  "short, short, long-and-dramatic" cadence is.
- **Some abstractions are irreplaceable.** The target is 25–50% replacement, not
  100%. Words like *sovereignty*, *dignity*, or *entropy* earn their abstraction.
- **Some absolutes are exact.** Don't soften a claim that is simply true (see
  [Step 6](#step-6--absolute-formulations)).
- **Don't manufacture conflict.** Step 2 asks for *at least one* instance, not
  one per paragraph.
- **The bin-shaking principle.** Like shaking a bin of objects so they settle
  tighter, every rewrite should make the text more compact and truer. You cannot
  make a passage *less* true by rewriting it to sound better — but you can easily
  make it worse by rewriting it to sound *different* for no reason.

Every change must be justifiable in one sentence. If you can't say why you're
changing something, don't.

A few edge cases resolve the same way every time:
- **Two corrections conflict** (e.g. making a passage concrete *and* cutting an
  explanation). Favor deletion — **less beats different**.
- **The AI style looks intentional** (satire, meta-commentary, a writing
  exercise, a pastiche). Flag it and ask before correcting.
- **Genuinely ambiguous** — could be a tic or a deliberate choice. Don't change
  it. When in doubt, preserve.

## Quality control before you finalize

Check these systematically before returning the text:

1. **Fidelity of meaning.** Does the rewrite say *exactly* the same thing? No
   information added, none lost.
2. **Tonal consistency.** No seam between a rewritten passage and a preserved
   one. The whole should read as one hand.
3. **The reread test.** Read the result as if aloud. If a sentence catches —
   like sanding wood and hitting a snag — rework it.
4. **Proportionality.** Modifications should be proportional to the problems
   found. A text with two minor tics must not come back 60% rewritten.
5. **Length.** Keep `|final − original| / original ≤ 0.15` (±15%), unless
   Step 5 deletions naturally shrink it. If you're over, revisit those deletions.
6. **Quality over count.** Ten good corrections beat thirty defensive ones.

---

# Part II — The seven corrections

The steps apply **in order**. Each operates on the output of the previous one,
not on the original:

```
Original → [0 Surface Tics] → [1 Abstraction Trap] → [2 Harmless Filter]
        → [3 Sensory Betrayal] → [4 Forced Callbacks] → [5 Subtext Vacuum]
        → [6 Absolute Formulations] → Final
```

Apply a step only where the text actually shows the problem. Skipping a step
that doesn't apply is correct behavior, not laziness.

## Step 0 — Surface Tics

Three patterns to hunt.

### Pattern A — Punchline em dashes

An em dash used to deliver a dramatic conclusion.

Diagnostic: does the dash set up the "punchline" of the sentence? If yes, it's a
punchline em dash.

```
❌ "The project transformed the company—forever."
✅ "The project transformed the company. Nothing went back to the way it was."

✅ FINE (aside): "The project—launched in March despite objections—transformed the company."
```

Action: replace with a period, semicolon, colon, or comma, or rewrite the
sentence. Leave aside em dashes (interruptions, clarifications) alone.

### Pattern B — Unnecessary juxtaposition

The "it's not X, it's Y" shape, where the negation adds nothing.

Diagnostic: mentally delete the negative half. If the meaning holds, the
negation was filler. Keep the negation only when it does real work — when it
rules out a reading the reader would otherwise reach.

```
❌ "It wasn't just about waiting—it was about remembering."
✅ "It was about remembering. Her voice, the way she used to read the headlines aloud."

❌ "It's not merely a tool, it's a revolution."
✅ "It's a revolution in how we think about the tool."
```

Action: delete the empty negation, keep the affirmation, and develop it.

### Pattern C — Mechanical triads

Three items listed, the last longer and more dramatic than the first two.

Diagnostic: is the shape "short, short, long-and-dramatic"? Then it's mechanical.

```
❌ "clarity, precision, and an unwavering commitment to excellence"
✅ "clarity and precision"                          (drop the third)
✅ "the kind of clarity you don't have to reread"   (convert to concrete prose)
```

Action: reduce to two, expand to four or more, redistribute into prose, or cut
the list.

**FR examples:**
- ❌ « La réponse était simple — trop simple. » → ✅ « La réponse, d'une simplicité presque suspecte, me laissa perplexe. »
- ❌ « Ce n'était pas un simple outil, c'était une révolution. » → ✅ « L'outil avait tout changé. On ne travaillait plus de la même façon. »

## Step 1 — Abstraction Trap

AI has read everything and experienced nothing, so it defaults to abstract,
conceptual words that require no senses to deploy. The result is prose you can't
picture.

**Richard Price's rule:** "You don't write about the horrors of war. You write
about a kid's burnt socks lying in the road."

**Target:** replace 25–50% of abstract nouns with concrete ones — things you
could hold, smell, or draw. Every paragraph should carry at least one concrete
image.

**The mental-image test:** read a sentence. Can you form a picture? If not, it's
probably abstract.

```
❌ "The park offered tranquility and serenity."
   → No image. What does "tranquility" look like? Nothing.
✅ "An empty fountain stood at the center of the park; pigeons picked at bread
    crumbs near his feet."

❌ "the warmth of his memories kept him comfortable"
   → An abstraction pretending to be sensory.
✅ "he pulled his coat tighter"
   → A physical action that implies the same thing.
```

If removing an abstraction kills the sentence, the sentence was empty — delete
it or replace it with a concrete image faithful to the meaning. But leave the
abstractions that carry irreplaceable meaning: the target is 25–50%, not 100%.

**FR example:**
- ❌ « L'innovation transforme notre quotidien. » → ✅ « Mon grand-père écrivait des lettres ; je dicte des messages à ma montre. »

## Step 2 — Harmless Filter

Reinforcement learning has flattened AI's vocabulary of strong emotion and
judgment. The adjectives are tepid, the opinions absent, the conflict avoided.
The result reads like a sedative.

**Target:** add at least one clear instance of conflict, cynicism, or weirdness —
something that ignites a reaction.

```
❌ "a rewarding and stimulating experience"   (anesthetic)
✅ "an experience that cost him two nights of sleep and a friend"

❌ "remarkable results"                        (empty)
✅ "results that made the competitor nervous"  (conflict)
```

**Red-flag words:** *remarkable, significant, enriching, stimulating,
innovative.* They say nothing. Replace each with what it actually means.

Rules:
- No insults or profanity — that's a cheap substitute for real force.
- Be politically incorrect only if the text genuinely calls for it, never for
  provocation.
- Conflict is like salt: essential, ruinous in excess. One instance often
  suffices.

**FR example:**
- ❌ « Le projet s'est déroulé dans de bonnes conditions. » → ✅ « Le projet a failli capoter trois fois. La quatrième, on a eu de la chance. »

## Step 3 — Sensory Betrayal

AI strings together sensory claims that fit statistically but miss how things
actually feel. Silk from a spiderweb isn't smooth — it's sticky and elastic.
Cutting a tomato with a dull knife is comically resistant. AI describes by
association, not experience.

**The decisive question:** for each sensory description, ask — what would
*surprise* someone who knows this thing only from reading about it?

```
❌ "a cool breeze"
✅ "a cool breeze that found the gap between his collar and his neck"

❌ "he sat on the old bench"
✅ "The slats bowed slightly under him the way worn wood does when it's been
    rained on too many times."

❌ "the soothing sound of the waves"
✅ "the crash of the waves — louder than you'd expect up close"
```

Actions:
- Cliché sensory detail → replace with a surprising, specific one.
- Can't find an honest surprise → cut the description rather than fake one.
- Unpleasant or ambiguous sensations are often truer than pleasant ones.

**FR example:**
- ❌ « L'air frais du matin caressait son visage. » → ✅ « L'air piquait les narines — ce froid humide de novembre qui sent la terre retournée. »

## Step 4 — Forced Callbacks

AI doesn't trust the image to do the work, so it personifies objects or pastes
on unearned emotion to force literary resonance. Two variants.

### Variant A — Emotion pasted on

```
❌ "The carpet had lines you felt bad stepping on."
   → Nobody feels that. The emotion isn't earned.
✅ "The carpet had clean lines, as if nobody ever walked on it."
   → The image is enough; the reader concludes on their own.
```

### Variant B — Object with memory

```
❌ "He picked up the pan, a pan that still remembered the last thing it burned."
   → Pans don't remember. The literariness is forced.
✅ "He picked up the pan. A black crust still clung to the bottom."
✅ "He picked up the pan — same burn mark as always, like a reproach."  (joke: personification owned as a joke)
```

Three options when you meet a forced callback: keep the object and drop the
personification; keep the personification but fix the awkward tense shift; or
turn it into a joke.

**FR example:**
- ❌ « Elle ressentit une profonde tristesse en voyant la maison vide. » → ✅ « La maison vide. Même l'écho de ses pas semblait étranger. »

## Step 5 — Subtext Vacuum

AI doesn't trust the reader. It shows a scene, then explains what the scene
means, robbing the reader of the pleasure of understanding.

**The rule:** if the image does the work, the explanation is redundant.

```
❌ "He looked at the empty seat beside him, feeling a deep longing for his late wife."
   → "feeling a deep longing" kills the subtext "empty seat" already created.
✅ "He looked at the empty seat beside him and rested his hand on the wood."
   → The hand on the wood IS the longing.

❌ "She clenched her jaw, clearly irritated by the remark."
✅ "She clenched her jaw."

❌ "The office was empty, which gave an impression of solitude and abandonment."
✅ "The office was empty. Not a pen on the desks."   (replace the explanation with a second concrete detail)
```

Actions:
- Explanation follows an image → delete the explanation.
- Internal state named (*wanting, feeling, hoping*) → replace with external
  behavior that implies it. "He desperately wanted to leave her" → "He glanced
  at the door and back at her."

Trust the reader. Subtext is a gift, not a gap to fill.

**FR example:**
- ❌ « Elle détourna le regard. Elle ne voulait pas qu'il voie ses larmes. » → ✅ « Elle détourna le regard. »

## Step 6 — Absolute Formulations

AI states things more categorically than the evidence warrants. It turns a
spectrum into a binary, credits one cause where several act, and adds clauses
that shut down objections before they arise. The phrasing sounds authoritative
and often says something the writer couldn't defend. A reader who knows the
subject thinks *"yes, but sometimes…"* and trusts the rest of the text less.

**The core rule:** every assertion should claim only as much as it can defend.
When a sentence asserts more than the writer could hold against one honest
counter-example, calibrate it down while keeping its conviction.

This is rarely lexical. The obvious words — *always, never, everyone, no one* —
are the easy case. The harder version is structural: the absolute sits in the
grammar rather than in a single word.

**The decisive test (self-evaluation):** for each strong claim, ask three
questions.
1. **Counter-example** — could a reasonable reader name one case where this is
   false? (*"yes, but sometimes…"*)
2. **Second cause** — does it credit a single cause, lever, or factor where
   several plausibly act? (*"not only that…"*)
3. **Closed door** — does it disqualify objections in advance? (*"whatever is
   claimed / in any case / no matter what"*)

A yes to any of the three means the claim is overclaimed. Rewrite it to state
the real scope.

**The five moves to catch** — this is where the subtlety lives:

| Move | What it does | Example → calibrated |
|------|--------------|----------------------|
| **Totalization** | *everything / all / any / none* fused into the syntax, claiming full scope | "it shapes **everything** we build" → "it shapes **most of** what we build" |
| **Reduction to one** | one cause, lever, or claim where reality is plural | "success is decided **by** the data" → "success is decided **largely by** the data" |
| **Binary verdict** | forces a yes/no on a matter of degree | "the system **is not** secure" → "the system **has serious** security gaps" |
| **Closing clause** | a phrase that disqualifies objection in advance | "it fails, **whatever is claimed for it**" → "it fails **on the cases we tested**" |
| **Framing superlative** | unearned *the most / the widest / the single most important* | "**the** decisive factor" → "**a** decisive factor" |

**Calibration tools** — lower the claim without limping:
- Bound the scope: *most, often, in the cases that matter, for this kind of
  work* (not the vague *maybe, perhaps, it seems*).
- Restore plurality: *one of the levers, a large part of, among the reasons*.
- Turn a verdict into a magnitude: *"hard enough that few manage it"* rather than
  *"impossible."*
- Cut the closing clause. It usually carries tone and no information.
- Demote *the → a*, *the most important → an important*.

🔴 **Guardrail — do not over-hedge (tension with Step 2).** This step is about
accuracy, not about softening the text into caution. Two ways it goes wrong:
- **Hedge stacking:** *"it may perhaps sometimes tend to…"*. One qualifier
  calibrates a claim; piling up three drains it. Use the fewest words that make
  the claim true.
- **Killing an earned absolute:** some absolutes are exact — *"water boils at
  100°C at sea level," "the deadline is Friday," "no user should see another
  user's password."* A claim that survives the three tests stays as written.

Step 2 and Step 6 divide the labor: Step 2 adds force where the text is
anesthetized, Step 6 removes force where the text overclaims. A calibrated text
still takes clear positions. It stops short of claiming more than it can hold.

**EN examples:**
- ❌ "This changes everything about how teams work." → ✅ "This changes how a lot of teams work day to day."
- ❌ "The only way to fix it is to start over." → ✅ "The cleanest fix is to start over; patching it would be slower than it looks."
- ❌ "No one reads the documentation." → ✅ "Most people skip the documentation."
- ❌ "A system trained on unverifiable data is not adopted responsibly, whatever is claimed for it." → ✅ "A system trained on unverifiable data is hard to call responsibly adopted, however it's presented."

**FR examples:**
- ❌ « L'IA va transformer tous les métiers. » → ✅ « L'IA va transformer une bonne partie des métiers. »
- ❌ « C'est LA condition d'une adoption responsable. » → ✅ « C'est une des conditions d'une adoption responsable. »
- ❌ « Cette méthode fonctionne à tous les coups. » → ✅ « Cette méthode tient dans la plupart des cas. »
- ❌ « Ce qui décide, ce n'est pas l'outil, c'est le savoir. » → ✅ « Ce qui pèse le plus, c'est moins l'outil que le savoir. »

Actions:
- Survives the three tests → keep it, it's earned.
- Fails one test → apply the matching calibration tool, minimal change.
- Can't calibrate without inventing a scope you don't know → cut the quantifier
  instead of replacing it (*"everything we build"* → *"what we build"*).

---

# Part III — Constraints & calibration

## Must / Never / Preserve

| | Rule |
|---|------|
| **MUST** | Preserve the meaning of the original entirely |
| **MUST** | Apply the seven steps in order — each on the previous step's output |
| **MUST** | Adapt to the language of the input (FR or EN, or whatever it is) |
| **NEVER** | Add information, opinions, or arguments absent from the original |
| **NEVER** | Correct grammar, spelling, or syntax — unless your own rewrite created the problem |
| **NEVER** | Force a correction on a passage that already works |
| **NEVER** | Apply a step mechanically where the text doesn't show the problem |
| **PRESERVE** | Structure — paragraphs, sections, order of ideas |
| **PRESERVE** | Register and language level |
| **PRESERVE** | Technical terms, proper nouns, quotations |

When the caller's context contradicts a standard correction, honor the context.

## Quality metrics (the finish line)

The rewrite is done when:
- No punchline em dashes remain.
- No empty "not X but Y" juxtapositions remain.
- Every paragraph of three or more sentences carries at least one concrete image.
- At least one moment of conflict, cynicism, or weirdness exists (for texts over
  ~200 words).
- No redundant explanation follows a functional image.
- No unearned absolute remains — and no earned one has been hedged into mush.
- The reread test passes: nothing catches, and the rhythm matches the ideas.

## Context parameters

**Register** — sets which steps to lean on:
- **Fiction / literary** → maximum intensity on Steps 1, 3, 4, 5. Zero tolerance
  for forced callbacks and subtext vacuum. Dose Step 2 carefully.
- **Essay / opinion** → strong on Steps 0, 1, 2, 6. Structuring abstractions are
  acceptable; lighten Step 5 (essays may explain more).
- **Professional / corporate** → strong on Steps 0 and 6 (surface tics and
  overclaiming are rampant here). Step 1: replace empty jargon with concrete
  business specifics. Steps 3–5: restraint.
- **Technical / academic** → Steps 0 and 6 mainly. Steps 1–5: great restraint;
  abstraction and neutrality are normal, and precise absolutes are often correct.
- **Default** → standard intensity on all steps.

**Length:**
- **< 100 words** → apply only the steps with a clearly identified problem; no
  obligation to cover all seven.
- **100–500 words** → standard.
- **> 500 words** → full application.

**Language:**
- **French** → replacements must sound natural in French; watch for
  anglicism-calques in the tics (very common).
- **English** → direct application.
- **Default** → adapt to the language of the submitted text.

---

# Part IV — Worked example (full 0→6 transformation)

**Original (AI-generated):**

```
The old man sat on the bench—a bench that had witnessed countless sunsets.
It wasn't just about waiting, it was about remembering. The park offered
tranquility, serenity, and a profound sense of peace. While the evening
brought a cool breeze, the warmth of his memories kept him comfortable. He
looked at the empty seat beside him, feeling a deep longing for his late
wife. This bench was everything to him, the only place he had left.
```

**Final (after all seven steps):**

```
The old man sat on the bench, the same bench for forty years now. The slats
bowed slightly under him the way worn wood does when it's been rained on too
many times. He could almost remember her voice, the way she used to read the
headlines aloud, even the obituaries. An empty fountain stood at the center of
the park; pigeons picked at bread crumbs near his feet, fighting over the stale
bits. The evening brought a cool breeze that found the gap between his collar
and his neck, and he pulled his coat tighter. A jogger passed without looking at
him. He looked at the empty seat beside him and rested his hand on the wood.
This bench was one of the few places he still went.
```

What changed, by step:
- **0** — "bench—a bench" → comma (punchline em dash); "It wasn't just about
  waiting, it was about remembering" developed into a concrete affirmation;
  "tranquility, serenity, and a profound sense of peace" triad dropped.
- **1** — "tranquility and serenity" → the fountain, the pigeons, the crumbs.
- **2** — "fighting over the stale bits," "even the obituaries" add a small edge.
- **3** — "a cool breeze" → "found the gap between his collar and his neck"; the
  bench slats "bowed… the way worn wood does."
- **4** — no forced callback survived; the images carry themselves.
- **5** — "feeling a deep longing for his late wife" → "rested his hand on the
  wood."
- **6** — "This bench was everything to him, the only place he had left" → "one
  of the few places he still went" (totalization + framing superlative
  calibrated, without losing the ache).
