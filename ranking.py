import json
from datetime import datetime


class RankingEngine:
    """Simple percentage‑match engine for job skills."""

    def __init__(self, jd_skills):
        self.jd_skills = set(jd_skills or [])

    def rank_candidate(self, candidate):
        if not self.jd_skills:
            raise ValueError("Job description skills list cannot be empty")


        if isinstance(candidate, dict):
            skills = candidate.get("skills", [])
            cid = candidate.get("id")
        else:
            skills = getattr(candidate, "skills", [])
            cid = getattr(candidate, "id", None)

        candidate_skills = set(skills or [])
        matched = self.jd_skills.intersection(candidate_skills)
        score = (len(matched) / len(self.jd_skills)) * 100

        return {
            "candidate_id": cid,
            "match_score": round(score, 2),
            "matched_skills": list(matched),
        }

    def rank_candidates(self, candidates):
        """Rank an iterable of candidates and return list of results."""
        return [self.rank_candidate(c) for c in candidates]


def main():
    jd_skills = ["python", "data analysis", "machine learning"]
    candidates = [
        {"id": 1, "skills": ["python", "machine learning"]},
        {"id": 2, "skills": ["c++", "java"]},
    ]

    engine = RankingEngine(jd_skills)
    results = [engine.rank_candidate(c) for c in candidates]
    print(json.dumps(results, indent=2))


if __name__ == "__main__":
    main()


