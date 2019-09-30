
class UrlKeyGenerator(object):
	"""
		UrlKeyGenerator -- Generates the short_key for given counter(integer) and viceversa
		Using Base64 encoding/decoding here
	"""

	BASE62_KEYS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
	def __init__(self):
		pass

	def generate_short_url_key_from_id(self, counter):
		
		short_url_key = ""

		while(counter) :
			short_url_key = self.BASE62_KEYS[counter%62] + short_url_key
			counter /= 62

		return short_url_key



	def get_short_url_key_to_id(short_url_key):

		counter = 0

		for i in xrange(len(short_url_key)):
			if short_url_key[i] >= 'a' and short_url_key[i] <= 'z':
				counter = counter*62 + ord(short_url_key[i]) - ord('a')

			if short_url_key[i] >= 'A' and short_url_key[i] <= 'Z':
				counter = counter*62 + ord(short_url_key[i]) - ord('A') + 26

			if short_url_key[i] >= '0' and short_url_key[i] <= '9':
				counter = counter*62 + ord(short_url_key[i]) - ord('0') + 52


		return counter

urlKeyGenerator = UrlKeyGenerator()