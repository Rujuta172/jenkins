
import unittest
from app import get_status


class TestApp(unittest.TestCase):
    def test_get_status(self):
        self.assertEqual(
            get_status(),
            "DevOps CI/CD application is running!"
        )


if __name__ == "__main__":
    unittest.main()
