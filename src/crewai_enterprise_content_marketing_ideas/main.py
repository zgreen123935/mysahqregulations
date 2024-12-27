#!/usr/bin/env python
import sys
from crewai_enterprise_content_marketing_ideas.crew import (
    MysaHQRegulationsCrew,
)


def run():
    """
    Run the crew.
    """
    inputs = {
        "company": "Mysa HQ",
        "location": "North America"  # Default location
    }
    MysaHQRegulationsCrew().crew().kickoff(inputs=inputs)


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        "company": "Mysa HQ",
        "location": "North America"
    }
    try:
        MysaHQRegulationsCrew().crew().train(
            n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs
        )

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")


def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        MysaHQRegulationsCrew().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")


def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        "company": "Mysa HQ",
        "location": "North America"
    }
    try:
        MysaHQRegulationsCrew().crew().test(
            n_iterations=int(sys.argv[1]), openai_model_name=sys.argv[2], inputs=inputs
        )

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")
