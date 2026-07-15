// Footer year
document.getElementById('year').textContent = new Date().getFullYear();

// Navbar opacity on scroll
const nav = document.getElementById('mainNav');
window.addEventListener('scroll', () => {
  nav.style.background = window.scrollY > 40
    ? 'rgba(11,25,41,0.97)'
    : 'rgba(11,25,41,0.85)';
});

// Close mobile nav after link click
document.querySelectorAll('#navMenu .nav-link').forEach(link => {
  link.addEventListener('click', () => {
    const menu = document.getElementById('navMenu');
    if (menu.classList.contains('show')) {
      bootstrap.Collapse.getOrCreateInstance(menu).hide();
    }
  });
});

// Scroll-reveal for cards and timeline items
const targets = document.querySelectorAll(
  '.project-card, .timeline-item, .skill-block, .education-row'
);
const observer = new IntersectionObserver(entries => {
  entries.forEach(e => {
    if (e.isIntersecting) {
      e.target.style.opacity = '1';
      e.target.style.transform = 'translateY(0)';
      observer.unobserve(e.target);
    }
  });
}, { threshold: 0.12 });

targets.forEach(el => {
  el.style.opacity = '0';
  el.style.transform = 'translateY(16px)';
  el.style.transition = 'opacity 0.5s ease, transform 0.5s ease';
  observer.observe(el);
});
