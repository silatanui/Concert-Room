from pymongo import MongoClient
from datetime import datetime

from concertRoom import ConcertRoom

def main():
    # Connect to MongoDB
    client = MongoClient('mongodb://localhost:27017/')
    db = client['concert_room']
    
    # Create the 'concert_rooms' collection
    concert_room = ConcertRoom(db)
    
    """
    1. new event (beginning_of_the_event, end_of_the_event, name, responsible_person_name, responsible_person_phone) (There is only one room, in a given time there can be only one event)
    """
    from datetime import datetime

# Assuming concert_room is an instance of your ConcertRoom class
    concert_room.new_event(
        beginning_of_the_event=datetime(2024, 12, 7, 10, 0, 0), 
        end_of_the_event=datetime(2024, 12, 7, 12, 0, 0), 
        name='Rock Concert', 
        responsible_person_name='Tanui Sila', 
        responsible_person_phone='123456789'
    )

    concert_room.new_event(
        beginning_of_the_event=datetime(2024, 12, 8, 18, 0, 0), 
        end_of_the_event=datetime(2024, 12, 8, 21, 0, 0), 
        name='Jazz Night', 
        responsible_person_name='John Doe', 
        responsible_person_phone='987654321'
    )

    concert_room.new_event(
        beginning_of_the_event=datetime(2024, 12, 9, 20, 0, 0), 
        end_of_the_event=datetime(2024, 12, 9, 23, 0, 0), 
        name='Classical Music Concert', 
        responsible_person_name='Jane Smith', 
        responsible_person_phone='555123456'
    )

    concert_room.new_event(
        beginning_of_the_event=datetime(2024, 12, 10, 14, 0, 0), 
        end_of_the_event=datetime(2024, 12, 10, 16, 0, 0), 
        name='Pop Music Event', 
        responsible_person_name='Alex Brown', 
        responsible_person_phone='555987654'
    )
    
    
    """
    2. print every detail of the event in a given time (date_time)
    """
    print("#" * 80)
    print("Event Details:")
    print("#" * 80)
    concert_room.print_event_details(datetime(2024, 12, 7, 10, 0, 0))
    # print("^" * 80)
    # concert_room.print_event_details(datetime(2024, 12, 7, 12, 0, 0))
    # print("^" * 80)
    # concert_room.print_event_details(datetime(2024, 12, 8, 18, 0, 0))
    # print("^" * 80)
    # concert_room.print_event_details(datetime(2024, 12, 9, 20, 0, 0))
    # print("^" * 80)
    # concert_room.print_event_details(datetime(2024, 12, 10, 14, 0, 0))
    
    
    """
    3. list all events with every detail, order by beginning_of_the_event
    """
    print("#" * 80)
    print(f"List all events with every detail")
    print("#" * 80)
    concert_room.list_all_events()
    
    
    """
    4. create ticket type (name, price, description)
    """
    concert_room.create_ticket_type('VIP', 100, 'VIP ticket for the concert')
    concert_room.create_ticket_type('General Admission', 50, 'General Admission ticket for the concert')
    concert_room.create_ticket_type('Child', 20, 'Child ticket for the concert')
    concert_room.create_ticket_type('Senior', 70, 'Senior ticket for the concert')
    concert_room.create_ticket_type('Special Event', 150, 'Special Event ticket for the concert')
    
    
    """
    5. list ticket types
    """
    print("#" * 80)
    print("List ticket types:")
    print("#" * 80)
    concert_room.list_ticket_types()
    
    
    """
    6. a guest buys a ticket (email, name, birth_date, gender, ticket_type) (a guest can buy only one ticket)
    """
    concert_room.buy_ticket(
        email='john.doe@example.com',
        name='John Doe',
        birth_date=datetime(1990, 1, 1),
        gender='Male',
        ticket_type='VIP'
    )
    
    concert_room.buy_ticket(
        email='jane.smith@example.com',
        name='Jane Smith',
        birth_date=datetime(1985, 12, 31),
        gender='Female',
        ticket_type='General Admission'
    )
    
    concert_room.buy_ticket(
        email='alex.brown@example.com',
        name='Alex Brown',
        birth_date=datetime(1995, 7, 15),
        gender='Male',
        ticket_type='Child'
    )
    
    concert_room.buy_ticket(
        email='sarah.wilson@example.com',
        name='Sarah Wilson',
        birth_date=datetime(1992, 3, 20),
        gender='Female',
        ticket_type='Senior'
    )
    
    concert_room.buy_ticket(
        email='emily.davis@example.com',
        name='Emily Davis',
        birth_date=datetime(1998, 5, 25),
        gender='Female',
        ticket_type='Special Event'
    )
    
    """
    7. list of the guests
    """
    print("#" * 80)
    print("List of Guests:")
    print("#" * 80)
    concert_room.list_guests()
    
    """
    8. a guest likes an event (email, event) (a guest can like an event only one time)
    """
    concert_room.like_event(
        email='john.doe@example.com',
        event='Rock Concert'
    )
    concert_room.like_event(
        email='john.doe@example.com',
        event='Classical Music Concert'
    )
    concert_room.like_event(
        email='jane.smith@example.com',
        event='Rock Concert'
    )
    concert_room.like_event(
        email='alex.brown@example.com',
        event='Rock Concert'
    )
    concert_room.like_event(
        email='jane.smith@example.com',
        event='Jazz Night'
    )
    concert_room.like_event(
        email='alex.brown@example.com',
        event='Classical Music Concert'
    )
    
    concert_room.like_event(
        email='sarah.wilson@example.com',
        event='Pop Music Event'
    )
    concert_room.like_event(
        email='alex.brown@example.com',
        event='Pop Music Event'
    )
    concert_room.like_event(
        email='emily.davis@example.com',
        event='Pop Music Event'
    )
    
    concert_room.like_event(
        email='emily.davis@example.com',
        event='Special Event'
    )
    
    """
    9. list of the events order by number of likes descending
    """
    print("#" * 80)
    print("List of Events Order by Number of Likes Descending:")
    print("#" * 80)
    concert_room.list_events_by_likes()
    
    
    """
    10. list the events which is liked by a guest (email)
    """
    print("#" * 80)
    print("List of the events which is liked by a guest (john.doe@example.com)")
    print("#" * 80)
    concert_room.list_events_by_guest(email= 'john.doe@example.com')
    
    
if __name__ == '__main__':
    main()
    
    
    
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
