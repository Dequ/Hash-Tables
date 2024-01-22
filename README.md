# Hash-Tables

My code is an extension of the code shared by codebasics (Youtube channel) in his video titled "Hash Table - Data Structures & Algorithms in Python".

It updates the __delitem__ method by adding 2 new methods (backwards_mover_range and backwards_mover) to the original HashTable class created by codebasics, seeking to provide a more accurate depiction of linear probing, specifically improving the deletion mechanism of the HashTable class. 

When a key-value pair is deleted from the HashTable, my code's updated deletion mechanism searches through the rest of the HashTable and moves another key-value pair backwards into the now empty cell, and subsequently searches through yet again to move yet another key-value pair backwards into the empty cell created by moving the previous key-value pair through a recursion mechanism. 
