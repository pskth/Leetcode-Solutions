class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        ver1 = version1.split(".")
        ver2 = version2.split(".")
        minlen = min(len(ver1), len(ver2))

        for i in range(minlen):
            if int(ver1[i]) < int(ver2[i]):
                return -1
            if int(ver1[i]) > int(ver2[i]):
                return 1 
        
        if minlen < len(ver1):
            if re.fullmatch(r"^0+$", ''.join(ver1[minlen:])):
                return 0
            return 1
        elif minlen < len(ver2):
            if re.fullmatch(r"^0+$", ''.join(ver2[minlen:])):
                return 0
            return -1
        else:
            return 0
    