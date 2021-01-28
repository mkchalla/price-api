import axios from 'axios';
import API_ROOT_URL from "./api-config";


class ProductService {
  getProducts(headers) {
    return axios
      .get(`${API_ROOT_URL}/products`, headers)
      .then(response => {        
        return response.data;
      });
  }

  getProduct(product_id, headers) {
    return axios
      .get(`${API_ROOT_URL}/product/${product_id}`, headers)
      .then(response => {        
        return response.data;
      });
  }
}

export default new ProductService();