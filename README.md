

Connecting to RDS instance of Postgres
=======================================


Inside your EC2, you can do this:

```bash
psql -h <RDS_ENDPOINT> -U postgres -d postgres -p 5432
```

Replace the `RDS_ENDPOINT` with your own.

**Note** You may be required to type your password.