<template>
  <div class="column is-4-tablet is-3-desktop">
    <div class="card">
      <div class="card-image">
        <figure class="image is-4by3">
          <p>{{productPath}}</p>
          <img
            :src="productPath"
            alt="Placeholder image"
          />
        </figure>
      </div>
      <div class="card-content">
        <div class="media">
          <div class="media-left">
            <figure class="image is-48x48">
              <img
                src="https://bulma.io/images/placeholders/96x96.png"
                alt="Placeholder image"
              />
            </figure>
          </div>
          <div class="media-content">
            <p class="title is-4">{{ product.name }}</p>
            <!-- <p class="subtitle is-6">@johnsmith</p> -->
          </div>
        </div>
        <div class="content">
          {{ product.description }}
        </div>
        <!-- <div class="content">
          Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus nec
          iaculis mauris. <a>@bulmaio</a>. <a href="#">#css</a>
          <a href="#">#responsive</a>
          <br />
          <time datetime="2016-1-1">11:09 PM - 1 Jan 2016</time>
        </div> -->
      </div>
    </div>
  </div>
</template>

<script>
import { API_MEDIA_ROOT } from "@/services/api-config";
export default {
  props: ["product"],
  name: "ProductCard",
  computed: {
    productPath(){
      console.log(API_MEDIA_ROOT + '/images/' + this.product.image)
      return API_MEDIA_ROOT + '/images/' + this.product.image;

    }
  }
};
</script>

<style lang="scss" scoped>
div.card-content {
  width: 600px;
}
</style>
