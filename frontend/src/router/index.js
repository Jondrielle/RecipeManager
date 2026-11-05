import { createWebHistory, createRouter } from 'vue-router'

import recipeDetail from '../views/recipeDetail.vue'
import HomeView from '../views/HomeView.vue'

const routes = [
    { path: '/recipes/:id', component: recipeDetail },
    { path: '/', component: HomeView }
]

export const router = createRouter({ history: createWebHistory(), routes, })