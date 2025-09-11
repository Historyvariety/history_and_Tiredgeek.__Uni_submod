# All random and monika/player initated conversations go here
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="hv_c_fav_study",
            category=["School"], # list of categories this topic belongs in (These are automatically capitalized)
            prompt="Class Check in", # button text
            random=True
        )
    )

label hv_c_class_check_in:
    "How are classes? {"So [player] how are classes going lately?" 
    "I know the semester can feel like a rollercoaster—sometimes exciting, sometimes exhausting."
    "Did you know that in Japan, students actually take off their shoes when entering classrooms? It’s meant to keep the learning space clean and focused."
    "I think that’s kind of symbolic too… like leaving behind distractions before you study."
    "Maybe you can make your own little ritual like that—it might help you get into the right mindset."
return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="hv_c_fav_study",
            category=["School"], # list of categories this topic belongs in (These are automatically capitalized)
            prompt="Thoughs About Libraries", # button text
            random=True
        )
    )

label hv_c_library_thoughts:
   "The Library {"You know, I keep thinking about libraries."
   "They’re not just places to borrow books… they’ve always been symbols of knowledge and community."
   "Fun fact: the Library of Alexandria supposedly held over 400,000 scrolls at its peak. Imagine all the ideas stored in one place!"
   "I bet if we studied there together, you’d have to drag me out at closing time, ahaha~"
return
