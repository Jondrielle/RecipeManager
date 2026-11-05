import { createWebHistory, createRouter } from 'vue-router'

import recipeDetail from './recipeDetail.vue'

const routes = [
    { path: '/recipes/:id', compoenent: recipeDetail }
]

export const router = createRouter({ history: createWebHistory(), routes, })