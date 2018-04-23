    def FUNCTION_NAME(self, **kwargs):
        """Create a new user on the system."""
        return self.send_request('/users', 'post', **kwargs)

    def FUNCTION_NAME(self, **kwargs):
        """Get a list of users based on a provided list of user ids."""
        return self.send_request('/users/ids', 'post', **kwargs)

    def FUNCTION_NAME(self, **kwargs):
        """Get a list of users based on a provided list of usernames."""
        return self.send_request('/users/usernames', 'post', **kwargs)

    def FUNCTION_NAME(self, **kwargs):
        """Get a list of users based on search criteria provided in the request body. Searches are typically done against username, full name, nickname and email unless otherwise configured by the server."""
        return self.send_request('/users/search', 'post', **kwargs)

    def FUNCTION_NAME(self, **kwargs):
        """Update a user by providing the user object. The fields that can be updated are defined in the request body, all other provided fields will be ignored."""
        return self.send_request('/users/{user_id}', 'put', **kwargs)

    def FUNCTION_NAME(self, **kwargs):
        """Update a user's system-level roles. Valid user roles are "system_user", "system_admin" or both of them. Overwrites any previously assigned system-level roles."""
        return self.send_request('/users/{user_id}/roles', 'put', **kwargs)

    def FUNCTION_NAME(self, **kwargs):
        """Update user active or inactive status.
			
			__Since server version 4.6, users using a SSO provider to login can be activated or deactivated with this endpoint. However, if their activation status in Mattermost does not reflect their status in the SSO provider, the next synchronization or login by that user will reset the activation status to that of their account in the SSO provider. Server versions 4.5 and before do not allow activation or deactivation of SSO users from this endpoint.__"""
        return self.send_request('/users/{user_id}/active', 'put', **kwargs)

    def FUNCTION_NAME(self, **kwargs):
        """Set a user's profile image based on user_id string parameter."""
        return self.send_request('/users/{user_id}/image', 'post', **kwargs)

    def FUNCTION_NAME(self, **kwargs):
        """Update the password for a user using a one-use, timed recovery code tied to the user's account. Only works for non-SSO users."""
        return self.send_request('/users/password/reset', 'post', **kwargs)

    def FUNCTION_NAME(self, **kwargs):
        """Activates multi-factor authentication for the user if `activate` is true and a valid `code` is provided. If activate is false, then `code` is not required and multi-factor authentication is disabled for the user."""
        return self.send_request('/users/{user_id}/mfa', 'put', **kwargs)

    def FUNCTION_NAME(self, **kwargs):
        """Generates an multi-factor authentication secret for a user and returns it as a string and as base64 encoded QR code image."""
        return self.send_request('/users/{user_id}/mfa/generate', 'post', **kwargs)

    def FUNCTION_NAME(self, **kwargs):
        """Check if a user has multi-factor authentication active on their account by providing a login id. Used to check whether an MFA code needs to be provided when logging in."""
        return self.send_request('/users/mfa', 'post', **kwargs)

    def FUNCTION_NAME(self, **kwargs):
        """Update a user's password. New password must meet password policy set by server configuration. Current password is required if you're updating your own password."""
        return self.send_request('/users/{user_id}/password', 'put', **kwargs)

    def FUNCTION_NAME(self, **kwargs):
        """Send an email containing a link for resetting the user's password. The link will contain a one-use, timed recovery code tied to the user's account. Only works for non-SSO users."""
        return self.send_request('/users/password/reset/send', 'post', **kwargs)

    def FUNCTION_NAME(self, **kwargs):
        """Revokes a user session from the provided user id and session id strings."""
        return self.send_request('/users/{user_id}/sessions/revoke', 'post', **kwargs)

    def FUNCTION_NAME(self, **kwargs):
        """Revokes all user sessions from the provided user id and session id strings."""
        return self.send_request('/users/{user_id}/sessions/revoke/all', 'post', **kwargs)

    def FUNCTION_NAME(self, **kwargs):
        """Attach a mobile device id to the currently logged in session. This will enable push notiofications for a user, if configured by the server."""
        return self.send_request('/users/sessions/device', 'put', **kwargs)

    def FUNCTION_NAME(self, **kwargs):
        """Verify the email used by a user to sign-up their account with."""
        return self.send_request('/users/email/verify', 'post', **kwargs)

    def FUNCTION_NAME(self, **kwargs):
        """Send an email with a verification link to a user that has an email matching the one in the request body. This endpoint will return success even if the email does not match any users on the system."""
        return self.send_request('/users/email/verify/send', 'post', **kwargs)

    def FUNCTION_NAME(self, **kwargs):
        """Switch a user's login method from using email to OAuth2/SAML/LDAP or back to email. When switching to OAuth2/SAML, account switching is not complete until the user follows the returned link and completes any steps on the OAuth2/SAML service provider.
			
			To switch from email to OAuth2/SAML, specify `current_service`, `new_service`, `email` and `password`.
			
			To switch from OAuth2/SAML to email, specify `current_service`, `new_service`, `email` and `new_password`.
			
			To switch from email to LDAP/AD, specify `current_service`, `new_service`, `email`, `password`, `ldap_ip` and `new_password` (this is the user's LDAP password).
			
			To switch from LDAP/AD to email, specify `current_service`, `new_service`, `ldap_ip`, `password` (this is the user's LDAP password), `email`  and `new_password`.
			
			Additionally, specify `mfa_code` when trying to switch an account on LDAP/AD or email that has MFA activated."""
        return self.send_request('/users/login/switch', 'post', **kwargs)

    def FUNCTION_NAME(self, **kwargs):
        """Generate a user access token that can be used to authenticate with the Mattermost REST API.
			
			__Minimum server version__: 4.1"""
        return self.send_request('/users/{user_id}/tokens', 'post', **kwargs)

    def FUNCTION_NAME(self, **kwargs):
        """Revoke a user access token and delete any sessions using the token.
			
			__Minimum server version__: 4.1"""
        return self.send_request('/users/tokens/revoke', 'post', **kwargs)

    def FUNCTION_NAME(self, **kwargs):
        """Disable a personal access token and delete any sessions using the token. The token can be re-enabled using `/users/tokens/enable`.
			
			__Minimum server version__: 4.4"""
        return self.send_request('/users/tokens/disable', 'post', **kwargs)

    def FUNCTION_NAME(self, **kwargs):
        """Re-enable a personal access token that has been disabled.
			
			__Minimum server version__: 4.4"""
        return self.send_request('/users/tokens/enable', 'post', **kwargs)

    def FUNCTION_NAME(self, **kwargs):
        """Get a list of tokens based on search criteria provided in the request body. Searches are done against the token id, user id and username.
			
			__Minimum server version__: 4.7"""
        return self.send_request('/users/tokens/search', 'post', **kwargs)

    def FUNCTION_NAME(self, **kwargs):
        """Updates a user's authentication method. This can be used to change them to/from LDAP authentication for example.
			
			__Minimum server version__: 4.6"""
        return self.send_request('/users/{user_id}/auth', 'put', **kwargs)

    def FUNCTION_NAME(self, **kwargs):
        """Manually set a user's status. When setting a user's status, the status will remain that value until set "online" again, which will return the status to being automatically updated based on user activity."""
        return self.send_request('/users/{user_id}/status', 'put', **kwargs)

    def FUNCTION_NAME(self, **kwargs):
        """Get a list of user statuses by id from the server."""
        return self.send_request('/users/status/ids', 'post', **kwargs)

    def FUNCTION_NAME(self, **kwargs):
        """Update a team by providing the team object. The fields that can be updated are defined in the request body, all other provided fields will be ignored."""
        return self.send_request('/teams/{team_id}', 'put', **kwargs)

    def FUNCTION_NAME(self, **kwargs):
        """Search teams based on search term provided in the request body."""
        return self.send_request('/teams/search', 'post', **kwargs)

    def FUNCTION_NAME(self, **kwargs):
        """Using either an invite id or hash/data pair from an email invite link, add a user to a team."""
        return self.send_request('/teams/members/invite', 'post', **kwargs)

    def FUNCTION_NAME(self, **kwargs):
        """Add a number of users to the team by user_id."""
        return self.send_request('/teams/{team_id}/members/batch', 'post', **kwargs)

    def FUNCTION_NAME(self, **kwargs):
        """Get a list of team members based on a provided array of user ids."""
        return self.send_request('/teams/{team_id}/members/ids', 'post', **kwargs)

    def FUNCTION_NAME(self, **kwargs):
        """Sets the team icon for the team.
			
			__Minimum server version__: 4.9"""
        return self.send_request('/teams/{team_id}/image', 'post', **kwargs)

    def FUNCTION_NAME(self, **kwargs):
        """Update a team member roles. Valid team roles are "team_user", "team_admin" or both of them. Overwrites any previously assigned team roles."""
        return self.send_request('/teams/{team_id}/members/{user_id}/roles', 'put', **kwargs)

    def FUNCTION_NAME(self, **kwargs):
        """Invite users to the existing team usign the user's email."""
        return self.send_request('/teams/{team_id}/invite/email', 'post', **kwargs)

    def FUNCTION_NAME(self, **kwargs):
        """Import a team into a existing team. Import users, channels, posts, hooks."""
        return self.send_request('/teams/{team_id}/import', 'post', **kwargs)

    def FUNCTION_NAME(self, **kwargs):
        """Create a new channel."""
        return self.send_request('/channels', 'post', **kwargs)

    def FUNCTION_NAME(self, **kwargs):
        """Create a new direct message channel between two users."""
        return self.send_request('/channels/direct', 'post', **kwargs)

    def FUNCTION_NAME(self, **kwargs):
        """Create a new group message channel to group of users. If the logged in user's id is not included in the list, it will be appended to the end."""
        return self.send_request('/channels/group', 'post', **kwargs)

    def FUNCTION_NAME(self, **kwargs):
        """Get a list of public channels on a team by id."""
        return self.send_request('/teams/{team_id}/channels/ids', 'post', **kwargs)

    def FUNCTION_NAME(self, **kwargs):
        """Update a channel. The fields that can be updated are listed as paramters. Omitted fields will be treated as blanks."""
        return self.send_request('/channels/{channel_id}', 'put', **kwargs)

    def FUNCTION_NAME(self, **kwargs):
        """Partially update a channel by providing only the fields you want to update. Omitted fields will not be updated. The fields that can be updated are defined in the request body, all other provided fields will be ignored."""
        return self.send_request('/channels/{channel_id}/patch', 'put', **kwargs)

    def FUNCTION_NAME(self, **kwargs):
        """Restore channel from the provided channel id string.
			
			__Minimum server version__: 3.10"""
        return self.send_request('/channels/{channel_id}/restore', 'post', **kwargs)

    def FUNCTION_NAME(self, **kwargs):
        """Search public channels on a team based on the search term provided in the request body."""
        return self.send_request('/teams/{team_id}/channels/search', 'post', **kwargs)

    def FUNCTION_NAME(self, **kwargs):
        """Add a user to a channel by creating a channel member object."""
        return self.send_request('/channels/{channel_id}/members', 'post', **kwargs)

    def FUNCTION_NAME(self, **kwargs):
        """Get a list of channel members based on the provided user ids."""
        return self.send_request('/channels/{channel_id}/members/ids', 'post', **kwargs)

    def FUNCTION_NAME(self, **kwargs):
        """Update a user's roles for a channel."""
        return self.send_request('/channels/{channel_id}/members/{user_id}/roles', 'put', **kwargs)

    def FUNCTION_NAME(self, **kwargs):
        """Update a user's notification properties for a channel. Only the provided fields are updated."""
        return self.send_request('/channels/{channel_id}/members/{user_id}/notify_props', 'put', **kwargs)

    def FUNCTION_NAME(self, **kwargs):
        """Perform all the actions involved in viewing a channel. This includes marking channels as read, clearing push notifications, and updating the active channel."""
        return self.send_request('/channels/members/{user_id}/view', 'post', **kwargs)

    def FUNCTION_NAME(self, **kwargs):
        """Update a post. Only the fields listed below are updatable, omitted fields will be treated as blank."""
        return self.send_request('/posts/{post_id}', 'put', **kwargs)

    def FUNCTION_NAME(self, **kwargs):
        """Partially update a post by providing only the fields you want to update. Omitted fields will not be updated. The fields that can be updated are defined in the request body, all other provided fields will be ignored."""
        return self.send_request('/posts/{post_id}/patch', 'put', **kwargs)

    def FUNCTION_NAME(self, **kwargs):
        """Search posts in the team and from the provided terms string."""
        return self.send_request('/teams/{team_id}/posts/search', 'post', **kwargs)

    def FUNCTION_NAME(self, **kwargs):
        """Pin a post to a channel it is in based from the provided post id string."""
        return self.send_request('/posts/{post_id}/pin', 'post', **kwargs)

    def FUNCTION_NAME(self, **kwargs):
        """Unpin a post to a channel it is in based from the provided post id string."""
        return self.send_request('/posts/{post_id}/unpin', 'post', **kwargs)

    def FUNCTION_NAME(self, **kwargs):
        """Perform a post action, which allows users to interact with integrations through posts."""
        return self.send_request('/posts/{post_id}/actions/{action_id}', 'post', **kwargs)

    def FUNCTION_NAME(self, **kwargs):
        """Save a list of the user's preferences."""
        return self.send_request('/users/{user_id}/preferences', 'put', **kwargs)

    def FUNCTION_NAME(self, **kwargs):
        """Delete a list of the user's preferences."""
        return self.send_request('/users/{user_id}/preferences/delete', 'post', **kwargs)

    def FUNCTION_NAME(self, **kwargs):
        """Uploads a file that can later be attached to a post.
			
			This request can either be a multipart/form-data request with a channel_id, files and optional
			client_ids defined in the FormData, or it can be a request with the channel_id and filename
			defined as query parameters with the contents of a single file in the body of the request.
			
			Only multipart/form-data requests are supported by server versions up to and including 4.7.
			Server versions 4.8 and higher support both types of requests."""
        return self.send_request('/files', 'post', **kwargs)

    def FUNCTION_NAME(self, **kwargs):
        """Create a new job.
			__Minimum server version: 4.1__"""
        return self.send_request('/jobs', 'post', **kwargs)

    def FUNCTION_NAME(self, **kwargs):
        """Cancel a job.
			__Minimum server version: 4.1__"""
        return self.send_request('/jobs/{job_id}/cancel', 'post', **kwargs)

    def FUNCTION_NAME(self, **kwargs):
        """Recycle database connections by closing and reconnecting all connections to master and read replica databases."""
        return self.send_request('/database/recycle', 'post', **kwargs)

    def FUNCTION_NAME(self, **kwargs):
        """Send a test email to make sure you have your email settings configured correctly. Optionally provide a configuration in the request body to test. If no valid configuration is present in the request body the current server configuration will be tested."""
        return self.send_request('/email/test', 'post', **kwargs)

    def FUNCTION_NAME(self, **kwargs):
        """Send a test to validate if can connect to AWS S3. Optionally provide a configuration in the request body to test. If no valid configuration is present in the request body the current server configuration will be tested."""
        return self.send_request('/file/s3_test', 'post', **kwargs)

    def FUNCTION_NAME(self, **kwargs):
        """Submit a new configuration for the server to use. As of server version 4.8, the `PluginSettings.EnableUploads` setting cannot be modified by this endpoint."""
        return self.send_request('/config', 'put', **kwargs)

    def FUNCTION_NAME(self, **kwargs):
        """Reload the configuration file to pick up on any changes made to it."""
        return self.send_request('/config/reload', 'post', **kwargs)

    def FUNCTION_NAME(self, **kwargs):
        """Upload a license to enable enterprise features.
			
			__Minimum server version__: 4.0"""
        return self.send_request('/license', 'post', **kwargs)

    def FUNCTION_NAME(self, **kwargs):
        """Purge all the in-memory caches for the Mattermost server. This can have a temporary negative effect on performance while the caches are re-populated."""
        return self.send_request('/caches/invalidate', 'post', **kwargs)

    def FUNCTION_NAME(self, **kwargs):
        """Add log messages to the server logs."""
        return self.send_request('/logs', 'post', **kwargs)

    def FUNCTION_NAME(self, **kwargs):
        """Create a custom emoji for the team."""
        return self.send_request('/emoji', 'post', **kwargs)

    def FUNCTION_NAME(self, **kwargs):
        """Search for custom emoji by name based on search criteria provided in the request body. A maximum of 200 results are returned."""
        return self.send_request('/emoji/search', 'post', **kwargs)

    def FUNCTION_NAME(self, **kwargs):
        """Create an incoming webhook for a channel."""
        return self.send_request('/hooks/incoming', 'post', **kwargs)

    def FUNCTION_NAME(self, **kwargs):
        """Update an incoming webhook given the hook id."""
        return self.send_request('/hooks/incoming/{hook_id}', 'put', **kwargs)

    def FUNCTION_NAME(self, **kwargs):
        """Create an outgoing webhook for a team."""
        return self.send_request('/hooks/outgoing', 'post', **kwargs)

    def FUNCTION_NAME(self, **kwargs):
        """Update an outgoing webhook given the hook id."""
        return self.send_request('/hooks/outgoing/{hook_id}', 'put', **kwargs)

    def FUNCTION_NAME(self, **kwargs):
        """Regenerate the token for the outgoing webhook."""
        return self.send_request('/hooks/outgoing/{hook_id}/regen_token', 'post', **kwargs)

    def FUNCTION_NAME(self, **kwargs):
        """Upload the IDP certificate to be used with your SAML configuration. This will also set the filename for the IdpCertificateFile setting in your `config.json`."""
        return self.send_request('/saml/certificate/idp', 'post', **kwargs)

    def FUNCTION_NAME(self, **kwargs):
        """Upload the public certificate to be used for encryption with your SAML configuration. This will also set the filename for the PublicCertificateFile setting in your `config.json`."""
        return self.send_request('/saml/certificate/public', 'post', **kwargs)

    def FUNCTION_NAME(self, **kwargs):
        """Upload the private key to be used for encryption with your SAML configuration. This will also set the filename for the PrivateKeyFile setting in your `config.json`."""
        return self.send_request('/saml/certificate/private', 'post', **kwargs)

    def FUNCTION_NAME(self, **kwargs):
        """Create and save a compliance report."""
        return self.send_request('/compliance/reports', 'post', **kwargs)

    def FUNCTION_NAME(self, **kwargs):
        """Synchronize any user attribute changes in the configured AD/LDAP server with Mattermost."""
        return self.send_request('/ldap/sync', 'post', **kwargs)

    def FUNCTION_NAME(self, **kwargs):
        """Test the current AD/LDAP configuration to see if the AD/LDAP server can be contacted successfully."""
        return self.send_request('/ldap/test', 'post', **kwargs)

    def FUNCTION_NAME(self, **kwargs):
        """Uploads a brand image."""
        return self.send_request('/brand/image', 'post', **kwargs)

    def FUNCTION_NAME(self, **kwargs):
        """Create a command for a team."""
        return self.send_request('/commands', 'post', **kwargs)

    def FUNCTION_NAME(self, **kwargs):
        """Update a single command based on command id string and Command struct."""
        return self.send_request('/commands/{command_id}', 'put', **kwargs)

    def FUNCTION_NAME(self, **kwargs):
        """Generate a new token for the command based on command id string."""
        return self.send_request('/commands/{command_id}/regen_token', 'put', **kwargs)

    def FUNCTION_NAME(self, **kwargs):
        """Execute a command on a team."""
        return self.send_request('/commands/execute', 'post', **kwargs)

    def FUNCTION_NAME(self, **kwargs):
        """Register an OAuth 2.0 client application with Mattermost as the service provider."""
        return self.send_request('/oauth/apps', 'post', **kwargs)

    def FUNCTION_NAME(self, **kwargs):
        """Update an OAuth 2.0 client application based on OAuth struct."""
        return self.send_request('/oauth/apps/{app_id}', 'put', **kwargs)

    def FUNCTION_NAME(self, **kwargs):
        """Regenerate the client secret for an OAuth 2.0 client application registered with Mattermost."""
        return self.send_request('/oauth/apps/{app_id}/regen_secret', 'post', **kwargs)

    def FUNCTION_NAME(self, **kwargs):
        """Test the current Elasticsearch configuration to see if the Elasticsearch server can be contacted successfully.
			Optionally provide a configuration in the request body to test. If no valid configuration is present in the
			request body the current server configuration will be tested.
			
			__Minimum server version__: 4.1"""
        return self.send_request('/elasticsearch/test', 'post', **kwargs)

    def FUNCTION_NAME(self, **kwargs):
        """Deletes all Elasticsearch indexes and their contents. After calling this endpoint, it is
			necessary to schedule a new Elasticsearch indexing job to repopulate the indexes.
			__Minimum server version__: 4.1"""
        return self.send_request('/elasticsearch/purge_indexes', 'post', **kwargs)

    def FUNCTION_NAME(self, **kwargs):
        """Upload a plugin compressed in a .tar.gz file. Plugins and plugin uploads must be enabled in the server's config settings."""
        return self.send_request('/plugins', 'post', **kwargs)

    def FUNCTION_NAME(self, **kwargs):
        """Activate a previously uploaded plugin. Plugins must be enabled in the server's config settings."""
        return self.send_request('/plugins/{plugin_id}/activate', 'post', **kwargs)

    def FUNCTION_NAME(self, **kwargs):
        """Deactivate a previously activated plugin. Plugins must be enabled in the server's config settings."""
        return self.send_request('/plugins/{plugin_id}/deactivate', 'post', **kwargs)

    def FUNCTION_NAME(self, **kwargs):
        """Partially update a role by providing only the fields you want to update. Omitted fields will not be updated. The fields that can be updated are defined in the request body, all other provided fields will be ignored."""
        return self.send_request('/roles/{role_id}/patch', 'put', **kwargs)

    def FUNCTION_NAME(self, **kwargs):
        """Get a list of roles from their names."""
        return self.send_request('/roles/names', 'post', **kwargs)

