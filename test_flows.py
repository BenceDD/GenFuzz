import random
import string

class MattermostTestFlows:
    def __init__(self, mister):
        self.mr = mister

    def random_id(self):
        return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(3))

    def create_user_flow(self):
        return {
            "test": [
                { 
                    'input_data': { 'email': self.random_id() + '@test.com', 'username': 'TesztElek' + self.random_id(), 'password': 'Teszt' }, 
                    'target': self.mr.create_a_user, 
                    'post_process': lambda x: { "user_id": x["id"] } 
                }, {
                    'target': self.mr.deactivate_a_user_account,
                    'post_process': lambda x: { 'email': self.random_id() + '@test.com', 'username': 'TesztElek' + self.random_id() } 
                }
            ],
        }

    def create_team_flow(self):
        return {
            "setup": [],
            "test": [
                { 
                    'input_data': { 'name': 'testteam' + self.random_id(), 'display_name': 'Test team', 'type': 'O' }, 
                    'target': self.mr.create_a_team, 
                    'post_process': lambda x: { "team_id": x["id"] } 
                }
            ],
            "teardown": [
                { 
                    'input_data': None, 
                    'target': self.mr.delete_a_team, 
                    'post_process': None 
                }
            ]
        }
       
    def update_user_flow(self):
        return {
            "setup": [
                { 
                    'input_data': { 'email': self.random_id() + '@update.com', 'username': 'usertoupdate' + self.random_id(), 'password': 'Teszt' }, 
                    'target': self.mr.create_a_user, 
                    'post_process': lambda x: { "id": x["id"], "user_id": x["id"] } 
                }
            ],
            "test": [
                { 
                    'input_data': { 'first_name': 'Elek', 'last_name': 'Teszt' }, 
                    'target': self.mr.update_a_user, 
                    'post_process': None 
                }
            ],
            "teardown": [
                { 
                    'input_data': None, 
                    'target': self.mr.deactivate_a_user_account, 
                    'post_process': None 
                }
            ]
        }

    def update_password_flow(self):
        return  {
            "setup": [
                { 
                    'input_data': { 'email': self.random_id() + '@pword.com', 'username': 'updatepassworduser' + self.random_id(), 'password': 'oldpass' }, 
                    'target': self.mr.create_a_user, 
                    'post_process': lambda x: { 'user_id': x['id'] } 
                }
            ],
            "test": [
                { 
                    'input_data': { 'user_id': '', 'current_password': 'oldpass', 'new_password': 'newpass' }, 
                    'target': self.mr.update_a_users_password, 
                    'post_process': None 
                }
            ],
            "teardown": [
                { 
                    'input_data': None, 
                    'target': self.mr.deactivate_a_user_account, 
                    'post_process': None 
                }
            ]
        }

    def search_team_flow(self):
        return  {
            "setup": [
                { 
                    'input_data': { 'name': 'teamforsearch' + self.random_id(), 'display_name': 'Test team for search', 'type': 'O' },
                    'target': self.mr.create_a_team,
                    'post_process': lambda x: { "team_id": x["id"] } 
                }
            ],
            "test": [
                { 
                    'input_data': { 'term': 'teamforsearch' }, 
                    'target': self.mr.search_teams, 
                    'post_process': None 
                }
            ],
            "teardown": [
                { 
                    'input_data': None, 
                    'target': self.mr.delete_a_team, 
                    'post_process': None 
                }
            ]
        }

    def create_channel_flow(self):
        return  {
            "setup": [
                { 
                    'input_data': { 'name': 'teamfornewchannel' + self.random_id(), 'display_name': 'Test team for channel', 'type': 'O' },
                    'target': mr.create_a_team,
                    'post_process': lambda x: { "team_id": x["id"] } 
                }
            ],
            "test": [
                {
                    'input_data': { 'name': 'testchannel' + self.random_id(), 'display_name': 'testchannel', 'type': 'O', 'team_id': '' },
                    'target': mr.create_a_channel,
                    'post_process': lambda x: { "channel_id": x["id"] }
                }
            ],
            "teardown": [
                {
                    'input_data': None,
                    'target': self.mr.delete_a_channel,
                    'post_process': None 
                }, {
                    'input_data': None,
                    'target': self.mr.delete_a_team,
                    'post_process': None
                }
            ]
        }

    def add_user_to_team_flow(self):
        return  {
            "setup": [
                {
                    'input_data': { 'name': 'testteamforadduser' + self.random_id(), 'display_name': 'Test team', 'type': 'O' },
                    'target': self.mr.create_a_team,
                    'post_process': lambda x: { "team_id": x["id"] } 
                }, {
                    'input_data': { 'email': random_id() + '@usertoteam.com', 'username': 'TesztElek' + self.random_id(), 'password': 'Teszt' },
                    'target': self.mr.create_a_user,
                    'post_process': lambda x: { "user_id": x["id"] } 
                }
            ],
            "test": [
                {
                    'input_data': None,
                    'target': self.mr.add_user_to_team,
                    'post_process': None 
                }
            ],
            "teardown": [
                {
                    'input_data': None,
                    'target': self.mr.deactivate_a_user_account,
                    'post_process': None 
                }, {
                    'input_data': None,
                    'target': self.mr.delete_a_team,
                    'post_process': None
                }
            ]
        }

    def add_user_to_channel_flow(self):
        return  {
            "setup": [
                {
                    'input_data': { 'name': 'testteamforaddusertochannel' + self.random_id(), 'display_name': 'Test team', 'type': 'O' },
                    'target': self.mr.create_a_team, 
                    'post_process': lambda x: { "team_id": x["id"] } 
                }, {
                    'input_data': { 'name': 'testchannel' + self.random_id(), 'display_name': 'testchannel', 'type': 'O', 'team_id': '' },
                    'target': self.mr.create_a_channel,
                    'post_process': lambda x: { "channel_id": x["id"] } 
                }, {
                    'input_data': { 'email': self.random_id() + '@usertochannel.com', 'username': 'TesztElek' + self.random_id(), 'password': 'Teszt' },
                    'target': self.mr.create_a_user,
                    'post_process': lambda x: { "user_id": x["id"] } 
                }, {
                    'input_data': None,
                    'target': self.mr.add_user_to_team,
                    'post_process': None 
                }
            ],
            "test": [
                {
                    'input_data': None,
                    'target': self.mr.add_user_to_channel,
                    'post_process': None
                }
            ],
            "teardown": [
                {
                    'input_data': None,
                    'target': self.mr.deactivate_a_user_account,
                    'post_process': None 
                }, {
                    'input_data': None,
                    'target': self.mr.delete_a_channel,
                    'post_process': None
                }, {
                    'input_data': None,
                    'target': self.mr.delete_a_team,
                    'post_process': None 
                }
            ]
        }

    def view_channel_flow(self):
        return  {
            "setup": [
                {
                    'input_data': { 'name': 'testteamforviewchannel' + self.random_id(), 'display_name': 'Test team', 'type': 'O' },
                    'target': self.mr.create_a_team, 
                    'post_process': lambda x: { "team_id": x["id"] } 
                }, {
                    'input_data': { 'name': 'testchannel' + self.random_id(), 'display_name': 'testchannel', 'type': 'O', 'team_id': '' },
                    'target': self.mr.create_a_channel,
                    'post_process': lambda x: { "channel_id": x["id"] } 
                }, {
                    'input_data': { 'email': self.random_id() + '@viewchannel.com', 'username': 'TesztElek' + self.random_id(), 'password': 'Teszt' },
                    'target': self.mr.create_a_user,
                    'post_process': lambda x: { "user_id": x["id"] } 
                }, {
                    'input_data': None,
                    'target': self.mr.add_user_to_team,
                    'post_process': None 
                }
            ],
            "test": [
                {
                    'input_data': None,
                    'target': self.mr.view_channel,
                    'post_process': None
                }
            ],
            "teardown": [
                {
                    'input_data': None,
                    'target': self.mr.deactivate_a_user_account,
                    'post_process': None 
                }, {
                    'input_data': None,
                    'target': self.mr.delete_a_channel,
                    'post_process': None
                }, {
                    'input_data': None,
                    'target': self.mr.delete_a_team,
                    'post_process': None 
                }
            ]
        }

    def create_post_flow(self):
        return  {
            "setup": [
                {
                    'input_data': { 'name': 'testteamforcreatepost' + self.random_id(), 'display_name': 'Test team', 'type': 'O' },
                    'target': self.mr.create_a_team, 
                    'post_process': lambda x: { "team_id": x["id"] } 
                }, {
                    'input_data': { 'name': 'testchannel' + self.random_id(), 'display_name': 'testchannel', 'type': 'O', 'team_id': '' },
                    'target': self.mr.create_a_channel,
                    'post_process': lambda x: { "channel_id": x["id"] } 
                }
            ],
            "test": [
                {
                    'input_data': {'message': "Maximális hatékonysággal kell megtervezni a végtelen funkcionalitást."},
                    'target': self.mr.create_a_post,
                    'post_process': None
                }
            ],
            "teardown": [
                {
                    'input_data': None,
                    'target': self.mr.delete_a_channel,
                    'post_process': None
                }, {
                    'input_data': None,
                    'target': self.mr.delete_a_team,
                    'post_process': None 
                }
            ]
        }


    '''NOT IMPLEMENTED
    create_group_channel_flow = []
    '''

    '''NOT IMPLEMENTED
    create_direct_channel_flow = []
    '''

    '''NOT IMPLEMENTED
    add_multiple_user_to_team_flow = []
    '''

    '''NOT IMPLEMENTED
    get_users_by_id_flow = [
        { 'input_data': {}, 'target': mr.get_users, 'post_process': lambda x: [user["id"]
                for user in x
            ] },
        { 'input_data': None, 'target': mr.get_users_by_ids, 'post_process': None }
    ]
    '''
