from day06_frame.constant import constant
from day06_frame.constant.constant import iHrm_BaseUrl, iHrm_user, GrobleToken


class IhrmEmploy:

    def get_token(self):
        return {"Authorization": "Bearer " + constant.GrobleToken}

    def add_employ(self, session, data):
        return session.post(iHrm_user, json=data, headers=self.get_token())

    def modify_employ(self, session, empId, data):
        return session.put(iHrm_user + empId, json=data, headers=self.get_token())

    def find_employ(self, session, empId):
        return session.get(iHrm_user + empId, headers=self.get_token())

    def del_employ(self, session, empId):
        return session.delete(iHrm_user + empId, headers=self.get_token())
