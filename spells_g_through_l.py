"""
Realms spell list G-L
Version: 2023
"""

spells = [
        {
            "name": "ghost blade",
            "circle": 1,
            "uses": "2",
            "verbal": "20 words",
            "material": "A white ribbon with the words 'Ghost Blade' on it",
            "active": None,
            "caveats": ["Enchanted Items"],
            "description": (
                "This spell enchants a single weapon to no longer affect the casting of the "
                "spells Raise Dead or Regeneration or the breaking of Circle of Healing. "
                "Upon casting this spell, the spellcaster must tie the MC onto the enchanted "
                "weapon."
            ),
            "link": "https://www.realmsnet.net/rules/omnibus#ghost-blade"
        },
        {
            "name": "group healing",
            "circle": 2,
            "uses": "2",
            "verbal": "10 words",
            "material": "30' rope",
            "active": "Touch the rope",
            "caveats": ["Circles", "Suspension"],
            "description": (
                "This spells allows the spellcaster to cast an enchanted circle. This circle "
                "allows certain spells cast into it to affect all the people within the "
                "circle. The Group Healing circle may be used to enhance the power of the "
                "following spells: Combat Raise Dead, Cure Disease, Immunity to Poison, Heal "
                "Limb, and Raise Dead. Multiple castings of Group Healing from the same or "
                "different spellcasters may be used at the same time, creating a bigger "
                "circle. \n To enchant the Group Healing circle, lay the rope(s) in a circle "
                "on the ground with the ends touching. Then all the characters to be cast "
                "upon need to be gathered into the circle. The spellcaster(s) must then "
                "recite the VC, which empowers the circle. \n The next spell from the "
                "accepted list cast into this circle by any spellcaster affects all within "
                "as if it had been cast on each individually. If the spell has any MC, only "
                "one is used."
            ),
            "link": "https://www.realmsnet.net/rules/omnibus#group-healing"
        },
        {
            "name": "guidance",
            "circle": 2,
            "uses": "2",
            "verbal": None,
            "material": "Divining paraphernalia to indicate a yes/no answer",
            "active": None,
            "caveats": ["Spell Failure"],
            "description": (
                "This spell allows the spellcaster to ask the EH or MM a yes/no question. If "
                "the EH or MM does not know the answer because the question asked relates to "
                "PC actions, an answer may not be given. An answer will be given in the form "
                "of “Yes” or “No” by the EH or MM. If the spell is cast and an answer cannot "
                "be given because of any of the above limitations, the casting is still used "
                "up."
            ),
            "link": "https://www.realmsnet.net/rules/omnibus#guidance"
        },
        {
            "name": "heal limb",
            "circle": 2,
            "uses": "Unlimited",
            "verbal": "20 words",
            "active": "Spellcaster must be stationary, must touch the target limb",
            "material": None,
            "caveats": None,
            "description": (
                "This spell allows the spellcaster to heal one damaged limb at a time. The "
                "spellcaster must recite the VC while touching the recipient\'s injured "
                "limb. The spellcaster cannot move their feet while casting this spell, "
                "although they may be moving their arms (e.g. parrying, so long as they "
                "don\'t step backwards)."
            ),
            "link": "https://www.realmsnet.net/rules/omnibus#heal-limb"
        },
        {
            "name": "heartiness",
            "circle": 1,
            "uses": "Unlimited, one at a time",
            "verbal": None,
            "active": None,
            "material": None,
            "caveats": ["Precast"],
            "description": (
                "Having this spell makes it harder to destroy the spellcaster\'s body. The "
                "next time the spellcaster\'s body is destroyed it will take 200 extra blows "
                "to successfully destroy their body. If struck for only 200 blows, instead "
                "of the full 400 blows, the spellcaster must inform the individual(s) "
                "destroying their body that “The job is not yet done.” A spellcaster can "
                "only be under the effect of one Heartiness spell at a time. A use is "
                "considered to be over whenever the spellcaster receives at least 200 body "
                "destroying blows, but is in effect until either their body is destroyed or "
                "they are raised."
            ),
            "link": "https://www.realmsnet.net/rules/omnibus#heartiness"
        },
        {
            "name": "identify",
            "circle": 1,
            "uses": "3",
            "verbal": "30 words",
            "active": None,
            "material": None,
            "caveats": None,
            "description": (
                "This spell allows the spellcaster to take any one item (not a living/dead "
                "creature) to the EH or MM to ask what it is and expect an answer. This "
                "spell can also determine what species an unknown creature is. If the "
                "spellcaster can successfully reach visual inspection range, recite the "
                "verbal, and the creature is not hostile, it must state what species it is. "
                "The response is not IC speech by the creature, and it can answer while "
                "dead."
            ),
            "link": "https://www.realmsnet.net/rules/omnibus#identify"
        },
        {
            "name": "immunity to poison",
            "circle": 1,
            "uses": "3",
            "verbal": "10 words",
            "active": None,
            "material": "Disposable",
            "caveats": ["OOC Calls"],
            "description": (
                "This spell makes the recipient immune to the next dose of poison that would "
                "have otherwise affected their PC during the event. When damaged by the next "
                "poison attack, whether ingested or delivered by a poisoned weapon, call "
                "“Immunity to Poison!” Only one Immunity to Poison is used at a time. The "
                "recipient must take any mundane damage from a poisoned weapon regardless of "
                "whether they are protected from the actual poison. The recipient must be "
                "given the MC when the spell is cast, and they are responsible for disposing "
                "of it when the immunity has been used. More than one Immunity to Poison can "
                "be cast upon a recipient; the effect is stackable. The MC of the spell is "
                "not stealable or transferable after it is cast. This spell can also be cast "
                "as an antidote for any one poison that the recipient has been subjected to, "
                "but in this case it will not provide any further protection."
            ),
            "link": "https://www.realmsnet.net/rules/omnibus#immunity-to-poison"
        },
        {
            "name": "implement",
            "circle": 1,
            "uses": "Special",
            "verbal": None,
            "active": None,
            "caveats": None,
            "material": """Safe, non-weapon Staff (between 4\' and 6\' long, inclusive), 
            Wand (between 12" and 18" long, inclusive), Orb (at least 4" in diameter), 
            or Book (bound, minimum 1/2" x 4" x 7", cannot be the spellcaster\'s spell-book)""",
            "description": (
                "The spellcaster is able to create a staff, wand, orb, or book (hereafter "
                "called “implement”) that enhances their own spells. Each time the "
                "spellcaster learns this spell, they gain 1 point into a pool from which "
                "they may purchase special abilities from the choices below. A spellcaster "
                "may only have 5 points worth of implements per event. At the magic check-in "
                "of an event, the spellcaster may choose how the points in their pool are "
                "spent. \nUnless otherwise stated, abilities gained that augment or alter "
                "spells require that the spellcaster already knows that spell, otherwise "
                "there is no effect. In order to use the gained ability, the spellcaster "
                "must be holding the implement in one hand. \nThe implement is a magical "
                "manifestation and cannot be broken. Any blow that strikes the implement "
                "must be taken as if the implement is not there. You can not actively parry "
                "with an implement. \nAn implement may be disenchanted causing any effects "
                "or castings to be lost until the implement is restored. If disenchanted it "
                "takes 120 seconds of holding the implement with both hands and nothing else "
                "to restore. \nGain one additional casting of one of the following spells "
                "for 1 point each: Find the Path, Fortune Tell, Guidance, Precognition, Skew "
                "Divination, Raise Dead, Deep Pockets, Enfeeble Being, Beckon Corpse, "
                "Disenchant, or Disrupt. \nGain the following abilities for 1 point each: "
                "\nWhen using a Circle spell you may double the length of the rope. This may "
                "only be done once. \nThe AC for Death Watch is changed to “Spellcaster must "
                "kneel on one knee holding their Implement with both hands for 60 seconds "
                "before being killed.” Additionally, the spell no longer ends when the "
                "spellcaster is raised. \nThe spell Death Watch allows the spellcaster to "
                "move their head while dead. They still may not speak, try to communicate, "
                "or move in any other way while dead. \nGain one additional casting of one "
                "of the following spells for 2 points each: Call the Soul, Group Healing, "
                "Resist Magic, Animate Undead, or Soul Bane. \nGain the following abilities "
                "for 2 points each: \nThe uses for Speak become unlimited \nGain 1 point to "
                "spend on your familiar. This ability may not be taken more than once. When "
                "this augmentation is first used through Implement, you shall list an "
                "alternate build for the familiar. This alternate build can only be changed "
                "by learning or unlearning a use of Familiar. From now on, when you use your "
                "Familiar and it is augmented by Implement, it uses that new build. If you "
                "are using the augmented build, and you do not have your implement on you, "
                "you may not use your Familiar abilities \nGain one additional casting of "
                "one of the following spells for 3 points each: Vision or Séance. \nGain the "
                "following abilities for 3 points each: \nGain one use of Regeneration. You "
                "are not required to know the spell to use this ability \nGain one use of "
                "Regeneration. Upon completion, the spellcaster will be animated as a "
                "free-willed undead. You are not required to know the spell to use this "
                "ability. \nGain one additional Magic Missile prop."
            ),
            "link": "https://www.realmsnet.net/rules/omnibus#implement"
        },
        {
            "name": "intervention",
            "circle": 6,
            "uses": "1",
            "verbal": "Speak to EH or MM",
            "active": "A quest may be required",
            "material": "A sacrifice may be required",
            "caveats": ["Spell Failure"],
            "description": (
                "This spell allows the spellcaster to go to the EH or MM and ask a boon from "
                "whatever powers their magic. It only works if it is cast in the presence of "
                "the EH or MM. It is to be used to request favors such as: “Oh, please, "
                "great majestic god/Fire Spirit/Navel Lint, grant me a quest to search for "
                "the lost soul of my overlord, Sir Biff of Bonehead Ridge.” This spell comes "
                "with no guarantee that the EH or MM won\'t simply listen to the request and "
                "say “No.” This spell cannot create an effect that will last beyond the end "
                "of the event, other than for healing purposes. A spellcaster who uses drama "
                "and theatrics has a better chance of success, and simple, small requests "
                "are also more likely to be granted. Any requests that will unbalance the "
                "game will likely be either denied straight out, or assigned an unsolvable "
                "quest."
            ),
            "link": "https://www.realmsnet.net/rules/omnibus#intervention"
        },
        {
            "name": "light",
            "circle": 1,
            "uses": "Unlimited",
            "verbal": "3 syllables",
            "material": """Chemical light stick and dark bag or EH- or MM-approved electronic 
            light with an on/off mechanism in any color except red""",
            "active": "Snap and shake the chemical light stick or turn on the electronic light",
            "caveats": None,
            "description": (
                "This spell creates light. The spellcaster may use as many Light props as "
                "desired. Electronic light sources must be checked in before use and may be "
                "pulled if they may be too bright or unsafe for the event. If using chemical "
                "light sticks, the spellcaster must also carry a bag large enough to hold "
                "all of the glow sticks they will use and thick enough to prevent any light "
                "from escaping. The bag is to be used if they are affected by a Disrupt "
                "Light spell. The spellcaster may not give a Light prop to anyone who is "
                "going to travel beyond easy speaking distance. It is possible for this "
                "spell to be disrupted. It is the spellcaster\'s responsibility to know what "
                "the Disrupt Light spell is, how to recognize it, and how to respond to it."
            ),
            "link": "https://www.realmsnet.net/rules/omnibus#light"
        },
        {
            "name": "lightning bolt",
            "circle": 6,
            "uses": "1 prop, unlimited use",
            "verbal": "Lightning Bolt",
            "active": None,
            "material": '1 white boff arrow or javelin prop between 2\'6" and 3\'6" long',
            "caveats": ["OOC Calls"],
            "description": (
                "This spell allows the spellcaster to throw a stronger bolt of magic than "
                "Magic Missile. The MC for the spell must be made following the Weapon "
                "Construction rules for Lightning Bolts. \nThe prop is a physical "
                "representation of the magic. After it comes to rest, it cannot be affected "
                "or moved by anyone other than the spellcaster, but it may still be seen or "
                "guarded by anybody. The prop counts as a hand-and-a-half weapon and must be "
                "thrown, not shot from a bow. The prop, including its shaft, strikes as a "
                "piercing magic blow to anything it makes contact with, until it comes to "
                "rest. Once cast, it cannot be cast again until the spellcaster recovers the "
                "prop. The prop is not considered a weapon and does not cause Spell Failure, "
                "except while the spell is active (i.e. from when the prop is thrown until "
                "it comes to rest)."
            ),
            "link": "https://www.realmsnet.net/rules/omnibus#lightning-bolt"
        }
]
