document.getElementById('currentYear').textContent = new Date().getFullYear();


// Animation
const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('visible');
        }
    });
}, {
    threshold: 0.1 // يظهر العنصر عندما يكون 10% منه مرئياً
});

// تحديد جميع العناصر التي نريد مراقبتها
document.querySelectorAll('.fade-in, .slide-right, .slide-left, .scale-up').forEach((element) => {
    observer.observe(element);
});

// تفعيل التأثيرات للعناصر المرئية عند تحميل الصفحة
document.addEventListener('DOMContentLoaded', () => {
    const initialElements = document.querySelectorAll('.fade-in, .slide-right, .slide-left, .scale-up');
    initialElements.forEach(element => {
        if (element.getBoundingClientRect().top < window.innerHeight) {
            element.classList.add('visible');
        }
    });
});



const menu = document.getElementById("menu");
const actions = document.getElementById("actions");

menu.addEventListener("click", () => {
    hundleMenu();
})

function hundleMenu() {
    menu.classList.toggle("is-active");
    actions.classList.toggle("is-active");
}