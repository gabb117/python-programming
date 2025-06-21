#interaction with mySQL server "school" via python language

import pymysql  # Import the PyMySQL library to interact with a MySQL database

def main():
    # Establish a connection to the MySQL database
    conn = pymysql.connect(
        host="localhost",
        port=3306,
        user="gabriele",
        password="unipegaso",
        db="school"
    )

    # Create a cursor object to interact with the database
    cur = conn.cursor()

    # Define the SQL query to select all records from the 'student' table
    query = "SELECT * FROM student"
    
    # Execute the query and store the number of rows returned
    n_lines = cur.execute(query)

    print("Extracted " + str(n_lines) + " database lines")
    print()

    # Fetch all the results from the executed query and convert to a list
    results = list(cur.fetchall())

    # Print the type of 'results' (should be a list of tuples)
    print(type(results))
    print()

    # Print the raw query result
    print("Print query result\n ", results)

    print()
    print("Elements contained in results")

    # Print each row in the result set, every "el" is a tuple contained in cur.fetchall()
    for el in results:
        print(el)

    print()
    print("Alternative view of results content")

    # Print each individual value from each row, separated by spaces
    for element in results:
        for e in element:
            print(e, end=" ")
        print()

# Run the main function
main()