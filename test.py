#!/usr/bin/env python
import unittest

import events

class TestEventManager(unittest.TestCase):

    def test_can_set_event(self):
        mngr = events.EventManager()
        res = mngr.set_event("CTRL_DOWN", 2)
        self.assertEqual(res, True)
        self.assertEqual(mngr._events["CTRL_DOWN"], 2)

    def test_cannot_override_nonfetch_event(self):
        mngr = events.EventManager()
        mngr.set_event("CTRL_DOWN", 2)
        res = mngr.set_event("CTRL_DOWN", 4)
        self.assertEqual(res, False)
        self.assertEqual(mngr._events["CTRL_DOWN"], 2)

    def test_cannot_created_event(self):
        mngr = events.EventManager()
        res = mngr.set_event("FOO", 42)
        self.assertEqual(res, False)
        self.assertEqual("FOO" in mngr._events, False)

    def test_cannot_fetch_same_event_twice(self):
        mngr = events.EventManager()
        mngr.set_event("CTRL_DOWN", 2)
        mngr.get_event("CTRL_DOWN")
        evt = mngr.get_event("CTRL_DOWN")
        self.assertEqual(evt, None)

    def test_can_fetch_unknown_event(self):
        mngr = events.EventManager()
        evt = mngr.get_event("FOO")
        self.assertEqual(evt, None)

    def test_event_stored_after_fetched(self):
        mngr = events.EventManager()
        mngr.set_event("CTRL_DOWN", 2)
        mngr.get_event("CTRL_DOWN")
        self.assertEqual(mngr._last_events["CTRL_DOWN"], 2)
        mngr.set_event("CTRL_DOWN", 4)
        self.assertEqual(mngr._last_events["CTRL_DOWN"], 2)

    def test_can_set_upevent_if_same_downevent_fetched(self):
        mngr = events.EventManager()
        mngr.set_event("CTRL_DOWN", 2)
        mngr.get_event("CTRL_DOWN")
        res = mngr.set_event("CTRL_UP", 2)
        self.assertEqual(res, True)
        self.assertEqual(mngr._events["CTRL_DOWN"], None)
        self.assertEqual(mngr._events["CTRL_UP"], 2)
        self.assertEqual(mngr._last_events["CTRL_DOWN"], 2)

        mngr = events.EventManager()
        mngr.set_event("CTRL_DOWN", 2)
        res = mngr.set_event("CTRL_UP", 2)
        self.assertEqual(res, False)
        self.assertEqual(mngr._events["CTRL_DOWN"], 2)
        self.assertEqual(mngr._events["CTRL_UP"], None)

        mngr = events.EventManager()
        mngr.set_event("CTRL_DOWN", 2)
        mngr.get_event("CTRL_DOWN")
        res = mngr.set_event("CTRL_UP", 4)
        self.assertEqual(res, False)
        self.assertEqual(mngr._events["CTRL_DOWN"], None)
        self.assertEqual(mngr._events["CTRL_UP"], None)
        self.assertEqual(mngr._last_events["CTRL_DOWN"], 2)
        self.assertEqual(mngr._last_events["CTRL_UP"], None)


    def test_can_set_downevent_if_last_upevent_consummed(self):
        mngr = events.EventManager()
        mngr.set_event("CTRL_DOWN", 2)
        mngr.get_event("CTRL_DOWN")
        mngr.set_event("CTRL_UP", 2)
        res = mngr.set_event("CTRL_DOWN", 4)
        self.assertEqual(res, False)
        self.assertEqual(mngr._events["CTRL_DOWN"], None)
        self.assertEqual(mngr._events["CTRL_UP"], 2)
        self.assertEqual(mngr._last_events["CTRL_DOWN"], 2)
        self.assertEqual(mngr._last_events["CTRL_UP"], None)

    def test_success(self):
        mngr = events.EventManager()
        mngr.set_event("CTRL_DOWN", 2)
        evt1 = mngr.get_event("CTRL_DOWN")
        mngr.set_event("CTRL_UP", 2)
        evt2 = mngr.get_event("CTRL_UP")

        self.assertEqual(evt1, 2)
        self.assertEqual(evt2, 2)
        self.assertEqual(mngr._events["CTRL_DOWN"], None)
        self.assertEqual(mngr._events["CTRL_UP"], None)
        self.assertEqual(mngr._last_events["CTRL_DOWN"], None)
        self.assertEqual(mngr._last_events["CTRL_UP"], 2)

    def test_fail(self):
        mngr = events.EventManager()
        mngr.set_event("CTRL_DOWN", 2)
        evt = mngr.get_event("CTRL_DOWN")
        self.assertEqual(evt, 2)
        mngr.set_event("CTRL_DOWN", 3)
        evt = mngr.get_event("CTRL_DOWN")
        self.assertEqual(evt, None)
        mngr.set_event("CTRL_DOWN", 4)
        evt = mngr.get_event("CTRL_DOWN")
        self.assertEqual(evt, None)
        mngr.set_event("CTRL_DOWN", 5)
        evt = mngr.get_event("CTRL_DOWN")
        self.assertEqual(evt, None)


if __name__ == '__main__':
    unittest.main()
