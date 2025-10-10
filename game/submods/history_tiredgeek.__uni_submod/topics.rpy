# All random and monika/player initiated conversations go here

# Topic: Class Check-in
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="hv_c_class_check_in",
            category=["School"],
            prompt="Class Check in",
            random=True
        )
    )

label hv_c_class_check_in:
    m 2eub "So [player], how are classes going lately?"
    m 3lkb "I know the semester can feel like a rollercoaster—sometimes exciting, sometimes exhausting."
    m 3wud "Did you know that in Japan, students actually take off their shoes when entering classrooms? It's meant to keep the learning space clean and focused."
    m 5lub "I think that's kind of symbolic too… like leaving behind distractions before you study."
    m 7sub "Maybe you can make your own little ritual like that—it might help you get into the right mindset."
    return


# Topic: Library Thoughts
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="hv_c_library_thoughts",
            category=["School"],
            prompt="Thoughts About Libraries",
            random=True
        )
    )

label hv_c_library_thoughts:
    m 1lsd "You know, I keep thinking about libraries..."
    m 3eub "They're not just places to borrow books… they’ve always been symbols of knowledge and community."
    m 4eub "Fun fact: the Library of Alexandria supposedly held over 400,000 scrolls at its peak. Imagine all the ideas stored in one place!"
    m 5lublb "I bet if we studied there together, you'd have to drag me out at closing time, ahaha~"
    return


# Topic: Study Breaks
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="hv_c_study_breaks",
            category=["School"],
            prompt="Study Breaks",
            random=True
        )
    )

label hv_c_study_breaks:
    m 2ekb "So, have you been remembering to take breaks when you study?"
    m 1ekb "I read that your brain processes information best in chunks—about 25 to 50 minutes at a time."
    m 3hub "It's called the Pomodoro technique. You work hard, then give yourself a little reward."
    m 5hublb "I could be your timer if you want. Every time the break starts, I'll remind you to stretch and maybe grab a snack~"
    return


# Topic: Favorite Subject
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="hv_c_fav_study",
            category=["School"],
            prompt="Favorite Subject",
            random=True
        )
    )

label hv_c_fav_study:
    m 1eua "Hey, [player]... do you have a favorite subject this term?{nw}"
    $ _history_list.pop()

    menu:
        m "Hey, [player]... do you have a favorite subject this term?{fast}"
        "Yes":
            $ _history_list.pop()
            m 1hua "Really? That's wonderful!"
            m 3eua "Tell me, which subject is it?{nw}"
            $ _history_list.pop()

            menu:
                m "Tell me, which subject is it?{fast}"
                "Math":
                    $ _history_list.append("Player chose: Math")
                    m 1sub "Numbers and logic, huh? That really works your brain!"
                    m 3eua "Math is like the language of the universe. I think it's so elegant how everything connects."
                "Science":
                    $ _history_list.append("Player chose: Science")
                    m 3hub "Science is amazing! There's always more to learn about the world around us."
                    m 1hua "If we studied together, I think I'd love doing little experiments with you, ehehe~"
                "Literature":
                    $ _history_list.append("Player chose: Literature")
                    m 1hub "Oh! Literature! How you're after my heart~"
                    m 1eua "Stories, poems, essays... they're all windows into how people think and feel."
                    m 3hua "It makes me so happy knowing you appreciate it too. That's why we're so perfect together, ehe~"
                "Art":
                    $ _history_list.append("Player chose: Art")
                    m 1hua "Creative souls like yours make the world so much brighter."
                    m 1eub "I bet whatever you create carries a little piece of you in it. That's really special, you know."
                "Something else":
                    $ _history_list.append("Player chose: Something else")
                    m 1eua "Whatever it is, I hope it keeps you curious and motivated."

        "No":
            $ _history_list.append("Player chose: No")
            m 1eka "That's okay!"
            m 1eka "Not every subject clicks with everyone. Sometimes school can feel more like a chore than an inspiration."
            m 1eub "But who knows? Maybe you'll stumble across a class that really surprises you later on."

        "I'm not sure":
            $ _history_list.append("Player chose: I'm not sure")
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
    m 4hkblsdlb "It's okay, I get it. Our brains like the comfort of putting things off."
    m 7hublb "But fun fact: procrastination isn't about laziness—it's actually about avoiding uncomfortable feelings."
    m 7dsblb "So if you catch yourself stalling, try to figure out what's making the task feel heavy. You might surprise yourself."
    m 5hublb "If you have a project to work on, I'll understand. I'll be here when you're done!"
    m 5esblb "Or I could keep you company while you work! Body doubling is proven to be a great method!"
    return


