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
		<div class="Ingredients">
			<h2 class="listTitle">Ingredients</h2>
			<ul class="ingredientsContainer">
			  <li v-for="ingredient in recipe.ingredients" :key="ingredient"
			  class="list">
			    {{ ingredient }}
			  </li>
			</ul>
		</div>
		<ol>
			<li v-for="step in recipe.instructions"
				:key="instruction">
				{{step}}
			</li>
		</ol>
		<div class="stats">
			<span> Prep Time: {{recipe.prep_time}} mins </span>
			<span> Cook Time: {{recipe.cook_time}} mins </span> 
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
	}

	.stats{
		margin-top:auto;
		gap:12px;
		font-size:14px;
	  	padding:5px;
	}

	.stats span {
	  padding: 0 15px;
	  border-right: 1px solid #ddd;
	}

	.stats span:last-child {
	  border-right: none;
	}

	.buttons{
		display:flex;
		justify-content:flex-end;
		gap:8px;
	}

	.title{
		text-transform:uppercase
	}

	.listTitle {
	  margin: 0;
	  text-align: left;
	  border-bottom: 1px dotted red;
	  border-top: 1px dotted red;
	  padding-left:10px;
	  border-bottom: 1px solid red;
	  border-top: 1px solid red;
	  border-left:1px dotted red;
	  border-right:1px dotted red;
	}

	.ingredientsContainer {
	  border-bottom: 1px solid red;
	  border-left:1px dotted red;
	  border-right:1px dotted red;
	}

	.Ingredients{
		padding:10px;
	}

	.list{
		text-transform:uppercase;
	}
</style>

