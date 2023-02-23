// Composables
import { createRouter, createWebHistory } from 'vue-router'

// user routes
import UserRegisterView from '../views/User/UserRegisterView'
import UserLoginView    from '../views/User/UserLoginView'
import UserProfileView  from '../views/User/UserProfileView'

const routes = [
  {
    path: '/',
    component: () => import('@/layouts/default/Default.vue'),
    children: [
      {
        path: '',
        name: 'Home',
        // route level code-splitting
        // this generates a separate chunk (about.[hash].js) for this route
        // which is lazy-loaded when the route is visited.
        component: () => import(/* webpackChunkName: "home" */ '@/views/Home.vue'),
      },
      {
        path: '/register/',
        name: 'Register',
        component: UserRegisterView ,
        props: true
      },
      {
        path: '/login/',
        name: 'UserLoginView',
        component: UserLoginView,
        props: true
      },
      {
        path: '/profile/',
        name: 'Profile',
        component: UserProfileView,
        props: true
      },
    ],
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
})

export default router
