from django.contrib.auth import get_user_model  # after customizing the AUTH_SETTINGS
from django.test import TestCase
from .models import Post


class BlogTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username="ahmedesmail07",
            email="ahmedesmail@gmail.com",
            password="secret",
        )
        cls.post = Post.objects.create(
            author=cls.user,
            title="First Post",
            body="wow",
        )

    def test_post_model(self):
        self.assertEqual(self.post.author.username, "ahmedesmail07")
        self.assertEqual(self.post.title, "First Post")
        self.assertEqual(self.post.body, "wow")
