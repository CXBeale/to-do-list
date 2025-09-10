// Wait for the DOM to load
document.addEventListener('DOMContentLoaded', function() {
	// Get references to form, input, and list
	const form = document.getElementById('todo-form');
	const input = document.getElementById('todo-input');
	const list = document.getElementById('todo-list');

	// Listen for form submission
	form.addEventListener('submit', function(e) {
		e.preventDefault(); // Prevent page reload
		const taskText = input.value.trim(); // Get input value
		if (taskText !== '') {
			// Create new list item
			const li = document.createElement('li');
			li.textContent = taskText;
			list.appendChild(li); // Add to list
			input.value = ''; // Clear input
		}
	});
});
