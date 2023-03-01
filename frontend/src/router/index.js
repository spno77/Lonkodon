// Composables
import { createRouter, createWebHistory } from 'vue-router'

// user routes
import UserRegisterView from '../views/User/UserRegisterView'
import UserLoginView    from '../views/User/UserLoginView'
import UserProfileView  from '../views/User/UserProfileView'

// messages routes
import MessagesView     from '../views/Messages/MessagesView'
import MessageReplyView from '../views/Messages/MessageReplyView'

// connctions routes
import ConnectionsView from '../views/Connections/ConnectionsView'
import ConnectionsRequestView from '../views/Connections/ConnectionsRequestView'

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
        name: 'Login',
        component: UserLoginView,
        props: true
      },
      {
        path: '/profile/:id',
        name: 'Profile',
        component: UserProfileView,
        props: true
      },
      {
        path: '/messages/',
        name: 'Messages',
        component: MessagesView,
        props: true
      },
      {
        path: '/reply/',
        name: 'MessageReply',
        component: MessageReplyView,
        props: true
      },
      {
        path: '/connections/',
        name: 'Connections',
        component: ConnectionsView,
        props: true
      },
      {
        path: '/requests/',
        name: 'Requests',
        component: ConnectionsRequestView,
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
