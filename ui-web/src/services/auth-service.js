import axios from 'axios';
import API_ROOT_URL from "./api-config";


class AuthService {
  login(user, headers) {
    return axios
      .post(`${API_ROOT_URL}/login`, user, headers)
      .then(response => {
        const userData = {
            username: user.username
        }
        
        if (response.data.access_token) {
            userData['accessToken'] = response.data.access_token;
        }
        return userData;
      });
  }

  logout() {
    //handle any logout actions
  }

  register(user) {
    return axios.post(`${API_ROOT_URL}/signup`, {
      username: user.username,
      email: user.email,
      password: user.password
    });
  }
}

export default new AuthService();