class Solution:
    def compressedString(self, word: str) -> str:
        comp = ""
        word += "0"
        stack = []
        count = 1
        stack.append(word[0])
        for i in range(1,len(word)):
            if stack[-1] == word[i]:
                count += 1
            else:
                while(True):
                    if count > 9:
                        comp += str(9) + stack[-1]
                        count = count - 9
                    else:
                        comp += str(count) + stack[-1]
                        count = 1
                        break
            stack.append(word[i])
        return comp
