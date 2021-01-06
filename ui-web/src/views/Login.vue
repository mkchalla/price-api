<template>
  <div class="login">
    <div class="container has-text-centered">
      <div class="column is-4 is-offset-4">
        <h3 class="title has-text-black">Login</h3>
        <hr class="login-hr" />
        <p class="subtitle has-text-black">Please login to proceed.</p>
        <div class="box">
          <figure class="avatar">
            <img class="logo" src="../assets/user.png" />
          </figure>
          <form @submit.prevent="submit">
            <div class="field">
              <div class="control">
                <input
                  class="input is-large"
                  type="email"
                  v-model="user.email"
                  placeholder="Your Email"
                  autofocus=""
                />
              </div>
            </div>

            <div class="field">
              <div class="control">
                <input
                  class="input is-large"
                  type="password"
                  v-model="user.password"
                  placeholder="Your Password"
                />
              </div>
            </div>
            <div class="field has-text-left">
              <label class="checkbox">
                <input type="checkbox" />
                Remember me
              </label>
            </div>
            <button class="button is-block is-info is-large is-fullwidth">
              Login
              <!-- <font-awesome-icon icon="address-card" /> -->
            </button>
          </form>
        </div>
        <p class="has-text-grey">
          <router-link to="/register">Sign Up</router-link> &nbsp;·&nbsp;
          <a href="../">Forgot Password</a> &nbsp;·&nbsp;
          <a href="../">Need Help?</a>
        </p>
      </div>
    </div>

    <!-- 
        <form @submit.prevent="submit">
            <div class="columns">
                <div class="column is-4 is-offset-4">
                    <div>
                        <label for="username">Username:</label>
                        <input type="text" name="username" v-model="user.username">
                    </div>
                    <div>
                        <label for="password">Password:</label>
                        <input type="password" name="password" v-model="user.password">
                    </div>
                    <button type="submit">Sign Up</button>
                    <p v-if="showError" id="error">Username already exists</p>
                </div>
            </div>            
        </form>  -->
  </div>
</template>

<script>
import { mapActions } from "vuex";
import User from '@/models/user'
import { library } from "@fortawesome/fontawesome-svg-core";
// import { faSpinner, faAlignLeft } from '@fortawesome/free-solid-svg-icons'
import { faAddressCard } from "@fortawesome/free-solid-svg-icons";

library.add(faAddressCard);

export default {
  name: "login",
  components: {},
  data() {
    return {
      user: new User('',''),
      showError: false,
    };
  },
  methods: {
    ...mapActions(["login"]),
    async submit() {
      try {          
        await this.login(this.user);
        this.$router.push("/items");
        this.showError = false;
      } catch (error) {
        this.showError = true;
      }
    },
  },
  computed: {},
};
</script>

<style lang="scss" scoped>
.avatar {
  img.logo {
    width: 128px;
    height: 128px;
  }
}
.has-text-left {
  text-align: left;
}
</style>