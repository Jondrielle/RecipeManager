<script setup>

const props = defineProps({
	recipe: Object
})

const emit = defineEmits(['edit','delete'])

function editRecipe(){
	emit('edit',props.recipe)
	console.log("Editing Recipe")
}

function deleteRecipe(){
	emit('delete',props.recipe.id)
}
</script>

<template>
	<div class="card">
		<h2 class="title">{{recipe.name}}</h2>
		<p>{{recipe.description}}</p>
		<div class="Ingredients">
			<h2 class="listTitle">Ingredients</h2>
			<ul class="ingredientsContainer">
			  <li v-for="ingredient in recipe.ingredients" :key="ingredient.name"
			  class="list">
			    {{ingredient.amount}} {{ingredient.unit}} {{ingredient.name}}
			  </li>
			</ul>
		</div>
		<ol>
			<li
			  v-for="(instruction, index) in recipe.instructions"
			  :key="index"
			>
			  {{ instruction }}
			</li>
		</ol>
		<div class="stats">
			<span> Prep Time: {{recipe.prep_time}} mins </span>
			<span> Cook Time: {{recipe.cook_time}} mins </span> 
			<span> Servings: {{recipe.servings}}</span> 
			<span> Difficulty: {{recipe.difficulty}}</span>
		</div>
		<div class="buttons">
			<button @click="editRecipe">EDIT</button>
			<button @click="deleteRecipe">DELETE</button>
		</div>
	</div>
</template>

<style scoped>
.card {
  display: flex;
  flex-direction: column;

  width: 100%;
  max-width: 500px;

  background: white;

  border: 1px solid #eaded5;
  border-radius: 16px;

  padding: 22px;

  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.06);

  transition:
    transform 0.2s ease,
    box-shadow 0.2s ease;
}

.card:hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 20px rgba(0, 0, 0, 0.1);
}

/* =========================
   HEADER
   ========================= */

.cardHeader {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  gap: 15px;
  margin-bottom: 18px;
}

.title {
  margin: 0;
  font-size: 24px;
  font-weight: 700;
  color: #3d3028;
  text-transform: capitalize;
}

.description {
  margin: 6px 0 0;
  color: #75685f;
  font-size: 14px;
  line-height: 1.5;
}

.difficulty {
  flex-shrink: 0;
  padding: 5px 10px;
  border-radius: 999px;
  background: #fff0df;
  color: #c56f28;
  font-size: 12px;
  font-weight: 600;
}

/* =========================
   STATS
   ========================= */

.stats {
  display: grid;
  grid-template-columns: repeat(3, 1fr);

  border-top: 1px solid #eee3da;
  border-bottom: 1px solid #eee3da;

  margin-bottom: 20px;
}

.stat {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 12px 6px;
}

.stat + .stat {
  border-left: 1px solid #eee3da;
}

.statLabel {
  font-size: 12px;
  color: #8b7c72;
}

.statValue {
  margin-top: 3px;
  font-size: 14px;
  font-weight: 600;
  color: #46372e;
}

/* =========================
   SECTIONS
   ========================= */

.section {
  margin-bottom: 20px;
}

.sectionTitle {
  margin: 0 0 10px;
  font-size: 17px;
  font-weight: 700;
  color: #46372e;
}

/* =========================
   INGREDIENTS
   ========================= */

.ingredients {
  list-style: none;
  margin: 0;
  padding: 0;

  display: flex;
  flex-direction: column;
  gap: 7px;
}

.ingredientItem {
  display: flex;
  align-items: baseline;
  gap: 8px;

  padding: 8px 10px;

  background: #fff8f1;
  border-radius: 7px;

  font-size: 14px;
}

.amount {
  min-width: 75px;
  font-weight: 600;
  color: #c56f28;
}

.ingredientName {
  color: #493d35;
}

/* =========================
   INSTRUCTIONS
   ========================= */

.instructions {
  list-style: none;
  margin: 0;
  padding: 0;

  display: flex;
  flex-direction: column;
  gap: 12px;
}

.instructionItem {
  display: flex;
  align-items: flex-start;
  gap: 10px;
}

.stepNumber {
  display: flex;
  align-items: center;
  justify-content: center;

  flex-shrink: 0;

  width: 25px;
  height: 25px;

  border-radius: 50%;

  background: #e89b5a;
  color: white;

  font-size: 12px;
  font-weight: 700;
}

.instructionText {
  padding-top: 3px;

  color: #493d35;

  font-size: 14px;
  line-height: 1.5;
}

/* =========================
   ACTIONS
   ========================= */

.actions {
  display: flex;
  gap: 10px;

  margin-top: auto;
  padding-top: 10px;
}

.actions button {
  flex: 1;

  padding: 10px 14px;

  border: none;
  border-radius: 8px;

  font-size: 14px;
  font-weight: 600;

  cursor: pointer;

  transition:
    background-color 0.2s ease,
    transform 0.1s ease;
}

.actions button:active {
  transform: translateY(1px);
}

.editButton {
  background: #e89b5a;
  color: white;
}

.editButton:hover {
  background: #d9823b;
}

.deleteButton {
  background: #f3e7e4;
  color: #c0392b;
}

.deleteButton:hover {
  background: #ead4d0;
}

/* =========================
   MOBILE
   ========================= */

@media (max-width: 500px) {
  .card {
    padding: 18px;
  }

  .cardHeader {
    flex-direction: column;
  }

  .difficulty {
    align-self: flex-start;
  }

  .stats {
    grid-template-columns: 1fr;
  }

  .stat + .stat {
    border-left: none;
    border-top: 1px solid #eee3da;
  }

  .amount {
    min-width: auto;
  }
 }
</style>