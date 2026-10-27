# Baserow makes whoever signs up first the instance admin. Create that
# account from BASEROW_ADMIN_EMAIL / BASEROW_ADMIN_PASSWORD and close public
# sign-up, so a fresh public URL can't be claimed. Skipped once users exist.
import os
from django.contrib.auth import get_user_model
from baserow.core.handler import CoreHandler
from baserow.core.user.handler import UserHandler

if get_user_model().objects.exists():
    print("[railway] users exist, admin not seeded")
else:
    email = os.environ["BASEROW_ADMIN_EMAIL"]
    UserHandler().create_user(
        name=os.environ.get("BASEROW_ADMIN_NAME", "Admin"),
        email=email,
        password=os.environ["BASEROW_ADMIN_PASSWORD"],
        email_verified=True,
    )
    settings = CoreHandler().get_settings()
    settings.allow_new_signups = False
    settings.save()
    print(f"[railway] admin {email} created, public sign-up closed")
