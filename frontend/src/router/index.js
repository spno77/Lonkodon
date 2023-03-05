// Composables
import { createRouter, createWebHistory } from 'vue-router'

// user routes
import UserRegisterView from '../views/User/UserRegisterView'
import UserLoginView    from '../views/User/UserLoginView'
import UserProfileView  from '../views/User/UserProfileView'

// messages routes
import MessagesView     from '../views/Messages/MessagesView'
import MessageReplyView from '../views/Messages/MessageReplyView'

// connections routes
import ConnectionsView        from '../views/Connections/ConnectionsView'
import ConnectionsRequestView from '../views/Connections/ConnectionsRequestView'
import FindConnectionsView    from '../views/Connections/FindConnectionsView'

// articles routes
import ArticlesListView from '../views/Articles/ArticlesListView'
import ArticleView      from '../views/Articles/ArticleView'

// jobs routes 
import JobListView from '../views/Jobs/JobListView'
import JobPostView from '../views/Jobs/JobPostView'

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
      {
        path: '/connections/find',
        name: 'FindConnections',
        component: FindConnectionsView,
        props: true
      },
      {
        path: '/articles/',
        name: 'Articles',
        component: ArticlesListView,
        props: true
      },
      {
        path: '/articles/:id',
        name: 'Article',
        component: ArticleView,
        props: true
      },
      {
        path: '/jobs/',
        name: 'JobList',
        component: JobListView,
        props: true
      },
      {
        path: '/jobs/post',
        name: 'JobPostView',
        component: JobPostView,
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
