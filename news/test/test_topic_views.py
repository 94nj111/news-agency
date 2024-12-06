from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from news.models import Topic

TOPIC_PUBLIC_URL = reverse("news:topic-list")
TOPIC_PRIVAT_URL = reverse("news:topic-update", args=[1])


class PublicNewspaperTest(TestCase):
    def test_public_page(self):
        res = self.client.get(TOPIC_PUBLIC_URL)
        self.assertEqual(res.status_code, 200)

    def test_login_required(self):
        res = self.client.get(TOPIC_PRIVAT_URL)
        self.assertNotEqual(res.status_code, 200)


class PrivatNewspaperTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="test_user", password="test_password"
        )
        self.client.force_login(self.user)

    def test_public_page(self):
        Topic.objects.create(name="test_name")
        res = self.client.get(TOPIC_PUBLIC_URL)
        topic = Topic.objects.all()
        self.assertEqual(res.status_code, 200)
        self.assertEqual(list(res.context["topic_list"]), list(topic))
        self.assertTemplateUsed(res, "news/topic_list.html")

    def test_login_required(self):
        Topic.objects.create(id=1, name="test_name")
        res = self.client.get(TOPIC_PRIVAT_URL)
        self.assertEqual(res.status_code, 200)
        self.assertContains(res, "form")

    def test_create_topic(self):
        form_data = {"name": "new_topic"}
        res = self.client.post(reverse("news:topic-create"), data=form_data)
        self.assertEqual(res.status_code, 302)
        new_topic = Topic.objects.get(name=form_data["name"])
        self.assertEqual(new_topic.name, form_data["name"])
