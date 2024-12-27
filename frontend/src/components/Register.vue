<template>
    <div>
      <!-- If user is logged in, render DataTable component -->
      <template v-if="isLoggedIn">
        <DataTable :data="displayedData" />
      </template>
    
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  import DataTable from './DataTable.vue'; 
//   import LoginForm from './views/LoginForm.vue';
  
  export default {
    name: 'App',
    components: {
      DataTable
    },
    data() {
      return {
        displayedData: [],
        isLoggedIn: false
      };
    },
    methods: {
    //   loginHandler(credentials) {
    //     // Simulate login logic with hardcoded credentials
    //     if (credentials.username === 'admin' && credentials.password === 'admin') {
    //       console.log("login success")
    //       // Set isLoggedIn to true upon successful login
    //       this.isLoggedIn = true;
    //       // Fetch data for DataTable
    //       this.fetchDataTableData();
    //     } else {
    //       // If credentials are incorrect, show an error message
    //       console.error('Invalid username or password');
    //     }
    //   },
      fetchDataTableData() {
        // Fetch data for DataTable from API
        axios.get('http://127.0.0.1:8080/api/dashboard/')
        .then(response => {
          console.log(typeof response.data,"type")
          const jsonData = JSON.parse(response.data)
          console.log('Response data:', response.data);
          // Parse the response data into an array
          
          // Set displayedData to allData to pass it to DataTable
          this.displayedData =jsonData;
        //  / this.jsonDataArray = JSON.parse(this.displayedData);
          console.log(this.displayedData,"jj");
          //#console.log(this.jsonDataArray,"jj");
        })
        .catch(error => {
          console.error('There was an error!', error);
        });
      }
    }
  };
  </script>
  