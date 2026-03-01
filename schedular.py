from datetime import datetime


class Scheduler:
    """Simple scheduler that tracks interviewer bookings and detects conflicts."""

    def __init__(self):
        self.bookings = []

    def is_conflict(self, interviewer, start, end):
        """Return True if the given time range clashes with an existing booking."""
        for booking in self.bookings:
            if booking.interviewer == interviewer:
                if not (end <= booking.start_time or start >= booking.end_time):
                    return True
        return False

    def schedule(self, interview):
        """Attempt to add ``interview`` to the calendar.

        ``interview`` must have ``interviewer``, ``start_time`` and ``end_time``
        attributes.  Returns ``True`` on success, ``False`` if the slot is
        already taken.
        """
        if self.is_conflict(interview.interviewer, interview.start_time, interview.end_time):
            return False

        self.bookings.append(interview)
        return True


if __name__ == "__main__":
    class DummyInterview:
        def __init__(self, interviewer, start, end):
            self.interviewer = interviewer
            self.start_time = start
            self.end_time = end

    sched = Scheduler()
    iv1 = DummyInterview("alice", datetime(2026, 3, 1, 10), datetime(2026, 3, 1, 11))
    iv2 = DummyInterview("alice", datetime(2026, 3, 1, 10, 30), datetime(2026, 3, 1, 11, 30))

    print(sched.schedule(iv1))   
    print(sched.schedule(iv2))   