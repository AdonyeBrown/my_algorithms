def count_construct(target, word_bank):
    if target == "":
        return 1
    total_count = 0
    for word in word_bank:
        if target.startswith(word):
            numWaysForRest = count_construct(target[len(word):], word_bank)
            total_count += numWaysForRest

    return total_count


def count_construct_2(target, word_bank, memo={}):
    if target in memo:
        return memo[target]
    if target == "":
        return 1
    total_count = 0
    for word in word_bank:
        if target.startswith(word):
            numWaysForRest = count_construct_2(target[len(word):], word_bank)
            total_count += numWaysForRest

    memo[target] = total_count
    return total_count


print(count_construct_2("abcdef", ["ab", "abc", "cd", "def", "abcd"]))   # true
print(count_construct_2("skateboard", [
      "bo", "rd", "ate", "t", "ska", "sk", "boar"]))  # output false
print(count_construct_2("enterapotentpot", [
      "a", "p", "ent", "enter", "ot", "o", "t"]))
print(count_construct_2("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef",
                        ["e", "ee", "eee", "eeee", "eeeee", "eeeeee",]))

print(count_construct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))   # true
print(count_construct("skateboard", [
      "bo", "rd", "ate", "t", "ska", "sk", "boar"]))  # output false
print(count_construct("enterapotentpot", [
      "a", "p", "ent", "enter", "ot", "o", "t"]))
# print(count_construct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef",["e","ee","eee","eeee","eeeee","eeeeee",]));
