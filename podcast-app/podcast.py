from bs4 import BeautifulSoup
import requests as re


class Episode:
    def __init__(self, title, description, audio_url, pub_date):
        """ Initializes an Episode object with its title, description,
        audio URL, and publication date
        """
        self.title = title
        self.description = description
        self.audio_url = audio_url
        self.pub_date = pub_date

    @classmethod
    def from_item_tag(cls, entry):
        """
        Given a BeautifulSoup <item> tag, extracts the relevant
        information and returns an Episode object
        """
        title = entry.find("title").text.strip()
        description = entry.find("description").text.strip()
        audio_url = entry.find("enclosure")["url"].strip()
        pub_date = entry.find("pubDate").text.strip()

        return cls(title, description, audio_url, pub_date)


class Podcast:
    def __init__(self, title, description, image_url, episodes):
        self.title = title
        self.description = description
        self.image_url = image_url
        self.episodes = episodes

    @classmethod
    def from_rss(cls, rss_url: str):
        response = re.get(rss_url)
        soup = BeautifulSoup(response.text, "xml")
        channel = soup.find("channel")

        title = channel.find("title").text.strip()
        description = channel.find("description").text.strip()
        image_tag = channel.find("image")
        if image_tag.find("url") is not None:
            image_url = image_tag.find("url").text.strip()
        else:
            image_url = image_tag["href"].strip()
        # image_url = channel.find("image").find("url").text.strip()
        items = channel.find_all("item")

        episodes = []
        for item in items:
            episodes.append(Episode.from_item_tag(item))

        return cls(title, description, image_url, episodes)
