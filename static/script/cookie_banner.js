document.addEventListener("DOMContentLoaded", function () {
    const banner = document.getElementById("cookieBanner");
    const overlay = document.getElementById("cookieOverlay");

    if (!banner || !overlay) return;

    const cookiesAccepted = document.cookie
        .split("; ")
        .some(cookie => cookie.startsWith("cookiesAccepted="));

    if (!cookiesAccepted) {
        banner.style.display = "block";
        overlay.style.display = "block";
    } else {
        banner.style.display = "none";
        overlay.style.display = "none";
    }
});

function acceptCookies() {
    document.cookie = [
        "cookiesAccepted=true",
        "path=/",
        "max-age=31536000",
        "SameSite=Lax"
    ].join("; ");

    const banner = document.getElementById("cookieBanner");
    const overlay = document.getElementById("cookieOverlay");

    if (!banner || !overlay) return;

    banner.style.display = "none";
    overlay.style.display = "none";

    fetch('/accept-cookies/', {
        method: 'POST',
        credentials: 'include'
    })
    .then(response => {
        if (!response.ok) {
            console.error(
                "Error sending request:",
                response.status
            );
        }
    })
    .catch(error => console.error("Network error:", error));
}
