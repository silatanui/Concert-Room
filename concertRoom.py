
class ConcertRoom():
    def __init__(self, db):
        self.db = db
        self.event = self.db.event  # Reference to the 'event' collection in MongoDB
        
    """
    1. new event (beginning_of_the_event, end_of_the_event, name, responsible_person_name, responsible_person_phone) 
    (There is only one room, in a given time there can be only one event)
    """
    def is_event_added(self, beginning_of_the_event, end_of_the_event):
        # Check if there is an overlapping event in the same time range
        result = self.db.event.find_one({
            '$or': [
                {'beginning_of_the_event': {'$lt': end_of_the_event}, 'end_of_the_event': {'$gt': beginning_of_the_event}}
            ]
        })
        return result is not None
    
    def new_event(self, beginning_of_the_event, end_of_the_event, name, responsible_person_name, responsible_person_phone):
        if self.is_event_added(beginning_of_the_event, end_of_the_event):
            print("Event already exists during this time.")
            return
        
        self.db.event.insert_one({
            'beginning_of_the_event': beginning_of_the_event,
            'end_of_the_event': end_of_the_event,
            'name': name,
            'responsible_person_name': responsible_person_name,
            'responsible_person_phone': responsible_person_phone
        })
        print("Event added successfully.")
        
    """
    2. print every detail of the event in a given time (date_time)
    """
    def print_event_details(self, date_time):
        result = self.db.event.find_one({'beginning_of_the_event': date_time})
        if result is None:
            print("No event found for the given date.")
            return
        

        print(f"Name: {result['name']}")
        print(f"Beginning of the event: {result['beginning_of_the_event']}")
        print(f"End of the event: {result['end_of_the_event']}")
        print(f"Responsible person name: {result['responsible_person_name']}")
        print(f"Responsible person phone: {result['responsible_person_phone']}")
        
        
        
    """
    3. list all events with every detail, order by beginning_of_the_event
    """
    def list_all_events(self):
        result = self.db.event.find().sort('beginning_of_the_event')
        for event in result:
            print(f"Name: {event['name']}")
            print(f"Beginning of the event: {event['beginning_of_the_event']}")
            print(f"End of the event: {event['end_of_the_event']}")
            print(f"Responsible person name: {event['responsible_person_name']}")
            print(f"Responsible person phone: {event['responsible_person_phone']}")
            print("^" * 80)
            
    """
    4. create ticket type (name, price, description)
    """
    # Check if the ticket type is already in the database
    def is_ticket_type_added(self, name):
        result = self.db.ticket_types.find_one({'name': name})
        return result is not None
    
    def create_ticket_type(self, name, price, description):
        if self.is_ticket_type_added(name):
            print("Ticket type already exists.")
            return
        
        self.db.ticket_types.insert_one({
            'name': name,
            'price': price,
            'description': description
        })
        print("Ticket type added successfully.")
        
    
    """
    5. list ticket types
    """
    def list_ticket_types(self):
        result = self.db.ticket_types.find()
        for ticket_type in result:
            print(f"Name: {ticket_type['name']}")
            print(f"Price: {ticket_type['price']}")
            print(f"Description: {ticket_type['description']}")
            print("^" * 80)
    
    """
    6. a guest buys a ticket (email, name, birth_date, gender, ticket_type) (a guest can buy only one ticket)
    """
    # Check if the guest is already in the database
    def is_guest_added(self, email):
        result = self.db.guests.find_one({'email': email})
        return result is not None
    
    def buy_ticket(self, email, name, birth_date, gender, ticket_type):
        if self.is_guest_added(email):
            print("Guest already exists.")
            return
        
        # Check if the ticket type exists
        ticket_type_result = self.db.ticket_types.find_one({'name': ticket_type})
        if ticket_type_result is None:
            print("Ticket type does not exist.")
            return
        
        self.db.guests.insert_one({
            'email': email,
            'name': name,
            'birth_date': birth_date,
            'gender': gender,
            'ticket_type': ticket_type
        })
        print("Ticket bought successfully.")
        
    """ 
    7. list of the guests
    """
    def list_guests(self):
        result = self.db.guests.find()
        for guest in result:
            print(f"Email: {guest['email']}")
            print(f"Name: {guest['name']}")
            print(f"Birth date: {guest['birth_date']}")
            print(f"Gender: {guest['gender']}")
            print(f"Ticket type: {guest['ticket_type']}")
            print("^" * 80)
            
    """
    8. a guest likes an event (email, event) (a guest can like an event only one time)
    """
    # Check if the guest has already liked the event
    def is_event_liked(self, email, event):
        result = self.db.guests.find_one({'email': email, 'liked_events': event})
        return result is not None
    
    def like_event(self, email, event):
        if not self.is_guest_added(email):
            print("Guest does not exist.")
            return
        
        if self.is_event_liked(email, event):
            print("Guest has already liked this event.")
            return
        
        self.db.guests.update_one({'email': email}, {
            '$push': {
                'liked_events': event
            }
        })
        
        print("Event liked successfully.")
        
        
    """
    9. list the events order by number of likes descending 
    """
    def list_events_by_likes(self):
        # Use aggregate function
        pipeline = [
                { 
                    '$unwind': '$liked_events' },
                {
                    '$group': {
                        '_id': '$liked_events',
                        'NumberofLikes': { 
                            '$sum': 1 }
                }
                },
                { 
                    '$sort': { 'NumberofLikes': -1 } 
                }
            ]
        
        result = self.db.guests.aggregate(pipeline)
        for event in result:
            print(f"Event: {event['_id']}")
            print(f"Number of likes: {event['NumberofLikes']}")
            print("^" * 80)
            
    """
    10. list the events which is liked by a guest (email)
    """
    def list_events_by_guest(self, email):
        result = self.db.guests.find_one({'email': email, 'liked_events': {'$exists': True}})
        if result is None:
            print("Guest does not exist or has not liked any events.")
            return
        
        print("Liked events:")
        liked_events = result.get('liked_events')
        for event in liked_events:
            print(f"Event: {event}")
            print("^" * 80)
      
"""
Concert room

1. new event (beginning_of_the_event, end_of_the_event, name, responsible_person_name, responsible_person_phone) (There is only one room, in a given time there can be only one event)
2. print every detail of the event in a given time (date_time)
3. list all events with every detail, order by beginning_of_the_event
4. create ticket type (name, price, description)
5. list ticket types 
6. a guest buys a ticket (email, name, birth_date, gender, ticket_type) (a guest can buy only one ticket)
7. list of the guests
8. a guest likes an event (email, event) (a guest can like an event only one time)
9. list the events order by number of likes descending 
10. list the events which is liked by a guest (email)

"""