from django.contrib.sitemaps import Sitemap
from django.urls import reverse

class Static_Sitemap(Sitemap):

    priority = 1.0
    changefreq = 'weekly'

    def items(self):
        return ['index', 'membership', 'login', 'kisan_card','kisan_card_apply','health_card','health_card_apply','privacypolicy','reachus','termscondition','cookiepolicy','aboutus','gallery','career','rules_regulation','academic_notice','administrative_notice','requirement_notice','verify_membership','verify_health','verify_kisan','attendance']

    def location(self, item):
        return reverse(item)