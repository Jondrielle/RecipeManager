<script setup>
import {ref} from 'vue'

const props = defineProps({
	editMode:Boolean,
	recipe:Object
})

const emit = defineEmits(["submit","add","edit","cancel"])

const form = ref({
	id: props.recipe?.id || null,
	name: props.recipe?.name || "",
	description: props.recipe?.description || "",
	ingredients: props.recipe?.ingredients || [],
	instructions: props.recipe?.instructions || [],
	prep_time: props.recipe?.prep_time || 0,
	cook_time: props.recipe?.cook_time || 0,
	servings: props.recipe?.servings || 1,
	difficulty: props.recipe?.difficulty || "",
	image_url: props.recipe?.image_url || ""
})

function submit(){
	console.log("form submitted", form.value)
	
	if(props.editMode){
		emit("edit",form.value)
	}
	else{
		emit("add",form.value)
		clearForm()
	}
}

function cancel(){
	emit("cancel")
}

function clearForm(){
	form.value = {
    id: null,
    name: "",
    description: "",
    ingredients: [],
    instructions: [],
    prep_time: 0,
    cook_time: 0,
    servings: 1,
    difficulty: ""
  }
}
</script>

<template>
	<div class="container">
		<form @submit.prevent="submit" class="form">
			<input v-model="form.name" placeholder="Name"></input>

			<input v-model="form.description" placeholder="Description"></input>
		  
			<input v-model="form.ingredients" placeholder="Ingredients"></input>
		  
			<input v-model="form.instructions"
		  	placeholder="Instructions"></input>

		  	<input v-model.number="form.prep_time"
			  placeholder="Prep"></input>

			<input v-model.number="form.cook_time"
			  placeholder="Cook"></input>
			  
			<input v-model.number="form.servings"
			  placeholder="Servings"></input>

			<input v-model="form.image_url" placeholder="Image URL"></input>
			  
			<select v-model="form.difficulty">
				<option disabled value="">Select Difficulty</option>
			    <option value="Easy">Easy</option>
			    <option value="Medium">Medium</option>
			    <option value="Hard">Hard</option>
			</select>

			<button class="button" type="submit">{{ editMode ? "Update Recipe" : "Add Recipe" }}</button>
			<button @click="cancel">Cancel</button>
		</form>
	</div>
</template>

<style scoped>
	.form{
		display:flex;
		flex-direction:column;
		gap:10px;
	}

	.container {
	  width: 350px;
	  margin: 20px auto;
	  border: 1px solid orange;
	  border-radius: 12px;
	  padding: 16px;
	  background-color: #ffecd2;
	  margin-top:45px;
	}

</style>