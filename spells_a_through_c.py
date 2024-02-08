"""
Realms spell list A-C
Version: 2023
"""

spells = [
        {
            "name": "animal companion",
            "circle": 4,
            "uses": "1, and the spellcaster may only have one in-play",
            "material": 'A stuffed or toy animal that must be at least 4" tall',
            "active": None,
            "caveats": ["Suspension"],
            "description": """The spellcaster has an animal companion represented 
            by a specific stuffed or toy animal. 
            The animal companion cannot be slain or disenchanted, 
            but can be stolen. 
            The stuffed animal must be labeled with the spellcaster\'s name and the words “Event-Stealable.” 
            The animal companion grants two separate abilities. 
            The first ability is that the spellcaster may send their animal companion to 
            gather information once per learning of the spell. 
            The information gathered can only be relayed in a short sentence or concept, such as “the way ahead is blocked,” 
            or “there are many foes,” etc. 
            This ability is represented by the spellcaster giving their animal companion to the 
            EH or MM and asking them a question. If the spellcaster asks for information that their 
            animal companion is unable to obtain, they receive no answer. 
            \nThe second ability that the animal companion grants is the ability to cast a single spell up to third circle, 
            except the spell Implement, which cannot be chosen. 
            This spell will function as if it were learned normally, 
            with the same requirements, limitations, number of castings, and components. 
            While the animal companion is out gathering information the spells provided from 
            the secondary ability are suspended. \nAny additional spells provided by the animal 
            companion require the animal companion to cast and maintain, as if the animal companion 
            were a spell focus. Each spell must meet the requirement for verbal, material 
            and active components. Spells with lasting effects (protections, immunities, etc.) 
            can only be cast upon the spellcaster. 
            Any blow that strikes the animal companion must be taken as if the animal companion is not there. 
            \nWhen the spellcaster first learns this spell, they choose their animal companion\'s abilities. 
            These abilities are not alterable from event to event. The spellcaster must list in their 
            spellbook every spell their animal companion grants them as if they have learned the spell. 
            \nIf they learn the spell additional times, the animal companion gets stronger. 
            They may alter the abilities of their animal companion upon completion of 
            each learning by giving it an additional spell and question. 
            If the spellcaster unlearns a use of the spell, 
            the animal companion becomes weaker and must be adjusted accordingly.""",
            "link": "https://www.realmsnet.net/rules/omnibus#animal-companion"
        },
        {
            "name": "animate lesser undead",
            "circle": 3,
            "uses": "3",
            "material": """A tabard, or sash which clearly states “Undead,” “Skeleton,” 
            “Ghost” or the like, or an appropriate mask""",
            "active": None,
            "caveats": ["Compulsions", "Thrall", "Undead"],
            "description": """This spell animates a weak undead thrall 
            that cannot use any armor or spells. 
            It will work on PCs but won\'t always work on NPCs; 
            if cast on NPCs, they can refuse. 
            If an NPC refuses a casting of the spell, the casting is not spent.""",
            "link": "https://www.realmsnet.net/rules/omnibus#animate-lesser-undead"       
        },
        {
            "name": "animate undead",
            "circle": 4,
            "uses": "2",
            "verbal": "30 words, and an explanation",
            "material": """A tabard, or sash which clearly states “Undead,” “Skeleton,” 
            “Ghost” or the like, or an appropriate mask""",
            "active": None,
            "caveats": ["Compulsions", "Thrall", "Undead"],
            "description": """This spell animates an undead thrall that can use any spells or 
            weapons the target normally could use. 
            If Animate Lesser Undead is cast upon the target while the target is still undead, 
            it will reanimate the target as if another Animate Undead spell were cast upon it, 
            but the target\'s loyalties transfer to the person who cast Animate Lesser Undead.""",
            "link": "https://www.realmsnet.net/rules/omnibus#animate-undead"
        },
        {
            "name": "animate undead general",
            "circle": 5,
            "uses": "1",
            "verbal": "40 words, and an explanation",
            "active": None,
            "material": """A tabard, or sash which clearly states “Undead,” “Skeleton,” 
            “Ghost” or the like, or an appropriate mask, a written explanation of what 
            this spell does, and you must supply them with 3 MCs 
            for the Animate Lesser Undead spells they will cast.""",
            "caveats": ["Compulsions", "Thrall", "Undead"],
            "description": None,
            "link": "https://www.realmsnet.net/rules/omnibus#animate-undead-general"
        },
        {
            "name": "armor-piercing weapon",
            "circle": 5,
            "uses": "4",
            "material": "A cloth",
            "active": "Wipe the entire length of the weapon's striking surface 5 times",
            "caveats": ["Enchanted Items", "OOC Calls", "Weapon Calls"],
            "description": """This spell gives the spellcaster the ability to 
            enhance their weapon to pass through and destroy armor. 
            After preparing the spell the spellcaster must call “Piercing” 
            on the next attack with that weapon.""",
            "link": "https://www.realmsnet.net/rules/omnibus#armor-piercing-weapon"
        },
        {
            "name": "armored cloak",
            "circle": 4,
            "uses": "Unlimited, one at a time",
            "verbal": "30 words",
            "material": "Garb with obvious runes or mystic symbols",
            "active": """Kneel while wearing the garb, with no weapons or shields in hands, 
            or lie on back while wearing the garb""",
            "caveats": ["OOC Calls", "Precast"],
            "description": """This spell enchants some of your garb to provide one call of 
            armor against an attack. It provides one point of armor against 
            the next blow that lands upon one of the garments or any 
            location at least 75% covered by one of the garments. 
            \nThis Armored Cloak cannot be worn in combination with any other form of armor, ever. 
            It can be worn while protected by a Protection from Missile or Resist Magic spell, 
            in which case the wearer can choose to call either protection, 
            saving the other for later. It can only be worn by the spellcaster, 
            and the spell cannot be cast on any of the garments more than once at a time. 
            Specific garb must be chosen for the MC at the beginning of the event, 
            and it cannot be changed during the course of the event without the EH\'s or MM\'s permission.
                \nA spellcaster can only cast one Armored Cloak at a time.""",
            "link": "https://www.realmsnet.net/rules/omnibus#armored-cloak"
        },
        {
            "name": "assassin's blade",
            "circle": 6,
            "uses": "Unlimited, one at a time",
            "verbal": None,
            "material": """A cloth, and either a single weapon or arrow 
            within the spellcaster\'s weapon restriction, 
            labeled with “Assassin\'s Blade” and the spellcaster\'s name""",
            "active": "Wipe the entire length of the blade 5 times",
            "caveats": ["Enchanted Items", "OOC Calls", "Precast", "Weapon Calls"],
            "description": """This spell allows the spellcaster to prepare their MC with the 
            spells Armor-Piercing Weapon, Enchant Weapon, or Create Poison, 
            without expending a casting, although a use of the spell must still remain in order to prepare it. 
            To prepare the weapon with one of the listed spells, 
            they must wipe the blade of the weapon with the cloth 5 times. 
            Only one spell may be prepared at a time onto the Assassin\'s Blade. 
            Anyone may use the weapon, but only the spellcaster may utilize the special call with it. 
            The weapon is one-handed, but may not be used in conjunction with another weapon or shield by the spellcaster. 
            If the MC is IC broken, it will retain its magical properties if repaired. 
            \nIn addition, any body destroying blow dealt by 
            an Assassin\'s Blade counts as two blows dealt.""",
            "link": "https://www.realmsnet.net/rules/omnibus#assassins-blade"
        },
        {
            "name": "aura of protection",
            "circle": 2,
            "uses": "Unlimited, one at a time per learning",
            "verbal": "20 words",
            "material": "Spell Sash",
            "active": "Kneel or lie on back, no weapons in hand",
            "caveats": ["Enchanted Items", "OOC Calls", "Spell Sash", "Precast"],
            "description": """The recipient of this spell lessens the effect of the next 
            hit they take from a call of “Magic,” “Silver,” “Disease,” 
            “Piercing,” “Lightning Bolt,” or “Poison.” 
            Rather than taking the effect they were hit with, 
            the recipient of the spell takes the blow as a normal sword blow instead. 
            It is necessary to call “Protection” when the spell activates. 
            \nWhen the spell is cast, the recipient of the spell must be kneeling 
            or be lying on their back with no weapons in hand. 
            This spell may be cast on a recipient other than the spellcaster; 
            to do so the spellcaster must have no weapons in hand and touch the 
            recipient while the spell is being cast. 
            More than one casting of this spell may be in effect on a single PC. 
            If the spellcaster casts this spell on another PC, 
            they may not re-cast the spell until the sash is returned to them.""",
            "link": "https://www.realmsnet.net/rules/omnibus#aura-of-protection"
        },
        {
            "name": "beckon corpse",
            "circle": 3,
            "uses": "5",
            "verbal": "20 words, repeated continuously, stating purpose of spell",
            "material": None,
            "active": "Spellcaster must be stationary until finished",
            "caveats": ["Chanting", "Suspension", "Undead", "Walking Dead"],
            "description": """This spell allows the spellcaster to summon a corpse 
            to get up and move to them as the Walking Dead. 
            The spellcaster must first get the attention of the player of said 
            corpse and begin chanting the verbal. As long as the chanting continues, 
            the corpse will get up and walk in the most direct (but OOC safe) 
            path to the spellcaster as if under the effects of the spell Zombie Walk. 
            If the corpse is interrupted, it will fall to the ground, 
            but the spellcaster may finish the current round of the verbal, 
            regain the corpse\'s attention, 
            and resume chanting the verbal to renew the effect on the corpse. 
            The spell will end if the corpse reaches the spellcaster, 
            the spellcaster stops chanting to do something else, 
            or they move from where they are standing (although they may be moving their arms).""",
            "link": "https://www.realmsnet.net/rules/omnibus#beckon-corpse"
        },
        {
            "name": "call the soul",
            "circle": 4,
            "uses": "2",
            "verbal": "30 words",
            "material": """Five objects of equal size and shape, 
            four of one color or design and one of a second color or design, 
            and an opaque pouch or other way to keep them hidden""",
            "active": "A quest may be required",
            "caveats": None,
            "description": """Allows the spellcaster to possibly find and reattach 
            the soul of a soulless character. When cast, the spellcaster presents 
            the pouch of objects to the soulless character, 
            who must then reach in and take one without looking. 
            If the object is one of the four, the soul is reattached. 
            If the object is the second color or design, 
            nothing happens. This spell must be cast in the presence of the EH or MM, 
            who may require an additional quest be completed.""",
            "link": "https://www.realmsnet.net/rules/omnibus#call-the-soul"
        },
        {
            "name": "cantrip",
            "circle": 3,
            "uses": "3",
            "verbal": None,
            "material": None,
            "active": None,
            "caveats": None,
            "description": """Allows the spellcaster to gain one casting of any First Circle spell, 
            chosen at the time of casting. 
            The spell gained must be cast following the rules for that spell, 
            including VC, MC, and ACs. This spell cannot be 
            used to cast Implement or Strange Brew.""",
            "link": "https://www.realmsnet.net/rules/omnibus#cantrip"
        },
        {
            "name": "circle of healing",
            "circle": 5,
            "uses": "1",
            "verbal": "25 words",
            "material": "10-foot rope",
            "active": "Touch the rope",
            "caveats": ["Circles", "Suspension"],
            "description": """This spell allows the spellcaster to create a Circle of Healing. 
            The spellcaster may name the circle with Cure Disease, Heal Limb, 
            or Raise Dead, chosen at the time of casting. 
            The spellcaster does not need to have the named spell in their spellbook. 
            While the spellcaster is standing in the Circle of Healing, 
            they may cast the named spell as many times as desired without 
            consuming a use of that spell. Except for the MC of Cure Disease, 
            all of the requirements of the named spell must be met for each casting, 
            including the AC and VC. No one but the spellcaster may use the Circle of Healing 
            in this manner. This spell is broken if a weapon crosses the plane of the circle. 
            For this purpose, a weapon is considered to be anything with a legal 
            striking surface - therefore, swords and arrows are weapons, 
            although bows and shields are not.""",
            "link": "https://www.realmsnet.net/rules/omnibus#circle-of-healing"
        },
        {
            "name": "circle of protection",
            "circle": 4,
            "uses": "Unlimited, one at a time",
            "verbal": "10 words",
            "material": "15-foot white rope, or less",
            "active": None,
            "caveats": ["Circles", "Suspension", "Enchanted Beings"],
            "description": None,
            "link": "https://www.realmsnet.net/rules/omnibus#circle-of-protection"
        },
        {
            "name": "combat raise dead",
            "circle": 4,
            "uses": "3",
            "verbal": "3 words",
            "material": None,
            "active": "Must touch recipient of spell",
            "caveats": None,
            "description": """This spell will raise a dead character, 
            healing all of their injured limbs. 
            The VC must clearly state the effects of the spell. 
            For example, “Rise and fight” is a VC that would make it 
            clear that the individual is being raised.""",
            "link": "https://www.realmsnet.net/rules/omnibus#combat-raise-dead"
        },
        {
            "name": "commune with spirit",
            "circle": 3,
            "uses": "1",
            "verbal": None,
            "material": None,
            "active": """Ritual - it is required that the spellcaster not actively 
            seek out the EH or MM. The ritual must, in effect, 
            be spectacular enough that the EH or MM comes of their own volition""",
            "caveats": None,
            "description": """Allows the spellcaster to gain a boon of insight/wisdom 
            from the EH or MM. This spell allows the spellcaster to ask a spirit 
            something relating to the plot of the event. 
            How detailed the response or how lengthy the conversation is with the spirit, 
            is determined completely by the spirit. It should be noted that the 
            spirit does not have to answer the call of the spellcaster, 
            and that sometimes instead of helping solve a problem, 
            may give the spellcaster an awareness of more problems that need solving.""",
            "link": "https://www.realmsnet.net/rules/omnibus#commune-with-spirit"
        },
        {
            "name": "create poison",
            "circle": 4,
            "uses": "6",
            "verbal": None,
            "material": "Disposable edible or drinkable component",
            "active": None,
            "caveats": ["Enchanted Items", "Compulsions", "OOC Calls", "Weapon Calls"],
            "description": None,
            "link": "https://www.realmsnet.net/rules/omnibus#create-poison"
        },
        {
            "name": "cry of life",
            "circle": 6,
            "uses": "1",
            "verbal": "All in the sound of my voice, rise and fight",
            "active": None,
            "material": None,
            "caveats": None,
            "description": """This spell instantly raises all dead characters 
            whose players hear the verbal. The spell affects all who hear it, 
            including NPCs and characters fighting against the spellcaster.""",
            "link": "https://www.realmsnet.net/rules/omnibus#cry-of-life"
        },
        {
            "name": "cure disease",
            "circle": 1,
            "uses": "5",
            "verbal": "20 words",
            "active": None,
            "material": "disposable",
            "caveats": None,
            "description": """This spell will cure the recipient of all diseases
              that are currently affecting them. It will not provide 
              protection from catching a disease after the spell is cast.""",
            "link": "https://www.realmsnet.net/rules/omnibus#cure-disease"
        }
    ]
