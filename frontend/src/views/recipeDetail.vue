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
    <div v-if="selectedRecipe">
        <h2>{{ selectedRecipe.name }}</h2>
            <img
                v-if="selectedRecipe.image_url"
                :src="selectedRecipe.image_url"
                :alt="selectedRecipe.name"
                class="image"
            />
            <div v-else class="no-image">
                <p>No image available</p>
            </div>
        <div class="container">
            <div class="ingredients">
                <label class="label">Ingredients</label>
                <ul v-for="ingredient in selectedRecipe.ingredients" :key="ingredient">{{ ingredient.amount }} {{ ingredient.unit }} {{ ingredient.name }}</ul>
            </div>
            <div class="vertical-divider"></div>
            <div class="instructions">
                <label class="label">Directions</label>
                <ul v-for="instruction in selectedRecipe.instructions" :key="instruction">{{instruction}}</ul>
            </div>
        </div>
    </div> 
    <p v-else>Loading recipe...</p>
</template>

<style scoped>
    .container {
        display: flex;
        flex-direction: row;
        align-items: stretch;
        justify-content: center;
        border: 2px solid red;
        border-radius: 5px;
        padding: 20px;
        gap: 20px;
    }

    .image{
        width: 100%;
        height: 250px;
        object-fit: cover;
        border-radius: 5px;
        justify-content: center;
    }

    .no-image {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 250px;
        background-color: #f0f0f0;
        border-radius: 5px;
        color: #777;
    }

    .ingredients {
        flex: 1;
        border: 2px solid gray;
        border-radius: 15px;
        padding:15px;
    }

    .instructions {
        flex: 1;
    }

   .vertical-divider {
        width: 0;
        border-left: 2px solid lightgray;
    }

    .label{
        display:flex;
        justify-content: center;
        font-size: 35px;
    }
</style>