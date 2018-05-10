def random_id():
	return ''.join(random.choices(string.ascii_lowercase + string.digits, k = 10))

create_user_flow = [
    "setup": [],
    "test": [
        { 
	        'input_data': { 'email': 'test@test.com', 'username': 'TesztElek' + random_id(), 'password': 'Teszt' }, 
	        'target': mr.create_a_user, 
	        'post_process': lambda x: { "user_id": x["id"] } 
        }
    ],
    "teardown": [
        { 'target': mr.deactivate_a_user_account }
    ]
]

create_team_flow = [
    "setup": [],
    "test": [
        { 
	        'input_data': { 'name': 'testteam' + random_id(), 'display_name': 'Test team', 'type': 'O' }, 
	        'target': mr.create_a_team, 
	        'post_process': lambda x: { "team_id": x["id"] } 
        }
    ],
    "teardown": [
        { 
	        'input_data': None, 
	        'target': mr.delete_a_team, 
	        'post_process': None 
        }
    ]
]

update_user_flow = [
    "setup": [
        { 
	        'input_data': { 'email': random_id() + '@update.com', 'username': 'usertoupdate' + random_id(), 'password': 'Teszt' }, 
	        'target': mr.create_a_user, 
	        'post_process': lambda x: { "id": x["id"], "user_id": x["id"] } 
        }
    ],
    "test": [
        { 
	        'input_data': { 'first_name': 'Elek', 'last_name': 'Teszt' }, 
	        'target': mr.update_a_user, 
	        'post_process': None 
        }
    ]
    "teardown": [
        { 
	        'input_data': None, 
	        'target': mr.deactivate_a_user_account, 
	        'post_process': None 
        }
    ]
]

update_password_flow = [
    "setup": [
        { 
	        'input_data': { 'email': random_id() + '@pword.com', 'username': 'updatepassworduser' + random_id(), 'password': 'oldpass' }, 
	        'target': mr.create_a_user, 
	        'post_process': lambda x: { 'user_id': x['id'] } 
        }
    ],
    "test": [
        { 
	        'input_data': { 'user_id': '', 'current_password': 'oldpass', 'new_password': 'newpass' }, 
	        'target': mr.update_a_users_password, 
	        'post_process': None 
        }
    ],
    "teardown": [
        { 
	        'input_data': None, 
	        'target': mr.deactivate_a_user_account, 
	        'post_process': None 
        }
    ]
]

search_team_flow = [
    "setup": [
        { 
	        'input_data': { 'name': 'teamforsearch' + random_id(), 'display_name': 'Test team for search', 'type': 'O' },
	        'target': mr.create_a_team,
	        'post_process': lambda x: { "team_id": x["id"] } 
        }
    ],
    "test": [
        { 
	        'input_data': { 'term': 'teamforsearch' }, 
	        'target': mr.search_teams, 
	        'post_process': None 
        }
    ],
    "teardown": [
        { 
	        'input_data': None, 
	        'target': mr.delete_a_team, 
	        'post_process': None 
        }
    ]
]

create_channel_flow = [
    "setup": [
	    { 
	    	'input_data': { 'name': 'teamfornewchannel' + random_id(), 'display_name': 'Test team for channel', 'type': 'O' },
	    	'target': mr.create_a_team,
	    	'post_process': lambda x: { "team_id": x["id"] } 
	    }
    ],
    "test": [
	    {
	    	'input_data': { 'name': 'testchannel' + random_id(), 'display_name': 'testchannel', 'type': 'O', 'team_id': '' },
	    	'target': mr.create_a_channel,
	    	'post_process': lambda x: { "channel_id": x["id"] }
	    }
    ],
    "teardown": [
        {
	        'input_data': None,
	        'target': mr.delete_a_channel,
	        'post_process': None 
        }, {
	        'input_data': None,
	        'target': mr.delete_a_team,
	        'post_process': None
	    }
    ]
]

add_user_to_team_flow = [
    "setup": [
	    {
	    	'input_data': { 'name': 'testteamforadduser' + random_id(), 'display_name': 'Test team', 'type': 'O' },
	    	'target': mr.create_a_team,
	    	'post_process': lambda x: { "team_id": x["id"] } 
	    }, {
	    	'input_data': { 'email': random_id() + '@usertoteam.com', 'username': 'TesztElek' + random_id(), 'password': 'Teszt' },
	    	'target': mr.create_a_user,
	    	'post_process': lambda x: { "user_id": x["id"] } 
	    }
    ],
    "test": [
	    {
	    	'input_data': None,
	        'target': mr.add_user_to_team,
	        'post_process': None 
	    }
    ],
    "teardown": [
	    {
	    	'input_data': None,
	        'target': mr.deactivate_a_user_account,
	        'post_process': None 
	    }, {
	    	'input_data': None,
	    	'target': mr.delete_a_team,
	    	'post_process': None
	    }
    ]
]

add_user_to_channel_flow = [
    "setup": [
    	{
	    	'input_data': { 'name': 'testteamforaddusertochannel' + random_id(), 'display_name': 'Test team', 'type': 'O' },
	    	'target': mr.create_a_team, 
	    	'post_process': lambda x: { "team_id": x["id"] } 
	    }, {
	    	'input_data': { 'name': 'testchannel' + random_id(), 'display_name': 'testchannel', 'type': 'O', 'team_id': '' },
	    	'target': mr.create_a_channel,
	    	'post_process': lambda x: { "channel_id": x["id"] } 
	    }, {
	    	'input_data': { 'email': random_id() + '@usertochannel.com', 'username': 'TesztElek' + random_id(), 'password': 'Teszt' },
	    	'target': mr.create_a_user,
	    	'post_process': lambda x: { "user_id": x["id"] } 
	    }, {
	    	'input_data': None,
	    	'target': mr.add_user_to_team,
	    	'post_process': None 
    	}
    ],
    "test": [
    	{
	    	'input_data': None,
	    	'target': mr.add_user_to_channel,
	    	'post_process': None
    	}
    ],
    "teardown": [
    	{
	    	'input_data': None,
	    	'target': mr.deactivate_a_user_account,
	    	'post_process': None 
	    }, {
	    	'input_data': None,
	    	'target': mr.delete_a_channel,
	    	'post_process': None
	    }, {
	    	'input_data': None,
	    	'target': mr.delete_a_team,
	    	'post_process': None 
	    }
	]
]

view_channel_flow = [

]

create_post_flow = [

]

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