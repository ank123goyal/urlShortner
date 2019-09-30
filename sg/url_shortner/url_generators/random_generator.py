import random
import string

SHORT_URL_CHARACTERS = string.ascii_letters + string.digits
SHORT_URL_LENGTH = 4


class RadomURLGenerator(object):

    def __init__(self):
        pass


    def get_random_url_key(self, chars, k):
        res = []
        for i in range(k):
            res += random.choice(chars)

        return res

    def generate_short_url(self):
        """Generate a short URL not in use already"""

        
        return "".join(self.get_random_url_key(SHORT_URL_CHARACTERS, k=SHORT_URL_LENGTH))
