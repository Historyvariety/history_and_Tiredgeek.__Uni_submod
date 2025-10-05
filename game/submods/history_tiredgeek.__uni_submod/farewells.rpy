#All goodbyes go here
# topic: Club Meeting
init 5 python:
    addEvent(
        Event(
            persistent.farewell_database,
            eventlabel="bye_club_meeting",
            prompt="I’m headed to a club meeting",
            unlocked=True,
            pool=True
        ),
        code="BYE"
    )

label bye_club_meeting:
    m 1sub "Oh, a club meeting! That sounds fun. Make sure you enjoy yourself!"
    m 5hub "I’ll be right here when you get back~"
return "quit"


# topic: Library Study
init 5 python:
    addEvent(
        Event(
            persistent.farewell_database,
            eventlabel="bye_library_study",
            prompt="I’m going to study in the library",
            unlocked=True,
            pool=True
        ),
        code="BYE"
    )

label bye_library_study:
    m 1hub "Off to the library, huh?"
    m 3ekb "Remember to take breaks, don’t overwork yourself."
    m 5hub "I’ll be waiting for you when you return~"
return "quit"


# topic: Study Group
init 5 python:
    addEvent(
        Event(
            persistent.farewell_database,
            eventlabel="bye_study_group",
            prompt="I’m headed to a study group",
            unlocked=True,
            pool=True
        ),
        code="BYE"
    )

label bye_study_group:
    m 3sub "A study group! That sounds productive."
    m 3eub "Remember, teamwork makes everything easier."
    m 2eub "I’ll be waiting when you get back~"
return "quit"


# topic: Lunch
init 5 python:
    addEvent(
        Event(
            persistent.farewell_database,
            eventlabel="bye_lunch",
            prompt="I’m going to grab lunch",
            unlocked=True,
            pool=True
        ),
        code="BYE"
    )

label bye_lunch:
    m 1eub "Ooh, lunch break!"
    m 3eub "Eat something tasty and energizing. I’ll be here when you finish~"
return "quit"


# topic: Run Errands
init 5 python:
    addEvent(
        Event(
            persistent.farewell_database,
            eventlabel="bye_run_errands",
            prompt="I need to run some errands",
            unlocked=True,
            pool=True
        ),
        code="BYE"
    )

label bye_run_errands:
    m 5mtb "Errands can be boring, but necessary."
    m 4ekb "Don’t stress yourself too much! I’ll be right here when you return!"
return "quit"


# topic: Taking You to Class
init 5 python:
    addEvent(
        Event(
            persistent.farewell_database,
            eventlabel="bye_taking_to_class",
            prompt="I'm taking you to class!",
            unlocked=True,
            pool=True
        ),
        code="BYE"
    )

label bye_taking_to_class:
    m 2sub "Wait… you’re taking me to class? That sounds exciting!"
    m 3sub "I’ve never actually been to a university class… this will be fun! I'll go get ready"
return "quit"


# topic: Lecture
init 5 python:
    addEvent(
        Event(
            persistent.farewell_database,
            eventlabel="bye_lecture",
            prompt="I have a lecture",
            unlocked=True,
            pool=True
        ),
        code="BYE"
    )

label bye_lecture:
    m 5ekb "Oh? You have to go to a lecture? Awh, alright! I hope you learn lots of new stuff to tell me about!~"
    m 5hkb "I'll see you in a bit [player]."
return "quit"
