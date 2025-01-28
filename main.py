
from crew import CompanyFeedbackCrew

def run():
    crew_instance = CompanyFeedbackCrew()
    inputs = {
    'company': 'Getbeamer'
    }
    result = crew_instance.crew().kickoff(inputs=inputs)
    print("Résultat de l'analyse des retours :")
    print(result)

if __name__ == "__main__":
    run()
