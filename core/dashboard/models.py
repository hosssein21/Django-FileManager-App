from django.db import models

from django.contrib.auth import get_user_model

User = get_user_model()

class Folder(models.Model):
    name = models.CharField(max_length=255)
    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='subfolders'
    )
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='folders'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('parent', 'name')
        ordering = ['name']

    def __str__(self):
        # Show full path for clarity
        if self.parent:
            return f"{self.parent}/{self.name}"
        return self.name


class File(models.Model):
    name = models.CharField(max_length=255)
    file = models.FileField(upload_to='user_uploads/%Y/%m/%d/')
    folder = models.ForeignKey(
        Folder,
        on_delete=models.CASCADE,
        related_name='files'
    )
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='files'
    )
    size = models.PositiveBigIntegerField(editable=False)
    mime_type = models.CharField(max_length=50, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('folder', 'name')
        ordering = ['-created_at']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        # auto‑fill size and mime_type
        if self.file:
            self.size = self.file.size
            import mimetypes
            self.mime_type = mimetypes.guess_type(self.file.name)[0] or ''
        super().save(*args, **kwargs)
