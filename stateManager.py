class StateManager:
    

    VALID_SEQUENCE = (
        "Applied",
        "Screening",
        "Interview",
        "Selected",
        "Offer",
        "Hired",
    )

    def validate_transition(self, current: str, new: str) -> bool:
        """Return ``True`` if moving ``current``->``new`` is allowed."""
        
        if new == "Rejected":
            return True

    
        if current == new:
            return True

        try:
            curr_index = self.VALID_SEQUENCE.index(current)
            new_index = self.VALID_SEQUENCE.index(new)
        except ValueError:
            
            return False

        
        return new_index == curr_index + 1


if __name__ == "__main__":
    sm = StateManager()
    print(sm.validate_transition("Applied", "Screening"))