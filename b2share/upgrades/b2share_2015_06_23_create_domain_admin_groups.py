"""
Upgrade script that creates the groups of domain administrators
"""

depends_on = ['invenio_release_1_1_0']

def info():
    """Create the groups of domain administrators."""
    return "Create the groups of domain administrators."


def do_upgrade():
    """Implement your upgrades here."""
    from b2share.modules.b2deposit.edit import get_domain_admin_group
    from b2share.modules.b2deposit.b2share_model import metadata_classes

    from invenio_accounts.models import User
    from invenio_ext.login import login_user
    from flask.ext.login import current_user
    admin_user = User.query.get(1)
    login_user(admin_user.get_id())

    if not current_user.is_super_admin:
        raise Exception("Cannot find the superadmin user")

    for domain in metadata_classes():
        groupname = get_domain_admin_group(domain)
        print "Creating domain administrator group: ", groupname
        create_user_group(groupname,
                'Administrators of the {} domain'.format(domain),
                admin_user)


def create_user_group(usergroup_name, description, admin_user_of_group):
    from invenio_ext.sqlalchemy import db
    from invenio_accounts.models import Usergroup, UserUsergroup

    group = Usergroup.query.filter(Usergroup.name == usergroup_name).first()
    if group:
        return False

    ug = Usergroup()
    ug.name = usergroup_name
    ug.description = description
    ug.join_policy = Usergroup.JOIN_POLICIES['VISIBLEMAIL']
    ug.login_method = u'INTERNAL'

    ug.join(status=UserUsergroup.USER_STATUS['ADMIN'], user=admin_user_of_group)

    db.session.add(ug)
    try:
        db.session.commit()
    except:
        db.session.rollback()
        raise
    return True


from invenio_base.factory import with_app_context
@with_app_context()
def main():
    print info()
    do_upgrade()

if __name__ == '__main__':
    print("Starting!")
    main()
    print("Done!")