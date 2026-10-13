def group_anagrams(words):

    groups = {}

    for word in words:

        # Frequency array for a-z
        count = [0] * 26

        # Count characters
        for char in word:
            index = ord(char) - ord('a')
            count[index] += 1

        # Convert list to hashable tuple
        key = tuple(count)
        # Create group if key doesn't exist
        if key not in groups:
            groups[key] = []
        print(groups)
        # Add word to its group
        groups[key].append(word)

    return list(groups.values())
group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])