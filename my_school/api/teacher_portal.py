import frappe
from frappe import _

@frappe.whitelist(allow_guest=False)
def get_teacher_summary():
    user = frappe.session.user
    teacher = frappe.get_value("Instructor", {"user_id": user, "enabled": 1}, ["name", "instructor_name"], as_dict=True)
    if not teacher:
        frappe.throw(_("No Instructor record linked to current user."), title=_("Unauthorized"))

    courses = frappe.get_all(
        "Course",
        filters={"owner": teacher.name},
        fields=["name", "course_name", "course_code"]
    )

    return {"teacher": teacher, "courses": courses}
