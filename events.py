
class EventManager(object):
    def __init__(self):
        self._last_events = {
            "CTRL_DOWN" : None,
            "CTRL_UP" : None,
        }
        self._events = {
            "CTRL_DOWN" : None,
            "CTRL_UP" : None,
        }

    def show_state(self, inst):
        print "*", inst
        print "LAST"
        print "\t", "CTRL_DOWN", self._last_events["CTRL_DOWN"]
        print "\t", "CTRL_UP  ", self._last_events["CTRL_UP"]
        print "CURRENT"
        print "\t", "CTRL_DOWN", self._events["CTRL_DOWN"]
        print "\t", "CTRL_UP  ", self._events["CTRL_UP"]
        print "*"*30

    def get_event(self, event_type):
        evt = None
        if event_type in self._events and self._events[event_type] != None:
            evt = self._events[event_type]
            self._events[event_type] = None
            self._last_events[event_type] = evt
            if event_type == "CTRL_UP":
                self._last_events["CTRL_DOWN"] = None
        # self.show_state("get_event(%s) => %s" % (event_type, evt))
        return evt

    def set_event(self,event_type, value):
        res = False
        if event_type in self._events and self._events[event_type] == None:
            if event_type == "CTRL_DOWN" and self._events["CTRL_UP"] == None and self._last_events["CTRL_DOWN"] == None:
                self._events[event_type] = value
                res = True
            elif event_type == "CTRL_UP" and self._last_events["CTRL_DOWN"] == value:
                self._events[event_type] = value
                res = True
        # self.show_state("set_event(%s, %s) => %s" % (event_type, value, res))
        return res
