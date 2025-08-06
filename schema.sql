CREATE TABLE agent_skills (
    user_id INTEGER,
    category TEXT,
    FOREIGN KEY(user_id) REFERENCES users(id)
);
