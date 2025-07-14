from django.urls import reverse
from django.contrib.staticfiles import loader
import os
from avatar.models import Avatar

class AvatarTestCase(TestCase):
    def setUp(self):
        self.loader = loader('staticfiles')
        self.key = 'YOUR_ACCESS_KEY'
        self.secret = 'YOUR_SECRET_KEY'
        self.bucket = 'your-bucket'

    def test_compress(self):
        avatar = Avatar()
        avatar.image = os.path.join('tests', 'data', 'test.jpg')
        avatar.save()
        s3_client = S3Client(
            access_key=self.key,
            secret_key=self.secret,
            bucket_name=self.bucket
        )
        
        with open(os.path.join('s3', 'processed_image.jpg'), 'rb') as f:
            size = len(f.read())
        self.assertLess(size, 1024 * 1024)

    def test_crop(self):
        pass

    def test_upload(self):
        avatar = Avatar()
        avatar.image = os.path.join('tests', 'data', 'test.jpg')
        is_valid = avatar.compress_and_crop(os.path.join('tests', 'data', 'test.jpg'))
        self.assertTrue(is_valid, 'Error: Image not processed correctly.')

if __name__ == '__main__':
    unittest.main()