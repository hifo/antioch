"""
Realms spell list M-P
Version: 2023
"""

spells = [
{
            "name": "magic missile",
            "circle": 4,
            "uses": "Unlimited, while spellcaster has MC handy",
            "verbal": "Magic Missile",
            "material": '2 beanbags or foam & duct tape blocks, about 3" diameter',
            "active": None,
            "caveats": ["OOC Calls"],
            "description": """When thrown, this spell strikes whatever it hits as 
            if it were a magic sword. It will damage every location it hits, 
            until it comes to rest. The prop is a physical representation of the magic. 
            After it comes to rest, it cannot be affected or moved by anyone 
            other than the spellcaster, but it may still be seen or guarded by anybody. 
            A magic missile MC can be thrown with one hand. 
            When a MC is being thrown, the other hand may contain only a single magic 
            missile MC or a single-handed weapon or shield, and does not count 
            toward dual-wielding for the purposes of weapon restrictions. 
            The prop is not considered a weapon and does not cause Spell Failure 
            except while the spell is active 
            (i.e. from when the prop is thrown until it comes to rest). 
            The spellcaster may only throw their spell props, 
            and may not pick up those thrown by another spellcaster.""",
            "link": "https://www.realmsnet.net/rules/omnibus#magic-missile"
        },
        {
            "name": "masterwork hammer",
            "circle": 6,
            "uses": "1/special",
            "verbal": "50 words",
            "material": """A boff hammer within the spellcaster\'s weapon restriction with 
            “Masterwork Hammer” and the spellcaster\'s name written on it""",
            "active": 'Special',
            "caveats": ["Enchanted Items", "Precast"],
            "description": """This spell creates a Masterwork Hammer which the spellcaster 
            may use to repair non-armor, non-magic items (bows, weapons, shields) 
            in 30 seconds. The spellcaster may also use the hammer to repair 
            all armor on a target player by using the hammer as the focus of 
            the spell for 60 seconds. While using the hammer to make any type of repair, 
            the spellcaster cannot move their feet and is encouraged to actively use 
            the hammer to simulate repairing the target. 
            If the hammer is broken or disenchanted, the spellcaster may 
            repair it by holding the item in both hands for 120 seconds.""",
            "link": "https://www.realmsnet.net/rules/omnibus#masterwork-hammer"
        },
        {
            "name": "mentor",
            "circle": 1,
            "uses": "Unlimited",
            "verbal": None,
            "material": None,
            "active": None,
            "caveats": None,
            "description": """Allows the spellcaster to teach a legal spell or alternative from 
            their spell mastery list, otherwise following the normal rules for learning spells.""",
            "link": "https://www.realmsnet.net/rules/omnibus#mentor"
        },
        {
            "name": "mystic forge",
            "circle": 4,
            "uses": "1",
            "verbal": "25 words",
            "material": "10-foot rope",
            "active": "Touch the rope",
            "caveats": ["Circles", "Suspension"],
            "description": """This spell allows the spellcaster to create a Mystic Forge. 
            The spellcaster may name the circle with Enchant Weapon or Repair Item, 
            chosen at the time of casting. 
            The spellcaster does not need to have the named spell in their spellbook. 
            Until the Mystic Forge is broken, the spellcaster need only stand in the circle, 
            touch the target item, and recite the named spell\'s VC to cast the spell. 
            This does not use up any castings of the named spell, 
            and this can be done as many times as desired. 
            No one but the spellcaster may use the Mystic Forge in this manner.""",
            "link": "https://www.realmsnet.net/rules/omnibus#mystic-forge"
        },
        {
            "name": "pas",
            "circle": 1,
            "uses": "3",
            "verbal": "Pas, friend…",
            "material": "Food, coin, or some offering",
            "active": "Offer the MC to the target",
            "caveats": ["Compulsions"],
            "description": """This spell creates an uneasy, 
            temporary truce between the target and the PC. 
            To cast this spell, the spellcaster offers something of value to the target and 
            says something along the lines of, 
            “Pas, friend orc, and accept these shiny bits to let me pass unharmed.” 
            If the target accepts the offering, they are magically bound to not attack 
            the spellcaster for 60 seconds, unless the target is attacked. 
            If the target is attacked or the spellcaster is slain, this spell ends immediately. 
            Protect the Soul will block the effects of this spell, as will Resist Magic.""",
            "link": "https://www.realmsnet.net/rules/omnibus#pas"
        },
        {
            "name": "precognition",
            "circle": 3,
            "uses": "3",
            "verbal": None,
            "material": "Divining paraphernalia (such as a crystal ball or mirror)",
            "active": None,
            "caveats": None,
            "description": """This spell allows the spellcaster to gain non-specified information 
            about the plot from the EH or MM. How much information 
            (if any) is at the discretion of the EH or MM.""",
            "link": "https://www.realmsnet.net/rules/omnibus#precognition"
        },
        {
            "name": "prophecy",
            "circle": 6,
            "uses": "1",
            "verbal": None,
            "material": None,
            "active": "Ritual (Optional)",
            "caveats": None,
            "description": """This spell allows the spellcaster to ask the EH or MM a 
            question pertaining to the plot of the event. 
            The EH or MM will give the spellcaster as complete an answer as they are willing. 
            The method of delivering this knowledge is at the EH\'s or MM\'s discretion. 
            A spellcaster may use drama, theatrics, or sacrifice during the ritual 
            to have a better chance of gaining information. After casting this spell, 
            the EH or MM may choose to release additional information to the spellcaster 
            at any time during the remainder of the event or until a spell reset.""",
            "link": "https://www.realmsnet.net/rules/omnibus#prophecy"
        },
        {
            "name": "protect item",
            "circle": 1,
            "uses": "3",
            "verbal": "20 words",
            "material": """Ribbon tied onto the item protected. 
            Remove the ribbon soon after the spell is expended/used to protect the item""",
            "active": None,
            "caveats": ["Enchanted Items", "OOC Calls"],
            "description": """This spell allows a single non-armor item to be protected 
            from the next attack that would normally damage it. 
            For example, a protected sword struck by a boulder would not be destroyed, 
            but the wielder would still suffer normal damage (e.g. death usually). 
            The call for this spell is “Protect Item.” 
            A particular item may only have one casting of Protect Item on it at a time. 
            This spell does not protect against Disenchant.""",
            "link": "https://www.realmsnet.net/rules/omnibus#protect-item"
        },
        {
            "name": "protect the soul",
            "circle": 2,
            "uses": "1",
            "verbal": "30 words and an explanation",
            "material": "Spell Sash",
            "active": None,
            "caveats": ["Enchanted Items", "OOC Calls", "Precast", "Spell Sash"],
            "description": None,
            "link": "https://www.realmsnet.net/rules/omnibus#protect-the-soul"
        },
        {
            "name": "protection from boulder",
            "circle": 1,
            "uses": "2",
            "verbal": "20 words",
            "material": "Spell sash",
            "active": None,
            "caveats": ["Enchanted Items", "OOC Calls", "Precast", "Spell Sash"],
            "description": """The spellcaster is protected from the next “boulder” 
            call that strikes them. This protection extends to all equipment they are carrying.""",
            "link": "https://www.realmsnet.net/rules/omnibus#protection-from-boulder"
        },
        {
            "name": "protection from missile",
            "circle": 2,
            "uses": "Unlimited, one at a time",
            "verbal": "10 words",
            "material": "Spell Sash",
            "active": "Kneel or lie on back, no weapons in hand",
            "caveats": ["Enchant Items", "OOC Calls", "Precast", "Spell Sash"],
            "description": """The recipient of this spell is protected from the 
            next hit they take from an arrow, javelin, or Magic Missile spell. 
            It is necessary to call “Protection” when the spell activates. 
            This spell will also protect equipment (such as armor) 
            that would otherwise be affected by the missile. \n When the spell is cast,
              the recipient of the spell must be kneeling or be lying on 
              their back with no weapons in hand. This spell may be cast on a 
              recipient other than the spellcaster; to do so the spellcaster must 
              have no weapons in hand and touch the recipient while 
              the spell is being cast. More than one casting of this 
              spell may be in effect on a single PC. If the spellcaster 
              casts this spell on another PC, they may not re-cast the 
              spell until the sash is returned to them.""",
            "link": "https://www.realmsnet.net/rules/omnibus#protection-from-missile"
        },
        {
            "name": "purity to disease",
            "circle": 3,
            "uses": "1, Self-only",
            "verbal": "10 words",
            "material": "Spell Sash",
            "active": "Lie on back, no weapons in hand",
            "caveats": ["Enchanted Items", "OOC Calls", "Precast", "Spell Sash"],
            "description": """Upon casting this spell, the spellcaster 
            becomes completely immune to the effects of diseases.""",
            "link": "https://www.realmsnet.net/rules/omnibus#purity-to-disease"
        },
        {
            "name": "purity to poison",
            "circle": 3,
            "uses": "1, Self-ony",
            "verbal": "10 words",
            "material": "Spell Sash",
            "active": "Lie on back, no weapons in hand",
            "caveats": ["Enchanted Items", "OOC Calls", "Precast", "Spell Sash"],
            "description": """Upon casting this spell, the spellcaster becomes 
            completely immune to the effects of poisons.""",
            "link": "https://www.realmsnet.net/rules/omnibus#purity-to-poison"
        }
]