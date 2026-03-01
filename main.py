import json
from datetime import datetime, timedelta

from ranking import RankingEngine
from schedular import Scheduler
from pipeline import PipelineManager
from leave import LeaveManager


class Candidate:
    def __init__(self, cid, skills):
        self.id = cid
        self.skills = skills
        self.state = None

    def __repr__(self):
        return f"<Candidate id={self.id} state={self.state}>"


class Interview:
    def __init__(self, candidate_id, interviewer, start, end):
        self.candidate = candidate_id
        self.interviewer = interviewer
        self.start_time = start
        self.end_time = end



c1 = Candidate("C1", ["python", "ml", "sql"])
c2 = Candidate("C2", ["java", "sql"])

candidates = [c1, c2]


engine = RankingEngine(["python", "sql"])
ranked = engine.rank_candidates(candidates)


scheduler = Scheduler()
interview = Interview(
    "C1",
    "Interviewer1",
    datetime.now(),
    datetime.now() + timedelta(hours=1)
)

scheduled = scheduler.schedule(interview)


pipeline = PipelineManager()
pipeline.transition(c1, "Screening")
pipeline.transition(c1, "Interview")


leave_manager = LeaveManager()
leave_manager.set_balance("E1", casual=5, sick=5)
leave_status = leave_manager.apply_leave("E1", "casual", 2)


output = {
    "ranking": ranked,
    "interview_scheduled": scheduled,
    "candidate_state": c1.state,
    "leave_approved": leave_status
}

print(json.dumps(output, indent=4))