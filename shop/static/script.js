
document.querySelector('.menu-toggle').addEventListener('click', function() {
    document.querySelector('.nav-links').classList.toggle('show');
})
























document.addEventListener("DOMContentLoaded", function () {
    const motivationSection = document.querySelector(".motivation");
    const observer = new IntersectionObserver(entries => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                motivationSection.classList.add("scroll-active");
            }
        });
    }, { threshold: 0.5 });

    observer.observe(motivationSection);
});