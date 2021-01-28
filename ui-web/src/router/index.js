import { createRouter, createWebHistory } from 'vue-router'
import Products from '../views/Products.vue'
import Signup from '@/views/Signup.vue'
import Login from "@/views/Login.vue";
// import store from '@/store/modules'

const routes = [
  {
    path: '/',
    name: 'Products',
    component: Products
  },
  {
    path: '/signup',
    name: 'signup',
    component: Signup
  },
  {
    path: '/login',
    name: 'login',
    component: Login
  },
  {
    path: '/about',
    name: 'About',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})



// router.beforeEach((to, from, next) => {
//     // other than login and signup.
//     const publicPages = ['/login', '/signup', '/about'];
//     const authRequired = !publicPages.includes(to.path);
  
//     // trying to access a restricted page + not logged in
//     // redirect to login page
//     if (authRequired && !store.getters.isAuthenticated) {
//       next('/login');
//     } else {
//       next();
//     }
//   });

export default router
