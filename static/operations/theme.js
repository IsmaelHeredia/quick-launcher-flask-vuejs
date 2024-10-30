window.onload = function () {

    const toggle = document.getElementById("btnChangeTheme");
    const theme = document.getElementById("themeCSS");
    const icon = document.getElementById("iconCurrentTheme");

    toggle.addEventListener("click", async function () {

        await axios.get('/changeTheme');

        if (theme.getAttribute("href").includes("dark_style.css")) {
            icon.classList.remove("fa-sun-o");
            icon.classList.add("fa-moon-o");
        } else {
            icon.classList.remove("fa-moon-o");
            icon.classList.add("fa-sun-o");
        }

        if (theme.getAttribute("href").includes("dark_style.css")) {
            theme.href = "/static/css/light_style.css";
        } else {
            theme.href = "/static/css/dark_style.css";
        }

    });
}