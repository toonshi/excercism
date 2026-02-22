"""Module for generating the 'For Want of a Nail' proverb based on input words."""

def proverb(*words, qualifier=None):
    """
    Generate the lines of the proverb based on a sequence of items.
    
    :param words: Variadic arguments of items in the chain.
    :param qualifier: An optional adjective for the final item.
    :return: A list of strings representing the proverb.
    """
    if not words:
        return []

    lines = []
    
    # Using 'index' instead of 'i' to satisfy [disallowed-name]
    for index in range(len(words) - 1):
        lines.append(f"For want of a {words[index]} the {words[index + 1]} was lost.")

    # Determine the final word with the optional qualifier
    final_item = f"{qualifier} {words[0]}" if qualifier else words[0]
    lines.append(f"And all for the want of a {final_item}.")

    return lines