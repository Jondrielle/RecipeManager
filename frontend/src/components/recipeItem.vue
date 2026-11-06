
<script setup>
import { formatTime } from '@/utils/formatTime'

const props = defineProps({
  recipe: Object
})

const emit = defineEmits(['edit', 'delete'])

function editRecipe() {
  emit('edit', props.recipe)
}

function deleteRecipe() {
  emit('delete', props.recipe.id)
}
</script>

<template>
  <div class="card">
    <h2 class="title">{{ recipe.name }}</h2>
    <RouterLink :to="`/recipes/${recipe.id}`">
      <img
        v-if="recipe.image_url"
        :src="recipe.image_url"
        :alt="recipe.name"
        class="recipeImage"
      />
      <div v-else class="no-image">
        <p>No image available</p>
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

.no-image {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 250px;
  background-color: #f0f0f0;
  border-radius: 5px;
  color: #777;
}
</style>
