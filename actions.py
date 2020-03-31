# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

from rasa_sdk.forms import FormAction
from rasa_sdk import Tracker
from rasa_sdk.executor import CollectingDispatcher
from typing import Any, Dict, List, Text, Union, Optional

from rasa_sdk.events import (
    SlotSet,
    UserUtteranceReverted,
    ConversationPaused,
    EventType,
    ActionExecuted,
    UserUttered,
)

class InfoMail (FormAction):
    """Collects sales information and adds it to the spreadsheet"""

    def name(self) -> Text:
        return "info_mail"

    @staticmethod
    def required_slots(tracker) -> List[Text]:
        return [
            "message",
            "business_email",
            "person_name",
        ]

    #def submit(
    #        self,
    #        dispatcher: CollectingDispatcher,
    #        tracker: Tracker,
    #        domain: Dict[Text, Any],
    #    ) -> List[Dict]:
    #    dispatcher.utter_message("Merci, votre message a bien été envoyé")
    #    return []

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:

        """A dictionary to map required slots to
            - an extracted entity
            - intent: value pairs
            - a whole message
            or a list of them, where a first match will be picked"""

        return {
            "email": [self.from_entity(entity='business_email'),
                      self.from_text(intent="inform")],
            "person_name":[self.from_entity(entity='person_name'),
                      self.from_text(intent="inform")],
            "message":[self.from_text()]}


    def submit(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> List[EventType]:
        """Once we have an email, attempt to add it to the database"""

        email = tracker.get_slot("business_email")
        person_name = tracker.get_slot("person_name")
        message = tracker.get_slot("message")
        dispatcher.utter_message("Merci, votre message a bien été envoyé")
        print("message enregistré :", message)
        return []