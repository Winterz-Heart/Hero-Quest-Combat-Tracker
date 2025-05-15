# Hero-Quest-Combat-Tracker
A Combat tracker for the Hero Quest boardgame

Needs to eventually be able to:
  - Add players to a party list with their stats (would need to be manually entered each time as gear can cause changes to the stats of the players)
      - Attack Dice
      - Defence Dice
      - Body Points
      - Mind Points

  - Add named monsters to an monster list with their custom stats (named monster stats can range from a slight increase to base stats to over doubke the base stats)
      - Attack Dice
      - Defence Dice
      - Body Points
      - Mind Points
 
  - Pull Basic Monsters from a list that has all their values
      - should be able to have multiple copies of the same mob.
          (for example 3 goblins would need to be named goblin1, goblin2 and goblin3)
 
  - Track damage and Healing to Body and Mind for all members in both the party and monster list
      - mark both players and monsters as dead when body points reach zero
        - have option to remove monsters from monster list when their body points reach 0
        - some may be able to heal (typically named monsters)
        - have a quest failed pop up if all party members are dead
        - if any are healed when dead they are revived with their current body point being equal to the amount healed
