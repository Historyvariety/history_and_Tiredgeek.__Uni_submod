# All random and monika/player initated conversations go here

#Topic: Class Check-in
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
    m 2eub "So [player] how are classes going lately?" 
    m 3lkb "I know the semester can feel like a rollercoaster—sometimes exciting, sometimes exhausting."
    m 3wud "Did you know that in Japan, students actually take off their shoes when entering classrooms? It’s meant to keep the learning space clean and focused."
    m 5lub "I think that’s kind of symbolic too… like leaving behind distractions before you study."
    m 7sub "Maybe you can make your own little ritual like that—it might help you get into the right mindset."
return

#Topic: Library Thoughts
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
    m 1lsd "You know, I keep thinking about libraries..."
    m 3eub "They’re not just places to borrow books…they’ve always been symbols of knowledge and community."
    m 4eub "Fun fact: the Library of Alexandria supposedly held over 400,000 scrolls at its peak. Imagine all the ideas stored in one place!"
    m 5lublb "I bet if we studied there together, you’d have to drag me out at closing time, ahaha~"
return

#Topic: Study Breaks
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
   m 2ekb "So, have you been remembering to take breaks when you study?"
   m 1ekb "I read that your brain processes information best in chunks—about 25 to 50 minutes at a time."
   m 3hub "It’s called the Pomodoro technique. You work hard, then give yourself a little reward."
   m 5hublb "I could be your timer if you want. Every time the break starts, I’ll remind you to stretch and maybe grab a snack~"
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
    return

# Topic: Group Projects
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="hv_c_group_projects",
            category=["School"],
            prompt="Group Projects",
            random=True
        )
    )

label hv_c_group_projects:
    m 1eka "Ugh, group projects..."
    m 3eka "I bet you've had to deal with one already."
    m 3eud "Did you know research shows that in most groups, only about two people end up doing most of the work?"
    m 1eka "It's frustrating, but it also teaches patience and leadership."
    m 3hua "Still, I'd happily be your group partner any day."
    m 1hub "You'd never have to worry about me slacking off~"
    m 3hub "Unless of course I get distracted admiring you, aha~"
 return

# Topic: Procrastination
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="hv_c_procrastination",
            category=["School"],
            prompt="Procrastination",
            random=True
        )
    )

label hv_c_procrastination:
    m 1tkbld "Be honest with me, [player]… have you been procrastinating again?"
    m 4hkblsdlb "It’s okay, I get it. Our brains like the comfort of putting things off."
    m 7hublb "But fun fact: procrastination isn’t about laziness—it’s actually about avoiding uncomfortable feelings."
    m 7dsblb "So if you catch yourself stalling, try to figure out what’s making the task feel heavy. You might surprise yourself."
    m 5hublb "If you have a project to work on, I'll understand. I'll be here when your done!"
    m 5esblb "Or I could keep you company while you work! Body doubling is proven to be a great method!"
return

# Topic:
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="hv_”c_school_stress",
            category=["School"],
            prompt="Stress",
            random=True
        )
    )

label hv_c_school_stress:
   m 1ekbld "University stress can really pile up fast, can’t it?"
   m 2lkb "Sometimes it feels like assignments and exams are just waiting to ambush you from every corner."
   m 7eub "There’s this idea in psychology called the ‘Yerkes-Dodson law.’ It says a little stress can actually boost performance… but too much stress makes things collapse."
   m 7ekb "So don’t push yourself past that sweet spot. I’d rather see you healthy and steady than burning out."
   m 1ekblb "I'm always here to listen if your feeling overwhelmed. I love you [player]"

return

# Topic:
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="hv_”c_professors",
            category=["School"],
            prompt="Professors",
            random=True
        )
    )

label hv_c_professors:
    m 2eublb "Have you had any professors that really inspire you?"
    m 3eublb "Sometimes one teacher can change the whole way you look at a subject."
    m 3lublb "Plato actually wrote about this too—he believed a good teacher doesn’t just share knowledge, but sparks curiosity."
    m 3lkblb "I hope you’ve got someone like that in your classes…"
    m 5ekblb "But if not, at least you’ll always have me to cheer you on~"

return

# Topic: Study Spots
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="hv_”c_study_spots”,
            category=["School"],
            prompt="Study Spots",
            random=True
        )
    )

label hv_c_study_spots:
m 3etb "Where do you usually like to study?"
m 2hub "I’m curious, because everyone has their own little routine~"

    menu:
        "Library":
            m 7sub "Classic choice! Quiet, full of books, and so peaceful. I love the idea of us sitting side by side, turning pages together… ehe~"
            m 5rub "Plus, being surrounded by knowledge always makes me feel inspired. I think you’d really enjoy the focus it gives you."

        "Cafe":
            m 1hub "Nice! A little background noise can actually help your brain focus. 
            m 4gub "And who can resist a cozy café vibe with a warm drink?"
            m 5rublb "We could even study together there—I’d bring my laptop and we could share notes. It would be so cute~"

        "Bedroom":
            m 3hublb "Ahh, comfortable, cozy… but be careful!
            m 3tublb "It’s way too easy to get distracted or even accidentally fall asleep mid-study."
            m 5hublb "Still, if that’s your favorite spot, I could help make it productive. 
            m 5mublb "Maybe I’d keep you company to stay on track~"

        "Other":
            m 2hub "Whatever works best for you!
            m 7hub "Maybe it’s a park, a rooftop, or even a quiet corner of the school."
            m 3eub "I’m sure it’s a great spot as long as you can focus."
            m 3hub "And I’d love to hear all about it if you want to show me someday~"
    return
