<template>
  <div id="app">
    <!-- Sidebar -->
    <button class="toggle-button" @click="toggleSidebar">&#9776; Menu</button>
    <div id="sidebar" :class="{ 'active': showSidebar }">
      <ul>
        <li><a href="#">View Profile</a></li>
        <li><a href="#">Logout</a></li>
        <!-- Add other sidebar options here -->
      </ul>
    </div>

    <!-- Main Content -->
    <div id="main-content" :style="{ marginLeft: showSidebar ? '250px' : '0' }">
      <!-- New Header -->
      <header id="header">
        <h1>UPDISHT INFORMATION</h1>
      </header>
    
      <!-- Table to display Updisht information -->
      <!-- Container for the table with scrolling features -->
    <div class="table-container">      <!-- Table to display Updisht information -->
      
      <div class="table-scroll">
        <table>
          <thead style="background-color: #0a4275;">
            <tr>
              <th>S. No</th>
              <th>First Name</th>
              <th>Last Name</th>
              <th>Guardian Type</th>
              <th>Guardian Name</th>
              <th>Gender</th>
              <th>Age</th>
              <th>Contact No</th>
              <th>Email ID</th>
              <th>Education Qualification</th>
              <th>Occupation</th>
              <th>Vill/Mohalla</th>
              <th>Post</th>
              <th>City</th>
              <th>District</th>
              <th>State</th>
              <th>Pin</th>
              <th>Date of Updesh</th>
              <th>Place of Updesh</th>
              <th>Date Of Calling</th>
              <th>Caller's Introduction</th>
              <th>Status of Calling</th>
              <th>Comfortable Language</th>
              <th>Sadhna</th>
              <th>Photo</th>
              <th>Arti/vandana</th>
              <th>Remarks</th>
              <th>Called For Info</th>
              <th>Comment</th>
              <th>Caller Name</th>
              <th>Caller No</th>
              <th>Group Leader Name</th>
              <th>Group Leader Number</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(updisht, index) in displayedData" :key="index">
              <td>{{ index + 1 }}</td>
              <td>{{ updisht.firstName }}</td>
              <td>{{ updisht.lastName }}</td>
              <td>{{ updisht.guardianType }}</td>
              <td>{{ updisht.guardianName }}</td>
              <td>{{ updisht.gender }}</td>
              <td>{{ updisht.age }}</td>
              <td>{{ updisht.contactNo }}</td>
              <td>{{ updisht.email }}</td>
              <td>{{ updisht.education }}</td>
              <td>{{ updisht.occupation }}</td>
              <td>{{ updisht.village }}</td>
              <td>{{ updisht.post }}</td>
              <td>{{ updisht.city }}</td>
              <td>{{ updisht.district }}</td>
              <td>{{ updisht.state }}</td>
              <td>{{ updisht.pin }}</td>
              <td>{{ updisht.dateOfUpdesh }}</td>
              <td>{{ updisht.placeOfUpdesh }}</td>
              <td>
                <div class="date-picker-container">
                  <input type="text" v-model="updisht.dateOfCalling" @focus="showDatePicker">
                  <div v-if="showDatePickerFlag" class="date-picker" ref="datePicker"></div>
                </div>
              </td>
              <td>
                <select v-model="updisht.callersIntroduction">
                  <option value="Given">Given</option>
                  <option value="Not Given">Not Given</option>
                </select>
              </td>
              <td>
                <select v-model="updisht.statusOfCall">
                  <option value="Call Connected">Call Connected</option>
                  <option value="Call Not Connected">Call Not Connected</option>
                </select>
              </td>
              <td>
                <select v-model="updisht.comfortableLanguage">
                  <option value="English">English</option>
                  <option value="Hindi">Hindi</option>
                  <option value="Bengali">Bengali</option>
                  <option value="Bhojpuri">Bhojpuri</option>
                  <option value="Kannada">Kannada</option>
                </select>
              </td>
              <td>
                <select v-model="updisht.sadhna">
                  <option value="Regular/Twice a day">Regular/Twice a day</option>
                  <option value="Regular/once a day">Regular/once a day</option>
                  <option value="Irregular">Irregular</option>
                  <option value="Not at all">Not at all</option>
                  <option value="No info Provided">No info Provided</option>
                </select>
              </td>
              <td>
                <select v-model="updisht.photo">
                  <option value="yes">Yes</option>
                  <option value="No">No</option>
                  <option value="No info Provided">No info Provided</option>
                </select>
              </td>
              <td>
                <select v-model="updisht.aartiVandana">
                  <option value="yes">Yes</option>
                  <option value="No">No</option>
                  <option value="No info Provided">No info Provided</option>
                </select>
              </td>
              <td>
                <select v-model="updisht.remarks">
                  <option value="Believe in Vy need followup">Believe in Vy need followup</option>
                  <option value="Need Guidance by local updeshta">Need Guidance by local updeshta</option>
                  <option value="Not Interested">Not Interested</option>
                  <option value="Wrong Number">Wrong Number</option>
                  <option value="Unable To contact">Unable To contact</option>
                  <option value="Call picked but disconnected">Call picked but disconnected</option>
                  <option value="Old Vy member">Old Vy member</option>
                  <option value="Talks in different language">Talks in different language</option>
                  <option value="No info given">No info given</option>
                  <option value="Busy/ will talk later">Busy/ will talk later</option>
                  <option value="Already given info">Already given info</option>
                </select>
              </td>
              <td>
                <select v-model="updisht.callOn8586808820ForMoreInformation">
                  <option value="Number Given ">Number Given</option>
                  <option value="Number Not Given">Number Not Given</option>
                </select>
              </td>
              <td><input type="text" v-model="updisht.comment"></td>
              <td><input type="text" v-model="updisht.callerName"></td>
              <td><input type="text" v-model="updisht.callerNo"></td>
              <td><input type="text" v-model="updisht.groupLeaderName"></td>
              <td><input type="text" v-model="updisht.groupLeaderNo"></td>
              <td><button @click="submitRow(updisht)" class="submit-button">Submit</button></td> <!-- Submit button -->
            </tr>
          </tbody>
        </table>
      </div>

      <!-- Pagination -->
      <ul class="pagination">
        <li v-for="pageNumber in pageCount" :key="pageNumber" @click="setCurrentPage(pageNumber)">
          <a :class="{ active: currentPage === pageNumber }">{{ pageNumber }}</a>
        </li>
      </ul>
    </div>
     <!-- Footer -->
     <footer class="text-center text-white" style="background-color: #0a4275;">
      <div class="container p-4 pb-0">
        <section class="">
          <p class="d-flex justify-content-center align-items-center">
            <span class="me-3">Register for free</span>
            <button data-mdb-ripple-init type="button" class="btn btn-outline-light btn-rounded">
              Sign up!
            </button>
          </p>
        </section>
      </div>
      <div class="text-center p-3" style="background-color: rgba(0, 0, 0, 0.2);">
        © 2024 Copyright:
        <a class="text-white" href="https://Vihangamyoga.org/">VihangamYoga.com</a>
      </div>
    </footer>
    <!-- Footer -->
    <!-- Please Wait overlay -->
    <PleaseWait :show="showPleaseWait" />

  </div>
