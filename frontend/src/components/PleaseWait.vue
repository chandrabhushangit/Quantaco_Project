<template>
    <div class="please-wait-overlay" v-if="show">
      <div class="please-wait-content">
        <span>Please wait...</span>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    props: {
      show: Boolean
    }
  };
  </script>
  
  <style scoped>
  .please-wait-overlay {
    position: fixed;
    z-index: 9999;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.5);
    display: flex;
    justify-content: center;
    align-items: center;
  }
  
  .please-wait-content {
    background-color: white;
    padding: 20px;
    border-radius: 5px;
  }
  </style>
  