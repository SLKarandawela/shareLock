from django.test import TestCase

# Create your tests here.
import messages_api.models
import system_user.models


class TestCreateMessage(TestCase):
    @classmethod
    def setUpTestData(cls):
        test_user = system_user.models.CustomUser.objects.create_user(
            username='test',
            password='test'
        )
        test_message = messages_api.models.Message.objects.create(
            subject='django_test_subject',
            body='django_test_body',
            send_by=test_user
        )

    def test_message_content(self):
        message = messages_api.models.Message.objects.get(id=1)
        subject = f'{message.subject}'
        body = f'{message.body}'
        send_by = f'{message.send_by}'

        self.assertEqual(subject, 'django_test_subject')
        self.assertEqual(body, 'django_test_body')
        self.assertEqual(send_by, 'test_user')
