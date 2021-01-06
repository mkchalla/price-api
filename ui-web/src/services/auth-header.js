
import store from '@/store/modules'

export default function authHeader() {
    let user = store.getters.currentUser;

    if (user && user.access_token) {
        return { Authorization: 'Bearer ' + user.access_token };
    } else {
        return {};
    }
}