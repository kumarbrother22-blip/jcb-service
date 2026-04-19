import unittest

from app import app


class AppRoutesTestCase(unittest.TestCase):
    def setUp(self):
        app.config.update(TESTING=True)
        self.client = app.test_client()

    def test_all_public_routes_render(self):
        for route in ["/", "/services", "/gallery", "/about", "/contact"]:
            response = self.client.get(route)
            self.assertEqual(response.status_code, 200, route)

    def test_gallery_uses_real_jcb_images(self):
        response = self.client.get("/gallery")

        self.assertEqual(response.status_code, 200)
        self.assertIn(b"jcb-excavators-real.jpg", response.data)
        self.assertIn(b"jcb-excavator-real.jpg", response.data)
        self.assertIn(b"jcb-backhoe-loader-real.jpg", response.data)

    def test_contact_form_redirects_with_flash_message(self):
        response = self.client.post(
            "/contact",
            data={"name": "Ravi", "email": "ravi@example.com", "message": "Need leveling work"},
            follow_redirects=True,
        )

        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Thank you, Ravi!", response.data)
        self.assertIn(b"Call or WhatsApp us directly", response.data)


if __name__ == "__main__":
    unittest.main()
