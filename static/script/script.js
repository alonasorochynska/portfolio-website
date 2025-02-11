document.addEventListener("DOMContentLoaded", function() {
  const menuElement = document.getElementById("js-menu");
  const menuIcon = menuElement.querySelector(".burger-menu");
  const menuText = menuElement.querySelector(".menu-text");
  const closeButton = menuElement.querySelector(".menu-close-btn");
  const navbar = document.querySelector(".navbar");

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

  document.addEventListener("click", function(event) {
    if (!menuElement.contains(event.target)) {
      closeMenu();
    }
  });

  function closeMenu() {
    menuElement.classList.remove("menu-opened");
    navbar.classList.remove("open");
    closeButton.style.display = "none";
    menuIcon.style.display = "inline-block";
  }

  const navbarItems = document.querySelectorAll(".navbar-item");
  const currentUrl = window.location.href;
  navbarItems.forEach(item => {
    if (item.href === currentUrl) {
      menuText.textContent = item.textContent;
    }
  });
});