</div>
</template>

<script>
import PleaseWait from './/PleaseWait.vue';
import axios from 'axios';
export default {
  components: {
    PleaseWait
  },
  // props: {
  //   data: {
  //     type: Array,
  //     required: true
  //   }
  // },
  data() {
    return {
      showDatePickerFlag: false,
      showSidebar: false,
      currentPage: 1,
      pageSize: 8,
      displayedData: [],
      showPleaseWait: false
    };
  },
  computed: {
    paginatedData() {
      if (!this.data) {
        return [];
      }
      const startIndex = (this.currentPage - 1) * this.pageSize;
      const endIndex = startIndex + this.pageSize;
      return this.data.slice(startIndex, endIndex);
    },
    pageCount() {
      if (!this.data) {
        return 0;
      }
      return Math.ceil(this.data.length / this.pageSize);
    }
  },
  methods: {
    async fetchData() {
      try {
        const response = await axios.get('/updisht/api/dashboard/');
        console.log(response.data)
        
        if (response.data && response.data[0]) {
        try {
          // Check if the response data is a valid JSON string
          const parsedData = JSON.parse(response.data);
          console.log(parsedData,"parsed ")
          this.displayedData = parsedData.map((item, index) => ({
            ...item,
            id: index
          }));
        } catch (e) {
          console.error('Error parsing JSON:', e);
          this.displayedData = [];
        }
      } else {
        this.displayedData = [];
      }
        // this.displayedData = [this.displayedData];
        // this.displayedData = JSON.stringify(this.displayedData);
         console.log( this.displayedData)
        this.expectedData=[{"firstName": "PUJA", "lastName": "PATEL", "guardianType": "father", "guardianName": "VIRENDRA KUAMR SINGH", "gender": "Female", "age": 32, "contactNo": "7267984373.0", "email": "0", "education": "B.A", "occupation": "0", "village": "RAMNA", "post": "RAMANA", "city": "0.0", "district": "Varanasi", "state": "Uttar Pradesh", "pin": 221011, "dateOfUpdesh": 20231231, "placeOfUpdesh": "SWARVED MAHAMANDIR DHAM", "motivatorName": "0.0", "motivatorContact": "0.0", "motivatorAddress": "0.0", "updeshtaName": "0.0", "updeshtaContact": "0.0", "updeshtaAddress": "0.0", "dateOfCalling": "0.0", "callersIntroduction": "0.0", "comfortableLanguage": "0.0", "sadhna": "0.0", "photo": "0.0", "aartiVandana": "0.0", "remarks": "0.0", "callOn8586808820ForMoreInformation": "0.0", "comment": "0.0", "callerName": "0.0", "callerNo": "0.0", "groupLeaderName": "0.0", "groupLeaderNo": "0.0", "statusOfCall": null}, {"firstName": "ALMA", "lastName": "GUPTA", "guardianType": "husband", "guardianName": "VIMAL GUPTA", "gender": "Female", "age": 35, "contactNo": "8817124545.0", "email": "0", "education": "M.A", "occupation": "0", "village": "JHANDA CHOK BAZAR", "post": "BADHRANJI", "city": "0.0", "district": "Jabalpur", "state": "Madhya Pradesh", "pin": 482001, "dateOfUpdesh": 20231231, "placeOfUpdesh": "SWARVED MAHAMANDIR DHAM", "motivatorName": "0.0", "motivatorContact": "0.0", "motivatorAddress": "0.0", "updeshtaName": "0.0", "updeshtaContact": "0.0", "updeshtaAddress": "0.0", "dateOfCalling": "0.0", "callersIntroduction": "0.0", "comfortableLanguage": "0.0", "sadhna": "0.0", "photo": "0.0", "aartiVandana": "0.0", "remarks": "0.0", "callOn8586808820ForMoreInformation": "0.0", "comment": "0.0", "callerName": "0.0", "callerNo": "0.0", "groupLeaderName": "0.0", "groupLeaderNo": "0.0", "statusOfCall": null}, {"firstName": "Ruby", "lastName": "Devi", "guardianType": "father", "guardianName": "Gopal Gupta", "gender": "Female", "age": 0, "contactNo": "6387736899.0", "email": "0", "education": "10th", "occupation": "0", "village": "Chittipur", "post": "0", "city": "0.0", "district": "Varanasi", "state": "Uttar Pradesh", "pin": 221001, "dateOfUpdesh": 20240101, "placeOfUpdesh": "SWARVED MAHAMANDIR DHAM", "motivatorName": "0.0", "motivatorContact": "0.0", "motivatorAddress": "0.0", "updeshtaName": "0.0", "updeshtaContact": "0.0", "updeshtaAddress": "0.0", "dateOfCalling": "0.0", "callersIntroduction": "0.0", "comfortableLanguage": "0.0", "sadhna": "0.0", "photo": "0.0", "aartiVandana": "0.0", "remarks": "0.0", "callOn8586808820ForMoreInformation": "0.0", "comment": "0.0", "callerName": "0.0", "callerNo": "0.0", "groupLeaderName": "0.0", "groupLeaderNo": "0.0", "statusOfCall": null}, {"firstName": "Sonam", "lastName": "Singh", "guardianType": "father", "guardianName": "Ajeet Singh", "gender": "Female", "age": 17, "contactNo": "6392979029.0", "email": "0", "education": "12th", "occupation": "Student", "village": "Nasirpur Maudha", "post": "0", "city": "0.0", "district": "Ghazipur", "state": "Uttar Pradesh", "pin": 233221, "dateOfUpdesh": 20240102, "placeOfUpdesh": "SWARVED MAHAMANDIR DHAM", "motivatorName": "0.0", "motivatorContact": "0.0", "motivatorAddress": "0.0", "updeshtaName": "0.0", "updeshtaContact": "0.0", "updeshtaAddress": "0.0", "dateOfCalling": "0.0", "callersIntroduction": "0.0", "comfortableLanguage": "0.0", "sadhna": "0.0", "photo": "0.0", "aartiVandana": "0.0", "remarks": "0.0", "callOn8586808820ForMoreInformation": "0.0", "comment": "0.0", "callerName": "0.0", "callerNo": "0.0", "groupLeaderName": "0.0", "groupLeaderNo": "0.0", "statusOfCall": null}, {"firstName": "MAYA", "lastName": "DEVI", "guardianType": "father", "guardianName": "GULSAN MAKR", "gender": "Female", "age": 60, "contactNo": "9810345253.0", "email": "0", "education": "0", "occupation": "0", "village": "NUH", "post": "NUH", "city": "0.0", "district": "Nuh", "state": "Haryana", "pin": 0, "dateOfUpdesh": 20231231, "placeOfUpdesh": "SWARVED MAHAMANDIR DHAM", "motivatorName": "0.0", "motivatorContact": "0.0", "motivatorAddress": "0.0", "updeshtaName": "0.0", "updeshtaContact": "0.0", "updeshtaAddress": "0.0", "dateOfCalling": "0.0", "callersIntroduction": "0.0", "comfortableLanguage": "0.0", "sadhna": "0.0", "photo": "0.0", "aartiVandana": "0.0", "remarks": "0.0", "callOn8586808820ForMoreInformation": "0.0", "comment": "0.0", "callerName": "0.0", "callerNo": "0.0", "groupLeaderName": "0.0", "groupLeaderNo": "0.0", "statusOfCall": null}, {"firstName": "Anshika", "lastName": "Gupta", "guardianType": "father", "guardianName": "Gopal Gupta", "gender": "Female", "age": 12, "contactNo": "8318164733.0", "email": "0", "education": "7th", "occupation": "Student", "village": "Lahtara", "post": "0", "city": "0.0", "district": "Varanasi", "state": "Uttar Pradesh", "pin": 221001, "dateOfUpdesh": 20240101, "placeOfUpdesh": "SWARVED MAHAMANDIR DHAM", "motivatorName": "0.0", "motivatorContact": "0.0", "motivatorAddress": "0.0", "updeshtaName": "0.0", "updeshtaContact": "0.0", "updeshtaAddress": "0.0", "dateOfCalling": "0.0", "callersIntroduction": "0.0", "comfortableLanguage": "0.0", "sadhna": "0.0", "photo": "0.0", "aartiVandana": "0.0", "remarks": "0.0", "callOn8586808820ForMoreInformation": "0.0", "comment": "0.0", "callerName": "0.0", "callerNo": "0.0", "groupLeaderName": "0.0", "groupLeaderNo": "0.0", "statusOfCall": null}, {"firstName": "Komal", "lastName": "Sinha", "guardianType": "father", "guardianName": "Sonu Kumar Sinha", "gender": "Female", "age": 18, "contactNo": "9336594156.0", "email": "0", "education": "12th", "occupation": "Student", "village": "Ratnapuri", "post": "0", "city": "0.0", "district": "Chandauli", "state": "Uttar Pradesh", "pin": 221008, "dateOfUpdesh": 20240102, "placeOfUpdesh": "SWARVED MAHAMANDIR DHAM", "motivatorName": "0.0", "motivatorContact": "0.0", "motivatorAddress": "0.0", "updeshtaName": "0.0", "updeshtaContact": "0.0", "updeshtaAddress": "0.0", "dateOfCalling": "0.0", "callersIntroduction": "0.0", "comfortableLanguage": "0.0", "sadhna": "0.0", "photo": "0.0", "aartiVandana": "0.0", "remarks": "0.0", "callOn8586808820ForMoreInformation": "0.0", "comment": "0.0", "callerName": "0.0", "callerNo": "0.0", "groupLeaderName": "0.0", "groupLeaderNo": "0.0", "statusOfCall": null}, {"firstName": "peehu", "lastName": "Maurya", "guardianType": "father", "guardianName": "Mr Rakesh Kumar Maurya", "gender": "Female", "age": 19, "contactNo": "7275877089.0", "email": "0", "education": "12th", "occupation": "Student", "village": "Paniyalpur", "post": "0", "city": "0.0", "district": "Varanasi", "state": "Uttar Pradesh", "pin": 221007, "dateOfUpdesh": 20240102, "placeOfUpdesh": "SWARVED MAHAMANDIR DHAM", "motivatorName": "0.0", "motivatorContact": "0.0", "motivatorAddress": "0.0", "updeshtaName": "0.0", "updeshtaContact": "0.0", "updeshtaAddress": "0.0", "dateOfCalling": "0.0", "callersIntroduction": "0.0", "comfortableLanguage": "0.0", "sadhna": "0.0", "photo": "0.0", "aartiVandana": "0.0", "remarks": "0.0", "callOn8586808820ForMoreInformation": "0.0", "comment": "0.0", "callerName": "0.0", "callerNo": "0.0", "groupLeaderName": "0.0", "groupLeaderNo": "0.0", "statusOfCall": null}, {"firstName": "SHREE", "lastName": "DEVI", "guardianType": "father", "guardianName": "SHEETAL PRASAD", "gender": "Female", "age": 55, "contactNo": "9532097909.0", "email": "0", "education": "5TH", "occupation": "0", "village": "SUSWAHI", "post": "SUSWAHI", "city": "0.0", "district": "Varanasi", "state": "Uttar Pradesh", "pin": 221011, "dateOfUpdesh": 20231231, "placeOfUpdesh": "SWARVED MAHAMANDIR DHAM", "motivatorName": "0.0", "motivatorContact": "0.0", "motivatorAddress": "0.0", "updeshtaName": "0.0", "updeshtaContact": "0.0", "updeshtaAddress": "0.0", "dateOfCalling": "0.0", "callersIntroduction": "0.0", "comfortableLanguage": "0.0", "sadhna": "0.0", "photo": "0.0", "aartiVandana": "0.0", "remarks": "0.0", "callOn8586808820ForMoreInformation": "0.0", "comment": "0.0", "callerName": "0.0", "callerNo": "0.0", "groupLeaderName": "0.0", "groupLeaderNo": "0.0", "statusOfCall": null}, {"firstName": "Neetu", "lastName": "Gupta", "guardianType": "father", "guardianName": "Rajendra Gupta", "gender": "Female", "age": 0, "contactNo": "6307582070.0", "email": "0", "education": "BA", "occupation": "Student", "village": "Varanasi", "post": "0", "city": "0.0", "district": "Varanasi", "state": "Uttar Pradesh", "pin": 0, "dateOfUpdesh": 20240103, "placeOfUpdesh": "SWARVED MAHAMANDIR DHAM", "motivatorName": "0.0", "motivatorContact": "0.0", "motivatorAddress": "0.0", "updeshtaName": "0.0", "updeshtaContact": "0.0", "updeshtaAddress": "0.0", "dateOfCalling": "0.0", "callersIntroduction": "0.0", "comfortableLanguage": "0.0", "sadhna": "0.0", "photo": "0.0", "aartiVandana": "0.0", "remarks": "0.0", "callOn8586808820ForMoreInformation": "0.0", "comment": "0.0", "callerName": "0.0", "callerNo": "0.0", "groupLeaderName": "0.0", "groupLeaderNo": "0.0", "statusOfCall": null}, {"firstName": "Swati", "lastName": "Verma", "guardianType": "father", "guardianName": "OmPrakash Verma", "gender": "Female", "age": 0, "contactNo": "7905433778.0", "email": "0", "education": "Graduate", "occupation": "0", "village": "Pandeypur", "post": "0", "city": "0.0", "district": "Varanasi", "state": "Uttar Pradesh", "pin": 0, "dateOfUpdesh": 20240103, "placeOfUpdesh": "SWARVED MAHAMANDIR DHAM", "motivatorName": "0.0", "motivatorContact": "0.0", "motivatorAddress": "0.0", "updeshtaName": "0.0", "updeshtaContact": "0.0", "updeshtaAddress": "0.0", "dateOfCalling": "0.0", "callersIntroduction": "0.0", "comfortableLanguage": "0.0", "sadhna": "0.0", "photo": "0.0", "aartiVandana": "0.0", "remarks": "0.0", "callOn8586808820ForMoreInformation": "0.0", "comment": "0.0", "callerName": "0.0", "callerNo": "0.0", "groupLeaderName": "0.0", "groupLeaderNo": "0.0", "statusOfCall": null}, {"firstName": "URMILA", "lastName": "SHUKLA", "guardianType": "father", "guardianName": "SASHIBUSHAN SHUKLA", "gender": "Female", "age": 55, "contactNo": "9839226300.0", "email": "0", "education": "12TH PASS", "occupation": "0", "village": "MANDUA DEH", "post": "MANDUA DEH", "city": "0.0", "district": "Varanasi", "state": "Uttar Pradesh", "pin": 221103, "dateOfUpdesh": 20231231, "placeOfUpdesh": "SWARVED MAHAMANDIR DHAM", "motivatorName": "0.0", "motivatorContact": "0.0", "motivatorAddress": "0.0", "updeshtaName": "0.0", "updeshtaContact": "0.0", "updeshtaAddress": "0.0", "dateOfCalling": "0.0", "callersIntroduction": "0.0", "comfortableLanguage": "0.0", "sadhna": "0.0", "photo": "0.0", "aartiVandana": "0.0", "remarks": "0.0", "callOn8586808820ForMoreInformation": "0.0", "comment": "0.0", "callerName": "0.0", "callerNo": "0.0", "groupLeaderName": "0.0", "groupLeaderNo": "0.0", "statusOfCall": null}, {"firstName": "RAM MANDAR", "lastName": "GUPTA", "guardianType": "husband", "guardianName": "SHRI BHOLA  GUPTA", "gender": "Female", "age": 45, "contactNo": "9794834998.0", "email": "0", "education": "B.COM", "occupation": "SERVICE", "village": "MANDUA DEH", "post": "MANDUA DEH", "city": "0.0", "district": "Varanasi", "state": "Uttar Pradesh", "pin": 221103, "dateOfUpdesh": 20231231, "placeOfUpdesh": "SWARVED MAHAMANDIR DHAM", "motivatorName": "0.0", "motivatorContact": "0.0", "motivatorAddress": "0.0", "updeshtaName": "0.0", "updeshtaContact": "0.0", "updeshtaAddress": "0.0", "dateOfCalling": "0.0", "callersIntroduction": "0.0", "comfortableLanguage": "0.0", "sadhna": "0.0", "photo": "0.0", "aartiVandana": "0.0", "remarks": "0.0", "callOn8586808820ForMoreInformation": "0.0", "comment": "0.0", "callerName": "0.0", "callerNo": "0.0", "groupLeaderName": "0.0", "groupLeaderNo": "0.0", "statusOfCall": null}, {"firstName": "MEENU", "lastName": "DEVI", "guardianType": "father", "guardianName": "RAJKUMAR", "gender": "Female", "age": 37, "contactNo": "8081083734.0", "email": "0", "education": "12TH PASS", "occupation": "0", "village": "SHREE NAGAR COLONY", "post": "SHIVPUR", "city": "0.0", "district": "Varanasi", "state": "Uttar Pradesh", "pin": 221000, "dateOfUpdesh": 20231231, "placeOfUpdesh": "SWARVED MAHAMANDIR DHAM", "motivatorName": "0.0", "motivatorContact": "0.0", "motivatorAddress": "0.0", "updeshtaName": "0.0", "updeshtaContact": "0.0", "updeshtaAddress": "0.0", "dateOfCalling": "0.0", "callersIntroduction": "0.0", "comfortableLanguage": "0.0", "sadhna": "0.0", "photo": "0.0", "aartiVandana": "0.0", "remarks": "0.0", "callOn8586808820ForMoreInformation": "0.0", "comment": "0.0", "callerName": "0.0", "callerNo": "0.0", "groupLeaderName": "0.0", "groupLeaderNo": "0.0", "statusOfCall": null}, {"firstName": "Khushboo", "lastName": "Singh", "guardianType": "father", "guardianName": "Mr Mohan Singh", "gender": "Female", "age": 22, "contactNo": "6387538457.0", "email": "0", "education": "M.Sc", "occupation": "Student", "village": "Saraiya", "post": "Sindhara", "city": "0.0", "district": "Mirzapur", "state": "Uttar Pradesh", "pin": 231001, "dateOfUpdesh": 20240101, "placeOfUpdesh": "SWARVED MAHAMANDIR DHAM", "motivatorName": "0.0", "motivatorContact": "0.0", "motivatorAddress": "0.0", "updeshtaName": "0.0", "updeshtaContact": "0.0", "updeshtaAddress": "0.0", "dateOfCalling": "0.0", "callersIntroduction": "0.0", "comfortableLanguage": "0.0", "sadhna": "0.0", "photo": "0.0", "aartiVandana": "0.0", "remarks": "0.0", "callOn8586808820ForMoreInformation": "0.0", "comment": "0.0", "callerName": "0.0", "callerNo": "0.0", "groupLeaderName": "0.0", "groupLeaderNo": "0.0", "statusOfCall": null}, {"firstName": "MUNNI", "lastName": "DEVI", "guardianType": "husband", "guardianName": "FEKU SAH", "gender": "Female", "age": 32, "contactNo": "6386440531.0", "email": "0", "education": "0", "occupation": "0", "village": "RAMNAGAR", "post": "RAM NAGAR", "city": "0.0", "district": "Varanasi", "state": "Uttar Pradesh", "pin": 0, "dateOfUpdesh": 20231231, "placeOfUpdesh": "SWARVED MAHAMANDIR DHAM", "motivatorName": "0.0", "motivatorContact": "0.0", "motivatorAddress": "0.0", "updeshtaName": "0.0", "updeshtaContact": "0.0", "updeshtaAddress": "0.0", "dateOfCalling": "0.0", "callersIntroduction": "0.0", "comfortableLanguage": "0.0", "sadhna": "0.0", "photo": "0.0", "aartiVandana": "0.0", "remarks": "0.0", "callOn8586808820ForMoreInformation": "0.0", "comment": "0.0", "callerName": "0.0", "callerNo": "0.0", "groupLeaderName": "0.0", "groupLeaderNo": "0.0", "statusOfCall": null}]
        console.log(this.expectedData)
        console.log(this.displayedData,"final ")
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    }
  },
   toArray(data) {
  if (Array.isArray(data)) {
    return data;
  } else if (data === null || data === undefined) {
    return [];
  } else if (typeof data === 'object') {
    return Object.values(data);
  } else {
    return [data];
  }
},
  
    setCurrentPage(pageNumber) {
      this.currentPage = pageNumber;
    },
    toggleSidebar() {
      this.showSidebar = !this.showSidebar;
    },
    submitRow(updisht) {
    // Show Please Wait overlay
    this.showPleaseWait = true;

    // Make a POST request to submit the row
    fetch('http://127.0.0.1:8000/updisht/api/submit/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(updisht)
    })
    .then(response => {
      if (!response.ok) {
        throw new Error('Network response was not ok');
      }
      return response.json();
    })
    .then(data => {
      console.log('Success:', data);
      // Hide Please Wait overlay
      this.showPleaseWait = false;
      // Handle success response from the server

      // After submitting, reload all the data
      window.location.reload();
      this.reloadData();
    })
    .catch(error => {
      console.error('Error:', error);
      // Hide Please Wait overlay
      this.showPleaseWait = false;
      // Handle error
    });
  },
  reloadData() {
    // Fetch data from your backend API
    fetch('http://127.0.0.1:8000/updisht/api/dashboard/')
    .then(response => {
        console.log('Dashboard data:', response.data);
        // Update the displayed data with the response data
        this.displayedData = response.data;
      })
    // .then(data => {
    //   // Emit an event to notify the parent component of the updated data
    //   this.$emit('data-updated', data);
    // })
    .catch(error => {
      console.error('Error fetching data:', error);
      // Handle error fetching data
    });
},
mounted() {
    // Call fetchData when the component is mounted
    this.fetchData();
  }

};
</script>

