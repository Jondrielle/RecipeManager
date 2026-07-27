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
        ingredients: ingredients.value.split(',').map(item => item.trim()),
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
    recipes.value.push(result)
    name.value = ""
    description.value = ""
    ingredients.value = ""
    instructions.value = ""
    prep_time.value = ""
    cook_time.value = ""
    servings.value = ""
    difficulty.value = "" 
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
      Name: {{recipe.name}}
      Description: {{recipe.description}}
      Ingredients: {{recipe.ingredients}}
      Instructions: {{recipe.instructions}}
      Prep: {{recipe.prep_time}}
      Cook: {{recipe.cook_time}}
      Servings: {{recipe.servings}}
      Difficulty: {{recipe.difficulty}}
    </div>
  </div>

  <input v-model="name" placeholder="Name"></input>

  <input v-model="description" placeholder="Description"></input>
  
  <input v-model="ingredients" placeholder="Ingredients"></input>
  
  <input v-model="instructions"
  placeholder="Instructions"></input>
  
  <input v-model.number="prep_time"
  placeholder="Prep"></input>

  <input v-model.number="cook_time"
  placeholder="Cook"></input>
  
  <input v-model.number="servings"
  placeholder="Servings"></input>
  
  <input v-model="difficulty"
  placeholder="Difficulty"></input>

  <button @click="createRecipe">Add Recipe</button>
</template>

<style scoped></style>
