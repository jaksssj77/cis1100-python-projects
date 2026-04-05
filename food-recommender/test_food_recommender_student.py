import unittest
import food_recommender


class TestStudentGetCuisines(unittest.TestCase):
    def test_student_get_cuisines_two_unique(self):
        """
        Checkpoint 1:
        Checks that get_cuisines returns unique cuisine names
        """
        test_input = {
            "Alpha Sushi": ("Japanese", 2, 0.7, 4),
            "Bravo Ramen": ("Japanese", 1, 1.4, 9),
            "Cafe Roma": ("Italian", 3, 0.2, 7),
        }
        expected = {"Japanese", "Italian"}
        actual = food_recommender.get_cuisines(test_input)
        self.assertEqual(expected, actual)


class TestStudentMaxDistance(unittest.TestCase):
    def test_student_max_distance_boundary(self):
        """
        Checkpoint 2:
        Checks that max_distance includes restaurants exactly at dist
        """
        test_input = {
            "Near": ("Thai", 1, 0.5, 0),
            "Edge": ("Thai", 2, 1.0, 3),
            "Far": ("Thai", 1, 1.0001, 10),
        }
        expected = {"Near", "Edge"}
        actual = food_recommender.max_distance(test_input, 1.0)
        self.assertEqual(expected, actual)


class TestStudentTAEndorsements(unittest.TestCase):
    def test_student_ta_endorsements_threshold(self):
        """
        Checkpoint 3:
        Checks that ta_endorsements includes restaurants at the threshold
        """
        test_input = {
            "Low": ("Mexican", 1, 0.2, 2),
            "Edge": ("Mexican", 1, 0.3, 5),
            "High": ("Mexican", 2, 0.4, 8),
        }
        expected = {"Edge", "High"}
        actual = food_recommender.ta_endorsements(test_input, 5)
        self.assertEqual(expected, actual)


class TestStudentFilterCuisine(unittest.TestCase):
    def test_student_filter_cuisine_case_insensitive(self):
        """
        Checkpoint 4:
        Checks that filter_cuisine matches ignoring letter case
        """
        test_input = {
            "A": ("Chicken", 1, 0.2, 1),
            "B": ("cHiCkEn", 2, 0.5, 2),
            "C": ("Italian", 1, 0.1, 3),
        }
        expected = {"A", "B"}
        actual = food_recommender.filter_cuisine(test_input, "CHICKEN")
        self.assertEqual(expected, actual)


class TestStudentMostRecommendedDiverse(unittest.TestCase):
    def test_student_most_recommended_diverse_tie(self):
        """
        Checkpoint 5:
        Checks that most_recommended_diverse keeps the first restaurant on
        a tie
        """
        test_input = {
            "Alpha Greek": ("Greek", 1, 0.9, 10),
            # tie, should NOT replace Alpha
            "Beta Greek": ("Greek", 2, 0.3, 10),
            "Gamma Indian": ("Indian", 1, 0.2, 4),
            "Delta Indian": ("Indian", 3, 0.6, 12),
        }
        expected = {"Alpha Greek", "Delta Indian"}
        actual = food_recommender.most_recommended_diverse(test_input)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
