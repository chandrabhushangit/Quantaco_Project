
<script>
import { defineComponent } from 'vue'
import { RouterView } from 'vue-router' 

export default defineComponent({
  name: 'App',
  components: {
    RouterView,
  },
})
</script>

<template>
  <RouterView />
</template>
<style>
@import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400&display=swap');
body {
  font-family: 'Roboto', sans-serif;
}

</style>