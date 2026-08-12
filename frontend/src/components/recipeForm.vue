<script setup>
import {ref} from 'vue'

const props = defineProps({
	editMode:Boolean,
	recipe:Object
})

const emit = defineEmits(["submit","add","edit","cancel"])

const ingredient = ref({
	name: "",
	amount: 0,
	unit: ""	
})

const instruction = ref("")

const form = ref({
	id: props.recipe?.id || null,
	name: props.recipe?.name || "",
	description: props.recipe?.description || "",
	ingredients: props.recipe?.ingredients
	? props.recipe.ingredients.map(item => ({ ...item }))
	: [],

	instructions: props.recipe?.instructions
	? [...props.recipe.instructions]
	: [],

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
    difficulty: "",
    image_url:""
  }

  ingredient.value = { 
  	name: "", 
  	amount: 0, 
  	unit: "" 
  }

  instruction.value = ""
}

function addIngredient() { 
	if (!ingredient.value.name) 
	{ return } 

	form.value.ingredients.push({ ...ingredient.value }) 

	ingredient.value = { 
		name: "", 
		amount: 0, 
		unit: "" 
	} 
}

function addInstruction() {
  if (!instruction.value.trim()) {
    return
  }

  form.value.instructions.push(instruction.value.trim())

  instruction.value = ""
}

function removeIngredient(index) {
  form.value.ingredients.splice(index, 1)
}

function removeInstruction(index) {
	form.value.instructions.splice(index, 1)
}

</script>

<template>
	<div class="container">
		<form @submit.prevent="submit" class="form">
			<input v-model="form.name" placeholder="Name"></input>

			<input v-model="form.description" placeholder="Description"></input>

		  	<div class="ingredientForm">
			  <h2>Ingredients</h2>

			  <!-- Existing ingredients -->
			  <div
			    v-for="(item, index) in form.ingredients"
			    :key="index"
			    class="ingredientRow"
			  >
			    <input
			      v-model="item.name"
			      placeholder="Ingredient"
			    />

			    <input
			      v-model.number="item.amount"
			      type="number"
			      placeholder="Amount"
			    />

			    <input
			      v-model="item.unit"
			      placeholder="Unit"
			    />

			    <button
			      type="button"
			      @click="removeIngredient(index)"
			    >
			      Remove
			    </button>
			  </div>

			  <!-- New ingredient -->
				<div class="ingredient">
				<label>New Ingredient</label>
				  <input
				    v-model="ingredient.name"
				    placeholder="Ingredient"
				  />

				  <input
				    v-model.number="ingredient.amount"
				    type="number"
				    placeholder="Amount"
				  />

				  <input
				    v-model="ingredient.unit"
				    placeholder="Unit"
				  />

				  <button
				    type="button"
				    @click="addIngredient"
				  >
				    Add Ingredient
				  </button>
			  </div>
			</div>
			
			<div class="instructionForm">
			  <h2>Instructions</h2>

			  <!-- Existing instructions -->
			  <div
			    v-for="(item, index) in form.instructions"
			    :key="index"
			    class="instructionRow"
			  >
			    <label>
			      Step {{ index + 1 }}
			    </label>

			    <div class="instructionInput">
			      <input
			        v-model="form.instructions[index]"
			        :placeholder="`Step ${index + 1}`"
			      />

			      <button
			        type="button"
			        @click="removeInstruction(index)"
			      >
			        Remove
			      </button>
			    </div>
			  </div>

			  <!-- Add a new instruction -->
			  <div class="newInstruction">
			    <label>New instruction</label>

			    <input
			      v-model="instruction"
			      placeholder="Enter a new instruction..."
			    />

			    <button
			      type="button"
			      @click="addInstruction"
			    >
			      + Add Instruction
			    </button>
			  </div>
			</div>

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
			<button type="button" @click="cancel">Cancel</button>
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

	.ingredientForm{
		display: flex;
		flex-direction:column;
		gap: 5px;
		margin-bottom: 30px;
	}

	.instructionForm{
		display: flex;
		flex-direction: column;
		gap: 10px;
		padding-bottom:30px;
	}

	.newInstruction{
		display:flex;
		flex-direction:column;
		gap:5px;
	}

	.ingredient{
		padding-top:10px;
		display:flex;
		flex-direction:column;
		gap:5px

	}
</style>