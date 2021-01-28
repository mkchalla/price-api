import { createStore } from 'vuex';

import createPersistedState from 'vuex-persistedstate'
import auth from '@/store/modules/auth'
import product from '@/store/modules/product'

export default createStore({
    modules: {
        auth,
        product
    },
    plugins: [createPersistedState()]
});


