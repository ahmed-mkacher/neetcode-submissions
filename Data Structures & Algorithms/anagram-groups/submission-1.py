class Solution:
    def groupAnagrams(self, strs):
        result = []
        for word in strs:
            if len(result) == 0:
                result.append([word])
            else:
                for sub in result:
                    total = 0
                    count = 0
                    for c in sub[0]:
                        total += ord(c)
                    for c in word:
                        count += ord(c)
                    if count == total and len(word) == len(sub[0]) and sorted(list(word)) == sorted(list(sub[0])):
                        sub.append(word)
                        break
                else:
                    result.append([word])
        return result