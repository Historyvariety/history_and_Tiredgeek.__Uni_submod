# All random and monika/player initated conversations go here
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="hv_c_class_check_in",
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
            eventlabel="hv_c_library_thoughts",
            category=["School"], # list of categories this topic belongs in (These are automatically capitalized)
            prompt="Thoughts About Libraries", # button text
            random=True
        )
    )

label hv_c_library_thoughts:
   "You know, I keep thinking about libraries..."
   "They’re not just places to borrow books…they’ve always been symbols of knowledge and community."
   "Fun fact: the Library of Alexandria supposedly held over 400,000 scrolls at its peak. Imagine all the ideas stored in one place!"
   "I bet if we studied there together, you’d have to drag me out at closing time, ahaha~"
return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="hv_c_study_breaks",
            category=["School"], # list of categories this topic belongs in (These are automatically capitalized)
            prompt="Study Breaks", # button text
            random=True
        )
    )

label hv_c_study_breaks:
   "Breaks { "So, have you been remembering to take breaks when you study?"
    "I read that your brain processes information best in chunks—about 25 to 50 minutes at a time."
    "It’s called the Pomodoro technique. You work hard, then give yourself a little reward."
    "I could be your timer if you want. Every time the break starts, I’ll remind you to stretch and maybe grab a snack~"
return

# Topic: Favorite Subject / Class Check-in
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="hv_c_fav_study",
            category=["School"],  # Categories are automatically capitalized in MAS
            prompt="Class Check-in",  # Button text
            random=True
        )
    )

label hv_c_fav_study:
    m 1eua "Hey, [player]... do you have a favorite subject this term?"

    menu:
        "Yes":
            m 1hua "Really? That's wonderful!"
            m 3eua "Tell me, which subject is it?"

            menu:
                "Math":
                    m 1sub "Numbers and logic, huh? That really works your brain!"
                    m 3eua "Math is like the language of the universe. I think it's so elegant how everything connects."

                "Science":
                    m 3hub "Science is amazing! There's always more to learn about the world around us."
                    m 1hua "If we studied together, I think I'd love doing little experiments with you, ehehe~"

                "Literature":
                    m 1hub "Oh! Literature! How you're after my heart~"
                    m 1eua "Stories, poems, essays... they're all windows into how people think and feel."
                    m 3hua "It makes me so happy knowing you appreciate it too. That's why we're so perfect together, ehe~"

                "Art":
                    m 1hua "Creative souls like yours make the world so much brighter."
                    m 1eub "I bet whatever you create carries a little piece of you in it. That's really special, you know."

                "Something else":
                    m 1eua "Whatever it is, I hope it keeps you curious and motivated."

        "No":
            m 1eka "That's okay!"
            m 1eka "Not every subject clicks with everyone. Sometimes school can feel more like a chore than an inspiration."
            m 1eub "But who knows? Maybe you'll stumble across a class that really surprises you later on."

        "I'm not sure":
            m 1eka "That's fair!"
            m 1eua "School throws so many different subjects at you, it can be hard to pick just one."
            m 3eub "Just keep an open mind—you might find yourself loving something you never expected."

