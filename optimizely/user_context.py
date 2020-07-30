from .helpers import enums


class OptimizelyUserContext(object):
    user_id = None
    attributes = []
    default_decide_options: [enums.OptimizelyDecideOption]

    def __init__(self, user_id, attributes=None):
        valid_user_id = user_id
        if valid_user_id == "":
            uuid_key = "optimizely-uuid"
            valid_user_id = uuid_key
        self.user_id = valid_user_id
        self.attributes = attributes or []
        self.default_decide_options = []

    def set_attribute(self, key, value):
        self.attributes[key] = value

    def set_default_decide_options(self, options : [enums.OptimizelyDecideOption]):
        self.default_decide_options.extend(options)


