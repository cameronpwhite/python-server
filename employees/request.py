EMPLOYEES = [
    {
        "id": 1,
        "name": "Jessica Younker",
        "email": "jessica@younker.com"
    },
    {
        "id": 2,
        "name": "Jordan Nelson",
        "email": "jordan@nelson.com"
    },
    {
        "id": 3,
        "name": "Zoe LeBlanc",
        "email": "zoe@leblanc.com"
    },
    {
        "name": "Meg Ducharme",
        "email": "meg@ducharme.com",
        "id": 4
    },
    {
        "name": "Hannah Hall",
        "email": "hannah@hall.com",
        "id": 5
    }
]

def get_all_employees():
    return EMPLOYEES

def get_single_employee(id):
    
    requested_employee = None

    for employee in EMPLOYEES:
        if employee["id"] == id:
            requested_employee = employee

    return requested_employee
