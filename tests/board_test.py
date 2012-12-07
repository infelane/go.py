import unittest

from go import Board


class BoardTest(unittest.TestCase):
    """
    Won't test any of the array functionality.  That is covered in
    array_test.py.
    """

    def setUp(self):
        self.bo = Board(5)

    def test_init(self):
        e = Board.EMPTY
        b = Board.BLACK
        w = Board.WHITE

        self.assertEqual(self.bo._array, [
            [e, e, e, e, e],
            [e, e, e, e, e],
            [e, e, e, e, e],
            [e, e, e, e, e],
            [e, e, e, e, e],
        ])

        self.assertTrue(self.bo._turn is b)
        self.assertEqual(self.bo._score, {b: 0, w: 0})
        self.assertEqual(self.bo._history, [])
        self.assertEqual(self.bo._redo, [])

    def test_turn(self):
        self.assertEqual(self.bo.turn, 'Black')
        self.bo.move(1, 1)
        self.assertEqual(self.bo.turn, 'White')
        self.bo.move(2, 2)
        self.assertEqual(self.bo.turn, 'Black')
        self.bo.move(3, 3)
        self.assertEqual(self.bo.turn, 'White')

    def test_score(self):
        e = Board.EMPTY
        b = Board.BLACK
        w = Board.WHITE

        self.assertEqual(self.bo.score, {
            'black': 0,
            'white': 0,
        })

        self.bo._array = [
            [w, b, e, e, e],
            [e, e, e, e, e],
            [e, e, e, e, e],
            [e, e, e, e, e],
            [e, e, e, e, e],
        ]
        self.bo.move(1, 2)

        self.assertEqual(self.bo.score, {
            'black': 1,
            'white': 0,
        })

        self.setUp()
        self.bo._array = [
            [w, b, e, e, e],
            [w, b, e, e, e],
            [e, w, b, e, e],
            [w, b, e, e, e],
            [b, e, e, e, e],
        ]
        self.bo.move(1, 3)

        self.assertEqual(self.bo.score, {
            'black': 4,
            'white': 0,
        })

    def test_next_turn(self):
        b = Board.BLACK
        w = Board.WHITE

        self.assertTrue(self.bo._next_turn is w)
        self.bo.move(1, 1)
        self.assertTrue(self.bo._next_turn is b)
        self.bo.move(2, 2)
        self.assertTrue(self.bo._next_turn is w)
        self.bo.move(3, 3)
        self.assertTrue(self.bo._next_turn is b)

    def test_flip_turn(self):
        b = Board.BLACK
        w = Board.WHITE

        self.assertEqual(self.bo._turn, b)
        self.bo._flip_turn()
        self.assertEqual(self.bo._turn, w)
        self.bo._flip_turn()
        self.assertEqual(self.bo._turn, b)
        self.bo._flip_turn()
        self.assertEqual(self.bo._turn, w)

    def test_state(self):
        e = Board.EMPTY
        b = Board.BLACK
        w = Board.WHITE

        state = (
            [
                [e, e, e, e, e],
                [e, e, e, e, e],
                [e, e, e, e, e],
                [e, e, e, e, e],
                [e, e, e, e, e],
            ],
            b,
            {
                b: 0,
                w: 0,
            },
        )
        _state = self.bo._state

        self.assertEqual(_state[0], state[0])
        self.assertEqual(_state[1], state[1])
        self.assertEqual(_state[2], state[2])

        self.assertTrue(_state[0] is not state[0])
        self.assertTrue(_state[1] is state[1])
        self.assertTrue(_state[2] is not state[2])

        self.bo.move(3, 3)

        state = (
            [
                [e, e, e, e, e],
                [e, e, e, e, e],
                [e, e, b, e, e],
                [e, e, e, e, e],
                [e, e, e, e, e],
            ],
            w,
            {
                b: 0,
                w: 0,
            },
        )
        _state = self.bo._state

        self.assertEqual(_state[0], state[0])
        self.assertEqual(_state[1], state[1])
        self.assertEqual(_state[2], state[2])

        self.assertTrue(_state[0] is not state[0])
        self.assertTrue(_state[1] is state[1])
        self.assertTrue(_state[2] is not state[2])

    def test_load_state(self):
        state = self.bo._state

        self.bo.move(3, 3)

        self.assertNotEqual(self.bo._state, state)

        self.bo._load_state(state)

        self.assertEqual(self.bo._state, state)

    def test_push_history(self):
        self.assertEqual(self.bo._history, [])

        state = self.bo._state

        self.bo._push_history()

        self.assertTrue(len(self.bo._history) == 1)
        self.assertEqual(self.bo._history[0], state)
