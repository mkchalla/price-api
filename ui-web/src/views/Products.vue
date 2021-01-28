<template>
    <div class="container products-container">
        <h1>
          This is where all the items will be listed in cronological order
        </h1>
        <div class="columns m-5 is-variable">
          <div class="row columns is-multiline">
            <ProductCard v-for="product in stateProducts" :key="product" :product=product>{{
          product
        }}</ProductCard>
          </div>
          
        </div>
      </div>
</template>

<script>
// @ is an alias to /src
import { mapActions, mapGetters } from "vuex";
import ProductCard from "@/components/ProductCard";

export default {
  name: "Products",
  components: {
    ProductCard,
  },
  data() {
    return {
      products: [1, 2, 3, 4, 5, 6],
    };
  },
  computed: {
    ...mapGetters(['stateProducts'])
  },
  methods: {
    ...mapActions(['getProducts'])
  },
  mounted() {
    this.getProducts()
  }
};
</script>

<style lang="scss" scoped>
.products-container {
  background-color: #FFFFFF;
  min-height: 100vh;
}
</style>