from django.http import JsonResponse
from rest_framework.views import APIView
from .utils import get_connection
import json
from .models import UpdishtSubmit,Updisht,AccessUser,CustomUser
import base64

class Login(APIView):

    pass
class Dashboard(APIView):
    
    def get(self, request, format=None):
        print("api called")
        connection = get_connection(autocommit=True)
        sql_query = "SELECT \
        First_Name AS firstName, \
        Last_Name AS lastName, \
        Guardian_Type AS guardianType, \
        Guardian_Name AS guardianName, \
        Gender AS gender, \
        Age AS age, \
        Contact_No AS contactNo, \
        Email_ID AS email, \
        Education_Qualification AS education, \
        Occupation AS occupation, \
        Vill_Mohalla AS village, \
        Post AS post, \
        City AS city, \
        District AS district, \
        State AS state, \
        Pin AS pin, \
        Date_of_Updesh AS dateOfUpdesh, \
        Place_of_Updesh AS placeOfUpdesh, \
        Name_Of_Motivator AS motivatorName, \
        Motivator_Contact_No AS motivatorContact, \
        Motivator_Address AS motivatorAddress, \
        Updeshta_Name AS updeshtaName, \
        Updeshta_Contact_No AS updeshtaContact, \
        Address AS updeshtaAddress, \
        Date_Of_Calling AS dateOfCalling, \
        Caller_Introduction AS callersIntroduction, \
        Comfortable_Language AS comfortableLanguage, \
        Sadhna AS sadhna, \
        Photo AS photo, \
        Aarti_Vandana AS aartiVandana, \
        Remarks AS remarks, \
        Call_on_8586808820_For_More_Information AS callOn8586808820ForMoreInformation, \
        Comment AS comment, \
        Caller_Name AS callerName, \
        Caller_No AS callerNo, \
        Group_Leader_Name AS groupLeaderName, \
        Group_Leader_No AS groupLeaderNo ,\
        Status_of_call AS statusOfCall\
    FROM updisht  where first_Name !='0';"

        # Create a cursor object
        cursor = connection.cursor()
        
        # Execute SQL query
        cursor.execute(sql_query)

        # Fetch the data
        data = cursor.fetchall()
        column_names = [desc[0] for desc in cursor.description]
        # Close cursor and connection
        cursor.close()
        connection.close()
        # print(data)
        # base64_encoded_data = base64.b64encode(data).decode('utf-8')
        # json_data = json.dumps({"bytes_data": base64_encoded_data})
        processed_data = []
        for item in data:
            print(item)
            if isinstance(item, dict):
                print("coming in doct")
                for key, value in item.items():
                    if isinstance(value, bytes):
                        item[key] = value.decode('utf-8')
                processed_data.append(item)
            elif isinstance(item, tuple):
                # print("coming in doct")
                # Convert tuple to dictionary assuming the tuple has a fixed structure
                item_dict = {column_names[i]: value for i, value in enumerate(item)}
                for key, value in item_dict.items():
                    if isinstance(value, bytes):
                        item_dict[key] = value.decode('utf-8')
                processed_data.append(item_dict)
            else:
                print("coming in else ")
                processed_data.append(item)

        # Convert to JSON
        print(processed_data)
        json_data = json.dumps(processed_data)
        #print(json_data,"json data")
        
          
        return JsonResponse(json_data, safe=False)


class Submit(APIView):
    def get_submit(self,submitted_data):
        updisht_submit = UpdishtSubmit.objects.create(
            First_Name=submitted_data.get('firstName'),
            Last_Name=submitted_data.get('lastName'),
            Guardian_Type=submitted_data.get('guardianType'),
            Guardian_Name=submitted_data.get('guardianName'),
            Gender=submitted_data.get('gender'),
            Age=submitted_data.get('age'),
            Contact_no=submitted_data.get('contactNo'),
            Email_ID=submitted_data.get('email'),
            Education_Qualification=submitted_data.get('education'),
            Occupation=submitted_data.get('occupation'),
            Vill_Mohalla=submitted_data.get('village'),
            Post=submitted_data.get('post'),
            City=submitted_data.get('city'),
            District=submitted_data.get('district'),
            State=submitted_data.get('state'),
            Pin=submitted_data.get('pin'),
            Date_of_Updesh=submitted_data.get('dateOfUpdesh'),
            Place_of_Updesh=submitted_data.get('placeOfUpdesh'),
            Name_Of_Motivator=submitted_data.get('motivatorName'),
            Motivator_Contact_No=submitted_data.get('motivatorContact'),
            Motivator_Address=submitted_data.get('motivatorAddress'),
            Updeshta_Name=submitted_data.get('updeshtaName'),
            Updeshta_Contact_No=submitted_data.get('updeshtaContact'),
            Address=submitted_data.get('updeshtaAddress'),
            Date_Of_Calling=submitted_data.get('dateOfCalling'),
            Caller_Introduction=submitted_data.get('callersIntroduction'),
            Comfortable_Language=submitted_data.get('comfortableLanguage'),
            Sadhna=submitted_data.get('sadhna'),
            Photo=submitted_data.get('photo'),
            Aarti_Vandana=submitted_data.get('aartiVandana'),
            Remarks=submitted_data.get('remarks'),
            Call_on_8586808820_For_More_Information=submitted_data.get('callOn8586808820ForMoreInformation'),
            Comment=submitted_data.get('comment'),
            Caller_Name=submitted_data.get('callerName'),
            Caller_No=submitted_data.get('callerNo'),
            Group_Leader_Name=submitted_data.get('groupLeaderName'),
            Group_Leader_No=submitted_data.get('groupLeaderNo'),
            Status_of_call=submitted_data.get('statusOfCall')
        )
    def get_delete(self,submitted_data):
        first_name = submitted_data.get('firstName')
        last_name = submitted_data.get('lastName')
        guardian_type = submitted_data.get('guardianType')
        guardian_name = submitted_data.get('guardianName')
        gender = submitted_data.get('gender')
        age = submitted_data.get('age')
        contact_no = submitted_data.get('contactNo')
        connection = get_connection(autocommit=True)
        sql_query = """
    DELETE FROM updisht
    WHERE First_Name = '{first_name}'
    AND Last_Name = '{last_name}'
    AND Guardian_Type = '{guardian_type}'
    AND Guardian_Name = '{guardian_name}'
    AND Gender = '{gender}'
    AND Age = {age}
    AND Contact_no = '{contact_no}'
"""

# Format the query with the provided data
        sql_query_formatted = sql_query.format(
            first_name=first_name,
            last_name=last_name,
            guardian_type=guardian_type,
            guardian_name=guardian_name,
            gender=gender,
            age=age,
            contact_no=contact_no
        )

        # Execute the SQL query
        cursor = connection.cursor()
        cursor.execute(sql_query_formatted)

        # Commit the changes
        connection.commit()

        # Close the cursor and database connection
        cursor.close()
        connection.close()
    def post(self, request, format=None):
        if request.method == 'POST':
            
            submitted_data = json.loads(request.body)# If the data is sent as form data
        # Or use request.body for JSON data: submitted_data = request.body
            
            # submitted_data = json.loads(request.body.decode('utf-8'))
            data_submit=self.get_submit(submitted_data)
            data_delete=self.get_delete(submitted_data)
            
            # Create a new instance of the UpdishtSubmit model using the submitted data
            

            # Print the request data
            
            
            # Return a JSON response indicating successful submission
            return JsonResponse({'message': 'Data submitted successfully'})
        else:
            # If the request method is not POST, return a 405 Method Not Allowed response
            return JsonResponse({'error': 'Method not allowed'}, status=405)