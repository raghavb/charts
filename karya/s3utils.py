from django.conf import settings
from storages.backends.s3boto import S3BotoStorage

MediaRootS3BotoStorage  = lambda: S3BotoStorage(
  location=settings.MEDIA_ROOT,
    file_overwrite=False
    )
