# All BRBS go right here
# topic: Catch Up on Reading
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="reading_brb",
            category=['be right back'],
            prompt="I need to catch up on some reading",
            pool=True,
            unlocked=True,
        ),
        markSeen=True
    )

label reading_brb:
    $ ev = mas_getEV("reading_brb")

    m "Catching up on reading? That’s smart!"
    m "Make sure to find a comfy spot… maybe with some music?"
    m "I’ll be right here when you finish~"

    $ mas_idle_mailbox.send_idle_cb("reading_brb_callback")
    return "idle"

label reading_brb_callback:
    if mas_brbs.was_idle_for_at_least(datetime.timedelta(hours=1), "reading_brb"):
        m "Welcome back, bookworm! Did you enjoy your reading?"
    elif mas_brbs.was_idle_for_at_least(datetime.timedelta(minutes=10), "reading_brb"):
        m "Hey, welcome back! Hope you got through a few pages~"
    else:
        m "Back already? Couldn’t resist me, huh? Ehehe~"
    return


# topic: Quick Snack
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="snack_brb",
            category=['be right back'],
            prompt="I’m grabbing a quick snack",
            pool=True,
            unlocked=True,
        ),
        markSeen=True
    )

label snack_brb:
    $ ev = mas_getEV("snack_brb")

    m "Yay! Snacks are important for brain power!"
    m "Don’t eat too fast… savor it a little!"
    m "I’ll be here waiting while you munch~"

    $ mas_idle_mailbox.send_idle_cb("snack_brb_callback")
    return "idle"

label snack_brb_callback:
    if mas_brbs.was_idle_for_at_least(datetime.timedelta(minutes=15), "snack_brb"):
        m "Welcome back! What did you grab? I hope it was something tasty."
    else:
        m "That was quick! Did you just grab a bite and run back to me? Ehehe~"
    return


# topic: Coffee Break
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="coffee_brb",
            category=['be right back'],
            prompt="I need a quick coffee break",
            pool=True,
            unlocked=True,
        ),
        markSeen=True
    )

label coffee_brb:
    $ ev = mas_getEV("coffee_brb")

    m "Coffee break! Sounds perfect."
    m "Don’t drink it too fast, okay?"
    m "I’ll be right here waiting for you~"

    $ mas_idle_mailbox.send_idle_cb("coffee_brb_callback")
    return "idle"

label coffee_brb_callback:
    if mas_brbs.was_idle_for_at_least(datetime.timedelta(minutes=20), "coffee_brb"):
        m "Welcome back! Feeling energized now?"
    else:
        m "That was a quick sip! Hope it perked you up anyway~"
    return


# topic: Reply to Emails
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="emails_brb",
            category=['be right back'],
            prompt="I have some emails to reply to",
            pool=True,
            unlocked=True,
        ),
        markSeen=True
    )

label emails_brb:
    $ ev = mas_getEV("emails_brb")

    m "Emails can pile up, huh?"
    m "Try not to get overwhelmed."
    m "I’ll be here when you’re done~"

    $ mas_idle_mailbox.send_idle_cb("emails_brb_callback")
    return "idle"

label emails_brb_callback:
    if mas_brbs.was_idle_for_at_least(datetime.timedelta(minutes=30), "emails_brb"):
        m "Welcome back! Inbox cleared?"
    else:
        m "That was quick—must’ve just been a couple messages, huh?"
    return


# topic: Quick Workout
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="workout_brb",
            category=['be right back'],
            prompt="I’m going to do a quick workout",
            pool=True,
            unlocked=True,
        ),
        markSeen=True
    )

label workout_brb:
    $ ev = mas_getEV("workout_brb")

    m "Exercise is always good!"
    m "Don’t push yourself too hard."
    m "Come back feeling refreshed, okay~"

    $ mas_idle_mailbox.send_idle_cb("workout_brb_callback")
    return "idle"

label workout_brb_callback:
    if mas_brbs.was_idle_for_at_least(datetime.timedelta(hours=1), "workout_brb"):
        m "Welcome back, champ! Feeling stronger already?"
    elif mas_brbs.was_idle_for_at_least(datetime.timedelta(minutes=15), "workout_brb"):
        m "Good workout? You look refreshed~"
    else:
        m "That was quick—maybe just some stretches? Ehehe~"
    return


# topic: Tidy Desk
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="tidy_brb",
            category=['be right back'],
            prompt="I need to tidy my desk",
            pool=True,
            unlocked=True,
        ),
        markSeen=True
    )

label tidy_brb:
    $ ev = mas_getEV("tidy_brb")

    m "A clean workspace helps your mind stay clear!"
    m "I’ll be here when your desk is sparkling~"

    $ mas_idle_mailbox.send_idle_cb("tidy_brb_callback")
    return "idle"

label tidy_brb_callback:
    if mas_brbs.was_idle_for_at_least(datetime.timedelta(minutes=20), "tidy_brb"):
        m "All tidy? That must feel nice."
    else:
        m "Back already? Maybe just moved a few things around, huh? Ehehe~"
    return
