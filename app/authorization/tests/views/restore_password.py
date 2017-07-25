from . import APITestCase, User

class ResstorePasswordViewTest(APITestCase):
    """ Test of RestorePassword view class """

    def setUp(self):
        """ Setting up test credentials """

        self.user = User.objects.create(email="example@mail.com")
        self.user.set_password('12345678')
        self.user.save()

    def test_success_restore_password(self):
        """ Test success workflow of restoring user password """

        response = self.client.post('/api/v1/restore_password/',  {
                'email': 'example@mail.com'
        })

        self.assertEqual('message' in response.data, True)

    def test_failed_restore_password(self):
        """ Tests failed workflow for restoring user's password """

        response = self.client.post('/api/v1/restore_password/',  {
                'email': ''
        })

        self.assertEqual('errors' in response.data, True)

    def test_failed_restore_password_if_user_does_not_exists(self):
        """ Tests failed workflow for restoring user's password if there is
            no such user """

        response = self.client.post('/api/v1/restore_password/',  {
                'email': 'example1@mail.com'
        })

        self.assertEqual('errors' in response.data, True)