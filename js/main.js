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
