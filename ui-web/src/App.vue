<template>
  <div id="app">
    <!-- <router-link to="/">Home</router-link> |
    <router-link to="/about">About</router-link> -->
    <Navbar />
    <router-view/>
  </div>
</template>

<script>
import Navbar from './components/partials/Navbar'
export default {
  name: 'app',
  components: {
    Navbar
  }
}
</script>

<style lang="scss">


#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  background: #F2F6FA;
  min-height: 100vh;
  color: #2c3e50;
}

</style>
