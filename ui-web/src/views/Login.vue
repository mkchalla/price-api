<template>
    <div class="login">
        <form @submit.prevent="submit">
            <div>
                <label for="username">Username:</label>
                <input type="text" name="username" v-model="form.username">
            </div>
        </form>
        <div>
            <label for="password">Password:</label>
            <input type="password" name="password" v-model="form.password">
        </div>
        <button type="submit">Sign Up</button>
        <p v-if="showError" id="error">Username already exists</p>
    </div>
</template>

<script>
import { mapActions } from "vuex";
export default {
    name: 'login',
    components: {},
    data() {
        return {
            form: {
                username: "",
                password: ""
            },
            showError: false
        }
    },
    methods: {
        ...mapActions(["login"]),
        async submit() {

            try {
                await this.login(this.form);
                this.$router.push('/items');
                this.showError = false;
            } catch (error) {
                this.showError = true
            }
        }
    }
}
</script>