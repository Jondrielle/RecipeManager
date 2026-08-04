<script setup>
import {ref,onMounted} from 'vue'

import recipeItem from "./components/recipeItem.vue"

import recipeForm from "./components/recipeForm.vue"

const recipes = ref([])

const isEditing = ref(false)

const selectedRecipe = ref(null)

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

async function createRecipe(recipe){
  try{
    const response = await fetch("http://localhost:8000/recipe",{
      method:"POST",
      headers:{
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        name: recipe.name,
        description: recipe.description,
        ingredients: recipe.ingredients.split(",").map(item => item.trim()),
        instructions: recipe.instructions,
        prep_time: recipe.prep_time,
        cook_time: recipe.cook_time,
        servings: recipe.servings,
        difficulty: recipe.difficulty
      })
    })

    if (!response.ok) {
        throw new Error("Failed to create recipe");
    }

    const result = await response.json()
    recipes.value.push(result) 

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

async function updateRecipe(recipe){
  try{
    const response = await fetch(`http://localhost:8000/recipes/${recipe.id}`,{
      method:"PATCH",
      headers:{
        "Content-Type": "application/json"
      },
      body:JSON.stringify({
        ...recipe,
        ingredients: recipe.ingredients.split(",").map(item => item.trim())
      })
    })

    if(!response.ok){
      throw new Error(`Status:${response.status}`)
    }

    await getRecipes()

    selectedRecipe.value = null
    isEditing.value = false
  }catch(error){
    console.error(error.message)
  } 
}

function startEdit(recipe){
  selectedRecipe.value = {...recipe}
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
    :key="selectedRecipe?.id || 'new'"
    :recipe="selectedRecipe"
    :editMode="isEditing"
    @add="createRecipe"
    @edit="updateRecipe" 
  />

  <div>
    <div v-for="recipe in recipes" :key="recipe.id">
      <recipeItem
        :recipe="recipe"
        @edit="startEdit"
        @delete="deleteRecipe"
      />
    </div>
  </div>


</template>

<style scoped></style>
