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

			<h2>Add Recipe</h2>
			<label>Recipe Details</label>
			<div class="details">
				<input class="fullWidth" v-model="form.name" placeholder="Name"></input>

				<input class="fullWidth" v-model="form.description" placeholder="Description"></input>

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
			</div>

		  <div class="ingredientForm">
			  <label>Ingredients</label>

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
			  <label>Instructions</label>

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
			        class="instructionInput"
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


			<button class="button" type="submit">{{ editMode ? "Update Recipe" : "Add Recipe" }}</button>
			<button type="button" @click="cancel">Cancel</button>
		</form>
	</div>
</template>

<style scoped>

.container {
  width: 600px;
  max-width: 90%;
  margin: 45px auto;
  padding: 25px;
  border: 1px solid #f4b183;
  border-radius: 16px;
  background-color: #ffecd2;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
}

.form {
  display: flex;
  flex-direction: column;
  gap: 20px;
}

/* =========================
   RECIPE DETAILS
   ========================= */

.details {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 12px;
}

.fullWidth {
  grid-column: 1 / -1;
}

/* =========================
   ALL INPUTS
   ========================= */

input,
select {
  box-sizing: border-box;
  width: 100%;
  padding: 10px 12px;
  border: 1px solid #d6c4b5;
  border-radius: 8px;
  background-color: white;
  font-size: 14px;
}

input:focus,
select:focus {
  outline: none;
  border-color: #e89b5a;
  box-shadow: 0 0 0 2px rgba(232, 155, 90, 0.15);
}

/* =========================
   INGREDIENTS
   ========================= */

.ingredientForm {
  display: flex;
  flex-direction: column;
  gap: 10px;
}

/* Existing ingredient rows */

.ingredientRow {
  display: grid;
  grid-template-columns: 2fr 1fr 1fr auto;
  gap: 10px;
  align-items: center;
  padding: 10px;
  background-color: white;
  border-radius: 8px;
  border: 1px solid #eaded5;
}

/* New ingredient */

.ingredient {
  display: grid;
  grid-template-columns: 2fr 1fr 1fr auto;
  gap: 10px;
  align-items: center;
  padding: 12px;
  background-color: #fff8f1;
  border: 1px dashed #e5a46d;
  border-radius: 8px;
}

/* =========================
   INSTRUCTIONS
   ========================= */

.instructionForm {
  display: flex;
  flex-direction: column;
  gap: 10px;
}

/* Existing instruction */

.instructionRow {
  display: flex;
  flex-direction: column;
  gap: 6px;
  padding: 12px;
  background-color: white;
  border-radius: 8px;
  border: 1px solid #eaded5;
}

.instructionInput {
  display: flex;
  gap: 8px;
  align-items: center;
}

.instructionInput input {
  flex: 1;
}

/* New instruction */

.newInstruction {
  display: flex;
  flex-direction: column;
  gap: 8px;
  padding: 12px;
  background-color: #fff8f1;
  border: 1px dashed #e5a46d;
  border-radius: 8px;
}

/* =========================
   BUTTONS
   ========================= */

button {
  padding: 9px 14px;
  border: none;
  border-radius: 8px;
  background-color: #e89b5a;
  color: white;
  font-size: 14px;
  cursor: pointer;
  transition: background-color 0.2s ease;
}

button:hover {
  background-color: #d9823b;
}

button:active {
  transform: translateY(1px);
}

/* Remove buttons */

.ingredientRow button,
.instructionInput button {
  background-color: #d9534f;
}

.ingredientRow button:hover,
.instructionInput button:hover {
  background-color: #c9302c;
}

/* Add buttons */

.ingredient button,
.newInstruction button {
  background-color: #6c9f58;
}

.ingredient button:hover,
.newInstruction button:hover {
  background-color: #568645;
}

/* =========================
   MAIN FORM BUTTONS
   ========================= */

.form > .button {
  background-color: #e67e22;
  font-size: 16px;
  font-weight: bold;
  padding: 12px;
}

.form > .button:hover {
  background-color: #cf6d17;
}

.form > button:last-child {
  background-color: #999;
}

.form > button:last-child:hover {
  background-color: #777;
}

/* =========================
   MOBILE
   ========================= */

@media (max-width: 650px) {

  .container {
    width: 90%;
    padding: 18px;
  }

  .details {
    grid-template-columns: 1fr;
  }

  .fullWidth {
    grid-column: auto;
  }

  .ingredientRow,
  .ingredient {
    grid-template-columns: 1fr;
  }

  .instructionInput {
    flex-direction: column;
    align-items: stretch;
  }

}
</style>