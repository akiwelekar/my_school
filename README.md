# my_school

Custom ERPNext / Frappe app for Department Education portal.

## Features
- Provides portal APIs:
  - `my_school.api.student_portal.get_student_summary`
  - `my_school.api.teacher_portal.get_teacher_summary`
- Example web pages in `www/`

## Install (on bench)
```bash
bench get-app https://github.com/<your-org>/my_school.git
bench --site yoursite install-app my_school
bench build
bench restart
```

## Notes
- Update `__version__` in `my_school/__init__.py` when releasing.
- Tag releases (git tag v0.1.0) so Frappe Cloud can pin branches/tags.
