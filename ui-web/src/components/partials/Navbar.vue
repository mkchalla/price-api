<template>
  <nav class="navbar" role="navigation" aria-label="main navigation">
    <div class="navbar-brand">
      <a class="navbar-item" href="/">
        <h1>Price</h1>
        <!-- <img
          src="https://bulma.io/images/bulma-logo.png"
          width="112"
          height="28"
        /> -->
      </a>

      <a
        role="button"
        class="navbar-burger"
        aria-label="menu"
        aria-expanded="false"
        data-target="navbarBasicExample"
      >
        <span aria-hidden="true"></span>
        <span aria-hidden="true"></span>
        <span aria-hidden="true"></span>
      </a>
    </div>

    <div id="navbarBasicExample" class="navbar-menu">
      <div class="navbar-start">
        <router-link to="/" class="navbar-item">Home</router-link>
        <router-link to="/about" class="navbar-item">About</router-link>

        <div class="navbar-item has-dropdown is-hoverable">
          <a class="navbar-link"> More </a>

          <div class="navbar-dropdown">
            <a class="navbar-item"> About </a>
            <a class="navbar-item"> Jobs </a>
            <a class="navbar-item"> Contact </a>
            <hr class="navbar-divider" />
            <a class="navbar-item"> Report an issue </a>
          </div>
        </div>
      </div>

      <div class="navbar-end">
        <div class="navbar-item">
          <div class="buttons">
            <span v-if="isAuthenticated">
              <a class="button is-danger is-light" @click="handleLogout">
                Logout
              </a>
            </span>
            <span v-else>
              <router-link to="/signup" class="button is-primary">
                <strong>SignUp</strong>
              </router-link>
              <router-link to="/login" class="button is-light">
                Login
              </router-link>
            </span>
          </div>
        </div>
      </div>
    <!-- Modal dialog to prompt the user to really logout -->
      <div :class="['modal', activeClass]">
        <div class="modal-background" @click="closeLogoutModal"></div>
        <div class="modal-card">
          <header class="modal-card-head">
            <p class="modal-card-title">Warning</p>
            <button class="delete" aria-label="close" @click="closeLogoutModal"></button>
          </header>
          <section class="modal-card-body">
            <!-- Content ... -->
            Confirm logout!
          </section>
          <footer class="modal-card-foot">
            <button class="button is-danger" @click="confirmLogout">Logout</button>
            <button class="button" @click="closeLogoutModal">Cancel</button>
          </footer>
        </div>
      </div>
    </div>
  </nav>
</template>
<script>
import { mapActions } from "vuex";
import { mapGetters } from "vuex";
export default {
  name: "Navbar",
  data() {
      return {
          activeClass: ''
      }
  },
  computed: {
    ...mapGetters(["isAuthenticated"]),
  },
  methods: {
    ...mapActions(["logout"]),
    handleLogout() {
        this.activeClass = 'is-active';
    },
    confirmLogout(){
        this.logout();
        this.closeLogoutModal();
    },
    closeLogoutModal() {
        this.activeClass = '';
    }
  },
};
</script>
<style lang="scss" scoped>
nav {
  a.navbar-item {
    &.router-link-exact-active {
      background-color: #fafafa;
      color: #3273dc;
    }
  }
}
</style>