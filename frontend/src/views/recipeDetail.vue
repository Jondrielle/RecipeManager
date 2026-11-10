<script setup>
import {ref,onMounted} from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { formatTime } from '@/utils/formatTime'

const router = useRouter()
const route = useRoute()

const selectedRecipe = ref()
const error = ref('')

const updatingFavorite = ref(false)

async function toggleFavorite() {
  if (!selectedRecipe.value || updatingFavorite.value) return

  updatingFavorite.value = true

  try {
    const response = await fetch(
      `https://recipemanager-40pu.onrender.com/recipes/${route.params.id}`,
      {
        method: 'PATCH',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          is_favorite: !selectedRecipe.value.is_favorite
        })
      }
    )

    if (!response.ok) {
      throw new Error(`Status: ${response.status}`)
    }

    const updatedRecipe = await response.json()
    selectedRecipe.value = updatedRecipe

  } catch (err) {
    console.error('Failed to update favorite:', err)
  } finally {
    updatingFavorite.value = false
  }
}

async function getRecipe(){
    try{
         const response = await fetch(`https://recipemanager-40pu.onrender.com/recipe/${route.params.id}`)

        if(!response.ok){
            throw new Error(`Status code: ${response.status}`)
        }

        selectedRecipe.value = await response.json()

        console.log(`Selected Recipe: ${selectedRecipe.value}`)

        
    }
    catch (err) {
        error.value = err.message
        console.error(err)
    }

}

onMounted(()=>{getRecipe()})
</script>

<template>
    <div v-if="selectedRecipe">
        <div class="details">
            <div class="title-row">
                <h2>{{ selectedRecipe.name }}</h2>

                <button
                    type="button"
                    class="favorite-button"
                    :class="{ active: selectedRecipe.is_favorite }"
                    :disabled="updatingFavorite"
                    :aria-pressed="!!selectedRecipe.is_favorite"
                    :aria-label="selectedRecipe.is_favorite
                        ? 'Remove from favorites'
                        : 'Add to favorites'"
                    @click="toggleFavorite"
                >
                    {{ selectedRecipe.is_favorite ? '♥' : '♡' }}
                </button>
            </div>

            <p>{{ selectedRecipe.description }}</p>
            <div class="stats">
                <span>Prep time: {{ formatTime(selectedRecipe.prep_time) }}</span>
                <span>Cook time: {{ formatTime(selectedRecipe.cook_time) }}</span>
                <span>Servings: {{ selectedRecipe.servings }}</span>
                <span>Difficulty: {{ selectedRecipe.difficulty }}</span>
            </div>
        </div>
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
                <h3 class="label">Ingredients</h3>
                <ul>
                    <li
                        v-for="(ingredient, index) in selectedRecipe.ingredients"
                        :key="index"
                    >
                        {{ ingredient.amount }}
                        {{ ingredient.unit }}
                        {{ ingredient.name }}
                    </li>
                 </ul>
            </div>
            <div class="vertical-divider"></div>
            <div class="instructions">
                <h3 class="label">Directions</h3>
                <ol>
                    <li
                        v-for="(instruction, index) in selectedRecipe.instructions"
                        :key="index"
                        >
                    {{ instruction }}
                    </li>
                </ol>
            </div>
        </div>
    </div> 
    <p v-else-if="error">{{ error }}</p>
    <p v-else>Loading recipe...</p>
</template>

<style scoped>
    .container {
        display: flex;
        flex-direction: row;
        align-items: stretch;
        justify-content: center;
        padding: 20px;
        gap: 20px;
    }

    .container ul{
        text-transform: capitalize;
    }

    .image{
        width: 100%;
        height: 250px;
        object-fit: cover;
        border-radius: 5px;
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
        border: 1px solid gray;
        border-radius: 15px;
        background-color: rgb(227, 225, 225);
        padding: 20px;
    }

    .instructions ol {
        display: flex;
        flex-direction: column;
        gap: 20px;
        padding-right: 20px;
        line-height: 1.6;
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

    .details {
        display: flex;
        flex-direction: row;
        justify-content: space-between;
        align-items: flex-start;
        gap: 20px;
    }

    .title{
        text-transform: capitalize;
        padding-left: 35px;
    }

    .title h2 { 
        font-size: 55px;
        padding-top: 20px;
        margin: 0;
    }

    .title p {
        font-size: 19px;
        font-style: italic;
        padding-left: 5px;
    }

    .stats {
        display: flex;
        flex-direction: column;
        gap: 10px;
        align-items: flex-end;
        padding: 30px;
    }

    .title-row {
        display: flex;
        align-items: center;
        gap: 20px;
    }

    .title-row h2 {
        font-size: 55px;
        margin: 0;
    }

    .favorite-button {
        background: transparent;
        border: none;
        font-size: 40px;
        color: #888;
        cursor: pointer;
        padding: 5px;
        line-height: 1;
        transition: color 0.2s ease, transform 0.2s ease;
    }

    .favorite-button:hover {
        transform: scale(1.15);
    }

    .favorite-button.active {
        color: #e63946;
    }

    .favorite-button:focus-visible {
        outline: 2px solid #e63946;
        outline-offset: 4px;
        border-radius: 5px;
    }

</style>