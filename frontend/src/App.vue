<script setup>
import {ref,onMounted} from 'vue'

const recipes = ref([])

const name = ref("")
const description = ref("")
const ingredients = ref([])
const instructions = ref("")
const prep_time = ref(0)
const cook_time = ref(0)
const servings = ref(1)
const difficulty = ref("")

async function getRecipes(){
  try{
    const response = await fetch("http//localhost:8000/")

    if (!response.ok){
      throw new Error(`Response status:${response.status}`)
    }

    const result = await response.json()

    recipes.value = result 
    console.log(result)

  }catch(error){
    console.error(error.message)
  }
}

async function createRecipe(){
  try{
    const response = await fetch("http://localhost:8000/recipe",{
      method:"POST",
      headers:{
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        name: name.value,
        description: description.value,
        ingredients: ingredients.value,
        instructions: instructions.value,
        prep_time: prep_time.value,
        cook_time: cook_time.value,
        servings: servings.value,
        difficulty: difficulty.value
      })
    })

    if (!response.ok) {
        throw new Error("Failed to create recipe");
    }

    const result = await response.json()
    recipes.values.push(result)

  }catch(error){
    console.error(error.message)
  }
  
}

async function deleteRecipe(){
  
}

async function updateRecipe(){
  
}

onMounted(()=>{})
</script>

<template>
  <h1>Recipe Manager</h1>

  <h4>List:</h4>
  <div v-for="recipe in recipes"
  :key="recipe.id">
    <div>
      {{recipe.name}}
    </div>

  </div>
  <input v-model="name" placeholder="Name"></input>

  <input v-model="description" placeholder="Description"></input>
  
  <input v-model="ingredients" placeholder="Ingredients"></input>
  
  <input v-model="instructions"
  placeholder="Instructions"></input>
  
  <input v-model="prep_time"
  placeholder="Prep time"></input>
  
  <input v-model="cook_time"
  placeholder="Cook time"></input>
  
  <input v-model="servings"
  placeholder="Servings"></input>
  
  <input v-model="difficulty"
  placeholder="Difficulty"></input>

</template>

<style scoped></style>
