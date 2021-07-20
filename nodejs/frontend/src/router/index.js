import Vue from 'vue'
import Router from 'vue-router'
import Read from '@/components/Read'
import View from '@/components/View'
import Detailview from '@/components/Detailview'


Vue.use(Router)

export default new Router({
  routes: [{
      path: '/',
      name: 'Read',
      component: Read
    },
    {
      path:'/view'  //상세페이지 추가
			,name:'View' 
			,component:View
    },
    {
      path:'/detailview/:contentid'  //상세페이지 추가
			,name:'Detailview'
			,component:Detailview
    }
    // {
    //   path: '/:id',
    //   name: 'detailmovie',
    //   component: DetailMoviePage
    // }
  ]
})


