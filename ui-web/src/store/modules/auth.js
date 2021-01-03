
// store/modules/auth.js


import axios from 'axios';


const state = {
    user: null,
    items: null
};

const getters = {
    isAuthenticated: state => !!state.user,
    stateItems: state => state.items,
    stateUser: state => state.user

};

const actions = {
    async register({dispatch}, form){
        await axios.post('register', form)
        let userForm = new FormData()
        userForm.append('username', form.username)
        userForm.append('password', form.password)
        await dispatch('login', userForm)
    },
    async login({commit}, user){
        await axios.post('login', user)
        await commit('setUser', user.get('username'))
    },
    async createItem({dispatch}, item){
        await axios.post('item', item)
        await dispatch('getItems')
    },
    async getItems({commit}){
        let response = await axios.get('items')
        commit('setItems', response.data)
    }

};

const mutations = {
    setUser(state, username){
        state.user = username
    },
    setItems(state, items){
        state.items = items
    },
    logout(state){
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