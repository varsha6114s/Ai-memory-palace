-- Initialize the AI Memory Palace database

-- Create database if it doesn't exist
SELECT 'CREATE DATABASE memory_palace'
WHERE NOT EXISTS (SELECT FROM pg_database WHERE datname = 'memory_palace')\gexec

-- Connect to the database
\c memory_palace;

-- Create extensions
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- Run the schema
\i /docker-entrypoint-initdb.d/schema.sql

-- Insert sample data for development
INSERT INTO users (username, email, password_hash) VALUES 
('demo_user', 'demo@example.com', '$2b$12$LQv3c1yqBWVHxkd0LHAkCOYz6TtxMQJqhN8/LewdBPj/RK.PZvO.G') -- password: demo123
ON CONFLICT (email) DO NOTHING;

INSERT INTO memory_palaces (title, description, user_id) VALUES 
('My First Palace', 'A beginner-friendly memory palace for learning basic concepts', 1),
('Study Palace', 'Dedicated space for academic learning and retention', 1)
ON CONFLICT DO NOTHING;

INSERT INTO rooms (name, description, palace_id, position_x, position_y) VALUES 
('Entrance Hall', 'The main entry point of the memory palace', 1, 0, 0),
('Library', 'A quiet space for storing book knowledge', 1, 100, 0),
('Laboratory', 'For scientific concepts and experiments', 2, 0, 0)
ON CONFLICT DO NOTHING;

INSERT INTO memory_items (title, content, room_id, position_x, position_y) VALUES 
('Welcome Note', 'Welcome to your first memory palace! This is where you store and organize information.', 1, 50, 50),
('Memory Technique', 'The method of loci uses spatial memory to enhance recall of information.', 2, 25, 75),
('Scientific Method', 'Observation → Hypothesis → Experiment → Analysis → Conclusion', 3, 75, 25)
ON CONFLICT DO NOTHING;