from django.db import models

class Avatar(models.Model):
    image = models.ImageField(
        upload_to='avatars',
        storage='custom_storage'
    )

    def save(self, *args, **kwargs):
        if not self.image:
            return
        with file_object = self.image.open()
        processed_image = process_image(file_object)
        storage, _ = split_storage(self.storage, storage_name)
        storage.save('processed_' + filename, processed_image.file)
        super().save(*args, **kwargs)