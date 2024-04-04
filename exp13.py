import sqlite3

# Connect to SQLite database (creates if not exists)
conn = sqlite3.connect('mydatabase.db')

# Create a cursor object
cursor = conn.cursor()

# Create a table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        age INTEGER
    )
''')

# Function to create a new user
def create_user(name, age):
    cursor.execute('INSERT INTO users (name, age) VALUES (?, ?)', (name, age))
    conn.commit()
    print('User created successfully!')

# Function to read all users
def read_users():
    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()
    if users:
        for user in users:
            print(f'ID: {user[0]}, Name: {user[1]}, Age: {user[2]}')
    else:
        print('No users found.')

# Function to update a user by ID
def update_user(user_id, name, age):
    cursor.execute('UPDATE users SET name=?, age=? WHERE id=?', (name, age, user_id))
    conn.commit()
    print('User updated successfully!')

# Function to delete a user by ID
def delete_user(user_id):
    cursor.execute('DELETE FROM users WHERE id=?', (user_id,))
    conn.commit()
    print('User deleted successfully!')

# Main function to demonstrate CRUD operations
def main():
    create_user('Alice', 25)
    create_user('Bob', 30)

    print('---Users---')
    read_users()

    update_user(1, 'Alice Smith', 26)

    print('---Updated Users---')
    read_users()

    delete_user(2)

    print('---After Deletion---')
    read_users()

# Execute the main function
if __name__ == "__main__":
    main()

# Close the connection
conn.close()
