<script setup>
import {ref,onMounted} from 'vue'
import { useRoute, useRouter } from 'vue-router'

const router = useRouter()
const route = useRoute()

const selectedRecipe = ref()

async function getRecipe(){
    try{
         const response = await fetch(`https://recipemanager-40pu.onrender.com/recipe/${route.params.id}`)
         selectedRecipe.value = await response.json()

        if(!response.ok){
            throw new Error(`Status code: ${response.status}`)
        }
        else{
            console.log(`Selected Recipe: ${selectedRecipe.value}`)
        }
        
    }
    catch(err){
        console.error(err)
    }

}

onMounted(()=>{getRecipe()})
</script>

<template>
    <div>
        <h1>Recipe Detail Page </h1>
        <p>Recipe ID: {{ route.params.id }}</p>

        <div v-if="selectedRecipe">
            <h2>{{ selectedRecipe.name }}</h2>
            <p>{{ selectedRecipe.description }}</p>
        </div>

    </div>
</template>

<style scoped>

</style>