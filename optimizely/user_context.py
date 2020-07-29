
class OptimizelyUserContext(object):
    user_id = None
    bucketing_id = None
    attributes = []

    def __init__(self, user_id, attributes=None):
        self.user_id = user_id
        self.attributes = attributes or []
        self.user_profile_updates = []

    def set_attribute(self, key, value):
        self.attributes[key] = value

    def set_bucketing_id(self, id):
        self.bucketing_id = id

    def set_user_profile(self, key, value):
        self.user_profile_updates.extend((key, value))


