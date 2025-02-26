window.onload = function () {
    const toggle = document.getElementById("btnChangeTheme");
    const themeCSS = document.getElementById("themeCSS");
    const icon = document.getElementById("iconCurrentTheme");

    toggle.addEventListener("click", function () {
        let theme;
        if (themeCSS.getAttribute("href").includes("dark_style.css")) {
            theme = "light";
            themeCSS.href = "/static/css/light_style.css";
            icon.classList.replace("fa-moon-o", "fa-sun-o");
        } else {
            theme = "dark";
            themeCSS.href = "/static/css/dark_style.css";
            icon.classList.replace("fa-sun-o", "fa-moon-o");
        }
        localStorage.setItem("theme", theme);
    });
};