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
  - utter_about <!-- will be a slot -->

## start writing after greetings
  - utter_greet
* affirm
  - utter_about <!-- will be a slot -->

## start writing after intro
  - utter_intro
* affirm
  - utter_about <!-- will be a slot -->

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
  - utter_lear_example <!--replace with custom action-->

## Lear example
  - utter_glad_you_enjoyed
* deny
  - utter_goodbye

## bad example
  - utter_could_be_worse
* ask_example
  - utter_bad_example
