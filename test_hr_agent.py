import pandas as pd
import json
from datetime import datetime



def clean_skills(skill_text):
    if pd.isna(skill_text):
        return []
    skills = skill_text.split(",")
    return list(set([s.strip().lower() for s in skills if s.strip() != ""]))


def parse_date(date_str):
    return datetime.strptime(date_str, "%Y-%m-%d")




class RankingEngine:
    def _init_(self, jd_skills):
        self.jd_skills = jd_skills  # dict with weights

    def rank_candidate(self, candidate_skills):
        score = 0
        max_score = sum(self.jd_skills.values())

        for skill, weight in self.jd_skills.items():
            if skill in candidate_skills:
                score += weight

        return round(score / max_score, 3)




class LeaveManager:
    def _init_(self, leave_data):
        self.leave_data = leave_data

    def is_overlap(self, new_start, new_end, team):
        for _, row in self.leave_data.iterrows():
            if row["team"] == team:
                old_start = parse_date(row["start_date"])
                old_end = parse_date(row["end_date"])
                if not (new_end <= old_start or new_start >= old_end):
                    return True
        return False

    def evaluate_leave(self, employee, leave_type, days_requested, start_date, end_date):
        record = self.leave_data[self.leave_data["employee"] == employee]

        if record.empty:
            return {"decision": "rejected", "rule": "Employee not found"}

        balance = record.iloc[0]["leave_balance"]
        role = record.iloc[0]["role"]
        team = record.iloc[0]["team"]

        # Check balance
        if days_requested > balance:
            return {"decision": "rejected", "rule": "Insufficient balance"}

        # Role-based leave eligibility example
        if role == "intern" and leave_type == "earned":
            return {"decision": "rejected", "rule": "Role not eligible"}

        # Check overlap
        new_start = parse_date(start_date)
        new_end = parse_date(end_date)

        if self.is_overlap(new_start, new_end, team):
            return {"decision": "rejected", "rule": "Team overlap conflict"}

        return {"decision": "approved", "rule": "Policy compliant"}




def load_resume_dataset(path):
    df = pd.read_csv(path)
    candidates = []

    for _, row in df.iterrows():
        skills = clean_skills(row["skills"])
        candidates.append({
            "name": row["name"],
            "skills": skills,
            "experience": row.get("experience", 0)
        })

    return candidates


def load_leave_dataset(path):
    return pd.read_csv(path)




def export_results(data):
    return json.dumps(data, indent=4)




if __name__ == "_main_":

    
    resumes = load_resume_dataset("resumes.csv")
    leave_df = load_leave_dataset("leave_data.csv")

    
    jd_skills = {
        "python": 5,
        "machine learning": 5,
        "sql": 3,
        "excel": 1
    }

    ranking_engine = RankingEngine(jd_skills)

   
    ranked_results = []

    for candidate in resumes:
        score = ranking_engine.rank_candidate(candidate["skills"])
        ranked_results.append({
            "name": candidate["name"],
            "score": score
        })

    ranked_results.sort(key=lambda x: x["score"], reverse=True)

   
    leave_manager = LeaveManager(leave_df)

    leave_decision = leave_manager.evaluate_leave(
        employee="Navya",
        leave_type="sick",
        days_requested=2,
        start_date="2026-03-01",
        end_date="2026-03-03"
    )

    
    final_output = {
        "ranked_candidates": ranked_results,
        "leave_decision": leave_decision
    }

    print(export_results(final_output))