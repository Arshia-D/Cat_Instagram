from django.test import TestCase
from django.contrib.auth import get_user_model
from django.utils import timezone
from posts.models import Post  
User = get_user_model()

class UserProfileTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        
        cls.test_user = User.objects.create_user(username='testuser', password='testpass123')
        cls.post = Post.objects.create(
            user=cls.test_user,
            caption='Just a test caption',
            post_img='posts/testimage.jpg',  
            likes=0,
            created_at=timezone.now(),
            tag=''
        )

    def test_caption_content(self):
        # Retrieve the post by caption and verify its content
        post = Post.objects.get(id=self.post.id)
        self.assertEqual(post.caption, 'Just a test caption')

    def test_likes_default_to_zero(self):
        # Verify that likes are set to zero by default
        self.assertEqual(self.post.likes, 0)

    def test_post_string_representation(self):
        # Verify the __str__ method for Post model
        expected_representation = f"{self.test_user.username} {self.post.id}"
        self.assertEqual(str(self.post), expected_representation)

