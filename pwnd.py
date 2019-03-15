import requests


class Pwnd:
    def __init__(self, sha1):
        self.sha1 = sha1
        self.url = f"https://api.pwnedpasswords.com/range/{self.sha1[:5]}"

    def check(self):
        response = requests.get(self.url)

        if response.status_code == 200:
            foundHashes = [_.split(':') for _ in response.text.splitlines()]
            for [h, count] in foundHashes:
                if h == self.sha1[5:]:
                    print(f"Your Password was found {count} times")
                    return True
            print("Your Password wasn't found")
        return False