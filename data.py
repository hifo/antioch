caveats = [
    {
        "name": "Suspension",
        "desc": "While a spell is suspended, the spell has no effect and does not function until the suspension ends. In addition, a suspended spell can be ended any way it normally could. It is the spellcaster’s responsibility to notify anyone else who is affected by this (such as any players carrying potions that the spellcaster created). When the suspension ends, any spell which has not already ended will resume functioning as per normal."
    },
    {
        "name": "OOC Calls",
        "desc": "These are special OOC calls to inform and describe specific IC game effects, These calls do not break verbals, chants or other VCs as they are purely game mechanics and martialing tools. All spells that utilize special combat calls describe the specific call that must be made with its use."
    },
    {
        "name": "Chanting",
        "desc": 'Some spells require that their VC be chanted continuously for the duration of the spell. These spells do not take effect until the VC has been recited fully, at least once. These spells last as long as the spellcaster continues the chant. OOC explanations (such as combat calls) do not interrupt these spells. For example, if a PC is chanting a Transmute Self spell and is hit by a weapon, they may call “No effect” without interrupting the spell; if a PC is chanting a Ward: Undead spell and a goblin hits their leg, they can call “Leg” (or “Armor,” or “Armored Cloak,” etc.) without having the spell end. The VC for these spells must be spoken clearly and loudly enough that anyone affected by the spell can understand them. Chanting spells can be disrupted by the 4th circle spell Disrupt. It is the PC’s responsibility to know what the Disrupt spell is, how to recognize it, and how to respond to it.'
    },
    {
        "name": "Circles",
        "desc": "There are a number of spells that are considered circle spells. A circle spell must be clearly defined by a length of rope that has been laid on the ground with the ends overlapping. The ends cannot be tied together or secured in any way, and the rope in general cannot be secured or bound in place or the spell fails. Only one spell may be cast with a particular rope at a given time, although after the spell ends, a different spell may be cast with that rope. The rope does not need to be laid down in a circular pattern. Although a given circle spell may have a specific way of being broken, all circle spells are broken if the rope is jostled enough to move the ends apart by a character able to cross it. Any circle spell can be suspended by the 4th circle spell Disrupt. It is the PC’s responsibility to know what the Disrupt spell is, how to recognize it, and how to respond to it."
    },
    {
        "name": "Compulsions",
        "desc": 'Some spells are able to magically compel a character to act in a way the player would prefer they did not. Compulsions can be ignored if they are humiliating or exceedingly difficult commands such as “Kiss my feet” or “Move that wall ten feet to the left.” They also cannot violate OOC mundane laws or ethical codes. They may not force a spellcaster to break their weapon restrictions. Additionally, if the character has been turned undead, they cannot be compelled to communicate knowledge gained before they were made undead.'
    },
    {
        "name": "Enchanted Beings",
        "desc": "All spellcasters, undead, and certain creatures are considered to be enchanted beings. Normal fighters are only enchanted beings if under the effect of certain spells, as per the Undead Caveat. Enchanted beings are affected by a certain number of spells, while non-enchanted beings are not. These spells include Circle of Protection and Ward: Enchanted Beings. By definition, any undead creature is an enchanted being."
    },
    {
        "name": "Enchanted Items",
        "desc": "Some spells create or enchant items, or are enhancements that affect players. These spells create magical effects, but are not potent enough for the items bearer or the target of the enchantment to be considered an Enchanted Being, nor is their magic potent enough for the item to be affected by the spell Circle of Protection once they are cast. If the MC of these spells are disenchanted (through the spells Disenchant or the Strange Brew: Potion of Disenchant option) the spell will end, rendering the MC inert. Magic items are not covered by the Enchanted Items Caveat."
    },
    {
        "name": "Potions",
        "desc": "A spellcaster who learns Alchemy must have a page in their spellbook listing the sigils that they will use to label potions. Each type of potion they can make, must have a unique, distinguishable sigil. When a potion is made, the spellcaster must put their legible signature, the appropriate sigil, and the date upon the container. Once created, all potions are considered stealable items. A potion can be a represented by a liquid, lotion, elixir, magical food, or anything else, as long as it is safe to be administered in a combat situation. Potions must be directly applied to the recipient. They may not be thrown, dropped, or remotely applied in any manner. The spellcaster need not be present in order to use their potions. \nPotions take a 60 second process called Brewing to be cast. At the beginning of an event, the spellcaster must describe in general terms their process of brewing. An alchemist may brew as many potions as their spells allow during the same 60 seconds. If they wish to create more later, they must begin the process again. If the alchemist is interrupted while brewing, Alchemy points are not lost, but the potions will not be made, and they must start over again in order to make any potions. Although not required, use of additional props or role-playing is encouraged for this process. \nNo potion created by a player can carry over from one event to another; it expires at the end of the event at which it is cast. The PC may choose whether or not to further limit the lifespan of a potion when it is brewed by writing a distinct expiration time among the required spell information on the container. Any potions lacking a specified expiration time last until the end of the event."
    },
    {
        "name": "Precast",
        "desc": 'Spells a spellcaster has learned with this caveat allow the spellcaster to begin play with that spell active on them or their gear. This represents the character casting the spell before arriving at the event. This uses up one use of the spell. Any material component that must be on the caster for the spell to work must still be present as per normal (such as sashes). A spell “precast” in this way may only be cast on the caster, and may not be “precast” on anyone else.'
    },
    {
        "name": "Regeneration",
        "desc": "Some spells grant the ability to regenerate. When this ability is triggered (by death, being wounded, etc.), the target’s wound(s) begin to heal. Until the specified amount of time has passed, this grants no benefit. A blow to any kill location on a dead body will cause a regeneration count to reset no matter where the killing blow was inflicted. Impaling stops regeneration; the count resets when the weapon is removed. Regenerating from death heals all healable wounds on the body. If examined by another person, wounds can be seen to be regenerating. Regeneration that brings a character back from death or soul loss takes 120 seconds. If you are diseased, it takes twice as long to regenerate. You may only be under the effects of one basic regeneration and one advanced regeneration at a time. If more than one source is causing you to regenerate, you may choose which of those spells is causing you to regenerate. A regeneration will only work on someone who is soulless if the spell directly states that it can."
    }
]

spells = [
        {
            "name": "animal companion",
            "circle": 4,
            "uses": "1, and the spellcaster may only have one in-play",
            "material": 'A stuffed or toy animal that must be at least 4" tall',
            "caveats": "Suspension"
        },
        {
            "name": "animate lesser undead",
            "circle": 3,
            "uses": "3",
            "material": 'A tabard, or sash which clearly states “Undead,” “Skeleton,” “Ghost” or the like, or an appropriate mask',
            "caveats": "Compulsions, Thrall, Undead"       
        },
        {
            "name": "heal limb",
            "circle": 2,
            "uses": "Unlimited",
            "verbal": "20 words",
            "active": "Spellcaster must be stationary, must touch the target limb"
        },
        {
            "name": "heartiness",
            "circle": 2,
            "uses": "Unlimited",
            "verbal": "20 words"
        },
        {
            "name": "Cure Disease",
            "circle": 1,
            "uses": "5"
        },
        {
            "name": "intervention",
            "circle": 6,
            "uses": "1"
        }
    ]