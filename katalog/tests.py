from django.test import TestCase
from katalog.models import CatalogItem

# Create your tests here.

class TestUrls(TestCase):
    def setUp(self):
        CatalogItem.objects.create(
                item_name = "Baju Anak",
                item_price = 48000,
                item_stock = 5,
                description = "Sayang Anak",
                rating = 8,
                item_url = "https://www.tokopedia.com/rehanstore28/setelan-anak-drees-anak-setelan-aleeya-kids-1-5-tahun-terbaru-hitam-5-tahun"
            )

    def test_urls(self):
        url = CatalogItem.objects.get(item_name = "Baju Anak")
        self.assertEquals("Baju Anak", url.item_name)