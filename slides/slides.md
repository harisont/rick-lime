---
title: Rick Lime - a nonsense poetry writing assistant
subtitle: Dialogue System course project, A.Y. 2019-2020
author: Arianna Masciolini
theme: mhthm
---

# Introducing Rick Lime
- helps writing __limericks__ \pause
  - very short and constrained form of nonsense poetry
    - AABBA \pause
  - not a competitive game but creative/entertaining activity \pause
- automatically generates the opening and closing verses based on user input \pause
- helps with rhymes \pause
- _speaks_ in rhymes!

# Technicalities
- ~~prototype only runs in the __RASA shell__~~ (actually works as a Telegram bot too)\pause
  - ~~meant to be a __Telegram bot__, but~~ the documentation is extremely unclear \pause
    - RASA installation disrupted several times in attempts \pause
  - also tried __Aimybox__, but realized it would be problematic for the presentation \pause
- rhymes suggestions fetched from an online database \pause
  - queries via __datamuse__, a word-finding query engine

# Relation to course contents
- theoretical concepts (partially supported):
  - over-answering
  - other-answering \pause
- custom actions
  - `action_add_verse`
  - `action_set_verses`
  - `action_suggest_rhymes` \pause
- forms
  - `www_form`

# Implementation challenges
- rhymes are not orthographically defined in English \pause
  - solution: "trust" the online database \pause
- hard-to-generalize slot values (entire verses and adjectives in particular, places seem to be more easily recognizable) \pause
  - adjectives: only solution seems to consists in adding more data in `nlu.md`
    - spacy and other pretrained embeddings do not help \pause
  - trick for verses: save entire user utterances, then set slots manually

# Future work
- make the assistant more stable (more training data, more robust actions) \pause
- better error handling \pause
- add possibility to use two different adjectives for the first and last verse, like in some variants of limerick \pause
- choose article (a/an) according to word \pause
- make it possible to modify verses after the poem is complete \pause
- ~~turn into Telegram bot~~ (done!) \pause
- ...
