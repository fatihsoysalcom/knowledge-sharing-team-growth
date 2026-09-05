import threading
import time

class TeamMember:
    def __init__(self, name):
        self.name = name
        self.knowledge = []
        self.lock = threading.Lock()

    def share_knowledge(self, topic, detail):
        # Simulate a team member discovering a new insight or technique
        print(f"\n{self.name} discovered a new insight: '{topic}' - {detail}")
        with self.lock:
            self.knowledge.append((topic, detail))
        print(f"{self.name} is sharing this knowledge with the team.")
        # Simulate the sharing process - could be a commit, a presentation, etc.
        time.sleep(0.5)

    def learn_from_team(self, source_member, topic, detail):
        # Simulate a team member learning from another's shared knowledge
        print(f"{self.name} is learning about '{topic}' from {source_member.name}.")
        with self.lock:
            # Avoid duplicate learning of the same exact knowledge
            if (topic, detail) not in self.knowledge:
                self.knowledge.append((topic, detail))
                print(f"{self.name} has successfully integrated the knowledge of '{topic}'.")
            else:
                print(f"{self.name} already knew about '{topic}'.")
        time.sleep(0.3)

    def display_knowledge(self):
        print(f"\n--- {self.name}'s Knowledge Base ---")
        if not self.knowledge:
            print("No knowledge yet.")
        else:
            for topic, detail in self.knowledge:
                print(f"- {topic}: {detail}")
        print("-----------------------------")

def simulate_knowledge_transfer(sharer, learners):
    # Simulate one member sharing their knowledge with multiple others
    if not sharer.knowledge:
        print(f"{sharer.name} has no knowledge to share yet.")
        return

    # Pick one piece of knowledge to share for simplicity
    topic, detail = sharer.knowledge[-1] # Share the latest discovered knowledge

    threads = []
    for learner in learners:
        if learner != sharer: # A member doesn't learn from themselves
            thread = threading.Thread(target=learner.learn_from_team, args=(sharer, topic, detail))
            threads.append(thread)
            thread.start()

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    # Initialize team members
    alice = TeamMember("Alice")
    bob = TeamMember("Bob")
    charlie = TeamMember("Charlie")
    david = TeamMember("David")

    team = [alice, bob, charlie, david]

    # Alice discovers a key piece of knowledge
    alice.share_knowledge("Efficient Database Querying", "Using indexes effectively reduces query time by 50%.")

    # Simulate Alice sharing this knowledge with the rest of the team
    simulate_knowledge_transfer(alice, team)

    # Bob discovers something new, potentially building on Alice's knowledge or independently
    bob.share_knowledge("API Rate Limiting", "Implement a sliding window algorithm for accurate rate limiting.")

    # Simulate Bob sharing his knowledge
    simulate_knowledge_transfer(bob, team)

    # Charlie learns from Bob
    charlie.learn_from_team(bob, "API Rate Limiting", "Implement a sliding window algorithm for accurate rate limiting.")

    # Display everyone's knowledge base to show the spread
    for member in team:
        member.display_knowledge()
