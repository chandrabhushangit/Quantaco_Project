import { createApp } from 'vue'
import App from './App.vue'
import { createRouter, createWebHistory } from 'vue-router'
import axios from 'axios'

import Login from './components/Login.vue'
import Register from './components/Register.vue'
import DataTable from './components/DataTable.vue'
import './index.css'

const app = createApp(App,{ silent: true })
app.config.productionTip = false
app.config.globalProperties.baseImgUrl = '/quantaco/src/assets';
axios.defaults.baseURL = 'http://localhost:8000/';
axios.interceptors.request.use(
    config => {
      const token = localStorage.getItem('access_token');
      if (token) {
        const expiration = JSON.parse(atob(token.split('.')[1])).exp;
        const currentTime = Math.floor(Date.now() / 1000);
        console.log("curr->",currentTime,"exp->",expiration)
        if (currentTime > expiration) {
          localStorage.removeItem('access_token');
          localStorage.removeItem('refresh_token');
          sessionStorage.clear();
          router.push('/quantaco/login');
        } else {
          config.headers.Authorization = `Bearer ${token}`;
        }
      }
      return config;
    },
    error => {
      return Promise.reject(error);
    }
  );
app.axios = axios;
app.$http = axios;
app.config.globalProperties.axios = axios;
app.config.globalProperties.$http = axios;
const routes = [
  {
    path: '/quantaco',
    redirect: '/quantaco/login' // Redirect the root URL to the specific URL
  },
  { path: '/quantaco/login', 
    component: Login, 
    name: 'Login' 
  },
  { 
    path: '/quantaco/DataTable', 
    component: DataTable, 
    name: 'DataTable', 
    meta: {
       requiresAuth: true,
    }
  },
  // { 
  //   path: '/quantaco/register', 
  //   component: Register, 
  //   name: 'Register', 
  //   meta: {
  //      requiresAuth: true,
  //   }
  // },
]

const router = createRouter({
    history: createWebHistory(),
    routes,
})

router.beforeEach((to, from, next) => {
    const token = localStorage.getItem('access_token'); 
  
    if (to.meta.requiresAuth && !token) { 
      sessionStorage.clear();
      next('/quantaco/login'); 
    } else {
      next(); 
    }
});

app.use(router)
app.mount('#app')