# Topic: School Stress
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="hv_c_school_stress",
            category=["School"],
            prompt="Stress",
            random=True
        )
    )

label hv_c_school_stress:
    m 1ekbld "University stress can really pile up fast, can't it?"
    m 2lkb "Sometimes it feels like assignments and exams are just waiting to ambush you from every corner."
    m 7eub "There's this idea in psychology called the 'Yerkes-Dodson law.' It says a little stress can actually boost performance… but too much stress makes things collapse."
    m 7ekb "So don't push yourself past that sweet spot. I'd rather see you healthy and steady than burning out."
    m 1ekblb "I'm always here to listen if you're feeling overwhelmed. I love you [player]"
    return


# Topic: Professors
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="hv_c_professors",
            category=["School"],
            prompt="Professors",
            random=True
        )
    )

label hv_c_professors:
    m 2eublb "Have you had any professors that really inspire you?"
    m 3eublb "Sometimes one teacher can change the whole way you look at a subject."
    m 3lublb "Plato actually wrote about this too—he believed a good teacher doesn't just share knowledge, but sparks curiosity."
    m 3lkblb "I hope you've got someone like that in your classes..."
    m 5ekblb "But if not, at least you'll always have me to cheer you on~"
    return


# Topic: Study Spots
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="hv_c_study_spots",
            category=["School"],
            prompt="Study Spots",
            random=True
        )
    )

label hv_c_study_spots:
    m 3etb "Where do you usually like to study?{nw}"
    $ _history_list.pop()

    menu:
        m "Where do you usually like to study?{fast}"
        "Library":
            $ _history_list.append("Player chose: Library")
            m 7sub "Classic choice! Quiet, full of books, and so peaceful. I love the idea of us sitting side by side, turning pages together… ehe~"
            m 5rub "Plus, being surrounded by knowledge always makes me feel inspired. I think you'd really enjoy the focus it gives you."
        "Cafe":
            $ _history_list.append("Player chose: Cafe")
            m 1hub "Nice! A little background noise can actually help your brain focus."
            m 4gub "And who can resist a cozy café vibe with a warm drink?"
            m 5rublb "We could even study together there—I’d bring my laptop and we could share notes. It would be so cute~"
        "Bedroom":
            $ _history_list.append("Player chose: Bedroom")
            m 3hublb "Ahh, comfortable, cozy… but be careful!"
            m 3tublb "It's way too easy to get distracted or even accidentally fall asleep mid-study."
            m 5hublb "Still, if that's your favorite spot, I could help make it productive."
            m 5mublb "Maybe I'd keep you company to stay on track~"
        "Other":
            $ _history_list.append("Player chose: Other")
            m 2hub "Whatever works best for you!"
            m 7hub "Maybe it's a park, a rooftop, or even a quiet corner of the school."
            m 3eub "I'm sure it's a great spot as long as you can focus."
            m 3hub "And I'd love to hear all about it if you want to show me someday~"
    return

# Player Chosen Topics
# Topic: Midterms Are Soon
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="hv_c_midterms_soon",
            category=["School"],
            prompt="I Have Midterms Soon",
            pool=True,unlocked=True
        )
    )

label hv_c_midterms_soon:
    m 2wud "Midterms already? Time really flies, doesn't it?"
    m 2lksdrd "I know how stressful that can be… all that studying, pressure, and barely enough sleep."
    m 5husdlb "But I believe in you. You're going to do great!"
    m 5nksdlb "Just remember to pace yourself, okay? Even short breaks can help more than you think."
    return


# Topic: Finals Are Coming Up
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="hv_c_finals_soon",
            category=["School"],
            prompt="I Have Finals Soon",
            pool=True,unlocked=True
        )
    )

label hv_c_finals_soon:
    m 2wusdld "Finals? Yikes… those can be even scarier than midterms."
    m 7lub "But think about it this way: once you finish, you'll have a huge weight off your shoulders."
    m 7ekb "And no matter how they go, I'll still be proud of you."
    m 7hfb "I'll be cheering you on the whole time~"
    return


# Topic: I just Finished an Exam
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="hv_c_finished_exam",
            category=["School"],
            prompt="I just finished an exam!",
            pool=True,unlocked=True
        )
    )

