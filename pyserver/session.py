class SessionManager:
    
    def __init__(self) -> None:
        self.user_id = {}
        self.sid = {}

    def add_user(self, sid, user_id):
        try:
            self.user_id[user_id]
            self.sid.pop(self.user_id[user_id])
        except:
            pass
        self.user_id.update({user_id: sid})
        self.sid.update({sid: user_id})
    
    def remove_user(self, sid):
        self.user_id.pop(self.sid[sid])
        self.sid.pop(sid)

    def get_user_id(self, sid):
        return self.sid[sid]

    def get_sid(self, user_id):
        return self.user_id[user_id]

    def get_state(self):
        return {
            'user_ids': self.user_id,
            'sids': self.sid
        }

