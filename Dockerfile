# Official Baserow all-in-one image (Caddy, backend, Celery, web frontend)
# with external Postgres and Redis, plus a first-boot admin from env.
FROM baserow/baserow:2.4.1
COPY --chmod=555 railway-start.sh railway-seed.py /railway/
ENTRYPOINT ["/railway/railway-start.sh"]
