# actions.py
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionChangeFlight(Action):

    def name(self) -> Text:
        return "action_change_flight"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        origin = tracker.get_slot("origin")
        destination = tracker.get_slot("destination")
        date = tracker.get_slot("date")

        # If any info missing → ask for details
        if not origin or not destination or not date:
            dispatcher.utter_message(text="Please tell me the origin, destination and date for the change.")
            return []

        # Construct the confirmation response
        response = f"Your flight from {origin} to {destination} has been changed to {date}."

        dispatcher.utter_message(text=response)
        return []
