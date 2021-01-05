import axios from 'axios';
import API_ROOT_URL from "./api-config";


class AuthService {
  login(user, headers) {
    return axios
      .post(`${API_ROOT_URL}/login`, user, headers)
      .then(response => {
        if (response.data.access_token) {
            const userData = {
                username: user.username,
                accessToken: response.data.access_token
            }
          localStorage.setItem('user', JSON.stringify(userData));
        }
        return response.data;
      });
  }

  logout() {
    localStorage.removeItem('user');
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