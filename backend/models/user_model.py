class UserModel:
    @staticmethod
    def subscribe_to_api(user_email, api_name):
        db.subscriptions.insert_one({"email": user_email, "api": api_name})

    @staticmethod
    def get_subscriptions(user_email):
        return list(db.subscriptions.find({"email": user_email}))
