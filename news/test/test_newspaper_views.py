from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from news.models import Newspaper, Topic

NEWSPAPER_PUBLIC_URL = reverse("news:index")
NEWSPAPER_PRIVAT_URL = reverse("news:newspaper-create")


class PublicNewspaperTest(TestCase):
    def test_public_page(self):
        res = self.client.get(NEWSPAPER_PUBLIC_URL)
        self.assertEqual(res.status_code, 200)

    def test_login_required(self):
        res = self.client.get(NEWSPAPER_PRIVAT_URL)
        self.assertNotEqual(res.status_code, 200)


class PrivatNewspaperTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="test_user", password="test_password"
        )
        self.client.force_login(self.user)
        self.newspaper = Newspaper.objects.create(
            title="test_title", content="test_content"
        )

    def test_public_page(self):
        Newspaper.objects.create(title="test_title", content="test_content")
        res = self.client.get(NEWSPAPER_PUBLIC_URL)
        newspapers = Newspaper.objects.all()
        self.assertEqual(res.status_code, 200)
        self.assertEqual(list(res.context["newspaper_list"]), list(newspapers))
        self.assertTemplateUsed(res, "news/newspaper_list.html")

    def test_login_required(self):
        res = self.client.get(NEWSPAPER_PRIVAT_URL)
        self.assertEqual(res.status_code, 200)
        self.assertContains(res, "form")

    def test_create_newspaper(self):
        topic = Topic.objects.create(name="test_name")
        form_data = {
            "title": "test_title_creation",
            "content": "test_content",
            "topics": [
                topic.id,
            ],
            "publishers": [
                self.user.id,
            ],
        }
        self.client.post(reverse("news:newspaper-create"), data=form_data)
        new_newspaper = Newspaper.objects.get(title=form_data["title"])
        self.assertEqual(new_newspaper.title, form_data["title"])
        self.assertEqual(new_newspaper.content, form_data["content"])

    def test_get_detail_view(self):
        res = self.client.get(
            reverse("news:newspaper-detail", args=[self.newspaper.pk])
        )
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.context["newspaper"].title, self.newspaper.title)
        self.assertTemplateUsed(res, "news/newspaper_detail.html")

    def test_update_newspaper(self):
        topic = Topic.objects.create(name="test_name")
        update_data = {
            "title": "test_title",
            "content": "test_content",
            "topics": [
                topic.id,
            ],
            "publishers": [
                self.user.id,
            ],
        }
        res = self.client.post(
            reverse("news:newspaper-update", args=[self.newspaper.pk]),
            data=update_data,
        )
        self.newspaper.refresh_from_db()
        self.assertEqual(self.newspaper.title, update_data["title"])
        self.assertEqual(self.newspaper.content, update_data["content"])
        self.assertRedirects(res, reverse("news:index"))

    def test_delete_newspaper(self):
        res = self.client.post(
            reverse("news:newspaper-delete", args=[self.newspaper.pk])
        )
        self.assertEqual(res.status_code, 302)
        self.assertFalse(
            Newspaper.objects.filter(pk=self.newspaper.pk).exists()
        )
