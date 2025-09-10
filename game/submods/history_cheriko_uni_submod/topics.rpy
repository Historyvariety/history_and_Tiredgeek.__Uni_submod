#Silly Faces
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="hv_c_fav_study",
            category=["School"], # list of categories this topic belongs in (These are automatically capitalized)
            prompt="Favorite Subject", # button text
            random=True
        )
    )

label hv_c_fav_study:
    m 1eua "Enter text here"
return
