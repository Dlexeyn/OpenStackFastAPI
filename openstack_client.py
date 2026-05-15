import openstack
from settings import settings


_conn = None


def get_conn():
    global _conn

    if _conn is None:
        print("[OpenStack] Creating connection...")

        _conn = openstack.connection.Connection(
            region_name='example-region',
            auth={
                'auth_url': settings.os_auth_url,
                'username': settings.os_username,
                'password': settings.os_username,
                'project_id': '044491489eda437dbcae90caaa344280',
                'user_domain_id': 'default',
            },
            compute_api_version='3',
        )


        try:
            list(_conn.compute.servers(limit=1))
            print("[OpenStack] API reachable (compute OK)")
        except Exception as e:
            print(f"[OpenStack] Connection test FAILED: {e}")
        print("[OpenStack] Connection created successfully")

    return _conn