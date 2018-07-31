from django.core.urlresolvers import reverse
from django.test import TestCase

from .models import Mineral


class MineralModelTests(TestCase):
    def setUp(self):
        self.mineral = Mineral.objects.create(
            name = "Abelsonite",
    		image_filename = "240px-Abelsonite_-_Green_River_Formation%2C_Uintah_County%2C_Utah%2C_USA.jpg",
    		image_caption = "sonite from the Green River Formation, Uintah County, Utah, US",
    		category =  "Organic",
    		formula =  "C<sub>31</sub>H<sub>32</sub>N<sub>4</sub>Ni",
    		color =  "Pink-purple, dark greyish purple, pale purplish red, reddish brown",
    		crystal_symmetry = "Space group: P1 or P1Point group: 1 or 1",
    		cleavage = "Probable on {111}",
    		optical_properties = "Biaxial",
            group = "Organic Minerals"
        )

        self.mineral2 = Mineral.objects.create(
            name = "Barstowite",
    		image_filename = "240px-Barstowite-90280.jpg",
    		image_caption = "Barstowite from Passa Limani area, Lavrion District, Attiki Prefecture, Greece",
    		category = "Halide",
    		color = "White to transparent",
    		luster = "Adamantine",
    		streak = "White",
    		group = "Halides"
        )

    def test_mineral_creation(self):
        mineral = self.mineral
        self.assertTrue(isinstance(mineral, Mineral))


    def test_mineral_list_view(self):
        resp = self.client.get(reverse('minerals:list'))
        self.assertEqual(resp.status_code, 200)
        self.assertIn(self.mineral, resp.context['minerals'])
        self.assertIn(self.mineral2, resp.context['minerals'])
        self.assertTemplateUsed(resp, 'minerals/mineral_list.html')
        self.assertContains(resp, self.mineral.name)


    def test_mineral_detail_view(self):
        resp = self.client.get(reverse('minerals:detail',
                                        kwargs={'pk': self.mineral.pk}))
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(self.mineral, resp.context['mineral'])
        self.assertTemplateUsed(resp, 'minerals/mineral_detail.html')


    def test_random_mineral_view(self):
        resp = self.client.get(reverse('minerals:random'))
        self.assertEqual(resp.status_code, 200)
        self.assertNotEqual(self.mineral, resp.context['mineral'])
        self.assertTemplateUsed(resp, 'minerals/mineral_detail.html')

    """
    def test_search_view(self):
        resp = self.client.get(reverse('minerals:search'))
        self.assertEqual(resp.status_code, 200)
    """

    def test_search_by_letter_view(self):
        resp = self.client.get(reverse('minerals:alphabet',
                            kwargs={'letter': self.mineral.name[0]}))
        self.assertEqual(resp.status_code, 200)
        self.assertIn(self.mineral, resp.context['minerals'])
        self.assertNotIn(self.mineral2, resp.context['minerals'])
        self.assertTemplateUsed(resp, 'minerals/mineral_list.html')


    def test_search_by_group_view(self):
        resp = self.client.get(reverse('minerals:group',
                                kwargs={'group': self.mineral.group}))
        self.assertEqual(resp.status_code, 200)
        self.assertIn(self.mineral, resp.context['minerals'])
        self.assertNotIn(self.mineral2, resp.context['minerals'])
        self.assertTemplateUsed(resp, 'minerals/mineral_list.html')
