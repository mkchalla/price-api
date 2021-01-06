
// store/modules/auth.js

import AuthService from '@/services/auth-service';

const state = {
    user: null
}

const getters = {
    isAuthenticated: state => !!state.user,
    stateItems: state => state.items,
    currentUser: state => state.user

};

const actions = {
    async register({ commit }, form) {
        // const headers = {
        //     'Content-Type': 'application/json'
        // }
        const userData = {
            username: form.email,
            email: form.email,
            password: form.password
        }
        return AuthService.register(userData).then(
            response => {
                commit('registerSuccess');
                return Promise.resolve(response.data);
            },
            error => {
                commit('registerFailure');
                return Promise.reject(error);
            })
    },
    async login({ commit }, user) {
        const headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }

        let userForm = new FormData()
        userForm.append('username', user.email)
        userForm.append('password', user.password)
        return AuthService.login(userForm, headers).then(
            userData => {
                commit('loginSuccess', userData);
                return Promise.resolve(userData);
            },
            error => {
                commit('loginFailure');
                return Promise.reject(error);
            }
        );
        //await commit('setUser', user.get('username'))
    },
    async logout({commit}){
        AuthService.logout();
        commit('logout')
    },
    async createItem({ dispatch }, item) {
        // await axios.post('item', item)
        console.log(item)
        await dispatch('getItems')
    },
    async getItems({ commit }) {
        // let response = await axios.get('items')
        let response = {}
        commit('setItems', response.data)
    }
};

const mutations = {
    loginSuccess(state, userData) {
        state.user = userData;
    },
    loginFailure(state) {
        state.user = null;
    },
    setItems(state, items) {
        state.items = items
    },
    logout(state) {
        state.user = null
        state.items = null
    }
};

export default {
    state,
    getters,
    actions,
    mutations
}