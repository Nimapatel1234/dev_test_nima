
# Dev Test - Nima

This project fulfills the requirements of the assignment given in `task.txt`, which includes:
- A CV Picture Detection program.
- A Django-based Ticketing System with Admin and Staff functionalities.

---

##  Features

### 1. CV Picture Detection
- Upload a CV file (PDF).
- Detect whether it contains a profile picture using OpenCV.

### 2. Ticketing System (Django)
#### Admin User:
- Create, edit, block/unblock, and delete Staff Users.
- Assign Staff Users to Projects.
- Manage Tickets (Create, Update, Delete).
- Change ticket status from Completed to Archived.

#### Staff User:
- View dashboard showing ticket counts (Draft, Ongoing, Completed).
- View only assigned tickets.
- Filter tickets by status.
- Update ticket status (Ongoing, Completed only).
- Logout functionality.

### 3. Ticket Management
- Ticket fields: Name (Unique), Description, Assigned To, Status, Attachments (multiple).
- Multiple file attachments allowed (Images, Videos, Documents).
- Status flow managed: Draft ➔ Ongoing ➔ Completed ➔ Archived.

### 4. Project Management
- Admin can create Projects and assign multiple Staff Users.
- Staff Users linked to multiple Projects.

---

## 🛠 Technologies Used

- Python 3.12
- Django 5.2
- OpenCV
- HTML/CSS (Simple custom styling)
- SQLite (default Django DB)

---

##  Installation Instructions

1. Clone the repository:

```bash
git clone https://github.com/Nimapatel1234/dev_test_nima.git
cd dev_test_nima
```

2. Create a virtual environment and activate it:

```bash
python -m venv venv
source venv/bin/activate   
```

3. Install requirements:

```bash
pip install -r requirements.txt
```

(If no requirements.txt provided, manually install Django, OpenCV, Pillow.)

4. Apply migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

5. Create superuser for Admin access:

```bash
python manage.py createsuperuser
```

6. Run the server:

```bash
python manage.py runserver
```

7. Access the application at:

```
http://127.0.0.1:8000/
```

---

##  Admin Panel

- Admin: `/admin/`
- Use superuser credentials created earlier.

---

## Project Structure Highlights

| Directory | Purpose |
|:---|:---|
| `cvchecker/` | App for CV picture detection |
| `tickets/` | App for ticket and project management |
| `users/` | App for managing Staff Users |
| `ticket_system/` | Project configuration (settings, urls) |

