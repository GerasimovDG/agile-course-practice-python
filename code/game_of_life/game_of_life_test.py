import unittest

from game_of_life import GameOfLife
from game_of_life import GameOfLifeParser

class TestGameOfLifeClass(unittest.TestCase):

    def test_add_empty_string_is_0(self):
        strcalc = GameOfLife()
        result = strcalc.add("")
        self.assertTrue(result == 0)


class TestGameOfLifeParserClass(unittest.TestCase):
    def test_can_create_parser(self):
        parser = GameOfLifeParser()
        self.assertTrue(isinstance(parser, GameOfLifeParser))

    def test_parse_check_string_2x2_all_points_are_dead(self):
        parser = GameOfLifeParser()
        field_test = [[0 for i in range(2)] for j in range(2)]
        result = parser.parse("..\n..")
        self.assertTrue(result == field_test)

    def test_parse_check_string_2x2_first_point_live(self):
        parser = GameOfLifeParser()
        field_test = [[0 for i in range(2)] for j in range(2)]
        field_test[0][0] = 1
        result = parser.parse("*.\n..")
        self.assertTrue(result == field_test)

    def test_parse_check_string_2x2_second_point_live(self):
        parser = GameOfLifeParser()
        field_test = [[0 for i in range(2)] for j in range(2)]
        field_test[0][1] = 1
        result = parser.parse(".*\n..")
        self.assertTrue(result == field_test)

    def test_parse_check_string_3x3_second_point_live(self):
        parser = GameOfLifeParser()
        field_test = [[0 for i in range(3)] for j in range(3)]
        field_test[0][1] = 1
        result = parser.parse(".*.\n...\n...")
        self.assertTrue(result == field_test)

    def test_parse_check_string_3x2_second_point_live(self):
        parser = GameOfLifeParser()
        field_test = [[0 for i in range(2)] for j in range(3)]
        field_test[0][1] = 1
        result = parser.parse(".*\n..\n..")
        self.assertTrue(result == field_test)

    def test_parse_check_string_3x3_second_line_second_point_live(self):
        parser = GameOfLifeParser()
        field_test = [[0 for i in range(3)] for j in range(3)]
        field_test[1][1] = 1
        result = parser.parse("...\n.*.\n...")
        self.assertTrue(result == field_test)

    def test_parse_check_string_3x2_second_line_second_point_live(self):
        parser = GameOfLifeParser()
        field_test = [[0 for i in range(2)] for j in range(3)]
        field_test[1][1] = 1
        result = parser.parse("..\n.*\n..")
        self.assertTrue(result == field_test)

    def test_parse_check_string_4x4_last_point_live(self):
        parser = GameOfLifeParser()
        field_test = [[0 for i in range(4)] for j in range(4)]
        field_test[3][3] = 1
        result = parser.parse("....\n....\n....\n...*")
        self.assertTrue(result == field_test)

    def test_parse_check_string_3x2_last_point_live(self):
        parser = GameOfLifeParser()
        field_test = [[0 for i in range(3)] for j in range(4)]
        field_test[3][2] = 1
        result = parser.parse("...\n...\n...\n..*")
        self.assertTrue(result == field_test)

    def test_parse_check_string_4x8_general_example(self):
        parser = GameOfLifeParser()
        field_test = [[0 for i in range(8)] for j in range(4)]
        field_test[1][4] = 1
        field_test[2][3] = 1
        field_test[2][4] = 1
        result = parser.parse("........\n....*...\n...**...\n........")
        self.assertTrue(result == field_test)
