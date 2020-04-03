# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/

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

from utils import mail

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


    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:

        """A dictionary to map required slots to
            - an extracted entity
            - intent: value pairs
            - a whole message
            or a list of them, where a first match will be picked"""

        return {
            "email": [self.from_entity(entity='business_email'),
                      self.from_text(intent="inform")],
            "person_name": [self.from_entity(entity='person_name'),
                      self.from_text(intent="inform")],
            "message": [self.from_text()]}


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

        # envoi de l'email
        succes = mail(message, person_name, email)
        if succes is True:
            dispatcher.utter_message("Merci, votre message a bien été envoyé")
            print("message enregistré :", message)
        else:
            dispatcher.utter_message("Oups, le message n'a pas pu être transmis : réessayez plus tard")

        return []