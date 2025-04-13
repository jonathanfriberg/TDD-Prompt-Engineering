"""
Concert Itinerary Builder

This module provides functionality to build an itinerary of upcoming concerts.
"""

class Concert:
    """
    Represents a concert event.
    
    Attributes:
        artist (str): The name of the artist performing.
        date (str): The date of the concert in 'YYYY-MM-DD' format.
        location (str): The location where the concert will take place.
        latitude (float): Latitude coordinate of the concert location.
        longitude (float): Longitude coordinate of the concert location.
    """
    
    def __init__(self, artist, date, location, latitude, longitude):
        self.artist = artist
        self.date = date
        self.location = location
        self.latitude = latitude
        self.longitude = longitude

class ItineraryBuilder:
    """
    A class to build concert itineraries. 
    """
    
    def build_itinerary(self, concerts):
        itinerary = []
        date_to_concerts = {}

        for concert in concerts:
            if not concert.date:
                itinerary.append(concert)
                continue

            if concert.date not in date_to_concerts:
                date_to_concerts[concert.date] = []
            date_to_concerts[concert.date].append(concert)

        # Step 1: Prioritize artists with only one concert
        artist_concert_count = {}
        for concert in concerts:
            artist_concert_count[concert.artist] = artist_concert_count.get(concert.artist, 0) + 1

        for date in sorted(date_to_concerts.keys()):
            same_day_concerts = date_to_concerts[date]

            single_concert_artists = [
                c for c in same_day_concerts if artist_concert_count[c.artist] == 1
            ]

            if single_concert_artists:
                itinerary.append(single_concert_artists[0])
                continue

            # If no unique-artist concerts, pick first as default
            itinerary.append(same_day_concerts[0])

        return itinerary


if __name__ == "__main__":
    from concerts_data import get_all_concerts
    
    all_concerts = get_all_concerts()