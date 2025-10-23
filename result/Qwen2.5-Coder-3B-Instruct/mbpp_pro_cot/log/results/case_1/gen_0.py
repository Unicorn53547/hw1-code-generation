# Write a function to find the first adverb and their positions in a given sentence.
import re
def find_adverb_position(text):
    # Use regular expression to find all adverbs in the sentence
    adverbs = re.findall(r'\b\w+ly\b', text)
    # If no adverbs are found, return an empty list
    if not adverbs:
        return []
    # Find the position of the first adverb
    start = text.index(adverbs[0])
    end = start + len(adverbs[0])
    # Return a tuple containing the start position, end position, and the adverb
    return (start, end, adverbs[0])

# Write a function to find all adverbs and their positions in multiple sentences. The function should return a list of tuples where each tuple contains the start position, end position, and the adverb for each sentence.
import re

def find_all_adverbs_positions(sentences):
    # Initialize an empty list to store the results
    results = []
    # Iterate over each sentence in the list
    for sentence in sentences:
        # Find the first adverb in the sentence
        start, end, adverb = find_adverb_position(sentence)
        # If an adverb is found, add a tuple containing the start position, end position, and the adverb to the results list
        if start != -1:
            results.append((start, end, adverb))
    # Return the list of results
    return results

assert find_all_adverbs_positions(['She quickly ran to the store.', 'He slowly walked home.']) == [(4, 11, 'quickly'), (3, 9, 'slowly')]
assert find_all_adverbs_positions(['The dog barked loudly.', 'The cat meowed softly.']) == [(15, 21, 'loudly'), (15, 21, 'softly')]
assert find_all_adverbs_positions(['There was no adverb in this sentence.']) == []