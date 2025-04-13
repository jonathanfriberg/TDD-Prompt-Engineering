"""
Unit tests for the Concert Itinerary Builder.

This file contains unit tests for the ItineraryBuilder class in main.py.
Participants will implement tests based on the system specifications.
"""

import unittest
from main import Concert, ItineraryBuilder
from concerts_data import get_all_concerts

class ItineraryBuilderTest(unittest.TestCase):
    """Test cases for the ItineraryBuilder class."""
    
    def setUp(self):
        """Set up for the tests."""
        self.builder = ItineraryBuilder()
        
        self.all_concerts = get_all_concerts()
    
    # ----- Manual Test Cases -----
    # Participants will implement their manual test cases here. 
    
    def test_manual_1(self):
        """First manually written test case."""
        """Constraint 4: Some artists may have no concerts on the list. In that case, that should be indicated in the itinerary."""

        conserts = [
            Concert("Anis Don Demina", "2025-04-13", "Karlskrona", 56.1616, 15.5866),
            Concert("Fröken Snusk", None, None, None, None)
            ]
        result = self.builder.build_itinerary(conserts)
        self.assertEqual(result[0].artist, "Fröken Snusk")
        self.assertIsNone(result[0].date)
        self.assertIsNone(result[0].location)
        self.assertIsNone(result[0].latitude)
        self.assertIsNone(result[0].longitude)


    def test_manual_2(self):
        """Constraint 2: The itinerary should return a list of concerts sorted in chronological order (by date from earliest to latest)."""

        conserts = [
            Concert("Anis Don Demina", "2025-04-20", "Karlskrona", 56.1616, 15.5866),
            Concert("Fröken Snusk", "2025-04-14", "Karlskrona", 56.1616, 15.5866)
            ]

        result = self.builder.build_itinerary(conserts)
        self.assertEqual(result[0].date, "2025-04-14")
        self.assertEqual(result[1].date, "2025-04-20")

    def test_manual_3(self):
        """Constraint 3: An artist has at most one concert in the itinerary. If an artist has more than one concert in the list, the itinerary should only include the one with the earliest start date."""

        conserts = [
            Concert("Anis Don Demina", "2025-04-22", "Karlskrona", 56.1616, 15.5866),
            Concert("Anis Don Demina", "2025-04-21", "Karlskrona", 56.1616, 15.5866)
            ]
        
        result = self.builder.build_itinerary(conserts)

        self.assertEqual(result[0].date, "2025-04-21")
        self.assertNotIn("2025-04-22", conserts)

    
    # ----- AI-Assisted Test Cases -----
    # Participants will implement their AI-assisted test cases here.
    # Please name your test in a way which indicates that these are AI-assisted test cases.

    def test_constraint_1_same_day_AI_assisted(self):
        concerts = [
            Concert("Artist A", "2025-05-01", "City1", 59.3293, 18.0686),
            Concert("Artist B", "2025-05-01", "City2", 57.7089, 11.9746),
        ]
        result = self.builder.build_itinerary(concerts)
        self.assertEqual(len(result), 1, "Only one concert should be included when two concerts are on the same day.")


    def test_constraint_2_itinerary_contains_correct_fields_AI_assisted(self):
        concerts = [
            Concert("Artist A", "2025-06-01", "Stockholm", 59.3293, 18.0686),
        ]
        result = self.builder.build_itinerary(concerts)
        self.assertEqual(result[0].artist, "Artist A")
        self.assertEqual(result[0].date, "2025-06-01")
        self.assertEqual(result[0].location, "Stockholm")
    
    def test_constraint_3_prioritize_single_concert_artists_AI_assisted(self):
        concerts = [
            Concert("Multi Artist", "2025-06-02", "City A", 60.0, 15.0),
            Concert("Multi Artist", "2025-06-05", "City B", 61.0, 16.0),
            Concert("Solo Artist", "2025-06-03", "City C", 62.0, 17.0),
        ]
        result = self.builder.build_itinerary(concerts)
        artists_in_itinerary = [c.artist for c in result]
        self.assertIn("Solo Artist", artists_in_itinerary, "Solo artist with only one concert should be included.")

if __name__ == "__main__":
    unittest.main()