<style scoped>

.table-container {
   width: 90% ; 
   height: 480px; 
   margin-top: 10px;
   margin-bottom: 20px;
  overflow: auto; /* Enable scrolling */
  border: 2px solid #ccc; /* Add border for the rectangle effect */
  border-radius: 8px; /* Add border radius for rounded corners */
  margin-left: 50px;
}
/* Toggle button */
.toggle-button {
  position: absolute;
  top: 10px;
  left: 10px;
  z-index: 999;
  padding: 10px;
  margin-bottom: 20px;
  background-color: #ff6a00;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
} 

/* Sidebar */
#sidebar {
  width: 250px;
  height: 100%;
  background-color:#002d72;
  
  color: rgb(75, 63, 63);
  position: fixed;
  top: 0;
  left: 0;
  
  padding-top: 20px;
  padding-bottom: 20 px;
  
  transition: transform 0.3s ease-in-out;
  transform: translateX(-250px);
}

#sidebar.active {
  transform: translateX(0);
}

#sidebar ul {
 
  margin-top: 40px;
  list-style-type: none;
  padding: 0;
}

#sidebar ul li {
  padding: 10px;
}

#sidebar ul li a {
  color: white;
  text-decoration: none;
  font-size: 16px;
  padding-top: 20px;
  font-family: 'Roboto', sans-serif;
  margin-top: 70px;
}
.sidebar-image {
  width: 10%;
  margin-bottom: 20px; /* Add some margin below the image */
}
/* Main content */
#main-content {
  transition: margin-left 0.3s ease-in-out;
}

