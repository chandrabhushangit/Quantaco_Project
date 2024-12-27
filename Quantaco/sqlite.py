import sqlite3
import os

# Path to the existing SQLite database
db_path = 'C:\Quantaco_Project\Quantaco\db.sqlite3'

# Check if the database file exists
if not os.path.exists(db_path):
    print(f"Database file '{db_path}' does not exist.")
else:
    # Connect to the existing database
    conn = sqlite3.connect(db_path)
    print(f"Connected to the database '{db_path}'.")

    # Create a cursor object
    cursor = conn.cursor()

    # Create the table
    cursor.execute('''
    
INSERT INTO `updisht` VALUES (0,'0','0','0','0','0',0,'0.0','0','0','0','0','0','0.0','0','0',0,0,'0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0',NULL),(485,'PUJA','PATEL','father','VIRENDRA KUAMR SINGH','Female',32,'7267984373.0','0','B.A','0','RAMNA','RAMANA','0.0','Varanasi','Uttar Pradesh',221011,20231231,'SWARVED MAHAMANDIR DHAM','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0',NULL),(486,'ALMA','GUPTA','husband','VIMAL GUPTA','Female',35,'8817124545.0','0','M.A','0','JHANDA CHOK BAZAR','BADHRANJI','0.0','Jabalpur','Madhya Pradesh',482001,20231231,'SWARVED MAHAMANDIR DHAM','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0',NULL),(487,'Ruby','Devi','father','Gopal Gupta','Female',0,'6387736899.0','0','10th','0','Chittipur','0','0.0','Varanasi','Uttar Pradesh',221001,20240101,'SWARVED MAHAMANDIR DHAM','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0',NULL),(488,'Sonam','Singh','father','Ajeet Singh','Female',17,'6392979029.0','0','12th','Student','Nasirpur Maudha','0','0.0','Ghazipur','Uttar Pradesh',233221,20240102,'SWARVED MAHAMANDIR DHAM','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0',NULL),(489,'MAYA','DEVI','father','GULSAN MAKR','Female',60,'9810345253.0','0','0','0','NUH','NUH','0.0','Nuh','Haryana',0,20231231,'SWARVED MAHAMANDIR DHAM','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0',NULL),(490,'Anshika','Gupta','father','Gopal Gupta','Female',12,'8318164733.0','0','7th','Student','Lahtara','0','0.0','Varanasi','Uttar Pradesh',221001,20240101,'SWARVED MAHAMANDIR DHAM','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0',NULL),(491,'Komal','Sinha','father','Sonu Kumar Sinha','Female',18,'9336594156.0','0','12th','Student','Ratnapuri','0','0.0','Chandauli','Uttar Pradesh',221008,20240102,'SWARVED MAHAMANDIR DHAM','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0',NULL),(492,'peehu','Maurya','father','Mr Rakesh Kumar Maurya','Female',19,'7275877089.0','0','12th','Student','Paniyalpur','0','0.0','Varanasi','Uttar Pradesh',221007,20240102,'SWARVED MAHAMANDIR DHAM','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0',NULL),(493,'SHREE','DEVI','father','SHEETAL PRASAD','Female',55,'9532097909.0','0','5TH','0','SUSWAHI','SUSWAHI','0.0','Varanasi','Uttar Pradesh',221011,20231231,'SWARVED MAHAMANDIR DHAM','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0',NULL),(494,'Neetu','Gupta','father','Rajendra Gupta','Female',0,'6307582070.0','0','BA','Student','Varanasi','0','0.0','Varanasi','Uttar Pradesh',0,20240103,'SWARVED MAHAMANDIR DHAM','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0',NULL),(495,'Swati','Verma','father','OmPrakash Verma','Female',0,'7905433778.0','0','Graduate','0','Pandeypur','0','0.0','Varanasi','Uttar Pradesh',0,20240103,'SWARVED MAHAMANDIR DHAM','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0',NULL),(496,'URMILA','SHUKLA','father','SASHIBUSHAN SHUKLA','Female',55,'9839226300.0','0','12TH PASS','0','MANDUA DEH','MANDUA DEH','0.0','Varanasi','Uttar Pradesh',221103,20231231,'SWARVED MAHAMANDIR DHAM','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0',NULL),(497,'RAM MANDAR','GUPTA','husband','SHRI BHOLA  GUPTA','Female',45,'9794834998.0','0','B.COM','SERVICE','MANDUA DEH','MANDUA DEH','0.0','Varanasi','Uttar Pradesh',221103,20231231,'SWARVED MAHAMANDIR DHAM','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0',NULL),(498,'MEENU','DEVI','father','RAJKUMAR','Female',37,'8081083734.0','0','12TH PASS','0','SHREE NAGAR COLONY','SHIVPUR','0.0','Varanasi','Uttar Pradesh',221000,20231231,'SWARVED MAHAMANDIR DHAM','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0',NULL),(499,'Khushboo','Singh','father','Mr Mohan Singh','Female',22,'6387538457.0','0','M.Sc','Student','Saraiya','Sindhara','0.0','Mirzapur','Uttar Pradesh',231001,20240101,'SWARVED MAHAMANDIR DHAM','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0',NULL),(500,'MUNNI','DEVI','husband','FEKU SAH','Female',32,'6386440531.0','0','0','0','RAMNAGAR','RAM NAGAR','0.0','Varanasi','Uttar Pradesh',0,20231231,'SWARVED MAHAMANDIR DHAM','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0',NULL);


    ''')

    # Commit the changes
    conn.commit()
    print("Table 'updisht' created successfully.")

    # Close the connection
    conn.close()
    print(f"Connection to the database '{db_path}' closed.")
