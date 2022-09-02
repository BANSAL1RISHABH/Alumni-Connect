import mysql.connector
from mysql.connector import errorcode

# Obtain connection string information from the portal

config = {
    'host': 'alumniconnect.mysql.database.azure.com',
    'user': 'alumniconnect',
    'password': 'Admin@123',
    'database': 'alumni_connect',
    'client_flags': [mysql.connector.ClientFlag.SSL],
    'ssl_ca': 'D:\Minor Project\Alumni Connect\Database files\DigiCertGlobalRootG2.crt.pem'
}

# Construct connection string

try:
    conn = mysql.connector.connect(**config)
    print("Connection established")
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with the user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)
else:
    cursor = conn.cursor()

    # Create table
    # cursor.execute(
    #     "CREATE TABLE alumni_students (register_no VARCHAR(15) NOT NULL PRIMARY KEY UNIQUE KEY, first_name VARCHAR(45) NOT NULL, last_name VARCHAR(45) NOT NULL, email_ID VARCHAR(45) UNIQUE KEY NOT NULL, phone_no VARCHAR(12) NOT NULL, college_name varchar(100) NOT NULL, DOB varchar(15) NOT NULL, Gender varchar(20) NOT NULL, linkedin_profile text, github_profile text, other_links text );")
    # print("Finished creating table.")

    # Insert some data into table
    # cursor.execute(
    #     "INSERT INTO inventory (name, quantity) VALUES (%s, %s);", ("orange", 154))
    # print("Inserted", cursor.rowcount, "row(s) of data.")

    # Read data
    cursor.execute("SELECT * FROM alumni_students;")
    rows = cursor.fetchall()
    print("Read", cursor.rowcount, "row(s) of data.")

    # Print all rows
    for row in rows:
        print("Data row = (%s, %s, %s)" %
              (str(row[0]), str(row[1]), str(row[2])))

    # Cleanup
    conn.commit()
    cursor.close()
    conn.close()
    print("Done.")
