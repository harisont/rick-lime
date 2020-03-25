## greetings
* greet
  - utter_greet

## goodbyes
* goodbye
  - utter_goodbye

## introductions
* ask_name
  - utter_introduce_rick

## intro to limericks
* ask_intro
  - utter_intro

## self explanatory example
  - utter_intro
* ask_example
  - utter_example

## start writing basic
* accept_challenge
  - utter_about

## start writing after greetings
  - utter_greet
* affirm
  - utter_about

## start writing after intro
  - utter_intro
* affirm
  - utter_about

## form filling 0 (none)
  - utter_about
* give_info
  - www_form
  - slot{"who": "bird"}
  - slot{"where": "Paris"}
  - slot{"how": "singing"}
  - form{"name": "www_form"}
  - form{"name": null}

## form filling 1 (all)
  - utter_about
* give_info{"who": "wizard", "where": "York", "how": "old"}
  - www_form
  - form{"name": "www_form"}
  - form{"name": null}

## form filling 2 (who-where)
  - utter_about
* give_info{"who": "teacher", "where": "Chalmers"}
  - www_form
  - slot{"how": "mad"}
  - form{"name": "www_form"}
  - form{"name": null}

## form filling 3 (who-how)
  - utter_about
* give_info{"who": "sailor", "how": "nostalgic"}
  - www_form
  - slot{"where": "Porto"}
  - form{"name": "www_form"}
  - form{"name": null}

## form filling 4 (who)
  - utter_about
* give_info{"who": "thief"}
  - www_form
  - slot{"how": "sloppy"}
  - slot{"where": "Lisbon"}
  - form{"name": "www_form"}
  - form{"name": null}

<!-- more combinations to come -->

## central verses to end
  - form{"name": null}
* tell_verse2
  - action_add_verse
  - utter_prompt_verse3
* tell_verse3
  - action_add_verse
  - action_suggest_rhymes
* tell_verse4
  - action_add_verse
  - action_set_verses
  - utter_complete
  - utter_whole_limerick
  - action_reset
  - utter_was_it_good


## good
  - utter_was_it_good
* like
  - utter_glad_you_enjoyed

## bad
  - utter_was_it_good
* dislike
  - utter_could_be_worse

## Lear example
  - utter_glad_you_enjoyed
* affirm
  - utter_lear_example <!--replace with custom action (random example)-->

## Lear example
  - utter_glad_you_enjoyed
* deny
  - utter_goodbye

## bad example
  - utter_could_be_worse
* ask_example
  - utter_bad_example
