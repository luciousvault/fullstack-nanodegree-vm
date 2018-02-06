#!/usr/bin/env python3
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from catalog_db_setup import Base, Category, Item

engine = create_engine('sqlite:///catalog.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()


# Game Categories pulled from Wikipedia
# https://en.wikipedia.org/wiki/List_of_video_game_genres
category1 = Category(name="Platform")

session.add(category1)
session.commit()

categoryGame1 = Item(name="Donkey Kong",
                    description="""Donkey Kong is considered to be the earliest
                    video game with a storyline that visually unfolds on
                    screen. The eponymous Donkey Kong character is the
                    game's de facto villain. The hero is a carpenter
                    originally unnamed in the Japanese arcade release,
                    later named Jumpman and then Mario. The ape kidnaps
                    Mario's girlfriend, originally known as Lady, but later
                    renamed Pauline. The player must take the role of Mario
                    and rescue her. This is the first occurrence of the
                    damsel in distress scenario that would provide the
                    template for countless video games to come.""")
session.add(categoryGame1)
session.commit()

categoryGame2 = Item(name="Super Mario Bros.",
                    description="""Super Mario Bros. takes place in the fantasy
                    setting of the Mushroom Kingdom. The game begins when a
                    tribe of a turtle-like race known as the Koopa Troopas
                    invade the kingdom and uses the magic of its king, Bowser,
                    to turn its inhabitants into inanimate objects such as
                    bricks. Bowser and his army also kidnap Princess Toadstool,
                    the daughter of the Mushroom King and the only one with the
                    ability to reverse Bowser's spell. After hearing the news,
                    Mario sets out to save the princess and free the kingdom
                    from Bowser. After traveling through various parts of
                    the kingdom and fighting Bowser's forces along the way,
                    Mario finally reaches Bowser's final stronghold, where he
                    is able to defeat him and send him falling into a pool of
                    lava, allowing the princess to be freed and the Mushroom
                    Kingdom saved.""")
session.add(categoryGame2)
session.commit()

category2 = Category(name="Shooter")

session.add(category2)
session.commit()

categoryGame1 = Item(name="DOOM",
                    description="""The player takes the role of an unnamed
                    space marine ("Doomguy") who has been punitively posted to
                    Mars after assaulting a superior officer, who ordered his
                    unit to fire on civilians. The Martian space marine base
                    acts as security for multi-planetary conglomerate Union
                    Aerospace Corporation's radioactive waste facilities, which
                    are used by the military to perform secret experiments with
                    teleportation by creating gateways between the two moons of
                    Mars, Phobos and Deimos. Mars is considered by space
                    marines to be the dullest assignment imaginable. This all
                    changes when the experiments go horribly wrong. Computer
                    systems on Phobos malfunction, Deimos disappears entirely,
                    and "something fraggin' evil" starts pouring out of the
                    gateways, killing or possessing all personnel. Responding
                    to a frantic distress call from the overrun scientists,
                    the Martian marine unit is quickly sent by ship from Mars
                    to Phobos to investigate, where the player character is
                    left to guard the perimeter with only a pistol while the
                    rest of the group proceeds inside. The marine hears
                    assorted radio messages, gunfire, and screams, followed
                    by silence: "Seems your buddies are dead." The player
                    cannot navigate the ship off of Phobos alone and sees that
                    the only way out is to fight through the Phobos complex.""")
session.add(categoryGame1)
session.commit()

categoryGame2 = Item(name="Splatoon",
                    description="""Octo Valley is the game's single player
                    campaign in which players are recruited by war veteran
                    Captain Cuttlefish to rescue The Great Zapfish, Inkopolis'
                    source of power, from the Octarians. Players use a default
                    ink weapon for this mode, which can be enhanced with
                    upgrades or additional power-ups by collecting Power Eggs
                    littered across each stage. The goal of each level is to
                    navigate through enemies and obstacles, including spongy
                    platforms, ink-eating robots, and ink-rails, in order to
                    reach the Great Zapfish at the end. Each level also
                    contains a hidden "sunken scroll", which reveal backstories
                    and lore surrounding the setting of Splatoon. After
                    clearing each level in an area, players face off against
                    that area's boss in order to proceed to the next. Clearing
                    each boss unlocks blueprints that can be exchanged at the
                    ink weapons shop for more weapon options.""")
session.add(categoryGame2)
session.commit()


category3 = Category(name="Fighting")

session.add(category3)
session.commit()

categoryGame1 = Item(name="Street Fighter",
                    description="""In this game, the player takes control of
                    martial artist Ryu, who competes in a worldwide martial
                    arts tournament, spanning five countries and 10 opponents.
                    A second player can join in at any time and take control of
                    Ryu's American rival, Ken.""")
session.add(categoryGame1)
session.commit()

categoryGame2 = Item(name="Street Fighter II",
                    description="""Street Fighter II is the first one-on-one
                    fighting game to give players a choice from a variety of
                    player characters with different moves. The choice of
                    multiple available characters allows for more varied
                    matches. In this game, each player character had a unique
                    fighting style with approximately 30 or more moves,
                    including then-new grappling moves and throws, as well as
                    two or three special attacks per character. In the
                    single-player mode, the player's chosen character is pitted
                    sequentially against the seven other main characters before
                    confronting the final four boss opponents, who consist of
                    CPU-controlled characters not selectable by the player. As
                    in the original, a second player could join in at any
                    point during single player mode and compete against the
                    other player in competitive matches.""")
session.add(categoryGame2)
session.commit()



category4 = Category(name="Stealth")

session.add(category4)
session.commit()

categoryGame1 = Item(name="Metal Gear",
                    description="""The first Metal Gear game for the MSX
                    follows Solid Snake, a rookie of the FOXHOUND special
                    operations unit. He is sent by his superior Big Boss to
                    the Eastern Pacific fortress Outer Heaven, with the goal
                    of finding the missing squad member Gray Fox and
                    investigating a weapon known as Metal Gear. However,
                    after Snake unexpectedly completes his goals, Big Boss is
                    revealed to be the leader of Outer Heaven, which he has
                    created as a place for soldiers to fight free of any
                    ideology that he believes has been forced upon them by
                    governments. He fights Snake and is killed. However, it
                    turns out that this was actually the body double from
                    Metal Gear Solid V: The Phantom Pain. In Metal Gear 2:
                    Solid Snake the real Big Boss has established a new
                    military nation, Zanzibar Land, and he and Snake face off
                    again, with Snake achieving victory and seemingly killing
                    Big Boss for good.""")
session.add(categoryGame1)
session.commit()

categoryGame2 = Item(name="Sly Cooper",
                    description="""Sly Cooper and the Thievius Raccoonus, also
                    known as Sly Raccoon in European countries, was released in
                    2002 for the PlayStation 2 platform. Sly must recover his
                    family's "Thievius Raccoonus", a book listing all the
                    special thieving skills his family has collected over
                    several centuries, which was stolen by a rival gang, the
                    Fiendish Five, led by Clockwerk, a giant mechanical owl.
                    Meanwhile, Sly and his gang must keep ahead of Interpol's
                    Inspector Carmelita Fox, who promises to one day capture
                    Sly and put him away for his crimes.""")
session.add(categoryGame2)
session.commit()


category5 = Category(name="Rhythm")

session.add(category5)
session.commit()

categoryGame1 = Item(name="Dance Dance Revolution",
                    description="""The core gameplay involves the player
                    stepping their feet to correspond with the arrows that
                    appears on screen and the beat. During normal gameplay,
                    arrows scroll upwards from the bottom of the screen and
                    pass over a set of stationary arrows near the top (referred
                    to as the "guide arrows" or "receptors", officially known
                    as the Step Zone). When the scrolling arrows overlap the
                    stationary ones, the player must step on the corresponding
                    arrows on the dance platform, and the player is given a
                    judgement for their accuracy of every streaked notes (From
                    highest to lowest: Marvelous, Perfect, Great, Good, Almost,
                    Miss""")
session.add(categoryGame1)
session.commit()

categoryGame2 = Item(name="Guitar Hero",
                    description="""The original Guitar Hero was released on the
                    PlayStation 2 in November 2005. Guitar Hero is notable
                    because it comes packaged with a controller peripheral
                    modeled after a black Gibson SG guitar. Rather than a
                    typical gamepad, this guitar controller is the primary
                    input for the game. Playing the game with the guitar
                    controller simulates playing an actual guitar, except it
                    uses five colored "fret buttons" and a "strum bar" instead
                    of frets and strings. The development of Guitar Hero was
                    inspired by Konami's Guitar Freaks video game, which at the
                    time, had not seen much exposure in the North American
                    market; RedOctane, already selling guitar-shaped
                    controllers for imported copies of GuitarFreaks, approached
                    Harmonix about creating a game to use an entirely new
                    Guitar controller. The concept was to have the gameplay of
                    Amplitude with the visuals of Karaoke Revolution, both of
                    which had been developed by Harmonix. The game was met with
                    critical acclaim and received numerous awards for its
                    innovative guitar peripheral and its soundtrack, which
                    comprised 47 playable rock songs (most of which were cover
                    versions of popular songs from artists and bands from the
                    1960s through modern rock). Guitar Hero has sold nearly
                    1.5 million copies to date.""")
session.add(categoryGame2)
session.commit()
