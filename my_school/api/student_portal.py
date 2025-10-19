import frappe
from frappe import _
from frappe.utils import now_datetime

@frappe.whitelist(allow_guest=False)
def get_student_summary():
    """Return a safe attendance + assessment summary for the logged-in student."""
    user = frappe.session.user
    student = frappe.get_value("Student", {"user_id": user, "enabled": 1}, ["name", "student_name"], as_dict=True)
    if not student:
        frappe.throw(_("No Student record linked to current user."), title=_("Unauthorized"))

    rows = frappe.get_all(
        "Student Attendance",
        filters={"student": student.name},
        fields=["status", "attendance_date"]
    )

    summary = {}
    for r in rows:
        status = r.get("status") or "Other"
        summary[status] = summary.get(status, 0) + 1

    assessments = frappe.get_all(
        "Student Assessment",
        filters={"student": student.name},
        fields=["name", "assessment", "score", "grade", "date"],
        order_by="date desc",
        limit_page_length=50
    )

    total = sum(summary.values())
    present = summary.get("Present", 0)
    attendance_pct = (present / total * 100) if total else None

    return {
        "student": student,
        "attendance_summary": summary,
        "attendance_total": total,
        "attendance_percentage": attendance_pct,
        "assessments": assessments,
        "fetched_at": now_datetime().isoformat()
    }
