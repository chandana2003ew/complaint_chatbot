from services.assignment_service import assign_ticket
from services.notification_service import send_email

...

assigned_to = assign_ticket(category, priority)

db.execute("""
    INSERT INTO complaints (user_id, message, category, priority, assigned_to) 
    VALUES (?, ?, ?, ?, ?)""",
    (user_id, message, category, priority, assigned_to))
db.commit()

# Notify user
user_email = db.execute("SELECT email FROM users WHERE id = ?", (user_id,)).fetchone()['email']
send_email(user_email, "Your complaint has been registered", f"Category: {category}\nPriority: {priority}\nAssigned to: {assigned_to or 'pending'}")
