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
  - utter_was_it_good <!--provisory, just for testing-->

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

## form filling 1 (all)
  - utter_about
* give_info{"who": "wizard", "where": "York", "how": "old"}
  - www_form

## form filling 2 (who-where)
  - utter_about
* give_info{"who": "teacher", "where": "Chalmers"}
  - www_form

## form filling 3 (who-how)
  - utter_about
* give_info{"who": "sailor", "how": "nostalgic"}
  - www_form

## form filling 4 (who)
  - utter_about
* give_info{"who": "Robert"}
  - www_form

<!-- more combinations to come -->

## www_form path
  - www_form
  - form{"name": "www_form"}
  - form{"name": null}

## second verse path
  - form{"name": null}
* tell_second_verse

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
