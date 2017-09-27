import unittest
import webclip


class Tests(unittest.TestCase):
    def setUp(self):
        # Perform any setup that should occur
        # before every test
        pass

    def tearDown(self):
        # Perform any tear down that should
        # occur after every test
        pass

    def testPass(self):
        self.assertEqual(True, True)

    def testVersionAvailable(self):
        x = getattr(webclip, "__version__", None)
        self.assertTrue(x is not None)

    def testSetAndGetClipboard(self):
        # Set our clipboard value
        # user: test-user
        # value: test-value
        webclip.set_clipboard(
            'localhost',
            'test-user',
            'test-value'
        )

        # Assert we get it back
        # when we ask for it
        self.assertEqual(
            'test-value',
            webclip.get_clipboard(
                'localhost',
                'test-user'
            )
        )


if __name__ == "__main__":
    unittest.main()
