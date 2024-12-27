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
    <div class="table-container">
      <!-- Table to display Updisht information -->
      
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
            <tr v-for="(updisht, index) in paginatedData" :key="index">
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

export default {
  components: {
    PleaseWait
  },
  props: {
    data: {
      type: Array,
      required: true
    }
  },
  data() {
    return {
      showDatePickerFlag: false,
      showSidebar: false,
      currentPage: 1,
      pageSize: 8,
      showPleaseWait: false
    };
  },
  computed: {
    paginatedData() {
      const startIndex = (this.currentPage - 1) * this.pageSize;
      const endIndex = startIndex + this.pageSize;
      return this.data.slice(startIndex, endIndex);
    },
    pageCount() {
      return Math.ceil(this.data.length / this.pageSize);
    }
  },
  methods: {
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
    fetch('http://127.0.0.1:8080/caller/submit/', {
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
    fetch('http://127.0.0.1:8080/api/dashboard/')
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
}
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