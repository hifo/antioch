"""
Realms spell list R-Z
Version: 2023
"""


spells = [
    {
            "name": "raise dead",
            "circle": 3,
            "uses": "5",
            "verbal": "30 words",
            "material": None,
            "active": """Spellcaster must be within 2 feet of corpse and there can 
            be no weapons within 10 feet of the spellcaster""",
            "caveats": ["Spell Failure"],
            "description": """This spell will raise a dead character, 
            healing all of their injured limbs. 
            There can be no weapons within 10 feet of the spellcaster 
            at any point while casting this spell, or the spell will fail to work. 
            For this purpose, a weapon is considered to be anything 
            with a legal striking surface - swords and arrows are weapons, 
            although bows are not. The player of the character being raised must be 
            present to represent the corpse. No proxy can be used for the corpse.""",
            "link": "https://www.realmsnet.net/rules/omnibus#raise-dead"
        },
        {
            "name": "reforge",
            "circle": 5,
            "uses": "2",
            "verbal": "30 words",
            "material": "Special",
            "active": "Special",
            "caveats": None,
            "description": None,
            "link": "https://www.realmsnet.net/rules/omnibus#reforge"
        },
        {
            "name": "regenerate the soul",
            "circle": 5,
            "uses": "1",
            "verbal": "30 words",
            "material": None,
            "active": None,
            "caveats": ["Precast", "Regeneration", "Advanced Regeneration"],
            "description": """This spell grants an advanced regeneration 
            which returns a character to life from soullessness only.""",
            "link": "https://www.realmsnet.net/rules/omnibus#regenerate-the-soul"
        },
        {
            "name": "regeneration",
            "circle": 5,
            "uses": "2",
            "verbal": "30 words",
            "material": None,
            "active": """Spellcaster must sit on the ground with weapons a 
            minimum of 10 feet away while casting this spell""",
            "caveats": ["Precast", "Regeneration", "Advanced Regeneration", "Spell Failure"],
            "description": """This spell grants the spellcaster an advanced regeneration. 
            If you have learned this spell twice, you may cast a Raise Dead to “recharge” one usage. 
            These recharges cannot come from Circle of Healing, 
            or any other raising effects other than the Raise Dead spell.""",
            "link": "https://www.realmsnet.net/rules/omnibus#regeneration"
        },
        {
            "name": "repair armor",
            "circle": 1,
            "uses": "5",
            "verbal": None,
            "material": "Disposable or focus",
            "active": "Hold armor and MC for 15 second count",
            "caveats": None,
            "description": """This spell will repair one hit location of armor. 
            You are encouraged to simulate physically repairing the armor, 
            such as tapping it with a focus, like a boff-hammer.""",
            "link": "https://www.realmsnet.net/rules/omnibus#repair-armor"
        },
        {
            "name": "repair item",
            "circle": 2,
            "uses": "5",
            "verbal": "20 words",
            "material": None,
            "active": "Touch the target item with both hands",
            "caveats": None,
            "description": """This spell repairs any one normal object: a weapon, 
            shield, bow or armor. It cannot repair an item with a special property, 
            such as a magic item. If used to repair armor that is being worn, 
            a single casting will repair all pieces of armor that can be legally 
            called by the wearer. The spellcaster may have nothing else 
            in their hands while casting this spell.""",
            "link": "https://www.realmsnet.net/rules/omnibus#repair-item"
        },
        {
            "name": "resist death",
            "circle": 6,
            "uses": "Unlimited, one at a time",
            "verbal": "30 words",
            "material": "Spell Sash",
            "active": "Kneel or lie on back, no weapons in hand.",
            "caveats": ["Enchanted Items", "OOC Calls", "Precast", "Spell Sash"],
            "description": """The spellcaster is protected from any damaging attack for 1 hit. 
            The call for this is “Resist Death.” 
            The spellcaster can choose when to utilize this effect.""",
            "link": "https://www.realmsnet.net/rules/omnibus#resist-death"
        },
        {
            "name": "resist magic",
            "circle": 5,
            "uses": "3",
            "verbal": "20 words",
            "material": None,
            "active": None,
            "caveats": ["OOC Calls", "Precast"],
            "description": """This spell prepares a burst of null-magic within the spellcaster. 
            If the spellcaster so desires, they may ignore a single magical effect. 
            This ability can be used at any time, whether the spellcaster is dead or not. 
            A spellcaster may not be under the effect of more than one Resist Magic spell 
            at the same time. When targeted by a spell or effect against which Resist Magic 
            protects them and the spellcaster wishes to ignore the effect, 
            they call “Resist Magic.” For example: this spell will allow the spellcaster to 
            treat a blow from a magic weapon as if it were a normal weapon blow, 
            ignore the effect of any spell when it is first cast, 
            ignore any potion when it\'s first applied, or cross the boundary of a Circle of Protection. 
            The spell ends if the spell Disenchant is cast upon the spellcaster 
            (although the spellcaster can use the Resist Magic to prevent the Disenchant 
            from removing any other spells upon them). 
            This spell cannot be cast on anyone other than the spellcaster 
            and will only protect the spellcaster, not anything they have or possess.""",
            "link": "https://www.realmsnet.net/rules/omnibus#resist-magic"
        },
        {
            "name": "ritual of banishment",
            "circle": 6,
            "uses": "Special, see below",
            "verbal": "40 words in “burst” form, otherwise special, see below",
            "material": None,
            "active": None,
            "caveats": None,
            "description": None,
            "link": "https://www.realmsnet.net/rules/omnibus#ritual-of-banishment"
        },
        {
            "name": "seance",
            "circle": 4,
            "uses": "1",
            "verbal": "20 words to start",
            "material": "3-minute hourglass/timer",
            "active": "Speak to EH or MM",
            "caveats": None,
            "description": """This spell allows the spellcaster to 
            have an extended discussion with a spirit, 
            either one of another world or of a soulless character. 
            Upon informing the EH or MM of their intent to cast this spell, 
            the spellcaster must start the ritual by flipping the hourglass. 
            If the spirit does not arrive within the first three minutes, 
            then the casting is not used. If the spirit arrives, 
            let the glass run out and flip it again. 
            The spellcaster and spirit may then speak freely until all the sands have fallen. 
            If the spirit stays longer than three minutes, 
            the spellcaster may continue to converse with it. 
            Please note that this spell does not change any behavior on the part of the spirit, 
            and it may choose not to talk. 
            \n Whether a soulless character can answer is entirely up to the discretion of the EH or MM, 
            who must be present for the ritual. 
            This spell in no way grants the knowledge of the circumstances of a soulless character\'s death. 
            If they are allowed to be contacted, the soulless PC can still refuse to answer, 
            is not compelled to speak, can lie or tell the truth freely, 
            and can end the séance at any time. 
            A PC contacted with a séance must leave after three minutes.""",
            "link": "https://www.realmsnet.net/rules/omnibus#seance"
        },
        {
            "name": "second chance",
            "circle": 6,
            "uses": "1",
            "verbal": None,
            "material": None,
            "active": "Speak to EH or MM",
            "caveats": None,
            "description": """This spell allows the spellcaster to recover once, 
            even from the most grievous of wounds and situations. 
            \n After the spell is cast, the spellcaster may activate the spell, 
            which removes them from play. They must then go find the EH or MM. 
            All stealable items in possession of the spellcaster must be left behind. 
            This spell may be activated even if the spellcaster is dead or soulless. 
            \n The EH or MM will then place them somewhere on site 
            (location determined by the EH or MM). Upon being placed, 
            the spellcaster is alive and unwounded.""",
            "link": "https://www.realmsnet.net/rules/omnibus#second-chance"
        },
        {
            "name": "seed of life",
            "circle": 6,
            "uses": "Unlimited, while spellcaster has MC handy",
            "verbal": "30 words and an explanation",
            "material": ' 2 tokens with the spellcaster\'s name and the words “Seed of Life” on it',
            "active": None,
            "caveats": ["Regeneration", "Basic Regeneration"],
            "description": """When cast on a dead body, 
            this spell grants the recipient a basic regeneration. 
            The spellcaster must hand the MC to the recipient when the spell is cast. 
            \nOnce the spell ends, the recipient needs to return the MC to the spellcaster as soon as reasonably possible. 
            Other than this, the MC is neither stealable nor transferable in any way. 
            If the recipient is rendered soulless, the spell ends. 
            If the recipient is diseased, this spell will also cure them of their disease upon completion of the spell 
            (although the regeneration time will still be doubled from the effects of the disease). 
            This spell has no effect on animated undead. 
            \nIf the spell is cast with both tokens on the same recipient, 
            then the recipient will regenerate in 
            three-fourths the normal time (usually 90 seconds).""",
            "link": "https://www.realmsnet.net/rules/omnibus#seed-of-life"
        },
        {
            "name": "shapeshifting",
            "circle": 3,
            "uses": "2",
            "verbal": None,
            "material": "Makeup and/or mask and any disguise garb",
            "active": "Change into disguise",
            "caveats": ["Enchanted Items"],
            "description": """This allows the spellcaster to shapeshift into a humanoid 
            monster of about their height and size. 
            This transformation takes as long to complete as it takes the player 
            to change into the appropriate disguise outfit. The type and features 
            of the monster are up to the player. Once the shapeshifting is complete, 
            the player will respond to the spell Identify as the new type of monster. 
            This spell will mimic a general monster type, and cannot accurately 
            impersonate a named or unique monster, or appear to be another PC. 
            You are free however, to attempt to convince your victims that you 
            are more important than you actually are. \n The shapeshifted form 
            confers no combat benefit or other NPC power, though they can appear 
            to wear armor or carry larger weapons to complete the disguise. 
            You may in no way signal to NPCs that you are NPCing. The shapeshifted 
            form ends if you are killed or if any part of your disguise is disenchanted. 
            \n In addition, at the door of the event, the player is allowed to ask the 
            EH or MM to borrow an appropriate mask for the event in order to complete the illusion. 
            There is no guarantee that they will be able to provide the materials, 
            so you may wish to bring your own.""",
            "link": "https://www.realmsnet.net/rules/omnibus#shapeshifting"
        },
        {
            "name": "skew divination",
            "circle": 3,
            "uses": "2",
            "verbal": "30 words",
            "material": "Scroll with a name of an item, person, group, place, or situation",
            "active": "Give scroll to EH or MM",
            "caveats": None,
            "description": """This spell will alter the next Guidance, Fortune Tell, Precognition, 
            Find the Path, Foretell, Séance, Vision, or 
            Prophecy spell cast about the target at that event, giving them misinformation. 
            How much the spell is altered is up to the EH or MM. To cast this spell, 
            the spellcaster must write the name of the target (item, person, 
            group, place, or situation) on a scroll, sign the scroll, 
            and give the scroll to the EH or MM.""",
            "link": "https://www.realmsnet.net/rules/omnibus#skew-divination"
        },
        {
            "name": "soul bane",
            "circle": 3,
            "uses": "1",
            "verbal": None,
            "material": None,
            "active": """Destroy a dead body. 
            Following the final body destroying blow the spellcaster says “Soul Bane.”""",
            "caveats": ["OOC Calls"],
            "description": """This spell alters the next Call the Soul cast on the target 
            by reversing which object is successful and unsuccessful. 
            The spellcaster must inform the EH or MM whose body they destroyed 
            and cast Soul Bane on as soon possible. 
            The effect triggers the next time the target\'s soul is called. 
            The spell ends after the first Call the Soul, whether it was successful or not. 
            Only one Soul Bane can be active on a person at a time.""",
            "link": "https://www.realmsnet.net/rules/omnibus#soul-bane"
        },
        {
            "name": "speak",
            "circle": 1,
            "uses": "2",
            "verbal": "Speak, friend…",
            "material": "An offering for the creature to be spoken with",
            "active": """The spellcaster approaches the creature with no weapons
              and with an offering in plain sight, and hands it to the creature""",
            "caveats": None,
            "description": """This spell allows the spellcaster to approach a 
            creature and present an offering to them. 
            If the offering is taken, the creature now has the ability to speak 
            and understand the language of the spellcaster. 
            This ability lasts until the creature is no longer in possession of the offering. 
            No creature approached has to take the offering, 
            nor is there any guarantee that the creature will speak to you.""",
            "link": "https://www.realmsnet.net/rules/omnibus#speak"
        },
        {
            "name": "speak with dead",
            "circle": 1,
            "uses": "10",
            "verbal": "An explanation, followed by a question",
            "material": None,
            "active": None,
            "caveats": ["Compulsions"],
            "description": """This spell allows the spellcaster to ask
              a corpse one "yes or no" question. 
            The corpse may only answer "Yes," "No," or "Abstain," 
            and it may not lie. An abstention means that the spirit cannot or does not want to answer the question. 
            Before asking the questions, the spellcaster must explain to the corpse\'s 
            player what the acceptable responses are and that the character may not lie.""",
            "link": "https://www.realmsnet.net/rules/omnibus#speak-with-dead"
        },
        {
            "name": "strange brew",
            "circle": 1,
            "uses": "Special, see Alchemy",
            "verbal": None,
            "material": None,
            "active": None,
            "caveats": ["OOC Calls", "Potions"],
            "description": None,
            "link": "https://www.realmsnet.net/rules/omnibus#strange-brew"
        },
        {
            "name": "transformation",
            "circle": 6,
            "uses": "2",
            "verbal": None,
            "material": "A pair of Transformation Claws",
            "active": None,
            "caveats": ["Regeneration", "Advanced Regeneration",
                         "OOC Calls", "Precast", "Suspension"],
            "description": None,
            "link": "https://www.realmsnet.net/rules/omnibus#transformation"
        },
        {
            "name": "transmute self",
            "circle": 4,
            "uses": "3",
            "verbal": "10 word chant, repeated. The verbal must be chanted loudly and clearly",
            "material": None,
            "active": None,
            "caveats": ["Chanting", "OOC Calls", "Suspension"],
            "description": """This spell provides an immense amount of protection
              to the spellcaster,
              but also requires an immense amount of concentration. 
              This spell only takes effect once the spellcaster has completed the VC once. 
              While transmuted, the spellcaster is completely immune to all forms of damage, 
              magical or otherwise, regardless of whether the material into which the spellcaster 
              transmutes is vulnerable to any form of damage. 
              It does not make the spellcaster invisible or undetectable. 
              The spellcaster must choose what they are capable of attuning to when learning the spell. 
              Choices are: trees, stone, or earth. To transmute, 
              the spellcaster must embrace or lie down on the object they 
              are capable of attuning to (so those who can attune to trees 
              hug a tree, to stone lie on or hug a rock, or to earth lie on the ground). 
              While transmuted, the spellcaster is “stuck” and cannot be dragged. 
              The object the spellcaster attunes with MUST be at least as massive as the spellcaster. 
              The spellcaster must keep their eyes closed and remain perfectly still, 
              and they must be constantly chanting their verbal while transmuted. 
              The spellcaster must chant loudly and clearly. If anything interrupts the spellcaster\'s concentration, 
              the spell is broken. OOC explanations (such as combat calls) do not interrupt this spell. 
              For example, if a PC chanting a Transmute Self spell is hit by a weapon, 
              they may call “No effect” without interrupting the spell. 
              As soon as the spellcaster moves, opens their eyes, or stops chanting, the spell ends. 
              The spellcaster may not transmute for at least one slow 200 second count after regaining their proper form. 
              The spellcaster must use their common sense when deciding where to transmute. 
              Pick a safe location, not the middle of a trail or a high combat area.""",
            "link": "https://www.realmsnet.net/rules/omnibus#transmute-self"
        },
        {
            "name": "vision",
            "circle": 5,
            "uses": "1",
            "verbal": None,
            "material": None,
            "active": None,
            "caveats": None,
            "description": """This spell allows the spellcaster to ask the EH or MM a question. 
            The EH or MM will then reveal to the spellcaster as complete a description 
            as they are willing to give, giving them a vision relating to it.""",
            "link": "https://www.realmsnet.net/rules/omnibus#vision"
        },
        {
            "name": "ward enchanted beings",
            "circle": 5,
            "uses": "Unlimited",
            "verbal": "20 words, repeated continuously, stating purpose of spell",
            "material": "Focus",
            "active": None,
            "caveats": ["Chanting", "Suspension", "Wards"],
            "description": """This spell prevents Enchanted Beings
              from attacking the spellcaster while it is active.""",
            "link": "https://www.realmsnet.net/rules/omnibus#ward-enchanted-beings"
        },
        {
            "name": "ward undead",
            "circle": 2,
            "uses": "Unlimited",

            "verbal": "10 words, repeated continuously, stating purpose of spell",
            "material": "Focus",
            "active": None,
            "caveats": ["Chanting", "Suspension", "Wards"],
            "description": """This spell prevents Undead from 
            attacking the spellcaster while it is active.""",
            "link": "https://www.realmsnet.net/rules/omnibus#ward-undead"
        },
        {
            "name": "zombie walk",
            "circle": 1,
            "uses": "Unlimited, 1 at a time",
            "verbal": "10 words, plus an explanation",
            "material": None,
            "active": "Touch the target",
            "caveats": ["Undead", "Walking Dead"],
            "description": """This spell allows the spellcaster to animate a corpse, 
            making it follow them for as long as they concentrate on the spell. 
            If the spellcaster engages in combat either by attacking or by being struck, 
            the spell ends and the corpse falls to the ground. In order to cast this spell, 
            the spellcaster must recite the verbal and give the player of the corpse a 
            brief explanation of what they should do, making sure they know when to fall down.""",
            "link": "https://www.realmsnet.net/rules/omnibus#zombie-walk"
        },
]
