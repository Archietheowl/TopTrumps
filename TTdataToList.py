from sqliteConnect import *
import TTreadData
import time
import random
import TTshuffleAndDeal

"""
Add Data From Table to A SET of LISTS
"""
p1DeckCount = len(TTshuffleAndDeal.currentDeck)
cpuDeckCount = len(TTshuffleAndDeal.cc)
print(p1DeckCount)
print(cpuDeckCount)


def selectAndCompare():
    p1DeckCount = len(TTshuffleAndDeal.playerCards)
    cpuDeckCount = len(TTshuffleAndDeal.cpuCards)
    
    p1Card = None
    p1Attribute = None
    
    cpuCard = None
    cpuAttribute = None
    print(p1DeckCount)
    print(cpuDeckCount)

#selectAndCompare()

