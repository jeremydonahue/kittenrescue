# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## This is a sample controller
## - index is the default action of any application
## - user is required for authentication and authorization
## - download is for downloading files uploaded in the db (does streaming)
#########################################################################

def index():
    """
    example action using the internationalization operator T and flash
    rendered by views/default/index.html or views/generic.html

    if you need a simple wiki simply replace the two lines below with:
    return auth.wiki()
    """
    #response.flash = T("Hello World")
    return dict(message=T('Welcome to web2py!'))


def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/manage_users (requires membership in
    http://..../[app]/default/user/bulk_register
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    Field('address'),
      Field('city'),
        Field('zip'),
          Field('phone'),
            Field('skills'),

    """
    fields_to_hide = ['orientation_attended']

    if 'register' in request.args:
        for fieldname in ['address', 'city', 'zip', 'phone', 'skills']:
            fields_to_hide.append(fieldname)
    #else:
    #    fields_to_hide.append('email')

    for fieldname in fields_to_hide:
        field = db.auth_user[fieldname]
        field.readable = field.writable = False 
    db.auth_user.address.comment = "We ask for this so we can call on people for help who are close to where the help is needed."
    db.auth_user.skills.comment = "Please list any skills you believe may be beneficial to the Kitten Sanctuary. It can be anything!"
    return dict(form=auth())


@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()


