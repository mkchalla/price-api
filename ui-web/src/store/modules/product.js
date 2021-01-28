
// store/modules/product.js

import ProductService from '@/services/product-service';

const state = {
    prodcuts: [],
    currentProduct: null
}

const getters = {
    stateProducts: state => state.products,
    currentProduct: state => state.currentProduct
};

const actions = {
    async getProducts({ commit }) {

        return ProductService.getProducts().then(
            response => {
                
                commit('setProducts', response);
                return Promise.resolve(response);
            },
            error => {
                commit('registerFailure');
                return Promise.reject(error);
            })
        },
    async createProduct({ dispatch }, product) {
        ProductService.createProduct(product).then(
            response => {
                //commit('setProducts', response.data);
                dispatch('getProducts')
                return Promise.resolve(response.data);
            },
            error => {
                // commit('registerFailure');
                return Promise.reject(error);
            })
        
    }
};

const mutations = {
    setProducts(state, products) {
        state.products = products;
    },
    setProduct(currentProduct) {
        state.currentProduct = currentProduct;
    }
};

export default {
    state,
    getters,
    actions,
    mutations
}