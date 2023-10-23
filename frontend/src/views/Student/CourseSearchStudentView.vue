<template>
    <main class="form">
      <h2>Please enter a course to search for (Example: CSE 1010)</h2>
  
      <form @submit.prevent="createTodo" class="create-todo">
        <label for="todo">Search:</label>
        <input type="text" id="todo" name="todo" v-model="newTodo" />
        <button type="submit">Enter</button>
      </form>
  
      <ul>
        <!--
          v-for requires a unique key for every element so that it can efficiently keep track
          of each list item. it is possible for the user to type the same todo more than once,
          so the todo itself isn't necessarily unique. the index on its own is of course unique,
          it represents each unique place in the array. there are unfortunately edge case issues
          with using the index alone that we don't need to get into, so we combine the todo and
          the index into a unique key that will work in all situations
        -->
        <li v-for="(todo, index) in todos" :key="todo + index">
          {{ todo }}
          <button @click="deleteTodo(index)">Delete</button>
        </li>
        <li v-if="todos.length === 0">
          <p>You are not enrolled in any courses yet!</p>
        </li>
      </ul>
    </main>
  </template>
  
  <script setup>
  import { ref } from "vue";
  
  const newTodo = ref("");
  
  const todos = ref([]);
  
  // function to run when the create todo form is submitted
  function createTodo() 
  {
    // sanitize the input by removing the whitespace from the beginning and end of newTodo.value
    const todoToAdd = newTodo.value.trim();
  
    // if the sanitized input is not an empty string (i.e., an actual todo), add it to the list and reset the form
    if (todoToAdd !== "") {
      todos.value.push(todoToAdd);
      newTodo.value = "";
    }
  }
  
  // when a todo's delete button is clicked, the index of that todo is passed to this function
  // Array.splice takes an index in the array and a number of items to delete after that
  function deleteTodo(index) {
    todos.value.splice(index, 1);
  }

  function querySubjects(subject)
  {
    var AWS = require('aws-sdk');
    var dydb = new AWS.DynamoDB({apiVersion: '2019-11-21'});

    const params = {
      // Specify which items in the results are returned.
      FilterExpression: "Subject = :topic AND Season = :s AND Episode = :e",
      // Define the expression attribute value, which are substitutes for the values you want to compare.
      ExpressionAttributeValues: {
        ":topic": {S: "SubTitle2"},
        ":s": {N: 1},
        ":e": {N: 2},
      },
      // Set the projection expression, which are the attributes that you want.
      ProjectionExpression: "Season, Episode, Title, Subtitle",
      TableName: "Subjects",
};
  }




  </script>
  
  <style>
  .form {
    padding: 1rem;
  }
  
  .form h2 {
    font-size: 1.5rem;
    margin-bottom: 2rem;
  }
  
  .form p {
    margin-bottom: 1rem;
  }
  
  /* flex layouts allow us to position elements next to each other that would otherwise have been on top of each other */
  .form ul {
    display: flex;
    gap: 1rem;
    flex-direction: column;
  }
  .form li {
    display: flex;
    gap: 0.5rem;
    align-items: center;
  }
  
  /* create some space beneath the create todo form */
  .form form {
    margin-bottom: 1rem;
  }
  
  /* set some default styling to buttons and inputs for borders, heights, and padding */
  .form :is(input, button) {
    line-height: 2rem;
    padding-inline: 0.5rem;
    border-radius: 0.375rem;
    border: 1px solid #d9d9d9;
    margin-left: 0.5rem;
    color: #202020;
  }
  </style>
  