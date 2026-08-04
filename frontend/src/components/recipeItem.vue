<script setup>

const props = defineProps({
	recipe: Object
})

const emit = defineEmits(['edit','delete'])

function editRecipe(){
	emit('edit',props.recipe)
}

function deleteRecipe(){
	emit('delete',props.recipe.id)
}
</script>

<template>
	<div class="card">
		<h2 class="title">{{recipe.name}}</h2>
		<p>{{recipe.description}}</p>
		<ul>
		  <h2>Ingredients</h2>
		  <li v-for="ingredient in recipe.ingredients" :key="ingredient"
		  class="list">
		    {{ ingredient }}
		  </li>
		</ul>
		<p>{{recipe.instructions}}</p>
		<div class="stats">
			<span> Prep Time: {{recipe.prep_time}} </span>
			<span> Cook Time: {{recipe.cook_time}}</span> 
			<span> Difficulty: {{recipe.difficulty}}</span>
		</div>
		<div class="buttons">
			<button @click="editRecipe">EDIT</button>
			<button @click="deleteRecipe">DELETE</button>
		</div>
	</div>
</template>

<style scoped>
	.card{
		border: 2px solid orange;
		border-radius:5px;
		padding:8px;
	}

	.stats{
		margin-top:auto;
		display:flex;
		flex-direction:column;
		gap:12px;
	}

	.buttons{
		display:flex;
		justify-content:flex-end;
		gap:8px;
	}

	.title{
		text-transform:uppercase
	}

	.list{
		text-transform:uppercase
	}
</style>

