#!/bin/bash
# Migrate, create the admin while nothing is listening yet, then start the
# normal all-in-one stack (its own migrate step is then a no-op).
set -euo pipefail
# PORT is for Railway routing only; Nuxt would read it and bind Caddy's :80.
unset PORT
/baserow.sh backend-cmd wait_for_db
/baserow.sh backend-cmd setup
/baserow.sh backend-cmd manage shell -c "$(cat /railway/railway-seed.py)"
exec /baserow.sh start
