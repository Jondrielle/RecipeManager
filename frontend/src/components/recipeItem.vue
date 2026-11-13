
<script setup>
import { formatTime } from '@/utils/formatTime'

const props = defineProps({
  recipe: Object
})

const emit = defineEmits(['edit', 'delete','setFavorite'])

function editRecipe() {
  emit('edit', props.recipe)
}

function deleteRecipe() {
  emit('delete', props.recipe.id)
}

function setIsFavorite(){
  emit('setFavorite', props.recipe)
}
</script>

<template>
  <div class="card">
    <h2 class="title">{{ recipe.name }}
        <button class="favorite" @click="setIsFavorite">{{ recipe.is_favorite ? '♥️' : '♡' }}</button></h2>
    <RouterLink :to="`/recipes/${recipe.id}`" class="recipeLink">
      <img
        v-if="recipe.image_url"
        :src="recipe.image_url"
        :alt="recipe.name"
        class="recipeImage"
      />
      <div v-else class="no-image">
        <span class="placeholder-icon">🖼️</span>
        <p>No image available</p>
        <span class="view-recipe">View Recipe →</span>
      </div>
    </RouterLink>
    

    <p>{{ recipe.description }}</p>

    <div class="stats">
      <div class="stat">
        <span class="statLabel">Prep Time</span>
        <span class="statValue">{{ formatTime(recipe.prep_time) }}</span>
      </div>

      <div class="stat">
        <span class="statLabel">Cook Time</span>
        <span class="statValue">{{ formatTime(recipe.cook_time) }}</span>
      </div>

      <div class="stat">
        <span class="statLabel">Servings</span>
        <span class="statValue">{{ recipe.servings }}</span>
      </div>

      <div class="stat">
        <span class="statLabel">Difficulty</span>
        <span class="statValue">{{ recipe.difficulty }}</span>
      </div>
    </div>

    <div class="actions">
      <button @click="editRecipe">EDIT</button>
      <button @click="deleteRecipe">DELETE</button>
    </div>
  </div>
</template>

<style scoped>
.card {
  position: relative;
  padding: 20px;
  border-radius: 12px;
  background: white;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

.title {
  margin-bottom: 15px;
}

.recipeImage {
  width: 100%;
  max-height: 250px;
  object-fit: cover;
  border-radius: 8px;
  margin-bottom: 15px;
}

.listTitle {
  margin-bottom: 10px;
}

.stats {
  display: grid;
  grid-template-columns: repeat(4, minmax(0, 1fr));
  border-top: 1px solid #ddd;
  border-bottom: 1px solid #ddd;
  margin: 20px 0;
}

.stat {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  text-align: center;
  padding: 12px 4px;
  min-width: 0;
}

.stat + .stat {
  border-left: 1px solid #ddd;
}

.statLabel {
  font-size: 0.8rem;
  color: #666;
  margin-bottom: 5px;
}

.statValue {
  font-size: 0.95rem;
  font-weight: bold;
  overflow-wrap: anywhere;
}

.actions {
  display: flex;
  gap: 10px;
  justify-content: flex-end;
}

.actions button {
  padding: 8px 16px;
  cursor: pointer;
  border: none;
  border-radius: 6px;
}

.recipeLink {
  text-decoration: none;
  color: inherit;
  display: block;
  cursor: pointer;
}

.recipeLink {
  display: block;
  text-decoration: none;
  color: inherit;
  cursor: pointer;
}

.no-image {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  gap: 12px;

  height: 250px;
  background-color: #f8f4ef;
  border: 2px dashed #e6c8b0;
  border-radius: 8px;
  color: #777;

  transition: background-color 0.2s ease,
              border-color 0.2s ease;
}

.placeholder-icon {
  font-size: 45px;
}

.no-image p {
  margin: 0;
  font-size: 16px;
  color: #777;
}

.view-recipe {
  display: inline-block;
  font-size: 14px;
  font-weight: 600;
  color: #d9823b;
  text-decoration: none;

  transition: transform 0.2s ease;
}

.recipeLink:hover .view-recipe {
  text-decoration: underline;
  text-underline-offset: 4px;
  transform: translateX(5px);
}

.recipeLink:hover .no-image {
  background-color: #fff0e6;
  border-color: #e89b5a;
}

.recipeLink:focus-visible {
  outline: 2px solid #e89b5a;
  outline-offset: 4px;
  border-radius: 8px;
}

.favorite {
  position: absolute;
  top: 15px;
  right: 15px;

  border: none;
  border-radius: 5px;
  background-color: transparent;
  font-size: 25px;
  cursor: pointer;
}
</style>
