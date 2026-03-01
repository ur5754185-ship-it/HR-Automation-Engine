class PipelineManager:
    

    VALID_TRANSITIONS = {
        "Applied": ["Screening"],
        "Screening": ["Interview"],
        "Interview": ["Offer"],
        "Offer": ["Hired", "Rejected"],
        "Hired": [],
        "Rejected": [],
    }

    def transition(self, candidate, new_state):
       
        current = getattr(candidate, "state", None)
        if current is None:
            
            return False

        allowed = self.VALID_TRANSITIONS.get(current, [])
        if new_state in allowed:
            candidate.state = new_state
            return True
        return False


if __name__ == "__main__":
    # demonstration
    class Candidate:
        def __init__(self, state):
            self.state = state

        def __repr__(self):
            return f"<Candidate state={self.state}>"

    mgr = PipelineManager()
    c = Candidate("Applied")
    print(c, mgr.transition(c, "Screening"), c)
    print(c, mgr.transition(c, "Hired"), c)  
    print(c, mgr.transition(c, "Interview"), c)  