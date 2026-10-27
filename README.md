# Deploy and Host Baserow on Railway

[![Deploy on Railway](https://railway.com/button.svg)](https://railway.com/new/template/baserow-database?referralCode=sLjDXb&utm_medium=integration&utm_source=button&utm_campaign=baserow-database)

[Baserow](https://baserow.io/) is an open-source no-code database and app builder, the self-hosted alternative to Airtable. Teams build tables with linked records, formulas, files and many views (grid, gallery, form, kanban, calendar), automate with webhooks and a full REST API, and publish simple apps on top. This template runs Baserow 2.4.1 from the official image on its own Postgres 17 and Redis, creates the admin account on first boot and closes public sign-up.

## About Hosting Baserow

The stack is three services: Baserow, Postgres and Redis.

- **Upstream's image, pinned.** Baserow runs the official all-in-one `baserow/baserow` image at a fixed release (2.4.1), not `latest`. A thin wrapper ([source](https://github.com/two-workspaces/baserow)) adds one start script and a seed script, nothing else.
- **Admin on first boot, sign-up closed.** Migrations run first, then the admin is created from `BASEROW_ADMIN_EMAIL` and the generated `BASEROW_ADMIN_PASSWORD` and new sign-ups are switched off, so your public URL never offers an open registration page. Invite teammates from the workspace, or turn sign-ups back on in the Admin settings.
- **External Postgres and Redis.** The bundled database and Redis are off. Your data lives in a dedicated Postgres 17 service and the job queue in Redis, both on the private network only.
- **Sized for Railway.** The image runs in its minimal mode (one combined Celery worker) with two web workers, which keeps the stack at about 1.6 GB of RAM when idle (Baserow 1.5 GB, Postgres 100 MB, Redis 15 MB). That is above the Free plan's limit, so use Hobby or higher.
- **Files on a volume.** Uploaded files and images are stored on a volume at `/baserow/data` and served from your domain.

## Common Use Cases

- Replacing Airtable for project trackers, CRMs, content calendars and inventory with no per-seat pricing
- A shared database for operations teams, with forms for intake and kanban or calendar views for planning
- A backend for internal tools and automations through Baserow's REST API, webhooks, n8n or Zapier
- Keeping sensitive business data on your own infrastructure for GDPR or company policy

## Dependencies for Baserow Hosting

- Postgres 17 (included, private network only)
- Redis 8 (included, private network only)

### Deployment Dependencies

- [Baserow documentation](https://baserow.io/docs/index)
- [Configuration and environment variables](https://baserow.io/docs/installation/configuration)
- [Baserow on GitLab](https://gitlab.com/baserow/baserow)
- [Template source on GitHub](https://github.com/two-workspaces/baserow)

### Implementation Details

**First boot takes a few minutes.** Baserow runs a few hundred migrations and loads its templates before it answers. Wait for the deploy to turn green.

**Sign in.** Open your Baserow domain and sign in with `BASEROW_ADMIN_EMAIL` and the password in the Baserow service's `BASEROW_ADMIN_PASSWORD` variable. The variables are only read on the first boot; change the password in Baserow afterwards (Settings, Password).

**Email.** Invitations and password resets need SMTP, and Railway only allows outbound SMTP on the Pro plan. To send, set `EMAIL_SMTP=true`, `EMAIL_SMTP_HOST`, `EMAIL_SMTP_PORT`, `EMAIL_SMTP_USER`, `EMAIL_SMTP_PASSWORD`, `EMAIL_SMTP_USE_TLS` and `FROM_EMAIL` on the Baserow service. Without SMTP, Baserow prints every email it would send, invitation links included, to the Baserow service's deploy logs, so you can copy an invite link from there.

**Custom domains.** Add the domain to the Baserow service in Railway, then set `BASEROW_PUBLIC_URL` to `https://your.domain` and redeploy.

**Upgrading.** Bump the version in the Dockerfile of your fork and redeploy. Migrations run on every start, so back up Postgres before a major version.

**Back up.** Tables and settings are in Postgres; uploaded files are on the Baserow volume. Use Railway's volume backups or `pg_dump`.

## Why Deploy Baserow on Railway?

Railway is a singular platform to deploy your infrastructure stack. Railway will host your infrastructure so you don't have to deal with configuration, while allowing you to vertically and horizontally scale it.

By deploying Baserow on Railway, you are one step closer to supporting a complete full-stack application with minimal burden. Host your servers, databases, AI agents, and more on Railway.
