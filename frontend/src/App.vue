<script setup>
import {ref,onMounted} from 'vue'

import recipeItem from "./components/recipeItem.vue"

import recipeForm from "./components/recipeForm.vue"

const recipes = ref([])

const name = ref("")
const description = ref("")
const ingredients = ref([])
const instructions = ref("")
const prep_time = ref(0)
const cook_time = ref(0)
const servings = ref(1)
const difficulty = ref("")

const isEditing = ref(false)

const recipe = ref(null)

async function getRecipes(){
  try{
    const response = await fetch("http://localhost:8000/")

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

    console.log(recipes)
  }catch(error){
    console.error(error.message)
  }
}

async function deleteRecipe(id){
  try{
    const response = await fetch(`http://localhost:8000/recipe/${id}`,{
      method:"DELETE"
    })

    if(!response.ok){
      throw new Error(`Status:${response.status}`)
    }

    recipes.value = recipes.value.filter(recipe => recipe.id !== id)

  }catch(error){
    console.error(error.message)
  }
}

async function updateRecipe(id){
  try{
    const response = await fetch(`http://localhost:8000/recipes/${id}`,{
      method:"PATCH",
      headers:{
        "Content-Type": "application/json"
      },
      body:JSON.stringify({
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

    if(!response.ok){
      throw new Error(`Status:${response.status}`)
    }

    getRecipes()

    name.value = ""
    description.value = ""
    instructions.value = ""
    ingredients.value = ""
    prep_time.value = ""
    cook_time.value = ""
    servings.value = ""
    dfficulty.value = ""
  }catch(error){
    console.error(error.message)
  } 
}

function loadRecipe(recipe){
  name.value = recipe.name
  description.value = recipe.description
  ingredients.value = recipe.ingredients
  instructions.value = recipe.instructions
  prep_time.value = recipe.prep_time
  cook_time.value = recipe.cook_time
  servings.value = recipe.servings
  difficulty.value = recipe.difficulty

}

function StartEdit(recipe){
  recipe.value = {...recipe}
  isEditing.value = true
}

onMounted(()=>{
  getRecipes()
})
</script>

<template>
  <h1>Recipe Manager</h1>

  <h4>Item:</h4>

  <recipeForm
    :recipe="recipe"
    :editMode="isEditing"
    @add="createRecipe"
    @edit="StartEdit" 
  />

  <div>
    <recipeItem
      :recipe="recipe"
      @edit="StartEdit()"
      @delete="deleteRecipe()"
    />
  </div>


</template>

<style scoped></style>
