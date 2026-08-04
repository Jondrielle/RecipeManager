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
		<h2>Name:{{recipe.name}}</h2>
		<p>{{recipe.description}}</p>
		<p>{{recipe.ingredients}}</p>
		<p>{{recipe.instructions}}</p>
		<span class="stats">{{recipe.prep_time}} </span>
		<span class="stats">{{recipe.cook_time}}</span> 
		<span class="stats">{{recipe.difficulty}}</span>

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
		display:flex;
		gap:12px;
	}

	.buttons{
		display:flex;
		justify-content:flex-end;
		gap:8px;
	}
</style>

