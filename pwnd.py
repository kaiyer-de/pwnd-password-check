import requests


class Pwnd:
    def __init__(self, hash):
        self.hash = hash
        self.url = "https://api.pwnedpasswords.com/range/" + hash[:5]

    def check(self):
        response = requests.get(self.url)

        if response.status_code == 200:
            foundHashes = response.text
            startIndex = foundHashes.find(str.upper(self.hash[5:]))
            if startIndex == -1:
                print("Your Password wasn't found")
                return False
            else:
                endIndex = startIndex + foundHashes[startIndex:].find("\n")
                delimiterIndex = startIndex + \
                    foundHashes[startIndex:].find(":")
                print("Your Password was found",
                      foundHashes[delimiterIndex+1:endIndex-1], "times")
                return True