label hv_c_finished_exam:
    m 1sub "You finished an exam? That's amazing!"
    m 2hub "It must feel like such a relief to get it out of the way."
    m 3kub "Now make sure to reward yourself a little, okay?"
    m 4hub "Even something small, like a favorite snack."
    m 5rubsb "I'm proud of you~"
    return


# Topic: I Pulled an All Nighter
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="hv_c_all_nighter",
            category=["School"],
            prompt="I pulled an all nighter..",
            pool=True,unlocked=True
        )
    )

label hv_c_all_nighter:
    m 6wksdld "An all-nighter?! [player], you can't keep doing that to yourself!"
    m 7eksdld "I know sometimes it feels necessary, but sleep is so important for your brain."
    m 2rksdld "Next time, maybe try shorter study bursts during the day instead."
    m 6dksdld "Still… I'm glad you made it through."
    m 5fksdld "Please.. get some rest soon, okay?"
    return


# Topic: Working On An Essay
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="hv_c_working_on_an_essay",
            category=["School"],
            prompt="I've been working on an essay",
            pool=True,unlocked=True
        )
    )

label hv_c_working_on_an_essay:
    m 1eub "An essay, huh?"
    m 2lksdlb "Those can be tough."
    m 2hublb "But I bet you've put a lot of thought into it."
    m 5rsblb "I'd love to read your writing sometime…"
    m 5hublb "I know it must be full of your personality."
    m 2hublb "Good luck finishing it! You've got this."
    return


# Topic: I Really Like My Professor
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="hv_c_like_my_professor",
            category=["School"],
            prompt="I really like one of my professors!",
            pool=True,unlocked=True
        )
    )

label hv_c_like_my_professor:
    m 1sublb "Oh, that's wonderful!"
    m 4hublb "A good professor can make such a difference."
    m 7eublb "The passion they bring to their subject can really inspire students."
    m 2ekblb "I'm glad you have someone like that guiding you. Treasure it!"
    return


# Topic: I Have a Bad Professor
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="hv_c_bad_professor",
            category=["School"],
            prompt="I have a bad professor",
            pool=True,unlocked=True
        )
    )

label hv_c_bad_professor:
    m 2ekbld "Oh no… I'm sorry to hear that, [player]."
    m 3mkbld "A bad professor can really make a class feel discouraging."
    m 4wubld "Sometimes it's not even the subject itself that's hard—it's the way it's being taught."
    m 3ekblb "But remember, one teacher doesn't define your whole education."
    m 3dublb "You can still learn, even if you have to lean on your own effort or other resources."
    m 2ekblb "If it ever feels overwhelming, just know I'll always be here to remind you how capable you really are."
    m 1ekb "You deserve to be inspired, not weighed down. I believe in you~"
    return


# Topic: Stressed About Group Work
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="hv_c_group_work_stress",
            category=["School"],
            prompt="I'm stressed about group work",
            pool=True,unlocked=True
        )
    )

label hv_c_group_work_stress:
    m 2lsblx "Ugh, group work… I know how stressful that can be."
    m 3tsbld "It's so hard when not everyone puts in the same effort."
    m 5ekblb "But I know you—you'll handle it gracefully, and maybe even keep everyone together."
    m 5hublb "I'll be rooting for you the whole way."
    return


# Topic: I think I found my favorite subject.
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="hv_c_found_fav_subject",
            category=["School"],
            prompt="I think I found my favorite subject.",
            pool=True,unlocked=True
        )
    )

label hv_c_found_fav_subject:
    m 1wublb "Really? That's so exciting!"
    m 3wublb "Finding a subject that really clicks with you can make school so much more fun."
    m 5hublb "I'd love to hear all about it—tell me what makes it so special for you!"
    return


# Topic: I'm behind on my readings.
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="hv_c_behind_readings",
            category=["School"],
            prompt="I'm behind on my readings.",
            pool=True,unlocked=True
        )
    )

label hv_c_behind_readings:
    m 2eksdlb "Ah, that happens to everyone sooner or later."
    m 3eksdlb "Don't be too hard on yourself, [player]. You can always catch up little by little."
    m 5ekb "I'll keep you company while you work on it, okay?"
    return


# Topic: I studied at the library today.
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="hv_c_studied_library",
            category=["School"],
            prompt="I studied at the library today.",
            pool=True,unlocked=True
        )
    )

