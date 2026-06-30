// Swasthi Computers — Main JS

document.addEventListener('DOMContentLoaded', function () {
  const mobileToggle = document.getElementById('mobile-menu-toggle');
  const mobileNav = document.getElementById('mobile-nav');
  const mobileSolutionsToggle = document.getElementById('mobile-solutions-toggle');
  const mobileSolutionsSub = document.getElementById('mobile-solutions-sub');

  // Mobile menu toggle
  if (mobileToggle && mobileNav) {
    mobileToggle.addEventListener('click', function () {
      const isOpen = mobileNav.classList.toggle('hidden');
      mobileToggle.setAttribute('aria-expanded', !isOpen);
      document.body.classList.toggle('mobile-nav-open');
    });
  }

  // Mobile solutions accordion
  if (mobileSolutionsToggle && mobileSolutionsSub) {
    mobileSolutionsToggle.addEventListener('click', function () {
      mobileSolutionsSub.classList.toggle('hidden');
      mobileSolutionsToggle.querySelector('.chevron')?.classList.toggle('rotate-180');
    });
  }

  // Close mobile nav on link click (for single-page sections)
  document.querySelectorAll('#mobile-nav a').forEach(function (link) {
    link.addEventListener('click', function () {
      if (mobileNav && !mobileNav.classList.contains('hidden')) {
        mobileNav.classList.add('hidden');
        mobileToggle?.setAttribute('aria-expanded', 'false');
        document.body.classList.remove('mobile-nav-open');
      }
    });
  });

  // Scroll reveal animations
  const revealElements = document.querySelectorAll('.reveal');
  if (revealElements.length && 'IntersectionObserver' in window) {
    const observer = new IntersectionObserver(
      (entries) => {
        entries.forEach(entry => {
          if (entry.isIntersecting) {
            entry.target.classList.add('visible');
            observer.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.15, rootMargin: '0px 0px -40px 0px' }
    );
    revealElements.forEach(el => observer.observe(el));
  }

  // Scroll-to-top button
  const scrollBtn = document.getElementById('scroll-top');
  if (scrollBtn) {
    window.addEventListener('scroll', () => {
      const show = window.scrollY > 500;
      scrollBtn.classList.toggle('opacity-0', !show);
      scrollBtn.classList.toggle('pointer-events-none', !show);
    });
    scrollBtn.addEventListener('click', () => {
      window.scrollTo({ top: 0, behavior: 'smooth' });
    });
  }

  // Close mega-menu on Escape
  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape') {
      const openMobile = mobileNav && !mobileNav.classList.contains('hidden');
      if (openMobile) {
        mobileNav.classList.add('hidden');
        mobileToggle?.setAttribute('aria-expanded', 'false');
        document.body.classList.remove('mobile-nav-open');
      }
    }
  });
});
