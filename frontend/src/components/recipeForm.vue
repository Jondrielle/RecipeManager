<script setup>

const props = defineProps({
	editMode:Boolean,
	recipe:Object
})

const emit = defineEmits(["submit","add","edit"])

function addRecipe(){
	emit("add",props.recipe)
}

function editRecipe(){
	emit("edit")
}
</script>

<template>
	<form @submit.prevent="submit">
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
		  
		<select v-model="difficulty">
			<option disabled value="">Select Difficulty</option>
		    <option value="Easy">Easy</option>
		    <option value="Medium">Medium</option>
		    <option value="Hard">Hard</option>
		</select>

		<button type="submit">{{ editMode ? "Update Habit" : "Add Habit" }}</button>
	</form>
</template>