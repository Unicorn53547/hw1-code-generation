# Write a function to find the first adverb and their positions in a given sentence.
import re
def find_adverb_position(text):
    # Use regular expression to find all adverbs in the sentence
    adverbs = re.findall(r'\b\w+ly\b', text)
    # If no adverbs are found, return an empty list
    if not adverbs:
        return []
    # Return the first adverb and its position
    return [(text.index(adverbs[0]), text.index(adverbs[0]) + len(adverbs[0]), adverbs[0])]

# Write a function to find all adverbs and their positions in multiple sentences. The function should return a list of tuples where each tuple contains the start position, end position, and the adverb for each sentence.
import re

def find_all_adverbs_positions(sentences):
    # Initialize an empty list to store the results
    results = []
    # Iterate over each sentence in the input list
    for sentence in sentences:
        # Find the first adverb and its position in the sentence
        adverb_position = find_adverb_position(sentence)
        # If an adverb is found, add it to the results list
        if adverb_position:
            results.append(adverb_position)
    # Return the list of results
    return results

# Test the function with the provided test case
assert find_all_adverbs_positions(['She quickly ran to the store.', 'He slowly walked home.']) == [(4, 11, 'quickly'), (3, 9, 'slowly')]

assert find_all_adverbs_positions(['She quickly ran to the store.', 'He slowly walked home.']) == [(4, 11, 'quickly'), (3, 9, 'slowly')]
assert find_all_adverbs_positions(['The dog barked loudly.', 'The cat meowed softly.']) == [(15, 21, 'loudly'), (15, 21, 'softly')]
assert find_all_adverbs_positions(['There was no adverb in this sentence.']) == []