# E-Commerce Dashboard — Django Conversion

This is a Django conversion of the original Flask + SQLite e-commerce dashboard.

## Features
- Dashboard statistics
- Product CRUD
- Search and filters
- Stock status
- Revenue analytics by category
- Django ORM + SQLite
- CSRF protection for POST forms
- Django admin

## Run

```bash
python -m venv venv
# Windows: venv\Scripts\activate
# macOS/Linux: source venv/bin/activate

pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Open http://127.0.0.1:8000/

### Existing data

The converted project includes the original `ecommerce.db` data. Because Django uses a slightly different model metadata layout, the included migration creates the Django table structure. To import the original records into the migrated database, run:

```bash
python manage.py shell
```

Then use the import script below, or simply use the included `import_legacy_data.py`:

```bash
python import_legacy_data.py
```

If you want a clean database instead, delete `ecommerce.db` before running `python manage.py migrate`.
