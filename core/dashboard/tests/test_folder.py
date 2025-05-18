from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from django.contrib.auth import get_user_model
from dashboard.models import Folder,File
from django.urls import reverse

User = get_user_model()

class FolderModelTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(email='user@example.com', password='pass')

    def test_create_folder(self):
        folder = Folder.objects.create(name='MyFolder', owner=self.user)
        self.assertEqual(folder.name, 'MyFolder')
        self.assertEqual(folder.owner, self.user)

class FolderViewTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(email='user@example.com', password='pass')
        self.client.login(email='user@example.com', password='pass')
        self.folder = Folder.objects.create(name='Folder1', owner=self.user)

    def test_folder_list_view(self):
        response = self.client.get(reverse('dashboard:folder-list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Folder1')

    def test_folder_detail_view(self):
        response = self.client.get(reverse('dashboard:folder-detail', args=[self.folder.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Folder1')


class FileTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(email='user@example.com', password='pass')
        self.folder = Folder.objects.create(name='MyFolder', owner=self.user)
        self.client.login(email='user@example.com', password='pass')

    def test_upload_file(self):
        file_data = SimpleUploadedFile("file.txt", b"hello world", content_type="text/plain")
        
        url = reverse('dashboard:add-file', kwargs={'folder_id': self.folder.id})
        response = self.client.post(url, {
            'name': 'file.txt',
            'file': file_data,
            'folder': self.folder.id,
        }, content_type='multipart/form-data')

       
        self.assertTrue(File.objects.filter(name='file.txt').exists())

