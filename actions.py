from typing import Any, List, Text, Dict

from rasa_sdk import Tracker
from rasa_sdk.forms import FormAction
from rasa_sdk.executor import CollectingDispatcher

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
        dispatcher.utter_message(template="utter_firstverse")
        return []
