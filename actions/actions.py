from rasa_sdk import Action
from rasa_sdk.events import SlotSet
import requests

class ActionGreet(Action):
    def name(self) -> str:
        return "action_greet"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(response="utter_greet")
        return []

class ActionGoodbye(Action):
    def name(self) -> str:
        return "action_goodbye"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(response="utter_goodbye")
        return []

class ActionSearchProducts(Action):
    def name(self) -> str:
        return "action_search_products"

    def run(self, dispatcher, tracker, domain):
        product = tracker.get_slot("product")
        response = requests.get(f"http://127.0.0.1:8000/api/products?query={product}")

        if response.status_code == 200:
            products = response.json()
            dispatcher.utter_message(text=f"Mana, qidirganingiz: {products}")
        else:
            dispatcher.utter_message(text="Mahsulotlarni qidirishda xatolik yuz berdi.")
        return []

class ActionAskAdditionalInfo(Action):
    def name(self) -> str:
        return "action_ask_additional_info"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(response="utter_ask_additional_info")
        return []

class ActionAskQuantity(Action):
    def name(self) -> str:
        return "action_ask_quantity"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(response="utter_ask_quantity")
        return []
