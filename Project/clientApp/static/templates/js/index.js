$(document).ready(function () {
  const adminSignInButton = document.getElementById('adminSignIn');
const patientSignInButton = document.getElementById('patientSignIn');
const container = document.getElementById('container');

adminSignInButton.addEventListener('click', () => {
	container.classList.add("right-panel-active");
});

patientSignInButton.addEventListener('click', () => {
	container.classList.remove("right-panel-active");
});



});