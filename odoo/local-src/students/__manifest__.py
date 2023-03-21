{
    "name": "Gestion des étudiants",
    "version": "2.0",
    "category": "Generic Modules/Others",
    "description": """Test création module gestion des étudiants Odoo v14""",
    "author": "BOTTA",
    "depends": ["base"],
    "data": [
        "data/students_training_data.xml",
        "data/students_student_data.xml",
        #"data/students_mark_data.xml",
        "views/students_views.xml",
        "views/studentscontinuous_views.xml",
        "views/trainings_views.xml",
        "views/res_partner_views.xml",
        "views/notes_views.xml",
        "reports/students_report.xml",
    ],
    "installable": True,
    "auto_install": False,
}








