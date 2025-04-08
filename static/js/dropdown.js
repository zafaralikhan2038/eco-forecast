document.addEventListener('DOMContentLoaded', function() {
  const dropdownTrigger = document.getElementById('profile-dropdown-trigger');
  const dropdownMenu = document.getElementById('profile-dropdown');

  // Toggle dropdown on click
  dropdownTrigger.addEventListener('click', function(e) {
    e.stopPropagation(); // Prevent event from bubbling
    dropdownMenu.classList.toggle('hidden');
  });

  // Close dropdown when clicking outside
  document.addEventListener('click', function() {
    dropdownMenu.classList.add('hidden');
  });

  // Prevent dropdown from closing when clicking inside
  dropdownMenu.addEventListener('click', function(e) {
    e.stopPropagation();
  });
});