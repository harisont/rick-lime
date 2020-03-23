from typing import Any, List, Text, Dict
import datamuse

from rasa_sdk import Tracker, Action
from rasa_sdk.forms import FormAction
from rasa_sdk.executor import CollectingDispatcher

def get_rhymes(word):
    '''
    Given a word, it queries the a rhymes database to get a list of 5
    words with similar endings.
    '''
    api = datamuse.Datamuse()
    response = api.words(rel_rhy=word, max=5)
    return list(map(lambda dict: dict["word"], response))

def format_rhymes(rhymes_list):
    '''
    Formats a list of words as a string of comma-separated items.
    '''
    return ", ".join(rhymes_list) # TODO: handle empty list

class WwwForm(FormAction):

    def name(self):
        return "www_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return ["who", "where", "how"]

    def slot_mappings(self) -> Dict[Text, Any]:
        return {"who": self.from_entity(entity="who", intent=["give_info", "inform_who"]),
                "where": self.from_entity(entity="where", intent=["give_info", "inform_where"]),
                "how": self.from_entity(entity="how", intent=["give_info", "inform_where"])}

    def submit(self,
               dispatcher: CollectingDispatcher,
               tracker: Tracker,
               domain: Dict[Text, Any]) -> List[Dict]:
        dispatcher.utter_message(template="utter_prompt_verse2")
        rhyme_with = tracker.current_slot_values()["where"]
        dispatcher.utter_message(text=format_rhymes(get_rhymes(rhyme_with)))
        return []

class ActionSuggestRhymes(Action):

    def name(self) -> Text:
        return "action_suggest_rhymes"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        rhyme_with = tracker.current_slot_values()["verse3"].split()[-1]
        dispatcher.utter_message(text=format_rhymes(get_rhymes(rhyme_with)))
        dispatcher.utter_message(template="utter_prompt_verse4")
        return []
