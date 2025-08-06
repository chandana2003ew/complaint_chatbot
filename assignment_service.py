from utils.database import get_db

# Sample logic to get available agents based on category and workload
def assign_ticket(category, priority):
    db = get_db()
    
    # Fetch agents with expertise in the category
    agents = db.execute("""
        SELECT id, name FROM users 
        WHERE role = 'agent' AND id IN (
            SELECT user_id FROM agent_skills WHERE category = ?
        )
    """, (category,)).fetchall()

    if not agents:
        return None  # No skilled agents available

    # Sort agents by fewest assigned open tickets
    best_agent = None
    min_load = float('inf')

    for agent in agents:
        open_tickets = db.execute("""
            SELECT COUNT(*) FROM complaints 
            WHERE assigned_to = ? AND status != 'Resolved'
        """, (agent['name'],)).fetchone()[0]

        if open_tickets < min_load:
            best_agent = agent
            min_load = open_tickets

    return best_agent['name'] if best_agent else None
