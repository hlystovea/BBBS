import requests

from django.conf import settings


class ImageFromUrlMixin:
    def load_image(self, *, save=False):
        if self.__class__.objects.exists():
            new_id = self.__class__.objects.latest('id').id + 1
        else:
            new_id = 1
        directory = self.__class__.image.field.upload_to
        try:
            response = requests.get(self.image_url)
            with open(
                settings.MEDIA_ROOT / f'{directory}/{new_id}_pic.jpg',
                'wb'
            ) as image:
                image.write(response.content)
                self.image = image.name
            if save:
                self.save()
        except requests.exceptions.ConnectionError:
            pass