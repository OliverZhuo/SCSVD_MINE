class Trainset:
    def __init__(self, ur,
                 ir,
                 n_users,
                 n_items,
                 n_ratings,
                 rating_scale,
                 raw2inner_id_users,
                 raw2inner_id_items):
        self.ur = ur
        self.ir = ir
        self.n_users = n_users
        self.n_items = n_items
        self.n_ratings = n_ratings
        self.rating_scale = rating_scale
        self.raw2inner_id_users = raw2inner_id_users
        self.raw2inner_id_items = raw2inner_id_items

    def all_users(self):
        return self.ir

    def to_inner_uid(self, user):
        try:
            uid = self.raw2inner_id_users[user]
            return int(uid)
        except KeyError:
            pass