/* Header */
#header {
  background-color:#0a4275;
  color: white;
  padding: 10px;
  text-align: center;
}

/* Table */
table {
  width: 100%;
  border-collapse: collapse;
  margin-top: 20px;
  box-shadow: 0px 2px 10px rgba(0, 0, 0, 0.1);
  border-radius: 8px;
  font-family: 'Roboto', sans-serif;
}

th, td {
    text-overflow: ellipsis;
    white-space: nowrap;
    overflow: hidden;
    padding: 8px;
  }
  thead th {
    color: #fff;
  }
  thead {
    position: sticky;
    top: 0;
  }
  tr:nth-child(even) {
    background-color: #f2f2f2;
  }
  tr:hover {
    background-color: #ddd;
  }
  .pagination {
    margin-top: 20px;
    list-style-type: none;
    display: flex;
    justify-content: center;
    align-items: center;
  }
  .pagination li {
    margin: 0 5px;
  }
  .pagination li a {
    text-decoration: none;
    color: #000;
    cursor: pointer;
    padding: 5px 10px;
  }
  .pagination li a.active {
    background-color: #002d72;
    color: #fff;
    border-radius: 5px;
  }
  footer {
  position: fixed;
  left: 0;
  bottom: 0;
  width: 100%;
  font-family: 'Roboto', sans-serif;
  color: #fff;
}
.text-white{
  color: #fff;
}
input[type="text"],
select {
 
  padding: 2px;
  
  border-radius: 1px;
  box-sizing: border-box;
  border: 2px solid #092a3c; /* Add border for the rectangle effect */
  border-radius: 5px;
}

/* Style for buttons */
button {
  background-color: #4CAF50;
  color: white;
  padding: 8px 20px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

button:hover {
  background-color: #45a049;
}

/* Style for dropdowns */
select {
  padding: 2px;
  border: 2px solid #092a3c; /* Add border for the rectangle effect */
  border-radius: 5px;
  box-sizing: border-box;
 
}
.submit-button {
  height: 100%; /* Match the height of table rows */
  width: 100%; /* Match the width of table cells */
  background-color: #4CAF50;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}
</style>