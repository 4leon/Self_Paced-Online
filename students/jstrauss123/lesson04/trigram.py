#!/usr/bin/env python3

# trigram based on sherlock short text file
# trigram based on short string of words to begin with
#str1 = "This is a long string of text by which to try writing out a trigram. I wish I knew how this was going to turn out."
#print(str)
#words = "One Two Three Four Five Six Seven Eight Nine Ten Eleven Twelve Thirteen Fourteen Fifteen Sixteen Seventeen Eighteen Nineteen Twenty".split()
#print(words)
words = "One night--it was on the twentieth of March, 1888--I was returning from a journey to a patient (for I had now returned to civil practice), when my way led me through Baker Street. As I passed the well-remembered door, which must always be associated in my mind with my wooing, and with the dark incidents of the Study in Scarlet, I was seized with a keen desire to see Holmes again, and to know how he was employing his extraordinary powers. His rooms were brilliantly lit, and, even as I looked up, I saw his tall, spare figure pass twice in a dark silhouette against the blind. He was pacing the room swiftly, eagerly, with his head sunk upon his chest and his hands clasped behind him. To me, who knew his every mood and habit, his attitude and manner told their own story. He was at work again. He had risen out of his drug-created dreams and was hot upon the scent of some new problem. I rang the bell and was shown up to the chamber which had formerly been in part my own. ".split()
 
def build_trigrams(words):
    """ 
    build up the trigrams dict from the list of words
    
    returns a dict with:
        keys: word pairs
        values: lsit of followers
    """
    #trigrams = {}
    # build up the dict here!


    #return trigrams

#if __name__ == "__main__":
    #trigrams = build_trigrams(words)
    #print(trigrams)

"""
if full_name not in donor_dict.keys():
        # add to dict
        donor_dict[full_name] = []
    # prompt for contribution amount and add to dict
    contrib_amt = float(input("Enter donation amount for donor: "))
    donor_dict[full_name].append(contrib_amt)
"""    
    

#dict1[val2] = follower
#dict1
#{"['One', 'Two']": 'Three'}
#val2.split()
#["['One',", "'Two']"]
#val1.split()    
    
trigrams = {}

for i in range(len(words)-2):
    pair = (words[i], words[i + 1])
    print(type(pair))
    print("pair is: ", pair)
    follower = [words[i + 2]]
    print("follower is: ", follower)
    if pair not in trigrams:
        # add to dict
        trigrams[pair] = follower
    else:
        trigrams[pair].append(words[i + 2])
        #trigrams[pair] = []
        #trigrams(pair) = [follower]
        #trigrams.append(pair) = [follower]
        #trigrams.append(pair)
print("")
print("keys are: ", trigrams.keys())        
print("\n\n")
print("trigram dict is: ", trigrams)






