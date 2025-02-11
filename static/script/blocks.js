document.addEventListener("DOMContentLoaded", function () {
    const blocks = document.querySelectorAll(".main-container");
    const colors = ["#571301", "#3a0157", "#011230", "#570143"];
    const popup = document.createElement("div");
    popup.classList.add("popup");
    popup.innerHTML = `<div class="popup-body"></div>`;
    document.body.appendChild(popup);
    const popupBody = popup.querySelector(".popup-body");

    blocks.forEach((block, index) => {
        block.style.backgroundColor = colors[index % colors.length];
        block.style.boxShadow = "0 4px 8px rgba(0, 0, 0, 0.5)";
        block.style.transition = "box-shadow 0.3s ease";

        setTimeout(() => {
            block.classList.add("appear");
        }, index * 200);

        block.addEventListener("click", function () {
            requestAnimationFrame(() => {
                const clonedContent = this.cloneNode(true);
                const bgColor = window.getComputedStyle(this).backgroundColor;

                clonedContent.querySelectorAll(".education-description").forEach(el => {
                    el.style.display = "block";
                });

                clonedContent.setAttribute("style", "transform: none !important;");
                clonedContent.style.backgroundColor = bgColor;
                clonedContent.style.cursor = "default";

                const closeBtn = clonedContent.querySelector(".close-btn");
                if (closeBtn) {
                    closeBtn.style.display = "block";
                    closeBtn.addEventListener("click", function () {
                        popup.style.display = "none";
                    });
                }

                popupBody.innerHTML = "";
                popupBody.appendChild(clonedContent);
                popup.style.display = "flex";
            });
        });
    });

    window.addEventListener("click", function (e) {
        if (e.target === popup) {
            popup.style.display = "none";
        }
    });
});
