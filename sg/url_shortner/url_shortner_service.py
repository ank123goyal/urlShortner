from models import URLMapping
from url_generators.url_generator import urlKeyGenerator
from url_generators.random_generator import RadomURLGenerator


HOST_DOMAIN = "localhost:8000/"


class UrlShortnerService(object):

	def __init__(self):
		self.randomUrlGenerator = RadomURLGenerator()


	def get_short_url(self, original_url):

		"""
		"""

		short_url_key = self.randomUrlGenerator.generate_short_url()

		while(URLMapping.objects.filter(short_url_key=short_url_key).exists()):
			short_url_key = self.randomUrlGenerator.generate_short_url()

		url_mapping = URLMapping.objects.create(short_url_key=short_url_key, original_url=original_url)


		return short_url_key


	def get_original_url(self, short_url_key):

		try :

			url_mapping = URLMapping.objects.filter(short_url_key=short_url_key).last()
			return  url_mapping.original_url

		except Exception as ex:
			print str(ex)
			raise ex



urlShortnerService = UrlShortnerService()