# -*- coding: utf-8 -*-
# try something like
@auth.requires_login()
def index(): 
	user_info = db().select(db.auth_user.first_name, 
				db.auth_user.last_name, 
				db.auth_user.orientation_attended,
				db.auth_user.phone,
				db.auth_user.zip,
				db.auth_user.skills,
				db.auth_user.email)
	return dict(message="hello from admin.py",
		    user_info=user_info)

