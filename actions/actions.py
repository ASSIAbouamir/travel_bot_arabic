from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker, FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict
from rasa_sdk.events import SlotSet

# === Recherche de Vols ===
class ActionSearchFlights(Action):
    def name(self) -> Text:
        return "action_search_flights"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        ville_depart = tracker.get_slot("ville_depart")
        ville_destination = tracker.get_slot("ville_destination")
        date_depart = tracker.get_slot("date_depart")

        flights = [
            {
                "airline": "الخطوط السعودية",
                "price": 950,
                "departure": "08:00",
                "arrival": "10:00",
                "duration": "2 ساعات"
            },
            {
                "airline": "طيران ناس",
                "price": 750,
                "departure": "12:00",
                "arrival": "14:15",
                "duration": "2 ساعات و15 دقيقة"
            },
            {
                "airline": "طيران أديل",
                "price": 620,
                "departure": "18:30",
                "arrival": "20:45",
                "duration": "2 ساعات و15 دقيقة"
            }
        ]

        if not flights:
            dispatcher.utter_message(text="عذرًا، لم يتم العثور على رحلات لخياراتك.")
            return []

        dispatcher.utter_message(text=f"🔍 تم العثور على رحلات من {ville_depart} إلى {ville_destination} في {date_depart}:\n")

        for i, flight in enumerate(flights, 1):
            message = (
                f"✈️ الخيار {i}: {flight['airline']}\n"
                f"💰 السعر: {flight['price']} ريال\n"
                f"⏰ الوقت: {flight['departure']} - {flight['arrival']}\n"
                f"🕐 المدة: {flight['duration']}\n"
            )
            dispatcher.utter_message(text=message)

        dispatcher.utter_message(text="أي خيار تفضل؟ اكتب رقم الخيار من فضلك 🎯")
        return [SlotSet("type_reservation", "vol")]


# === Recherche d'Hôtels ===
class ActionSearchHotels(Action):
    def name(self) -> Text:
        return "action_search_hotels"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        ville_hotel = tracker.get_slot("ville_hotel")

        hotels = [
            {
                "name": "فندق الفيصلية",
                "stars": "5 نجوم",
                "price": "850 ريال/ليلة",
                "location": "وسط المدينة",
                "rating": "4.8/5"
            },
            {
                "name": "منتجع الشاطئ الذهبي",
                "stars": "4 نجوم",
                "price": "650 ريال/ليلة",
                "location": "الكورنيش",
                "rating": "4.5/5"
            },
            {
                "name": "فندق النخيل",
                "stars": "3 نجوم",
                "price": "400 ريال/ليلة",
                "location": "المطار",
                "rating": "4.2/5"
            }
        ]

        dispatcher.utter_message(text=f"🏨 تم العثور على فنادق في {ville_hotel}:\n")

        for i, hotel in enumerate(hotels, 1):
            message = (
                f"🏨 الخيار {i}: {hotel['name']}\n"
                f"⭐ التصنيف: {hotel['stars']}\n"
                f"💰 السعر: {hotel['price']}\n"
                f"📍 الموقع: {hotel['location']}\n"
                f"⭐ التقييم: {hotel['rating']}\n"
            )
            dispatcher.utter_message(text=message)

        dispatcher.utter_message(text="أي فندق تفضل؟ اكتب رقم الخيار من فضلك 🎯")
        return [SlotSet("type_reservation", "hotel")]


# === Confirmation de la réservation selon type_reservation ===
class ActionConfirmReservation(Action):
    def name(self) -> Text:
        return "action_confirm_reservation"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        type_reservation = tracker.get_slot("type_reservation")

        if type_reservation == "vol":
            dispatcher.utter_message(text=(
                "📩 نود إعلامكم بأنه تم إتمام تأكيد حجز رحلتكم بنجاح. "
                "سيتم إرسال تفاصيل الحجز إلى بريدكم الإلكتروني قريبًا. "
                "شكرًا لاختياركم خدماتنا، ونتمنى لكم رحلة آمنة ومريحة ✈️."
            ))
        elif type_reservation == "hotel":
            dispatcher.utter_message(text=(
                "📩 نود إعلامكم بأنه تم إتمام تأكيد حجز الفندق الخاص بكم بنجاح. "
                "سيتم إرسال تفاصيل الحجز إلى بريدكم الإلكتروني قريبًا. "
                "شكرًا لاختياركم خدماتنا، ونتمنى لكم إقامة هانئة وممتعة 🏨."
            ))
        else:
            dispatcher.utter_message(text=(
                "📩 نود إعلامكم بأنه تم تأكيد حجزكم بنجاح. "
                "سيتم إرسال تفاصيل الحجز إلى بريدكم الإلكتروني قريبًا. "
                "شكرًا لاختياركم خدماتنا، ونتطلع لخدمتكم في المستقبل."
            ))

        return []

# === Action pour changer les options ===
class ActionChangeOptions(Action):
    def name(self) -> Text:
        return "action_change_options"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="تم تعديل خياراتك بنجاح! ✅ إليك البدائل الجديدة:")
        return []

# === Validation du formulaire de vol ===
class ValidateFlightForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_flight_form"

    def validate_ville_depart(self, slot_value: Any, dispatcher: CollectingDispatcher,
                               tracker: Tracker, domain: DomainDict) -> Dict[Text, Any]:
        if slot_value and len(slot_value) > 1:
            return {"ville_depart": slot_value}
        dispatcher.utter_message(text="من فضلك أدخل مدينة مغادرة صحيحة")
        return {"ville_depart": None}

    def validate_ville_destination(self, slot_value: Any, dispatcher: CollectingDispatcher,
                                   tracker: Tracker, domain: DomainDict) -> Dict[Text, Any]:
        if slot_value and len(slot_value) > 1:
            return {"ville_destination": slot_value}
        dispatcher.utter_message(text="من فضلك أدخل وجهة صحيحة")
        return {"ville_destination": None}

# === Validation du formulaire d'hôtel ===
class ValidateHotelForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_hotel_form"

    def validate_ville_hotel(self, slot_value: Any, dispatcher: CollectingDispatcher,
                              tracker: Tracker, domain: DomainDict) -> Dict[Text, Any]:
        if slot_value and len(slot_value) > 1:
            return {"ville_hotel": slot_value}
        dispatcher.utter_message(text="من فضلك أدخل مدينة صحيحة للفندق")
        return {"ville_hotel": None}
