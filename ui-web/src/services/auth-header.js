
import store from '@/store/modules'

export default function authHeader() {
    let user = store.getters.currentUser;

    if (user && user.accessToken) {
        return { Authorization: 'Bearer ' + user.accessToken };
    } else {
        return {};
    }
}