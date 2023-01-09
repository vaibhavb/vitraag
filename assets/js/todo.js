console.log("Running log for todo app - Dec 21.2022")

const todoForm = document.getElementById('todo-form')
const todoInput = document.getElementById('todo-input')
const todoList = document.getElementById('todo-list')
//import {timesince} from ".modules/clock";

//addTodo(timesince("Dec 1, 2022"))

// Add a new to-do item to the list
function addTodo(text) {
  const li = document.createElement('li')
  li.textContent = text
  todoList.appendChild(li)
}

// Retrieve the list of to-do items from the backend
async function getTodos() {
  //const response = await fetch('/api/todos')
  //const todos = await response.json()
  var todos = [{text: "vaibhav 1"}, {text: "vaibhav 2"}]
  todos.forEach(todo => addTodo(todo.text))
}

// Handle the form submission
todoForm.addEventListener('submit', async e => {
  e.preventDefault()
  const text = todoInput.value.trim()
  if (text !== '') {
    /* const response = await fetch('/api/todos', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ text })
    })
    if (response.ok) {
      addTodo(text)
      todoInput.value = ''
    } */
    addTodo(text);    
    todoInput.value = ''
  } 
})

// Initialize the app
getTodos()
console.log("Nov 1, 2022")