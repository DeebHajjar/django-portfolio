let currentSlide = 0;
const slides = document.querySelectorAll('.slide');
const thumbnails = document.querySelectorAll('.thumbnail');
const mainSlider = document.querySelector('.main-slider');

// Variables for tracking touch movement
let touchStartX = 0;
let touchEndX = 0;

function showSlide(index) {
    slides.forEach(slide => slide.classList.remove('active'));
    thumbnails.forEach(thumb => thumb.classList.remove('active'));
    
    slides[index].classList.add('active');
    thumbnails[index].classList.add('active');

    thumbnails[index].scrollIntoView({
        behavior: 'smooth',
        block: 'nearest',
        inline: 'center'
    });
}

function nextSlide() {
    currentSlide = (currentSlide + 1) % slides.length;
    showSlide(currentSlide);
}

function prevSlide() {
    currentSlide = (currentSlide - 1 + slides.length) % slides.length;
    showSlide(currentSlide);
}

// Add touch event listeners
mainSlider.addEventListener('touchstart', (e) => {
    touchStartX = e.touches[0].clientX;
});

mainSlider.addEventListener('touchmove', (e) => {
    // Prevent virtual dragging of the page while dragging
    e.preventDefault();
}, { passive: false });

mainSlider.addEventListener('touchend', (e) => {
    touchEndX = e.changedTouches[0].clientX;
    handleSwipe();
});

function handleSwipe() {
    const swipeThreshold = 50; // Minimum distance to be considered a draw
    const swipeDistance = touchEndX - touchStartX;

    if (Math.abs(swipeDistance) > swipeThreshold) {
        if (swipeDistance > 0) {
            // Swipe right - previous image
            prevSlide();
        } else {
            // Swipe left - next image
            nextSlide();
        }
    }
}

thumbnails.forEach((thumbnail, index) => {
    thumbnail.addEventListener('click', () => {
        currentSlide = index;
        showSlide(currentSlide);
    });
});

document.getElementById('currentYear').textContent = new Date().getFullYear();
