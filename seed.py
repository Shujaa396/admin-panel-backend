from sqlmodel import Session
from app.database.connection import engine
from app.models.user import User
from app.models.profile import Profile
from app.models.subscription import Subscription
from app.models.pos_module import POSModule

def seed_data():
    with Session(engine) as session:
        # Add sample users
        user1 = User(username="shuja", email="shuja@example.com", is_active=True)
        user2 = User(username="admin", email="admin@example.com", is_active=True)

        session.add_all([user1, user2])
        session.commit()

        # Add sample profiles
        profile1 = Profile(user_id=user1.id, bio="Software Developer")
        profile2 = Profile(user_id=user2.id, bio="Admin User")

        session.add_all([profile1, profile2])

        # Add subscriptions
        sub1 = Subscription(user_id=user1.id, plan="Free")
        sub2 = Subscription(user_id=user2.id, plan="Pro")

        session.add_all([sub1, sub2])

        # Add POS modules
        module1 = POSModule(name="Sales")
        module2 = POSModule(name="Inventory", is_active=False)

        session.add_all([module1, module2])
        session.commit()

if __name__ == "__main__":
    seed_data()
    print("✅ Seed data inserted.")
