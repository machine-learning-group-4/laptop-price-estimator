
document.addEventListener("DOMContentLoaded", function () {

    const themeToggle = document.getElementById("theme-toggle");

    // Load the saved theme
    let savedTheme = localStorage.getItem("theme") || "light";

    // Apply the saved theme
    document.documentElement.setAttribute("data-theme", savedTheme);

    // Set the correct button icon
    themeToggle.textContent = savedTheme === "dark" ? "☀️" : "🌙";

    // Switch themes when the button is clicked
    themeToggle.addEventListener("click", function () {

        let currentTheme = document.documentElement.getAttribute("data-theme");

        let newTheme = currentTheme === "dark" ? "light" : "dark";

        // Apply the new theme
        document.documentElement.setAttribute("data-theme", newTheme);

        // Update the button icon
        themeToggle.textContent = newTheme === "dark" ? "☀️" : "🌙";

        // Save the selected theme
        localStorage.setItem("theme", newTheme);

    });

});
