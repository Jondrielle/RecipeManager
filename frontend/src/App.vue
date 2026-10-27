<script setup>
import {ref,onMounted} from 'vue'

import recipeItem from "./components/recipeItem.vue"

import recipeForm from "./components/recipeForm.vue"

const recipes = ref([])

const isEditing = ref(false)

const selectedRecipe = ref(null)

const showForm = ref(false)

const error = ref("")

const loading = ref(false)

async function getRecipes(){
  error.value = ""
  loading.value = true

  try{
    const response = await fetch("https://recipemanager-40pu.onrender.com")

    if (!response.ok){
      throw new Error(`Response status:${response.status}`)
    }

    const result = await response.json()
    console.log(result)

    recipes.value = result 

  } catch (err) {
    error.value = err.message
  } finally {
    loading.value = false
  }
}

async function createRecipe(recipe){
  console.log("Adding recipe:", recipe)
  error.value = ""
  loading.value = true

  try{
    const response = await fetch("https://recipemanager-40pu.onrender.com/recipe",{
      method:"POST",
      headers:{
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        name: recipe.name,
        description: recipe.description,
        ingredients: recipe.ingredients,
        instructions: recipe.instructions,
        prep_time: recipe.prep_time,
        cook_time: recipe.cook_time,
        servings: recipe.servings,
        difficulty: recipe.difficulty,
        image_url: recipe.image_url
      })
    })

    if (!response.ok) {
      if (response.status === 422) {
        throw new Error("Please check the recipe information.")
      }

        throw new Error("Failed to create recipe");
    }


    const result = await response.json()
    recipes.value.push(result) 

    error.value = ""

    showForm.value = false
    isEditing.value = false
    selectedRecipe.value = null

    console.log(recipes)
  } catch (err) {
    error.value = err.message
  } finally {
    loading.value = false
  }
}

async function deleteRecipe(id){
  error.value = ""
  try{
    const response = await fetch(`https://recipemanager-40pu.onrender.com/recipe/${id}`,{
      method:"DELETE"
    })

    if(!response.ok){
      throw new Error(`Status:${response.status}`)
    }

    recipes.value = recipes.value.filter(recipe => recipe.id !== id)

    if(selectedRecipe.value?.id === id){
      selectedRecipe.value = null
      isEditing.value = false
    }

  }catch (err) {
    error.value = err.message
  }
}

async function updateRecipe(recipe){
  console.log(recipe)
  error.value = ""
  try{
    const response = await fetch(`https://recipemanager-40pu.onrender.com/recipes/${recipe.id}`,{
      method:"PATCH",
      headers:{
        "Content-Type": "application/json"
      },
      body:JSON.stringify({
        ...recipe,
        ingredients: recipe.ingredients,
        instructions: recipe.instructions
      })
    })

    const result = await response.json()
    console.log(result)

    if(!response.ok){
      throw new Error(`Status:${response.status}`)
    }

    await getRecipes()

    selectedRecipe.value = null
    isEditing.value = false
  } catch (err) {
    error.value = err.message
  }
}

function startEdit(recipe){
    selectedRecipe.value = {
    ...recipe,
    ingredients: recipe.ingredients.map(item => ({ ...item })),
    instructions: [...recipe.instructions]
  }
  
  isEditing.value = true
  showForm.value = true
}

function cancelForm(){
  error.value = ""
  selectedRecipe.value = null
  isEditing.value = false
  showForm.value = false
}

function openForm(){
  error.value = ""
  showForm.value = true
}

function closeForm() {
  error.value = ""
  selectedRecipe.value = null
  isEditing.value = false
  showForm.value = false
}

onMounted(()=>{
  getRecipes()
})
</script>

<template>
  <div class="titleBox">
    <h1 class="header">Recipe Manager</h1>
  </div>

  <div class="recipes">
    <div v-for="recipe in recipes" :key="recipe.id">
      <recipeItem
        :recipe="recipe"
        @edit="startEdit"
        @delete="deleteRecipe"
      />
    </div>
    <button v-if="!showForm"
    @click="openForm"
    class="openFormButton">+ Add Recipe</button>
  </div>

  <p v-if="error" class="error">
    {{ error }}
  </p>
  <div class="form">
    <recipeForm
      v-if="showForm"
      :key="selectedRecipe?.id || 'new'"
      :recipe="selectedRecipe"
      :editMode="isEditing"
      :loading ="loading"
      @add="createRecipe"
      @edit="updateRecipe" 
      @cancel="cancelForm"
      @exit="closeForm"
    />
    <p  v-if="recipes.length === 0">Your recipes will appear here. Add your recipe habit to get started.</p>
  </div>

</template>

<style scoped>
  .titleBox{
    width:100%;
    box-sizing: border-box;
    background: linear-gradient(135deg, #ffecd2, #fcb69f);
    margin-bottom:50px;
    box-shadow: 0 4px 12px rgba(255, 192, 203, 0.4);
  }

  .header{
    text-align:center;
    margin:0;
    padding:30px;
  }

  .form{
    margin-bottom:50px;
  }

  .recipes{
    display:flex;
    grid-template-columns: repeat(3, minmax(0, 1fr));
    gap:20px;
  }

  .openFormButton {
    display: block;
    margin: 20px auto;
    padding: 10px 20px;
    border: none;
    border-radius: 8px;
    background-color: #e89b5a;
    color: white;
    font-size: 15px;
    font-weight: 600;
    cursor: pointer;
    transition: 0.2s ease;
  }

  .openFormButton:hover {
    background-color: #d9823b;
    transform: translateY(-1px);
  }

  .openFormButton:active {
    transform: translateY(0);
  }

  .error {
  padding: 10px 14px;
  margin: 10px 0;
  border-radius: 8px;
  background: #fde2e2;
  border: 1px solid #e8a0a0;
  color: #a33;
}
  
  .form > p {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    color:dark-grey;
  }
</style>
