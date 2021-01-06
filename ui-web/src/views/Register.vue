<template>
  <div class="login">
    <div class="container has-text-centered">
      <div class="column is-4 is-offset-4">
        <h3 class="title has-text-black">SignUp</h3>
        <hr class="login-hr" />
        <p class="subtitle has-text-black">Please provide your details to SignUp.</p>
        <div class="box">
          <form @submit.prevent="submit">
            <div class="field">
              <div class="control">
                <input
                  class="input is-large"
                  type="email"
                  v-model="user.email"
                  placeholder="Enter Email"
                  autofocus=""
                />
              </div>
            </div>
            <div class="field">
              <div class="control">
                <input
                  class="input is-large"
                  type="text"
                  v-model="user.full_name"
                  placeholder="Full Name"
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
                  placeholder="Enter Password"
                />
              </div>
            </div>
            <div class="field">
              <div class="control">
                <input
                  class="input is-large"
                  type="password"
                  v-model="user.confirm_password"
                  placeholder="Confirm Password"
                />
              </div>
            </div>
            <button class="button is-block is-primary is-large is-fullwidth">
              SignUp 
              <!-- <font-awesome-icon icon="address-card" /> -->
            </button>
          </form>
          <p v-if="showError" id="error">Username already exists</p>
        </div>
        <p class="has-text-grey">
            
          <router-link to="/register">SignUp</router-link> &nbsp;·&nbsp;
          <a href="../">Forgot Password</a> &nbsp;·&nbsp;
          <a href="../">Need Help?</a>
        </p>
      </div>
    </div>
  </div>


    <!-- <div class="register">
        <form @submit.prevent="submit">
            <div>
                <label for="username">Username:</label>
                <input type="text" name="username" v-model="user.username">
            </div>
        </form>
        <div>
            <label for="full_name">Full Name:</label>
            <input type="text" name="full_name" v-model="user.full_name">
        </div>
        <div>
            <label for="password">Password:</label>
            <input type="password" name="password" v-model="user.password">
        </div>
        <button type="submit">Sign Up</button>
        <p v-if="showError" id="error">Username already exists</p>
    </div> -->
</template>

<script>
import { mapActions } from "vuex";
import User from '@/models/user';
export default {
    name: 'register',
    components: {},
    data() {
        return {
            user: new User('', ''),
            showError: false
        }
    },
    methods: {
        ...mapActions(["register"]),
        async submit() {

            try {
                this.showError = false;
                await this.register(this.user);
                this.$router.push('/items');
            } catch (error) {
                this.showError = true
            }
        }
    }
}
</script>

<style lang="scss" scoped>
#error{
    background-color: #f1c3c3;
    color: red;
}
</style>