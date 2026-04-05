import unittest
from podcast import Podcast


class TestPodcastReading(unittest.TestCase):
    def setUp(self):
        self.rss_url = (
            "https://www.cis.upenn.edu/~cis110/current/py/"
            "homework/hw06/rss.xml"
        )
        self.podcast = Podcast.from_rss(self.rss_url)

    def test_title(self):
        self.assertEqual(
            self.podcast.title,
            "CIS 1100 Py-Cast"
        )

    def test_description(self):
        self.assertEqual(
            self.podcast.description,
            "Do you want to know about Python? You've come to the right place."
        )

    def test_image_url(self):
        self.assertEqual(
            self.podcast.image_url,
            "https://upload.wikimedia.org/wikipedia/commons/f/f2/"
            "Python_at_Nairobi_National_Museum%2C_Kenya.jpg"
        )

    def test_number_of_episodes(self):
        self.assertEqual(
            len(self.podcast.episodes),
            3
        )

    def test_first_episode(self):
        first_episode = self.podcast.episodes[0]
        self.assertEqual(
            first_episode.title,
            "Types"
        )
        self.assertEqual(
            first_episode.description,
            "types"
        )
        self.assertEqual(
            first_episode.audio_url,
            "https://sphinx.acast.com/p/open/s/68521cb1002f9da49ab8d943/"
            "e/68749c2fea74e132fba0296a/media.mp3"
        )
        self.assertEqual(
            first_episode.pub_date,
            "Mon, 14 Jul 2025 07:00:00 GMT"
        )


if __name__ == "__main__":
    unittest.main()
