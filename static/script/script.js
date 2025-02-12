document.addEventListener("DOMContentLoaded", function() {
  const menuElement = document.getElementById("js-menu");
  const menuIcon = menuElement.querySelector(".burger-menu");
  const closeButton = menuElement.querySelector(".menu-close-btn");
  const navbar = document.querySelector(".navbar");
  const navbarItems = document.querySelectorAll(".navbar-item");

  menuIcon.addEventListener("click", function(event) {
    menuElement.classList.add("menu-opened");
    navbar.classList.add("open");
    menuIcon.style.display = "none";
    closeButton.style.display = "inline-block";
    event.stopPropagation();
  });

  closeButton.addEventListener("click", function(event) {
    closeMenu();
    event.stopPropagation();
  });

  navbarItems.forEach(item => {
    item.addEventListener("click", function(event) {
      event.stopPropagation();
    });
  });

  window.addEventListener("click", function(event) {
    if (!menuElement.contains(event.target) && !menuIcon.contains(event.target)) {
      closeMenu();
    }
  });

  function closeMenu() {
    menuElement.classList.remove("menu-opened");
    navbar.classList.remove("open");
    closeButton.style.display = "none";
    menuIcon.style.display = "inline-block";
  }
});
