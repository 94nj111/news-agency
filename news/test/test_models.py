from django.test import TestCase

from news.models import Newspaper, Topic


class ModelTest(TestCase):
    def test_newspaper_str(self):
        newspaper = Newspaper(title="test_title", content="test_content")
        self.assertEqual(
            str(newspaper), f"{newspaper.title}: {newspaper.content}"
        )

    def test_topic_str(self):
        topic = Topic(name="test_name")
        self.assertEqual(str(topic), topic.name)