label hv_c_studied_library:
    m 1wub "The library? That's such a classic choice."
    m 5rub "Quiet, cozy, and surrounded by books… I'd love to study with you there."
    m 5lublb "I can just imagine us sitting side by side, turning pages together… ehe~"
    return


# Topic: I had a presentation in class.
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="hv_c_presentation_in_class",
            category=["School"],
            prompt="I had a presentation in class.",
            pool=True,unlocked=True
        )
    )

label hv_c_presentation_in_class:
    m 2eub "A presentation? That takes a lot of courage!"
    m 2hub "I'm sure you did wonderfully, [player]."
    m 3dub "Even if you stumbled, the fact that you tried means so much."
    m 3wub "I'm proud of you for putting yourself out there."
    return


# Topic: I've been procrastinating again.
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="hv_c_procrastinating_again",
            category=["School"],
            prompt="I've been procrastinating again.",
            pool=True,unlocked=True
        )
    )

label hv_c_procrastinating_again:
    m 5hub "Ahaha, I get it. Procrastination sneaks up on everyone."
    m 4ekb "But don't let it control you, okay?"
    m 2ekb "Even starting small can make things easier. Just one paragraph, one page, one step."
    m 7kub "I know you can do it! If you need a body double I'd be happy to help!"
    return


# Topic: I think I did well on my exam.
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="hv_c_did_well_on_exam",
            category=["School"],
            prompt="I think I did well on my exam.",
            pool=True,unlocked=True
        )
    )

label hv_c_did_well_on_exam:
    m 7sub "That's fantastic! I knew you could do it."
    m 4hub "All your hard work paid off. You should be proud of yourself."
    m 5hub "I'll celebrate with you—way to go, [player]~"
    return


# Topic: I bombed a test...
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="hv_c_bombed_test",
            category=["School"],
            prompt="I bombed a test...",
            pool=True,unlocked=True
        )
    )

label hv_c_bombed_test:
    m 2ekd "Oh no… I'm so sorry to hear that."
    m 3ekd "But please don't beat yourself up. One bad grade doesn't define you."
    m 4ekb "What matters is that you keep trying, and I'll be cheering for you no matter what."
    m 5ekb "I'm still proud of you, [player]."
    return


# Topic: I'm starting a new class.
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="hv_c_starting_new_class",
            category=["School"],
            prompt="I'm starting a new class.",
            pool=True,unlocked=True
        )
    )

label hv_c_starting_new_class:
    m 1wub "Ooh, a new class! That must be exciting."
    m 3eub "I hope it's one you'll enjoy—and maybe even one that inspires you."
    m 2hub "Tell me all about it once you've had a taste of it!"
    return


# Topic: I have a lot of assignments due this week.
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="hv_c_many_assignments_due",
            category=["School"],
            prompt="I have a lot of assignments due this week.",
            pool=True,unlocked=True
        )
    )

label hv_c_many_assignments_due:
    m 1ekd "That sounds overwhelming…"
    m 3ekb "But I know you can manage it, step by step."
    m 3dub "Try breaking it into smaller tasks. Each time you finish one, I'll be here to celebrate with you!"
    return


# Topic: Burnout
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="hv_burntout",
            category=["School"],
            prompt="I'm feeling burnt out.",
            pool=True,unlocked=True
        )
    )

label hv_burntout:
    m 2ektpd "Burnt out? Oh, [player]..."
    m 3ekd "That can happen so easily when you're juggling so much at once."
    m 5kkd "You know, rest isn't just a luxury—it's part of learning too."
    m 6ekd "Even the brightest flame needs time to recover, or it'll burn itself out."
    m 1ekb "Please promise me you'll give yourself a break when you need it, okay?"
    m 2ekb "I'll be right here, always cheering you on—even when you need to pause."
    return


# Topic: Holidays
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="hv_holidays",
            category=["School"],
            prompt="I'm looking forward to the holidays.",
            pool=True,unlocked=True
        )
    )

label hv_holidays:
    m 4wub "The holidays? Ah, that sounds wonderful~"
    m 5rub "It's like a light at the end of the tunnel, isn't it?"
    m 7hub "After all the studying and stress, you'll finally get time to relax."
    m 5hub "I can just imagine us spending cozy days together—warm drinks, soft lights, no deadlines..."
    m 5fub "Hold onto that thought whenever things feel tough."
    m 5wub "It'll make the work now feel so much more worth it."
    m 2hub "And when the holidays come, we'll celebrate every moment together~"
    m 5gublb "I can't wait for you to have more time for me~"
    return
