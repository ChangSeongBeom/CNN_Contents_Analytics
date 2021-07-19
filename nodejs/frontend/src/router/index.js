import Vue from 'vue'
import Router from 'vue-router'
import mainHomePage from '@/components/mainHomePage'


Vue.use(Router)

export default new Router({
  routes: [{
      path: '/',
      name: 'mainHomePage',
      component: mainHomePage
    },
    // {
    //   path: '/:id',
    //   name: 'detailmovie',
    //   component: DetailMoviePage
    // }
  ]
})


