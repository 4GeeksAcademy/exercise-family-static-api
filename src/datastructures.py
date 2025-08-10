import random

class Family:
    def __init__(self, last_name):
        self.last_name = last_name
        self.members = [
            {
                "id": random.randint(1, 99999999),
                "first_name": "John",
                "age": 33,
                "lucky_numbers": [7, 13, 22]
            },
            {
                "id": random.randint(1, 99999999),
                "first_name": "Jane",
                "age": 35,
                "lucky_numbers": [10, 14, 3]
            },
            {
                "id": random.randint(1, 99999999),
                "first_name": "Jimmy",
                "age": 5,
                "lucky_numbers": [1]
            }
        ]

    def add_member(self, member):
        member['id'] = member.get('id', random.randint(1, 99999999))
        self.members.append(member)

    def get_member(self, id):
        return next((m for m in self.members if m['id'] == id), None)

    def get_all_members(self):
        return self.members

    def delete_member(self, id):
        member = self.get_member(id)
        if member:
            self.members.remove(member)
            return True
        return False
