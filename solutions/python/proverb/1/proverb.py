def proverb(*words, qualifier = None):
    if not words:
        return []

    lines = []
    if qualifier:
        final_word = f'{qualifier} {words[0]}'
    else:
        final_word = f'{words[0]}'
    for i in range(len(words) -1):
        lines.append(f'For want of a {words[i]} the {words[i+1]} was lost.')

    lines.append(f'And all for the want of a {final_word}.')

    return lines