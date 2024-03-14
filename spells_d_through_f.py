"""
Realms spell list D-F
Version: 2023
"""

spells = [
        {
            "name": "death watch",
            "circle": 2,
            "uses": "Unlimited, one at a time",
            "active": """Spellcaster must sit without weapons in-hand 
            for 60 seconds before they are killed""",
            "verbal": None,
            "material": None,
            "caveats": ["Precast"],
            "description": """Enables the spellcaster to see and hear while they are dead. 
            You may not speak or move while dead, except for addressing marshaling calls 
            or OOC unsafe/uncomfortable situations. If the spellcaster is rendered soulless, 
            all memories acquired through the current casting of Death Watch are erased 
            (i.e. all memories acquired from the time of your PC\'s last death). 
            The spell ends when the spellcaster is raised or animated as undead.""",
            "link": "https://www.realmsnet.net/rules/omnibus#death-watch"
        },
        {
            "name": "death wish",
            "circle": 4,
            "uses": "2",
            "verbal": "30 words, and an explanation",
            "material": "A scroll containing the trigger phrase and command",
            "active": None,
            "caveats": ["Compulsions"],
            "description": None,
            "link": "https://www.realmsnet.net/rules/omnibus#death-wish"
        },
        {
            "name": "deep pockets",
            "circle": 2,
            "uses": "3",
            "verbal": None,
            "material": 'A bag no larger than 6" by 12" by 3"',
            "active": None,
            "caveats": ["Precast"],
            "description": """Each casting allows spellcaster to deny any stealable items 
            that are completely within the MC to the next three characters that 
            search the spellcaster, while that bag is on the spellcaster\'s body. 
            If the spellcaster is not carrying any stealable items outside of the bag, 
            they may answer, “Nothing.” All other stealable items must be yielded to a search. 
            Each additional learning of this spell allows the spellcaster an additional 6" by 12" 
            by 3" volume of bag, either as a separate bag, or a larger bag. 
            However, the spellcaster can only have one usage cast at a time. 
            Each search denial is used up on all of the volumes simultaneously. 
            One Deep Pockets bag may never contain another. 
            No matter how many Deep Pockets castings are combined it does not combine 
            the amount of people that need to search it; it only increases the size of the bag.""",
            "link": "https://www.realmsnet.net/rules/omnibus#deep-pockets"
        },
        {
            "name": "detect magic",
            "circle": 1,
            "uses": "5",
            "verbal": "20 words",
            "active": None,
            "material": None,
            "caveats": None,
            "description": """This spell allows the spellcaster to take any one item 
            (not a living or dead creature) to the EH or MM to ask whether casting 
            Identify upon the object will yield any information the spellcaster 
            cannot determine by looking at it, such as “It\'s a stick,” or 
            “It\'s a sword.” It may be cast on a living or dead being to detect 
            a magical item it carries, such as a spell focus or magic weapon. 
            In this case, it will not tell what the item does, only that it is 
            there and which item it is. If cast in this manner multiple times and 
            there are multiple magical items, it will not repeat magic items 
            until there are no new items to reveal.""",
            "link": "https://www.realmsnet.net/rules/omnibus#detect-magic"
        },
        {
            "name": "disease weapon",
            "circle": 3,
            "uses": "3",
            "verbal": "10 words",
            "material": "Spellcaster\'s weapon",
            "active": None,
            "caveats": ["Enchanted Items", "OOC Calls", "Weapon Calls"],
            "description": """This spell allows the spellcaster to temporarily 
            enchant their weapon. After preparing it with the spell, 
            it is considered a diseased weapon and the spellcaster 
            must call “Disease” on the next attack with that weapon.""",
            "link": "https://www.realmsnet.net/rules/omnibus#disease-weapon"
        },
        {
            "name": "disenchant",
            "circle": 2,
            "uses": "2",
            "verbal": "30 words",
            "material": None,
            "active": "Touch the target item",
            "caveats": None,
            "description": """This spell will remove enchantments from the target item. 
            If the target item is a potion, panacea, or scroll, 
            it will be rendered inert. If the target is a magic weapon it will 
            no longer function as such until repaired by a Reforge spell. 
            Only magic items specified by the EH or MM are immune to this spell. 
            If the target is a Spell Sash, then the spell represented 
            by the sash is ended. Other spells are not affected unless 
            specified in their description.""",
            "link": "https://www.realmsnet.net/rules/omnibus#disenchant"
        },
        {
            "name": "disrupt",
            "circle": 4,
            "uses": "5",
            "verbal": '30 words, starting with "I disrupt this (spell name)..."',
            "material": None,
            "active": "Clearly point at the target",
            "caveats": ["Suspension"],
            "description": """This spell will suspend any circle or chanting spell. 
            It may only be cast upon a spell that is currently in use. 
            Once the spellcaster completes the disruption, 
            the target spell is suspended for five minutes and the spellcaster 
            of the target spell loses the ability to cast the target spell for five minutes. 
            If the target spell ends before the disruption is completed 
            (the spellcaster stops chanting, the circle is broken, etc.), 
            the spellcaster of that spell still loses the ability to cast that spell for five minutes. 
            This spell only stops the current learning of the target spell. 
            Therefore, if the spellcaster has taken Ward: Enchanted Beings twice, 
            they temporarily lose the ability to cast one, but retain 
            the ability to cast the other.""",
            "link": "https://www.realmsnet.net/rules/omnibus#disrupt"
        },
        {
            "name": "disrupt light",
            "circle": 1,
            "uses": "5",
            "verbal": "20 words, which must clearly state the effect of the spell",
            "active": None,
            "material": None,
            "caveats": None,
            "description": """This spell cancels Light spells cast by other spellcasters. 
            Once the Disrupt Light spellcaster is within sight and hearing of a Light spellcaster, 
            they may loudly call out their verbal. Upon completion of the verbal, 
            all other spellcasters within hearing range must put away their active 
            Light spells. This action is OOC, and those affected must do so even if they 
            hear the spell while dead. Spellcasters so affected cannot recast the 
            Light spell for five minutes, after which time they may reuse 
            the same chemical light sticks.""",
            "link": "https://www.realmsnet.net/rules/omnibus#disrupt-light"
        },
        {
            "name": "divine aid",
            "circle": 4,
            "uses": "1",
            "verbal": "Speak to EH or MM",
            "active": "A quest may be required",
            "material": "A sacrifice may be required",
            "caveats": None,
            "description": """This spell allows the spellcaster to send a request for 
            aid to a higher power. The request cannot be specific and the higher power 
            may send whatever aid they see fit. 
            This spell comes with no guarantee that the EH or MM won\'t 
            simply listen to the request and say “No.” 
            This spell cannot create an effect that will last beyond the end of the event, 
            other than for healing purposes. 
            A spellcaster who uses drama and theatrics has a better chance of success.""",
            "link": "https://www.realmsnet.net/rules/omnibus#divine-aid"
        },
        {
            "name": "dream",
            "circle": 2,
            "uses": "1",
            "verbal": "20 words",
            "material": "Incense or candle",
            "active": None,
            "caveats": None,
            "description": """The spellcaster, after meditation with the MC, goes to sleep. 
            In the morning, when the character wakes up, 
            they may obtain a dream from the EH or MM. 
            This dream will often (but not always) be based around the event plot, 
            and it may be as detailed as the marshal wishes it to be. 
            The spellcaster dreams very lucidly and may write down a permanent 
            record of what they learned through the dream. 
            This spell may be pre-registered, and the results of the Dream 
            will be presented to the spellcaster at check-in.""",
            "link": "https://www.realmsnet.net/rules/omnibus#dream"
        },
        {
            "name": "embrace death",
            "circle": 6,
            "uses": "1",
            "verbal": "40 words",
            "active": None,
            "material": """A container at least 4 inches in diameter, 
            labeled with “Event-Stealable”. The container cannot be placed into Deep Pockets.""",
            "caveats": ["Enchanted Items", "Precast", 
                        "Regeneration", "Basic Regeneration", "Undead"],
            "description": None,
            "link": "https://www.realmsnet.net/rules/omnibus#embrace-death"
        },
        {
            "name": "enchant armor",
            "circle": 4,
            "uses": "1",
            "verbal": "30 words and an explanation",
            "active": None,
            "material": """A non-stealable token with the spellcaster\'s 
            name and the words “Enchant Armor” on it""",
            "caveats": ["Enchanted Items", "Precast"],
            "description": """This spell creates a magical token that allows the 
            spellcaster to continually repair armor worn by a specified character 
            without expending other spells. When the spellcaster casts this spell, 
            they give the token to the specified character, 
            who must keep the token with them for the spell to remain in effect. 
            Once this spell is cast, it may be forcefully ended by disenchanting the token. 
            As long as the specified character has the token, and the spell has not ended, 
            the spellcaster may cast Repair Armor as an unlimited effect on any armor 
            worn by the specified character by performing that spell\'s 
            AC on the targeted hit location. This spell does not require 
            the spellcaster to currently have the spell Repair Armor or 
            have any remaining castings of Repair Armor in order to use this effect.""",
            "link": "https://www.realmsnet.net/rules/omnibus#enchant-armor"
        },
        {
            "name": "enchant weapon",
            "circle": 2,
            "uses": "5",
            "verbal": "10 words",
            "material": None,
            "active": "Hold the target weapon with both hands",
            "caveats": ["Enchanted Items", "OOC Calls", "Weapon Calls"],
            "description": """This spell gives the spellcaster the ability to temporarily 
            enchant a melee weapon or bow. After preparing it with the spell, 
            the weapon or bow user must call “Magic” or “Silver” the next 3 times 
            they swing that weapon or the next 3 times they fire that bow. 
            The spellcaster chooses which option, Magic or Silver, upon casting the spell, 
            and must inform the recipient which option they are imbuing it with. 
            These calls are expended and the casting is spent whether the user 
            scores a successful hit or not, unlike other spells with the Weapon Calls caveat. 
            Also unlike those other spells, anyone may wield the 
            enchanted weapon to make the calls.""",
            "link": "https://www.realmsnet.net/rules/omnibus#enchant-weapon"
        },
        {
            "name": "enfeeble being",
            "circle": 3,
            "uses": "2",
            "verbal": '30 words, starting with "I declare you mundane..."',
            "material": None,
            "active": None,
            "caveats": None,
            "description": """This spell allows the spellcaster to remove the special powers 
            and abilities from a single NPC creature. To cast the spell, 
            the spellcaster must get the creature\'s attention and begin the verbal. 
            Once the spell is completed, the target may lose access to some or all of its abilities. 
            This includes natural armor, spells, regeneration, etc. 
            Because this is a relatively low-circle spell, 
            it will probably have little or no effect on more powerful creatures, 
            such as unique enemies or the proverbial “Big Bad Guy,” 
            but it might work on things like a troll, a lesser demon, or a goblin shaman. 
            This spell will never work on PCs. A spellcaster should choose their targets wisely.""",
            "link": "https://www.realmsnet.net/rules/omnibus#enfeeble-being"
        },
        {
            "name": "familiar",
            "circle": 5,
            "uses": "1. The spellcaster may only have one in-play",
            "verbal": None,
            "material": """A stuffed or toy animal that must be at least 4" tall, 
            labeled with the spellcaster\'s name and the words “Event-Stealable”""",
            "active": None,
            "caveats": ["Suspension"],
            "description": None,
            "link": "https://www.realmsnet.net/rules/omnibus#familiar"
        },
        {
            "name": "feign death",
            "circle": 3,
            "uses": "Unlimited",
            "verbal": None,
            "material": "A cloth",
            "active": "Wipe cloth over face 5 times",
            "caveats": None,
            "description": """This spell allows the spellcaster to disguise themselves so as to 
            appear dead. If someone asks them if they are dead they can legally answer 
            “Yes,” and may lie down or sit with their sword or arm above their head as to 
            appear dead (see rules on character death and soul loss). 
            Feign Death ends once the spellcaster moves or speaks 
            (except for addressing marshaling calls or OOC uncomfortable/unsafe situations). 
            If a person moves them, thinking they are dead, 
            the Feign Death does not end; only when they move themselves. 
            If struck while using Feign Death, 
            the spellcaster is still affected by the blow as normal.""",
            "link": "https://www.realmsnet.net/rules/omnibus#feign-death"
        },
        {
            "name": "fighter's intuition",
            "circle": 1,
            "uses": "3",
            "verbal": None,
            "material": "Spell Sash",
            "active": "place sash on fighter",
            "caveats": ["Enchanted Items", "Spell Sash"],
            "description": """This spell must be cast on a non-spellcaster by placing the sash on 
            the fighter and giving an explanation of how it works. 
            This does not make the fighter an enchanted being. 
            \nThis fighter may now call out “Fighter\'s Intuition” once. 
            When the fighter does this, they may or may not learn information 
            about a monster they can see. It is up to the event staff to decide 
            to provide this information or not. The information can be anything: 
            weakness, methods of defeating, or even what the NPC likes to eat. 
            If the event staff does not provide any information about the monster, 
            the use of the spell is not expended and the fighter may attempt to use it again.""",
            "link": "https://www.realmsnet.net/rules/omnibus#fighters-intuition"
        },
        {
            "name": "find the path",
            "circle": 4,
            "uses": "1",
            "verbal": "30 words",
            "material": None,
            "active": None,
            "caveats": ["Spell Failure"],
            "description": """This spell provides the spellcaster a route to find, locate, 
            or travel to a person, place or thing that they know by name. 
            For instance, you can get a response from “Where is the body of King Joe?” 
            but not from “Take me to the person who stole my sword.” 
            The results of this spell can come as a guide, a map, a set of directions, 
            a divining rod, or any other mechanic that the EH or MM deems appropriate. 
            Be aware that the answer may not always be the safest or shortest path. 
            This spell will fail if an answer cannot be determined because of PC action.""",
            "link": "https://www.realmsnet.net/rules/omnibus#find-the-path"
        },
        {
            "name": "foretell",
            "circle": 4,
            "uses": "1",
            "verbal": "A prediction that the EH or MM must be present for",
            "material": None,
            "active": None,
            "caveats": None,
            "description": """Allows the spellcaster to make a prediction of an event to come, 
            e.g. “Sir Thomas will slay a dragon with a silver sword.” 
            If the event foretold comes to pass the EH or MM may grant a boon to the spellcaster 
            or anyone involved in the prediction. The nature and power of this boon is up to the EH or MM. 
            The greater the foretold event or more specific the prediction, 
            the more powerful the resulting boon should be.""",
            "link": "https://www.realmsnet.net/rules/omnibus#foretell"
        },
        {
            "name": "fortune tell",
            "circle": 3,
            "uses": "2",
            "verbal": None,
            "material": "Fortune-telling paraphernalia, such as runes or a tarot deck",
            "active": None,
            "caveats": ["Spell Failure"],
            "description": """This spell allows the spellcaster to ask a question of 
            the EH or MM, which will be answered in a symbolic manner. 
            How much information (if any) and the form in which it is given is 
            at the discretion of the EH or MM. 
            No proper names may be used in either the question or the answer for this spell. 
            or example, while a spellcaster cannot ask “Who killed Sir Schlep?” 
            they can ask, “Who killed this knight?” and the answer can be 
            “Tarot Card: Jack of Wands” but not “Bad Bart.” 
            This spell can only be used to determine information that is plot-related. 
            If the EH or MM does not know the answer because the question asked 
            relates to PC actions, an answer will not be given, but the spell is 
            still used. If the spell is cast and an answer cannot be given 
            because of any of the above limitations, the casting is still used up.""",
            "link": "https://www.realmsnet.net/rules/omnibus#fortune-tell"
        }
]
