document.addEventListener("DOMContentLoaded", function () {
    let banner = document.getElementById("cookieBanner");
    let overlay = document.getElementById("cookieOverlay");

    if (!document.cookie.includes("cookiesAccepted=true")) {
        banner.style.display = "block";
        overlay.style.display = "block";
    } else {
        banner.style.display = "none";
        overlay.style.display = "none";
    }
});

function acceptCookies() {
    document.cookie = "cookiesAccepted=true; path=/; max-age=31536000; SameSite=Lax";
    document.getElementById("cookieBanner").style.display = "none";
    document.getElementById("cookieOverlay").style.display = "none";

    fetch('/accept-cookies/', {
        method: 'POST',
        credentials: 'include'
    }).then(response => {
        if (!response.ok) {
            console.error("Error sending request:", response.status);
        }
    }).catch(error => console.error("Network error:", error));

}
